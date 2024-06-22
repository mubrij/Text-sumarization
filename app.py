import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader, TextLoader

from dotenv import load_dotenv
load_dotenv()


class TextSummarizer():
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="""Write a concise summary of the following and also provide few key bullet points:
            "{text}"
            CONCISE SUMMARY:"""
        )

    def summarize_text(self, text):
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        result = chain.run(text=text)
        return result

    def summarize_pdf(self, file):
        loader = PyPDFLoader(file)
        documents = loader.load_and_split()
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        result = chain.run(text=" ".join(
            [doc.page_content for doc in documents]))
        return result

    def summarize_doc(self, file):
        loader = TextLoader(file)
        documents = loader.load_and_split()
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        result = chain.run(text=" ".join(
            [doc.page_content for doc in documents]))
        return result

    def construct_app(self):
        st.title("Text Summarizer")
        st.sidebar.markdown(
            "This is a text summarization AI that will summarize your text and document into simple points"
        )

        st.markdown('---')

        prompt = st.text_area(
            'Enter your text to be summarized', '', height=200)

        uploaded_file = st.file_uploader(
            "Upload a PDF or DOC file to be summarized", type=["pdf", "doc"])

        if prompt:
            response = self.summarize_text(prompt)
            st.write(response)

        if uploaded_file:
            if uploaded_file.name.lower().endswith(".pdf"):
                response = self.summarize_pdf(uploaded_file)
            elif uploaded_file.name.lower().endswith(".doc"):
                response = self.summarize_doc(uploaded_file)
            st.write(response)


if __name__ == "__main__":
    text_summarize = TextSummarizer()
    text_summarize.construct_app()

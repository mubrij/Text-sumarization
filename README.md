# Text Summarizer

### Overview

The Text Summarizer is an AI-powered tool designed to summarize text and documents into concise points. It utilizes OpenAI's GPT-3.5 Turbo model to generate summaries based on user-provided input or uploaded files in PDF or DOC format.

## Features

- Text Summarization: Enter text into the provided textarea to receive a concise summary and key bullet points.

- File Upload: Upload PDF or DOC files to have their content summarized automatically.

### How to Run

1. Clone this repository:

```
git clone https://github.com/tImIhAcK/text-summarizer.git
```

2. Navigate to the project directory:

```
cd text-summarizer
```

3. Create a virtual environment and activate:

```
python -m venv <venv_name>
```

On Windows:

```
<venv_name>\Scripts\activate
```

on linux:

```
source <venv_name>/bin/activate
```

Replace `<venv_name>` with your environment name

4. Create a .env file:

```
OPENAI_API_KEY='your_api_key'
```

5. Install dependencies:

```
pip install -r requirements.txt
```

Replace `your_api_key` with your api from openai

6. Run the application:

```
streamlit run app.py
```

7. Access the application in your browser at http://localhost:8501.

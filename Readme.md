# Enterprise Agentic AI Knowledge Assistant using RAG and Multi-Agent LLMs

## Overview

This project is an AI-powered knowledge assistant that answers questions about company documents using Retrieval-Augmented Generation (RAG), a local Large Language Model (LLM), and modular AI agents.

The system retrieves relevant information from company documents, generates context-based answers, and performs basic answer validation.

## Features

- Document loading from CSV files
- Text chunking with overlap
- Semantic embeddings using Sentence Transformers
- Vector storage and retrieval using ChromaDB
- Local answer generation using Ollama and Llama 3.2:3B
- Modular retrieval, answer, and validation agents
- Interactive chat interface using Streamlit
- Basic numeric answer validation

## Technology Stack

- Python
- Sentence Transformers
- ChromaDB
- Ollama
- Llama 3.2:3B
- Streamlit
- Pandas / CSV processing

## Project Workflow

1. Load company documents from a CSV file.
2. Split document text into smaller chunks.
3. Convert chunks into numerical embeddings.
4. Store embeddings in ChromaDB.
5. Retrieve relevant context for a user question.
6. Generate an answer using the local LLM.
7. Validate the answer using basic rules.
8. Display the answer in the Streamlit interface.

## Project Structure

```text
Enterprise-Agentic-AI/
├── agents/
│   ├── answer_agent.py
│   ├── knowledge_agent.py
│   ├── retrieval_agent.py
│   └── validation_agent.py
├── app/
│   └── streamlit_app.py
├── data/
│   └── company-document-text.csv
├── rag/
│   ├── answer.py
│   ├── document_loader.py
│   ├── embedding.py
│   ├── retriever.py
│   ├── text_chunker.py
│   └── vector_store.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Install Python and Ollama.
2. Pull the required local model:

```bash
ollama pull llama3.2:3b
```

3. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:

```powershell
pip install -r requirements.txt
```

5. Build or populate the vector database using the project's vector-store workflow.
6. Start the application:

```powershell
python -m streamlit run app/streamlit_app.py
```

## Example Questions

- What is the total price of order 10718?
- Who is the customer for order 10718?
- What is the order date for order 10718?
- What is the shipping country for order 10718?

## Current Limitations

- Answer validation currently uses basic rules and is not a complete fact-checking system.
- Exact order-related queries use additional matching logic.
- Advanced autonomous multi-agent orchestration and automated test coverage are planned improvements.

## Future Improvements

- Add automated unit and integration tests.
- Improve answer validation and source citations.
- Add support for more document formats.
- Add advanced agent coordination.
- Introduce CI/CD with GitHub Actions.
- Improve logging and error handling.

## Author

Vivek Saini
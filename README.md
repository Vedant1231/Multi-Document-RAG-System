# Multi-Document RAG System

An AI-powered document question-answering system that uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from PDF documents and generate answers using an LLM.

## Overview

This project allows users to ask questions about the contents of a PDF document. The document is processed into smaller text chunks, converted into vector embeddings, stored in a ChromaDB vector database, and retrieved when a user asks a question.

The retrieved context is then provided to a Groq-hosted LLM to generate a response grounded in the document.

## How It Works

PDF Document  
↓  
Document Loading  
↓  
Text Chunking  
↓  
Hugging Face Embeddings  
↓  
ChromaDB Vector Store  
↓  
Similarity Retrieval  
↓  
Relevant Context  
↓  
Groq LLM  
↓  
Generated Answer

## Features

- PDF document loading
- Automatic text chunking
- Local Hugging Face embeddings
- ChromaDB vector storage
- Semantic retrieval of relevant document content
- LLM-powered question answering
- Interactive command-line interface
- Environment-variable based API key management

## Tech Stack

- Python
- LangChain
- Hugging Face Embeddings
- ChromaDB
- Groq API
- PyPDFLoader

## RAG Pipeline

- A PDF document is loaded using PyPDFLoader.
- The document text is divided into smaller chunks using RecursiveCharacterTextSplitter.
- Hugging Face embeddings are generated for each chunk.
- The embeddings are stored in ChromaDB.
- When a question is entered, the most relevant document chunks are retrieved.
- The retrieved context is passed to the Groq-hosted LLM.
- The LLM generates an answer based on the retrieved document context.

## Project Structure

Multi-Document-RAG-System/
├── rag_engine.py
├── requirements.txt
├── .gitignore
└── .env

.env contains the Groq API key and is excluded from version control using .gitignore.

The local ChromaDB database and test PDF are also excluded from version control.

## Setup

1. Clone the repository

git clone https://github.com/Vedant1231/Multi-Document-RAG-System.git

cd Multi-Document-RAG-System

2. Create a virtual environment

python -m venv venv

Windows:

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project directory:

GROQ_API_KEY=your_groq_api_key

5. Run the application

python rag_engine.py

The application will prompt you to provide the path to a PDF document and then allows you to ask questions about its contents.

## Example

Example workflow:

PDF → Chunking → Embeddings → ChromaDB → Retrieval → Groq LLM → Answer

The system retrieves relevant sections of the document before generating the final response, helping keep answers grounded in the provided document.

## Security

API credentials are loaded through environment variables rather than being hard-coded into the source code.

The .env file is excluded from Git using .gitignore.

## Future Improvements

- Support multiple PDF documents in a single knowledge base
- Add a web-based user interface
- Add conversation history
- Improve retrieval strategies
- Add document metadata filtering
- Add automated evaluation of RAG responses
- Add deployment configuration

## Author

Vedant Pawar

Electronics & Computer Science Engineering Graduate

Interested in Generative AI, LLM Applications, Prompt Engineering, RAG, and AI Automation.

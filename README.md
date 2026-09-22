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

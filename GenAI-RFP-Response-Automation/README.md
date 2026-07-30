# AI-Powered RFP Response Automation

An AI-powered Retrieval-Augmented Generation (RAG) system designed to automate responses to technical Request for Proposal (RFP) questions.

## Project Overview

The system retrieves relevant information from complex RFP documents and generates context-aware, evidence-backed responses using Google Gemini.

It combines semantic retrieval, LLM-based reranking, and grounded response generation to improve the speed, consistency, and reliability of RFP response preparation.

## Key Results

- 30% reduction in manual effort through RFP response automation
- 1,000+ context-aware responses generated
- 25+ RFP questions evaluated
- Multimodal document processing across text, tables, OCR, and image-derived information

## Architecture

RFP Documents  
↓  
Document Processing & Chunking  
↓  
Embeddings using Sentence Transformers  
↓  
ChromaDB Vector Store  
↓  
Semantic Retrieval  
↓  
Gemini-based Reranking  
↓  
Evidence-Grounded Response Generation  
↓  
RFP Answer

## Technologies

- Python
- Google Gemini
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Sentence Transformers
- LangChain
- Streamlit
- Pandas

## Project Structure

```text
├── answering.py
├── chunking.py
├── evaluate_queries.py
├── evaluate_with_expected.py
├── evaluation_with_rouge.py
├── streamlit3.py
├── requirements.txt
├── README.md
└── .gitignore
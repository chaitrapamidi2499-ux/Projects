# 🤖 RFPro.ai — AI-Powered RFP Response Automation

> A GenAI-powered RFP response automation system that uses **Retrieval-Augmented Generation (RAG), multimodal document understanding, vector search, and Gemini-based semantic reranking (VARAG)** to retrieve relevant information from large technical document repositories and generate accurate, context-grounded responses to RFP questions.

---

# 📌 Overview

**RFPro.ai** is an AI-powered solution designed to streamline the traditionally time-consuming process of responding to **Requests for Proposals (RFPs)**.

RFP responses often require proposal teams to search through hundreds or thousands of pages of product documentation to find accurate information. RFPro.ai addresses this challenge by transforming large, unstructured technical document collections into a searchable knowledge repository and using Generative AI to retrieve and synthesize relevant information.

The system processes **text, tables, OCR content, and images**, stores the extracted information in a vector database, retrieves relevant document chunks for a user query, and applies **Gemini-based semantic reranking** to identify the most useful context before generating the final answer.

The project was developed around a **Hitachi Content Platform (HCP)** product documentation corpus containing **2,244 pages across five documents**.

---

# 📸 Application Preview

<img width="1896" height="817" alt="1st question" src="https://github.com/user-attachments/assets/a7f40e18-04f5-4da4-9932-fe8e445d37a7" />
<img width="1917" height="832" alt="2nd " src="https://github.com/user-attachments/assets/1230bd50-2b4c-4c51-bf80-07d7dba5d14a" />

---

# 🎯 Objectives

- Automate the retrieval of information required for RFP responses.
- Reduce the time spent manually searching through large technical documents.
- Build a searchable knowledge repository from unstructured PDF documents.
- Extract and utilize text, tables, OCR content, and images.
- Improve retrieval quality beyond traditional vector similarity search.
- Generate concise and document-grounded answers using Generative AI.
- Provide transparency into retrieved chunks and generated prompts.
- Evaluate the effectiveness of the RAG and VARAG approaches.

---

# ✨ Features

- 📄 Multi-document PDF Processing
- 📝 Text Extraction
- 📊 Table Extraction and Flattening
- 🔍 OCR Content Extraction
- 🖼️ Image Extraction and Summarization
- ✂️ Custom Sliding-Window Chunking
- 🧠 Semantic Embeddings
- 🗄️ ChromaDB Vector Database
- 🔎 Dense Vector Retrieval
- 🔁 Query Rephrasing
- 🧠 Gemini-Based Semantic Reranking
- 🤖 Context-Grounded RFP Answer Generation
- 🌐 Streamlit Interactive Interface
- 🧩 Retrieved Chunk Inspection
- 🔍 Rephrased Query Inspection
- 🧾 Final Prompt Inspection
- 🖼️ Supporting Image Retrieval
- 📊 RAG vs VARAG Evaluation

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| LLM | Google Gemini |
| Generative AI | Gemini 1.5 Flash / Gemini 2.0 Flash |
| Framework | LangChain |
| Embeddings | Sentence Transformers |
| Embedding Model | `all-MiniLM-L6-v2` |
| Vector Database | ChromaDB |
| Document Processing | PyMuPDF / Fitz, pdfplumber |
| OCR | OCR-based document extraction |
| Image Processing | Pillow |
| Data Processing | Pandas, JSON |
| Frontend | Streamlit |

---

# 📂 Project Structure

~~~text
RFPro.ai/
│
├── answering.py
├── chunking.py
├── storing.py
├── streamlit3.py
│
├── Extracted/
│   ├── <PDF Folder 1>/
│   │   ├── structured_output.json
│   │   └── chunked_output.json
│   │
│   ├── <PDF Folder 2>/
│   │   ├── structured_output.json
│   │   └── chunked_output.json
│   │
│   └── chromadb/
│
├── rag_answers_output2.csv
├── README.md
└── ...
~~~

---

# 🔄 End-to-End Workflow

~~~text
Product Documentation
        │
        ▼
PDF Extraction
        │
        ├── Text
        ├── Tables
        ├── OCR Content
        └── Images
        │
        ▼
Structured JSON
        │
        ▼
Custom Chunking
        │
        ▼
Text / Table / OCR / Image Chunks
        │
        ▼
Sentence Transformer Embeddings
        │
        ▼
ChromaDB Vector Store
        │
        ▼
User RFP Question
        │
        ▼
Query Rephrasing
        │
        ▼
Dense Vector Retrieval
        │
        ▼
Top-K Candidate Chunks
        │
        ▼
Gemini Semantic Reranking
        │
        ▼
Top Relevant Context
        │
        ▼
Gemini Context-Grounded Generation
        │
        ▼
RFP Response
~~~

---

# 🌐 Streamlit Application

The project includes an interactive **Streamlit-based RFP chatbot**.

Users can either:

- Type their own RFP question.
- Select a question from a predefined evaluation dataset.

The application then retrieves relevant document content and generates an answer using the VARAG pipeline.

---

# 🖥️ Developer Features

The Streamlit interface provides optional debugging and explainability features.

Users can inspect:

- 🔁 Rephrased Query
- 🧩 Retrieved Chunks
- 🧾 Final Gemini Prompt
- 🖼️ Supporting Images

This provides visibility into how the RAG pipeline arrived at its final response.

---

# 📈 Evaluation

The system was evaluated using a defined set of **25 RFP questions** and compared against the baseline RAG implementation.

Two primary evaluation measures were used:

### Relevant Chunk Percentage

Measures the percentage of retrieved chunks that are actually useful for answering the question.

~~~text
Relevant Chunk Percentage =
(Relevant Chunks / Total Chunks Checked) × 100
~~~

### BERT Cosine Similarity

Measures the semantic similarity between the expected answer and the generated answer using BERT-based embeddings.

---

# 📊 RAG vs VARAG Performance

| Metric | Before VARAG | After VARAG |
|--------|--------------|-------------|
| Retriever | Plain Dense Retrieval | Vector Retrieval + Gemini Reranking |
| Embedding Model | `intfloat/e5-base-v2` | `all-MiniLM-L6-v2` |
| Reranking | None | Gemini-based |
| Chunking | Flat / Basic Paragraph | Structured Multimodal Chunks |
| Correct Answers | **14 / 25** | **23 / 25** |
| Accuracy | **56%** | **92%** |
| Average Cosine Similarity | **0.63** | **0.8515** |
| Relevant Chunk Percentage | **53%** | **71.90%** |
| Answer Quality | Generic / Incomplete | Context-grounded / Deep / Accurate |
| Explainability | Limited | High |

---

# 🏆 Key Insights

The project demonstrated several improvements over a conventional RAG pipeline:

- Improved answer accuracy from **56% to 92%** on the evaluated 25-question set.
- Improved correct answers from **14/25 to 23/25**.
- Improved average semantic similarity from **0.63 to 0.8515**.
- Improved relevant retrieval from **53% to 71.90%**.
- Gemini-based reranking improved semantic relevance beyond vector similarity alone.
- Multimodal retrieval allowed text, tables, OCR content, and images to contribute to answers.
- Query rephrasing improved retrieval for open-ended questions.
- Structured metadata improved traceability and explainability.
- Retrieved chunks and prompts can be inspected directly through the Streamlit interface.

---

# 🧪 System Improvements

Several design alternatives were evaluated during development.

| Component | Initial Approach | Final Approach | Reason |
|-----------|------------------|----------------|--------|
| Text Embeddings | `intfloat/e5-base-v2` | `all-MiniLM-L6-v2` | Faster embedding with good retrieval quality |
| Image Summarization | Gemini 2.0 Flash | Gemini 1.5 Flash | More concise and relevant summaries |
| Retrieval | Dense Vector Search | Vector Search + Gemini Reranking | Better semantic relevance |
| Table Processing | Nested JSON | Flattened Row-wise Chunks | Better fine-grained retrieval |
| Text Chunking | Recursive Character Splitter | Sliding Window | Better context retention |

These changes formed the final retrieval and generation architecture used by RFPro.ai.

---

# 🚀 Future Improvements

- Integrate publicly available competitor product documentation.
- Compare competitor offerings against the organization's product capabilities.
- Integrate previously submitted RFP proposals.
- Retrieve reusable answers from historical RFP responses.
- Reduce repetitive manual response writing.
- Improve answer consistency across proposals.
- Expand beyond technical RFP questions.
- Support legal and compliance documentation.
- Support business and finance-related RFPs.
- Introduce stronger multimodal reasoning.
- Add response generation and proposal drafting capabilities.
- Improve enterprise-scale document ingestion and indexing.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Generative AI
- Retrieval-Augmented Generation
- Vector Databases
- Semantic Search
- LLM-based Reranking
- Multimodal RAG
- Prompt Engineering
- Query Rewriting
- Document Intelligence
- PDF Processing
- OCR
- Table Extraction
- Image Understanding
- Text Chunking
- Sentence Transformer Embeddings
- ChromaDB
- LangChain
- Google Gemini
- Streamlit
- RAG Evaluation
- BERT Semantic Similarity
- AI Application Development

---

# 💡 Why RFPro.ai?

Traditional RFP workflows often require proposal teams to manually search through large collections of technical documents, identify relevant information, verify the source, and construct responses.

RFPro.ai transforms this workflow into an AI-assisted retrieval and response pipeline.

~~~text
Traditional RFP Process

RFP Question
     │
     ▼
Manual Document Search
     │
     ▼
Read Hundreds of Pages
     │
     ▼
Find Relevant Information
     │
     ▼
Verify Information
     │
     ▼
Draft Response
     │
     ▼
Final Answer


RFPro.ai

RFP Question
     │
     ▼
Query Rephrasing
     │
     ▼
Semantic Retrieval
     │
     ▼
Gemini Reranking
     │
     ▼
Relevant Multimodal Context
     │
     ▼
Grounded AI Response
~~~

The goal is to make RFP answering **faster, more consistent, more explainable, and less dependent on manual document searching**.

---


# 👩‍💻 Authors



*Artificial Intelligence • Generative AI • Data Science • Machine Learning • RAG*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with us!**
```

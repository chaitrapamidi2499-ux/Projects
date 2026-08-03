import streamlit as st
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import google.generativeai as genai
from chromadb.config import Settings

# ✅ Set up Streamlit page config
st.set_page_config(page_title="📜 RFP Chatbot", layout="centered")
st.title("📜 AI-Powered RFP Chatbot")
st.caption("Ask questions from your RFP PDFs (text, tables, screenshots). Answers are 100% grounded in documents.")

# ✅ Show path being used
VECTOR_DB_PATH = r"D:\Abishek\Capstone\Extracted\chromadb"
st.sidebar.markdown(f"📂 **Chroma Vector DB Path:**\n```\n{VECTOR_DB_PATH}\n```")

# ✅ Initialize ChromaDB
try:
    chroma_settings = Settings(persist_directory=VECTOR_DB_PATH, is_persistent=True)
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma(embedding_function=embedding_model, client_settings=chroma_settings)
    st.sidebar.success("✅ Vector DB loaded")
except Exception as e:
    st.sidebar.error(f"❌ ChromaDB load error: {e}")
    st.stop()

# ✅ Initialize Gemini
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Replace with your Gemini API key
    gemini_model = genai.GenerativeModel("gemini-2.0-flash")
    st.sidebar.success("✅ Gemini API loaded")
except Exception as e:
    st.sidebar.error(f"❌ Gemini API error: {e}")
    st.stop()


# ✅ RAG Function
def query_rag_with_images(query):
    # Step 1: Rephrase the user query
    try:
        prompt = f"Rephrase this question professionally without changing the intent:\n\n{query}"
        reformulated_query = gemini_model.generate_content(prompt).text.strip()
    except Exception as e:
        st.warning(f"⚠️ Query rephrasing failed: {e}")
        reformulated_query = query

    # Step 2: Retrieve from ChromaDB
    try:
        results = vector_store.similarity_search(reformulated_query, k=10)
    except Exception as e:
        return f"❌ Retrieval failed: {e}", []

    if not results:
        return "Not enough information is available in the retrieved content.", []

    # Step 3: Organize chunks by type
    retrieved = {
        "text": [],
        "table_fact": [],
        "ocr": [],
        "image_caption": []
    }
    retrieved_images = []

    for r in results:
        ctype = r.metadata.get("type", "text")
        source = r.metadata.get("source_pdf", "unknown")
        page = r.metadata.get("page", "N/A")
        content = r.page_content.strip()
        tag = f"[📄 {source} | Page {page}]\n{content}"
        if ctype in retrieved:
            retrieved[ctype].append(tag)
        if ctype == "image_caption" and r.metadata.get("image_path"):
            retrieved_images.append(r.metadata["image_path"])

    # Step 4: Build context for Gemini
    context_parts = []
    if retrieved["text"]:
        context_parts.append("**Text Content:**\n" + "\n\n".join(retrieved["text"]))
    if retrieved["table_fact"]:
        context_parts.append("**Facts from Tables:**\n" + "\n\n".join(retrieved["table_fact"]))
    if retrieved["ocr"]:
        context_parts.append("**OCR from Screenshots:**\n" + "\n\n".join(retrieved["ocr"]))
    if retrieved["image_caption"]:
        context_parts.append("**Image Captions:**\n" + "\n\n".join(retrieved["image_caption"]))

    full_context = "\n\n".join(context_parts)

    # Step 5: Compose Gemini prompt
    final_prompt = f"""
You are a document analysis assistant. Use only the content below to answer the user's question.

Rules:
- If the answer is present, respond clearly and concisely.
- If it can be inferred, do so with reasoning.
- If not available, respond with:
  **"Not enough information is available in the retrieved content."**
- Do not use outside knowledge. Never guess.

----------------------------
📄 **Context**:
{full_context}
----------------------------

💬 **User Question**:
{reformulated_query}

✍️ **Answer**:
"""

    # Step 6: Get Gemini Answer
    try:
        response = gemini_model.generate_content(final_prompt)
        return response.text.strip(), retrieved_images
    except Exception as e:
        return f"⚠️ Gemini API Error: {e}", retrieved_images


# ✅ Streamlit UI
user_query = st.text_input("🔹 Ask a question:")

if st.button("Ask AI") and user_query.strip():
    with st.spinner("💡 Thinking..."):
        answer, images = query_rag_with_images(user_query)

        st.subheader("🤖 Answer")
        st.write(answer)

        if images:
            st.subheader("🖼️ Supporting Images")
            for img in images:
                if os.path.exists(img):
                    st.image(img, use_column_width=True)
                else:
                    st.warning(f"⚠️ Missing image: {img}")

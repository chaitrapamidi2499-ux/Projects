import json
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import google.generativeai as genai

# ✅ Configure models and paths
VECTOR_DB_PATH = r"E:\Capstone\Extracted\chromadb"
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedding_model)
genai.configure(api_key="YOUR_API_KEY")
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

# ✅ Gemini Reranking (VARAG)
def rerank_chunks_with_gemini(query, chunks, top_n=10):
    if not chunks:
        return []
    prompt = f"""
You are ranking document chunks based on how well they help answer the question below.

🔹 Question: {query}

Here are the chunks:
{chr(10).join([f"{i+1}. {c.page_content[:300]}" for i, c in enumerate(chunks)])}

Please return the top {top_n} most relevant chunks based on the question.
Reply with the list of chunk numbers only (e.g., 1, 4, 7).
"""
    try:
        response = gemini_model.generate_content(prompt).text.strip()
        top_indices = [int(x.strip()) - 1 for x in response.split(",") if x.strip().isdigit()]
        return [chunks[i] for i in top_indices if i < len(chunks)]
    except Exception as e:
        print("⚠️ Reranking failed:", e)
        return chunks[:top_n]

# ✅ Main Answering Function
def query_rag_with_varag(query, return_debug=False):
    try:
        reform_prompt = f"Rephrase the following question professionally:\n\"{query}\""
        reformulated_query = gemini_model.generate_content(reform_prompt).text.strip()
    except Exception as e:
        print(f"⚠️ Rephrasing failed: {e}")
        reformulated_query = query

    results = vector_store.similarity_search(reformulated_query, k=20)
    if not results:
        return "Not enough information is available in the retrieved content.", [], {} if return_debug else []

    top_chunks = rerank_chunks_with_gemini(reformulated_query, results, top_n=10)

    # Prepare retrieved context
    sections = {"text": [], "table_fact": [], "ocr": [], "image_caption": []}
    image_paths = []
    for r in top_chunks:
        ctype = r.metadata.get("type", "text")
        src = r.metadata.get("source_pdf", "unknown")
        page = r.metadata.get("page", "N/A")
        tag = f"[📄 {src} | Page {page}]\n{r.page_content.strip()}"
        if ctype in sections:
            sections[ctype].append(tag)
        if ctype == "image_caption" and r.metadata.get("image_path"):
            image_paths.append(r.metadata["image_path"])

    context = ""
    if sections["text"]:
        context += "**Text Content:**\n" + "\n\n".join(sections["text"]) + "\n\n"
    if sections["table_fact"]:
        context += "**Facts from Tables:**\n" + "\n\n".join(sections["table_fact"]) + "\n\n"
    if sections["ocr"]:
        context += "**OCR Extracted Text:**\n" + "\n\n".join(sections["ocr"]) + "\n\n"
    if sections["image_caption"]:
        context += "**Image Captions:**\n" + "\n\n".join(sections["image_caption"]) + "\n\n"

    # ✅ Prompt - PDF Grounded Only
    final_prompt = f"""
You are a helpful assistant analyzing technical documents.
Use the context below to answer the question as accurately as possible.

If the answer is directly mentioned, quote it.  
If it is implied, infer based on facts provided.  
If the context does not help at all, say:
*"Not enough information is available in the retrieved content."*

Be concise but specific.

---CONTEXT---
{context}
---QUESTION---
{reformulated_query}
---ANSWER---
"""

    try:
        response = gemini_model.generate_content(final_prompt).text.strip()
    except Exception as e:
        response = f"⚠️ Gemini Error: {e}"

    if return_debug:
        return response, image_paths, {
            "rephrased": reformulated_query,
            "chunks": [c.page_content for c in top_chunks],
            "prompt": final_prompt
        }
    else:
        return response, image_paths

# ✅ CLI tester
if __name__ == "__main__":
    while True:
        user_q = input("\n🟢 Ask a Question (or type 'exit'): ")
        if user_q.lower() == "exit":
            break
        ans, imgs, dbg = query_rag_with_varag(user_q, return_debug=True)
        print("\n🤖 Answer:\n", ans)
        print("\n🧩 Chunks Used:")
        for i, chunk in enumerate(dbg["chunks"]):
            print(f"\n--- Chunk {i+1} ---\n{chunk[:300]}")
        if imgs:
            print("\n🖼️ Retrieved Images:\n", "\n".join(imgs))

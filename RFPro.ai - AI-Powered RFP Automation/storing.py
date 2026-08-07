import os
import json
import uuid
from PIL import Image
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.storage import InMemoryStore
import google.generativeai as genai

# ✅ Gemini API Key
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual key
vision_model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Paths
BASE_DIR = r"E:\Capstone\Extracted"
VECTOR_DB_PATH = os.path.join(BASE_DIR, "chromadb")

# ✅ Initialize embedding + vector DB
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedding_model)
doc_store = InMemoryStore()

# ✅ Helper: Gemini image summarization
def summarize_image(image_path):
    try:
        prompt = "Describe the image in detail for document understanding."
        img = Image.open(image_path)
        response = vision_model.generate_content([prompt, img])
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini image summary failed: {e}")
        return "No summary available."

# ✅ Helper: Split long lists into batches
def chunk_list(lst, size=5000):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

# ✅ Process all PDF folders
for folder_name in os.listdir(BASE_DIR):
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.isdir(folder_path):
        continue

    chunk_file = os.path.join(folder_path, "chunked_output.json")
    struct_file = os.path.join(folder_path, "structured_output.json")

    if not os.path.exists(chunk_file) or not os.path.exists(struct_file):
        print(f"⚠️ Skipping {folder_name} (missing extracted content)")
        continue

    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    with open(struct_file, "r", encoding="utf-8") as f:
        struct_data = json.load(f)

    doc_id = str(uuid.uuid4())
    doc_store.mset([(doc_id, {"chunks": chunks})])

    print(f"\n📁 Processing: {folder_name} | Chunks: {len(chunks)}")

    texts = []
    metadatas = []

    for chunk in chunks:
        text = chunk.get("chunk", "").strip()
        if not text:
            continue

        texts.append(text)
        metadatas.append({
            "chunk_id": chunk.get("chunk_id"),
            "type": chunk.get("type"),
            "page": chunk.get("page"),
            "source_pdf": chunk.get("source_pdf", folder_name),
            "doc_id": doc_id
        })

    # ✅ Store all chunks (text, table_fact, ocr)
    for text_batch, meta_batch in zip(chunk_list(texts), chunk_list(metadatas)):
        vector_store.add_texts(texts=text_batch, metadatas=meta_batch)

    # ✅ Handle image caption summarization
    image_captions = []
    image_meta = []

    for img in struct_data.get("extracted_images", []):
        image_path = img.get("image_path")
        if not os.path.exists(image_path):
            continue
        summary = summarize_image(image_path)
        image_captions.append(f"[Image Summary] {summary}")
        image_meta.append({
            "type": "image_caption",
            "image_path": image_path,
            "page": img.get("page"),
            "source_pdf": folder_name,
            "doc_id": doc_id
        })

    for text_batch, meta_batch in zip(chunk_list(image_captions), chunk_list(image_meta)):
        vector_store.add_texts(texts=text_batch, metadatas=meta_batch)

    print(f"✅ Stored {len(texts)} text/table/ocr chunks + {len(image_captions)} image captions for: {folder_name}")

print("\n🎉 All PDFs stored into ChromaDB successfully!")

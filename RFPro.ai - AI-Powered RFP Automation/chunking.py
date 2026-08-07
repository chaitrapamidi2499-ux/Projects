import os
import json

# ✅ Base directory containing PDF folders
BASE_DIR = r"E:\Capstone\Extracted"

# ✅ Chunking utility
def chunk_text(text, chunk_size=1000, overlap=100):
    words = text.split()
    chunks, current_chunk, current_length = [], [], 0

    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1

        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            current_length = sum(len(w) + 1 for w in current_chunk)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# ✅ Process each PDF's extracted folder
for folder_name in os.listdir(BASE_DIR):
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.isdir(folder_path):
        continue

    structured_path = os.path.join(folder_path, "structured_output.json")
    output_path = os.path.join(folder_path, "chunked_output.json")

    if not os.path.exists(structured_path):
        print(f"⚠️ Missing structured_output.json in {folder_name}")
        continue

    with open(structured_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_chunks = []

    def create_chunks(blocks, content_key="content"):
        for entry in blocks:
            content = entry.get(content_key, "").strip()
            if not content:
                continue
            chunks = chunk_text(content)
            for i, chunk in enumerate(chunks):
                all_chunks.append({
                    "chunk_id": f"{entry.get('type', 'unknown')}_p{entry.get('page', 'NA')}_{i+1}",
                    "chunk": chunk,
                    "type": entry.get("type", "text"),
                    "page": entry.get("page"),
                    "source_pdf": data.get("pdf_name", folder_name)
                })

    create_chunks(data.get("text_blocks", []))
    create_chunks(data.get("flattened_tables", []))
    create_chunks(data.get("ocr_blocks", []))

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=4)

    print(f"✅ Chunked {len(all_chunks)} items from: {folder_name}")

print("\n🎉 All PDFs chunked and saved successfully!")


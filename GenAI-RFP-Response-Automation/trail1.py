import os
import json
import hashlib
import fitz  # PyMuPDF
import pdfplumber
import pytesseract
from PIL import Image

# ✅ Path to Tesseract
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# ✅ Input & Output Paths
PDF_FOLDER = r"D:\Abishek\Capstone\PDF"
OUTPUT_DIR = r"D:\Abishek\Capstone\Extracted"

os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ PDF hashing for change detection
def get_pdf_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# ✅ Flatten table into fact-style strings
def flatten_table(table_data, page_num):
    facts = []
    if not table_data:
        return facts

    headers = table_data[0]
    rows = table_data[1:]

    for row in rows:
        for i in range(1, len(row)):
            key = str(headers[0]).strip()
            col = str(headers[i]).strip()
            val = str(row[i]).strip() if row[i] else "N/A"
            facts.append({
                "type": "table_fact",
                "page": page_num,
                "content": f"{key} - {col}: {val}"
            })
    return facts

# ✅ Main extractor
def process_pdf(pdf_path, output_subdir):
    print(f"\n📄 Processing: {os.path.basename(pdf_path)}")
    os.makedirs(output_subdir, exist_ok=True)

    pdf_hash = get_pdf_hash(pdf_path)
    hash_file = os.path.join(output_subdir, "pdf_hash.json")
    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            if json.load(f).get("pdf_hash") == pdf_hash:
                print("✅ No changes. Skipping.")
                return

    doc = fitz.open(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    image_dir = os.path.join(output_subdir, "Images")
    os.makedirs(image_dir, exist_ok=True)

    text_blocks = []
    ocr_blocks = []
    extracted_images = []
    flattened_tables = []

    # ✅ Text extraction
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()
        if text:
            text_blocks.append({
                "type": "text",
                "page": page_num,
                "content": text
            })

    # ✅ Table extraction
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for tbl in tables:
                facts = flatten_table(tbl, page.page_number)
                flattened_tables.extend(facts)

    # ✅ Image extraction & OCR
    for page_num, page in enumerate(doc, start=1):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            img_obj = doc.extract_image(xref)
            image_bytes = img_obj["image"]
            ext = img_obj["ext"]
            image_path = os.path.join(image_dir, f"page{page_num}_img{img_index + 1}.{ext}")
            with open(image_path, "wb") as f:
                f.write(image_bytes)

            extracted_images.append({"page": page_num, "image_path": image_path})

            # OCR
            try:
                text = pytesseract.image_to_string(Image.open(image_path)).strip()
                if text:
                    ocr_blocks.append({
                        "type": "ocr",
                        "page": page_num,
                        "content": text,
                        "image": image_path
                    })
            except Exception as e:
                print(f"❌ OCR failed for {image_path}: {e}")

    # ✅ Save unified JSON
    output_json = {
        "pdf_name": pdf_name,
        "text_blocks": text_blocks,
        "flattened_tables": flattened_tables,
        "ocr_blocks": ocr_blocks,
        "extracted_images": extracted_images
    }

    with open(os.path.join(output_subdir, "structured_output.json"), "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=4)

    with open(hash_file, "w") as f:
        json.dump({"pdf_hash": pdf_hash}, f)

    print(f"✅ Finished: {pdf_name} | Text: {len(text_blocks)} | Tables: {len(flattened_tables)} | OCR: {len(ocr_blocks)}")

# ✅ Loop through PDFs
pdfs = [f for f in os.listdir(PDF_FOLDER) if f.lower().endswith(".pdf")]
if not pdfs:
    print("⚠️ No PDFs found.")
else:
    for pdf in pdfs:
        process_pdf(
            os.path.join(PDF_FOLDER, pdf),
            os.path.join(OUTPUT_DIR, os.path.splitext(pdf)[0])
        )
    print("\n🎉 All PDFs processed.")


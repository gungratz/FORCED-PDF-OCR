import ocrmypdf
import os

input_folder = "PDF_INPUT"
output_folder = "PDF_OUTPUT"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"OCR_{filename}")
        try:
            ocrmypdf.ocr(
                input_path,
                output_path,
                language='ind',
                use_threads=True,
                deskew=True,
                force_ocr=True
            )
            print(f"✅ OCR selesai: {filename}")
        except Exception as e:
            print(f"❌ Gagal OCR {filename}: {e}")

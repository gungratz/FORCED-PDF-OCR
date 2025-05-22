Scrip ini untuk memaksa OCR pada PDF yang sebagian ada textnya. 
Kami buat agar PDF bisa diindex/ dicari dengan search di PDF viewer

✅ Langkah-langkah Sebelum Menjalankan Script
1. Install OCRmyPDF
Pastikan Python sudah terpasang, lalu install paketnya:
pip install ocrmypdf

2. Install Tesseract OCR
Windows: bisa install dari sini: https://github.com/tesseract-ocr/tesseract/wiki

Pastikan path-nya dikenali (tesseract.exe bisa dipanggil dari command line)

🔁 Versi Batch untuk Satu Folder
python

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



Isi FOLDERINPUT dengan PDF yang akan di OCR
Jalankan dengan klik kanan di foldernya, buka terminal, ketik python PAKSAOCR.py
jika sudah selesai --> File OCR akan ada di FOLDER_OUTPUT

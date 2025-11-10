import fitz  # PyMuPDF
import os

def pdf_to_image(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.jpg")
        pix.save(image_path)
        print(f"Saved image: {image_path}")

pdf_path = "hj"
output_folder = "path/to/output/folder"
pdf_to_image(pdf_path, output_folder)

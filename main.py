from pdf2image import convert_from_bytes
import os
import fitz  # PyMuPDF
import argparse


def pdf_to_png(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    doc = fitz.open(pdf_path)

    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f'page_{i + 1}.png')
        pix.save(image_path)
        print(f'Saved: {image_path}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF pages to PNG images.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder.")

    args = parser.parse_args()
    pdf_to_png(args.pdf_path, args.output_folder)

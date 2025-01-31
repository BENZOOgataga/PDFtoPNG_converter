# PDF to PNG Converter

## Description
This repository provides a Python script to convert PDF pages into PNG images using **PyMuPDF (fitz)**.

## Features
- 📄 Converts each page of a PDF into a separate PNG file.
- 🚀 Uses **PyMuPDF (fitz)** for efficient rendering.
- 💾 Saves images in a specified output directory.
- 🖥️ Command-line interface for easy usage.

## Requirements
Ensure you have Python installed and install the required dependency:
```sh
pip install pymupdf
```

## Usage
Run the script using the following command:
```sh
python main.py <pdf_path> <output_folder>
```
- `<pdf_path>`: Path to the PDF file.
- `<output_folder>`: Directory where PNG images will be saved.

### Example
```sh
python main.py example.pdf output_images
```
This will convert all pages of `example.pdf` and save them as PNG images in the `output_images` folder.

## License
📝 This project is licensed under the MIT License.

import os
from pdf2docx import Converter


def convert_pdf_to_word(pdf_path, output_path):
    # Convert PDF to temporary DOCX file
    temp_docx_path = "temp.docx"
    cv = Converter(pdf_path)
    cv.convert(temp_docx_path, start=0, end=None)
    cv.close()

    # Rename the temporary DOCX file to the desired output path
    os.rename(temp_docx_path, output_path)

if __name__ == '__main__':
    # Prompt the user for the PDF file path
    input_pdf_path = input("Enter the path to the PDF file: ")

    # Derive the output Word file path from the input PDF file path
    output_word_path = os.path.splitext(input_pdf_path)[0] + ".docx"

    # Call the conversion function
    convert_pdf_to_word(input_pdf_path, output_word_path)

    print("Conversion completed!")

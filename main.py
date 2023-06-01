import os
from pdf2docx import Converter


def convert_pdf_to_word(pdf_path, output_path):
    temp_docx_path = "temp.docx"
    cv = Converter(pdf_path)
    cv.convert(temp_docx_path, start=0, end=None)
    cv.close()

    os.rename(temp_docx_path, output_path)

if __name__ == '__main__':
    input_pdf_path = input("Enter the path to the PDF file: ")

    output_word_path = os.path.splitext(input_pdf_path)[0] + ".docx"

    convert_pdf_to_word(input_pdf_path, output_word_path)

    print("Conversion completed!")

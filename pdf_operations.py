# -*- coding: utf-8 -*-
"""pdf_operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/ayushisri01/bb73926bc36941d256e21a2fd95802b1/pdf_operations.ipynb
"""

import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    try:
        merger = PyPDF2.PdfFileMerger()

        # Add each PDF in the list to the merger
        for pdf_file in pdf_list:
            merger.append(pdf_file)

        # Write the merged PDFs to the output file
        merger.write(output_filename)
        merger.close()
        print(f"Merged PDFs successfully saved as '{output_filename}'")
    except Exception as e:
        print("Error merging PDFs:", str(e))

def compress_pdf(input_filename, output_filename):
    try:
        input_pdf = open(input_filename, 'rb')
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        # Add pages to the PDF writer object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # Set the compression level
        pdf_writer.setPageCompression(9)  # 0 for no compression, 9 for maximum compression

        # Write the compressed PDF to the output file
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"Compressed PDF saved as '{output_filename}'")

        input_pdf.close()
    except Exception as e:
        print("Error compressing PDF:", str(e))

def add_watermark(input_filename, output_filename, watermark_text):
    try:
        input_pdf = open(input_filename, 'rb')
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        watermark = PyPDF2.pdf.TextStringObject(watermark_text)

        # Add watermark text to each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.getPage(page_num)
            page.mergePage(watermark)
            pdf_writer.addPage(page)

        # Write the watermarked PDF to the output file
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"Watermarked PDF saved as '{output_filename}'")

        input_pdf.close()
    except Exception as e:
        print("Error adding watermark to PDF:", str(e))

def encrypt_pdf(input_filename, output_filename, password):
    try:
        input_pdf = open(input_filename, 'rb')
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        # Add each page to the PDF writer object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # Encrypt the PDF with the password
        pdf_writer.encrypt(user_pwd=password, use_128bit=True)

        # Write the encrypted PDF to the output file
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"Encrypted PDF saved as '{output_filename}'")

        input_pdf.close()
    except Exception as e:
        print("Error encrypting PDF:", str(e))


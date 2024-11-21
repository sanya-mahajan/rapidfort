import os
from docx import Document
from reportlab.pdfgen import canvas
from io import BytesIO
from pikepdf import Pdf

def convert_docx_to_pdf(input_path, output_path):
    # Extract text from .docx
    doc = Document(input_path)
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer)
    
    for paragraph in doc.paragraphs:
        c.drawString(50, 800, paragraph.text)  
        c.showPage()
    
    c.save()

    # Save PDF to file
    with open(output_path, 'wb') as pdf_file:
        pdf_file.write(pdf_buffer.getvalue())

def add_password_to_pdf(pdf_path, password):
    with Pdf.open(pdf_path) as pdf:
        pdf.save(pdf_path, encryption=Pdf.Encryption(owner=password, user=password))
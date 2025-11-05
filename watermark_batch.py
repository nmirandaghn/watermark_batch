from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from io import BytesIO
import os

def create_watermark(text, pagesize=letter):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=pagesize)
    # Gris claro con opacidad
    light_gray = Color(0.6, 0.6, 0.6, alpha=0.2)
    can.setFillColor(light_gray)
    can.setFont("Helvetica", 180)
    width, height = pagesize
    can.saveState()
    # Mover al centro
    can.translate(width / 2, height / 2)
    # Rotar 45 grados
    can.rotate(45)
    # Dibujar texto centrado en la posición actual (centro)
    can.drawCentredString(0, 0, text)
    can.restoreState()
    can.save()
    packet.seek(0)
    return PdfReader(packet)

def add_text_watermark(pdf_path, watermark_text, output_path):
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    watermark_pdf = create_watermark(watermark_text, (float(pdf_reader.pages[0].mediabox.width), float(pdf_reader.pages[0].mediabox.height)))

    watermark_page = watermark_pdf.pages[0]

    for page in pdf_reader.pages:
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    with open(output_path, 'wb') as f_out:
        pdf_writer.write(f_out)

def batch_add_text_watermark(input_dir, watermark_text, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            input_pdf = os.path.join(input_dir, filename)
            output_pdf = os.path.join(output_dir, filename)
            add_text_watermark(input_pdf, watermark_text, output_pdf)
            print(f"Marca de agua añadida: {filename}")

# Uso
input_directory = 'pdfs_originales'
watermark_text = 'Copia'
output_directory = 'pdfs_con_marca'

batch_add_text_watermark(input_directory, watermark_text, output_directory)

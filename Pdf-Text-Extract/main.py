from PyPDF2 import PdfReader
import os

reader = PdfReader("example.pdf")
page = reader.pages[0]
print(page.extract_text())
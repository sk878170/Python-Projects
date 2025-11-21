from PyPDF2 import PdfWriter, PdfReader
import getpass
pdfwriter=PdfWriter()
pdf=PdfReader("C:\Users\shubh\Downloads\6903368232.pdf")
for page_num in range(len(pdf.pages)):
  pdfwriter.add_page(pdf.pages[page_num])
passw=getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f:
  pdfwriter.write(f)
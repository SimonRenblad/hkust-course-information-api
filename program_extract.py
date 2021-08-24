import pickle
import PyPDF2  #
text = ""
with open("21-22ssci_requirements.pdf", "rb") as doc:
    read_pdf = PyPDF2.PdfFileReader(doc)
    num_pages = read_pdf.getNumPages()
    for i in range(num_pages):
        page = read_pdf.getPage(i)
        text += page.extractText()
print(text)
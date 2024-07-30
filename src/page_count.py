import PyPDF2

class PageCount:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def count_pages(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return len(reader.pages)

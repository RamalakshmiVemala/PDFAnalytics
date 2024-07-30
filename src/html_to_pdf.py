from pdfkit import from_file

class HTMLToPDF:
    def __init__(self, html_path, output_pdf):
        self.html_path = html_path
        self.output_pdf = output_pdf

    def convert(self):
        from_file(self.html_path, self.output_pdf)

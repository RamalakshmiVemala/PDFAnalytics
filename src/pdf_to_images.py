from pdf2image import convert_from_path

class PDFToImages:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def generate_images(self):
        images = convert_from_path(self.pdf_path)
        image_paths = []
        for i, image in enumerate(images):
            image_path = f"page_{i + 1}.jpg"
            image.save(image_path, "JPEG")
            image_paths.append(image_path)
        return image_paths

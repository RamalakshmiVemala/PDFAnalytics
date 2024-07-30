from PIL import Image

class ImagesToPDF:
    def __init__(self, image_paths, output_pdf):
        self.image_paths = image_paths
        self.output_pdf = output_pdf

    def generate_pdf(self):
        images = [Image.open(image_path) for image_path in self.image_paths]
        images[0].save(self.output_pdf, save_all=True, append_images=images[1:])

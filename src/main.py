from pdf_extractor import PDFExtractor
from pdf_to_images import PDFToImages
from images_to_pdf import ImagesToPDF
from html_to_pdf import HTMLToPDF
from page_count import PageCount

def main():
    print("Select an option:")
    print("1. Extract text from PDF")
    print("2. Generate images from PDF")
    print("3. Generate PDF from images")
    print("4. Convert HTML to PDF")
    print("5. Count pages in PDF")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        pdf_path = input("Enter the PDF file path: ")
        extractor = PDFExtractor(pdf_path)
        print(extractor.extract_text())
    elif choice == 2:
        pdf_path = input("Enter the PDF file path: ")
        converter = PDFToImages(pdf_path)
        images = converter.generate_images()
        print(f"Generated images: {images}")
    elif choice == 3:
        image_paths = input("Enter the image paths (comma-separated): ").split(',')
        output_pdf = input("Enter the output PDF file path: ")
        converter = ImagesToPDF(image_paths, output_pdf)
        converter.generate_pdf()
        print(f"Generated PDF: {output_pdf}")
    elif choice == 4:
        html_path = input("Enter the HTML file path: ")
        output_pdf = input("Enter the output PDF file path: ")
        converter = HTMLToPDF(html_path, output_pdf)
        converter.convert()
        print(f"Converted HTML to PDF: {output_pdf}")
    elif choice == 5:
        pdf_path = input("Enter the PDF file path: ")
        counter = PageCount(pdf_path)
        print(f"Page count: {counter.count_pages()}")
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()

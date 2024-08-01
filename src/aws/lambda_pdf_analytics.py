import json
import boto3
import os
import PyPDF2

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get the bucket name and object key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        
        # Log the bucket and object key
        print(f"Bucket: {bucket_name}, Key: {object_key}")
        
        # Download the PDF file from S3
        download_path = f'/tmp/{os.path.basename(object_key)}'
        s3.download_file(bucket_name, object_key, download_path)
        
        # Extract text from the PDF file
        text = extract_text_from_pdf(download_path)
        
        # Define the output file path
        output_key = f'out/{os.path.splitext(os.path.basename(object_key))[0]}.txt'
        upload_path = f'/tmp/{os.path.basename(output_key)}'
        
        # Save the extracted text to a new file
        with open(upload_path, 'w') as f:
            f.write(text)
        
        # Upload the text file to the S3 bucket
        s3.upload_file(upload_path, bucket_name, output_key)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Text extraction and upload complete')
        }
    except Exception as e:
        print(f"Error processing file: {e}")
        raise e

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        raise e
    return text

import streamlit as st
import PyPDF2
from io import BytesIO

# Title of the web app
st.title("PDF Content Extractor")

# Upload the PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to bytes
    bytes_data = BytesIO(uploaded_file.getvalue())
    
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfFileReader(bytes_data)
    
    # Initialize an empty string for the PDF text
    pdf_text = ""
    
    # Read the text from all pages
    for page_number in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_number)
        pdf_text += page.extractText()
    
    # Display the extracted text
    st.write(pdf_text)

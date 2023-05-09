import streamlit as st
import pdfplumber
from io import BytesIO

# Title of the web app
st.title("PDF Content Extractor")

# Upload the PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to bytes
    bytes_data = BytesIO(uploaded_file.getvalue())
    
    # Load the PDF with pdfplumber
    with pdfplumber.open(bytes_data) as pdf:
        # Initialize an empty string for the PDF text
        pdf_text = ""
        
        # Read the text from all pages
        for page in pdf.pages:
            page_text = page.extract_text()
            pdf_text += page_text + '\n'
    
    # Display the extracted text
    st.write(pdf_text)

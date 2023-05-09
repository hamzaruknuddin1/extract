import streamlit as st
import pdfplumber
import openai
from io import BytesIO
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    st.write('Extracted Text:')
    st.write(pdf_text)

    # Use OpenAI's GPT model to generate a completion based on the extracted text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pdf_text,
        temperature=0.5,
        max_tokens=100
    )

    # Display the generated text
    st.write('Generated Text:')
    st.write(response.choices[0].text.strip())

from pydantic import BaseModel, Field
from typing import List, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
from weasyprint import HTML
from pdf2image import convert_from_bytes
from html_tempate import *
from io import BytesIO
import pdfplumber

groq_api_key = st.secrets['GROQ_API_KEY']
PROMPT_TEMPLATE_SUMMARY = """
You are expert in generating summary of the document received from the user. Given the document
given below, generate the summary.

The summary should be formatted as a list of dictionaries, where:

Each dictionary represents a category.
The key is the category name (e.g., "Introduction", "Key Concepts").
The value is a list of bullet points under that category.
Do NOT include unnecessary text, only return JSON output

Given document: {document} 
                            """

# Structure the response schema using Pydantic
class Summary(BaseModel):
    """Create summary of the provided document"""
    title: str = Field(description="Title of the document.")
    bullet_points: Dict[str, List[str]] = Field(description="Summary of the document with categorized bullet points as a list of dictionary, where keys are "
                                                      "categories and values are single of multiple bullet points")

# LLM Initialization
def initialize_llm():
    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key, temperature=0.1)
    return llm

# Generate structured output of the summary of given topic
def generate_summary(extracted_text):
    # Initialize the LLM
    llm = initialize_llm()

    # Create prompt
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE_SUMMARY)
    prompt = prompt_template.format(document=extracted_text)

    # Get structured output from LLM
    structured_llm = llm.with_structured_output(Summary)
    structured_response = structured_llm.invoke(prompt)

    return structured_response.dict()

# Function to extract text from PDF file
def extract_text_from_pdf(pdf_file_path):
    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_file_path) as pdf:
        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Loop through all the pages and extract text
        for page in pdf.pages:
            extracted_text += page.extract_text()

    return extracted_text

# Display the summary in mark down format
def display_summary(response):
    st.write(f"## {response['title']}")
    for category, points in response["bullet_points"].items():
        st.subheader(f"{category}:")
        for point in points:
            st.write(f"* {point}")

# This function first converts the text into HTML format and then to PDF before downloading it
def create_pdf_from_text(response):
    html_content = generate_html_template(response)

    # Convert HTML contents to PDF bytes
    pdf_bytes = HTML(string=html_content).write_pdf()

    return pdf_bytes


def pdf_to_image(pdf_content):
    images = convert_from_bytes(pdf_content)
    image = images[0]

    # Convert PIL Image to Bytes
    img_bytes_io = BytesIO()
    image.save(img_bytes_io, format="JPEG")  # Use PNG if needed
    img_bytes = img_bytes_io.getvalue()  # Get byte data

    return img_bytes


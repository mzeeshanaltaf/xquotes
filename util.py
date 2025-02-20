from pydantic import BaseModel, Field
from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
from weasyprint import HTML
from pdf2image import convert_from_bytes
import math
from io import BytesIO

groq_api_key = st.secrets['GROQ_API_KEY']
PROMPT_TEMPLATE_SUMMARY = """
You are expert in generating summary of the topic received from the user. Given the topic
mentioned below, generate the summary 
Give Topic: {topic} 
                            """

# Structure the response schema using Pydantic
class Summary(BaseModel):
    """Create summary of the given topic"""
    title: str = Field(description="Title of the Topic.")
    bullet_points: List[str] = Field(description="Summary of the topic in bullet points")

# LLM Initialization
def initialize_llm():
    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key, temperature=0.1)
    return llm

# Generate structured output of the summary of given topic
def generate_summary(topic):
    # Initialize the LLM
    llm = initialize_llm()

    # Create prompt
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE_SUMMARY)
    prompt = prompt_template.format(topic=topic)

    # Get structured output from LLM
    structured_llm = llm.with_structured_output(Summary)
    structured_response = structured_llm.invoke(prompt)

    return structured_response.dict()

# Display the summary in markdown format
def display_summary(response):
    st.write(f"## {response['title']}")
    for points in response["bullet_points"]:
        st.write(f"* {points}")

# This function first converts the text into HTML format and then to PDF before downloading it
def create_pdf_from_text(response):
    title = f"<h1>{response['title']}</h1>\n"
    bp = "\n".join(f"<li>{points}</li>" for points in response["bullet_points"])
    content = '<ul>\n' + bp + '</ul>\n'

    # Estimate the font size needed to fill the page
    char_count = len(response['title']) + len(response['bullet_points'])
    estimated_font_size = math.sqrt(620000 / char_count)  # 620000 is an approximation of characters that fit on an A4 page
    font_size = min(max(estimated_font_size, 8), 36)  # Limit font size between 8 and 36

    # Define the HTML template
    html = f"""
        <html>
        <head>
            <style>
                @page {{ size: A4; margin: 1cm; }}
                body {{ 
                    font-family: Arial, sans-serif; 
                    font-size: {font_size}px;
                }}
                h1 {{ 
                    text-align: center; 
                    color: #333; 
                    font-size: {font_size * 1.5}px;
                }}
                p {{ 
                    color: #666; 
                    line-height: {font_size * 1.2}px;
                }}
            </style>
        </head>
        <body>
            {title}
            {content}
        </body>
        </html>
        """
    # Convert HTML contents to PDF bytes
    pdf_bytes = HTML(string=html).write_pdf()

    return pdf_bytes


def pdf_to_image(pdf_content):
    images = convert_from_bytes(pdf_content)
    image = images[0]

    # Convert PIL Image to Bytes
    img_bytes_io = BytesIO()
    image.save(img_bytes_io, format="JPEG")  # Use PNG if needed
    img_bytes = img_bytes_io.getvalue()  # Get byte data

    return img_bytes


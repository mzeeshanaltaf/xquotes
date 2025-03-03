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
from firecrawl import FirecrawlApp
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse as urlparse
import re

# Get API Keys from secrets
groq_api_key = st.secrets['GROQ_API_KEY']
firecrawl_api_key = st.secrets['FIRECRAWL_API_KEY']

# Define prompt
PROMPT_TEMPLATE_SUMMARY = """
You are expert in generating short and concise summary of the document received from the user. Given the document
given below, generate the one page summary.

The summary should be formatted as a list of dictionaries, where:

Each dictionary represents a category.
The key is the category name (e.g., "Introduction", "Key Concepts").
The value is a list of bullet points under that category.
Do NOT include unnecessary text, only return JSON output
Keep the summary short and concise, no more than one page

Given document: {document} 
                            """

PROMPT_TEMPLATE_TOPIC_SUMMARY = """
You are expert in generating short and concise summary of the topic received from the user. Given the topic
given below, generate the one page summary.

The summary should be formatted as a list of dictionaries, where:

Each dictionary represents a category.
The key is the category name (e.g., "Introduction", "Key Concepts").
The value is a list of bullet points under that category.
Do NOT include unnecessary text, only return JSON output
Keep the summary short and concise, no more than one page

Given topic: {topic} 
                            """

# Structure the response schema using Pydantic
class Summary(BaseModel):
    """Create summary of the provided document"""
    title: str = Field(description="Title of the document.")
    bullet_points: Dict[str, List[str]] = Field(description="Summary of the document with categorized bullet points as a list of dictionary, where keys are "
                                                      "categories and values are single of multiple bullet points")

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

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

# Extract text from input source. After extracting text, it returns only 7000 characters to limit LLM token usage
def extract_text(input_contents, input_method):
    if input_method == 'Upload PDF':
        text = extract_text_from_pdf(input_contents)
        return text[:7000]
    elif input_method == 'Web URL':
        text = extract_text_from_url(input_contents)
        return text[:7000]
    elif input_method == 'YouTube URL':
        video_id = get_video_id(input_contents)
        transcript_text = get_transcript_text(video_id)
        return transcript_text
    elif input_method == 'Topic':
        return input_contents

def extract_text_from_url(input_contents):
    app = FirecrawlApp(api_key=firecrawl_api_key)
    response = app.scrape_url(url=input_contents, params={'formats': ['markdown'], "onlyMainContent": True})
    extracted_text = response['markdown']

    # Remove URLs from extracted text using Regular expression
    url_pattern = r'https?://\S+'
    text_without_url = re.sub(url_pattern, '', extracted_text)
    return text_without_url

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
def create_pdf_from_text(response, design):
    if design == 1:
        html_content = generate_html_template_1(response)
    elif design == 2:
        html_content = generate_html_template_2(response)
    elif design == 3:
        html_content = generate_html_template_3(response)
    elif design == 4:
        html_content = generate_html_template_4(response)
    elif design == 5:
        html_content = generate_html_template_5(response)

    # Convert HTML contents to PDF bytes
    pdf_bytes = HTML(string=html_content).write_pdf()

    return pdf_bytes


def pdf_to_image(pdf_content):
    images = convert_from_bytes(pdf_content)
    # image = images[0]
    img_bytes = []

    for image in images:
        # Convert PIL Image to Bytes
        img_bytes_io = BytesIO()
        image.save(img_bytes_io, format="JPEG")  # Use PNG if needed
        img_bytes.append(img_bytes_io.getvalue())  # Get byte data

    return img_bytes

def get_video_id(youtube_url):
    """Extract video ID from a YouTube URL"""
    if "youtu.be" in youtube_url:
        return youtube_url.split("/")[-1].split("?")[0]
    elif "youtube.com/watch" in youtube_url:
        query = urlparse.parse_qs(urlparse.urlparse(youtube_url).query)
        return query["v"][0]
    else:
        # Assume the input is already a video ID
        return youtube_url

def get_transcript_text(video_id, languages=['en']):
    """Get transcript text only (without timestamps) for a YouTube video"""
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        # Extract only the text parts and join them
        transcript_text = ' '.join([entry['text'] for entry in transcript_data])
        return transcript_text
    except Exception as e:
        st.exception(f"An error occurred: {e}")
        return None
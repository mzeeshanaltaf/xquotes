import pathlib
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from util import *

# Page title of the application
page_title = "Summify"
page_icon = "✨"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# Session state variables
if "scope" not in st.session_state:
    st.session_state.scope = False
if "response" not in st.session_state:
    st.session_state.response = None
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None
if "image_content" not in st.session_state:
    st.session_state.image_content = None
if "design_selection" not in st.session_state:
    st.session_state.design_selection = 3
if "design_1" not in st.session_state:
    st.session_state.design_1 = True
if "design_2" not in st.session_state:
    st.session_state.design_2 = False
if "design_3" not in st.session_state:
    st.session_state.design_3 = False
if "design_4" not in st.session_state:
    st.session_state.design_3 = False
if "design_5" not in st.session_state:
    st.session_state.design_5 = False

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)

# Function to handle checkbox behavior
def update_design(selected):
    for key in ["design_1", "design_2", "design_3", "design_4", "design_5"]:
        if key != selected:
            st.session_state[key] = False

# Application Title and description
st.title(f'{page_title}{page_icon}')
st.write('***:blue[AI-Powered Summaries – Read Less, Know More!" 🤖📚]***')
st.write("""
*Summify is an AI-powered web app that generates concise and insightful summaries from various sources. 📖✨ Upload a 
document, provide a web URL, enter a YouTube video URL, or specify a topic, and Summify will create a clear and 
structured summary for you. Download your summary in PDF 📝 or JPEG 🖼️ format, making it easy to save and share. 
Simplify research, boost productivity, and stay informed effortlessly! 🚀💡*
""")

# Variable to store input provided by the user. In case of PDF upload, it will have path to pdf file and for Web URL, it
# will contain web URL
input_contents = None

# Configuration Options
st.subheader('Select Input Method:', divider='gray')
input_method = st.radio('Select Input Method', ['Upload PDF', 'Web URL', 'YouTube URL', 'Topic'], label_visibility='collapsed', horizontal=True)

# Configuration Options
st.subheader('Select Design:', divider='gray')
# Display images and handle clicks
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    selection_1 = st.checkbox("Design 1", key="design_1", on_change=update_design, args=("design_1",))
    if selection_1:
        st.session_state.design_selection = 1
    st.image('designs/design_1.jpg', width=200)

with col2:
    selection_2 = st.checkbox("Design 2", key="design_2", on_change=update_design, args=("design_2",))
    if selection_2:
        st.session_state.design_selection = 2
    st.image('designs/design_2.jpg', width=200)

with col3:
    selection_3 = st.checkbox("Design 3", key="design_3", on_change=update_design, args=("design_3",))
    if selection_3:
        st.session_state.design_selection = 3
    st.image('designs/design_3.jpg', width=200)

with col4:
    selection_4 = st.checkbox("Design 4", key="design_4", on_change=update_design, args=("design_4",))
    if selection_4:
        st.session_state.design_selection = 4
    st.image('designs/design_4.jpg', width=200)

with col5:
    selection_5 = st.checkbox("Design 5", key="design_5", on_change=update_design, args=("design_5",))
    if selection_5:
        st.session_state.design_selection = 5
    st.image('designs/design_5.jpg', width=200)

if input_method == 'Upload PDF':
    st.subheader('Upload PDF:📄️', divider='gray')
    uploaded_file = st.file_uploader("Choose a file", type=['pdf'], label_visibility='collapsed')
    input_contents = uploaded_file

elif input_method == 'Web URL':
    st.subheader('Enter Web URL:🌐️️', divider='gray')
    web_url = st.text_input('Enter Web URL', label_visibility='collapsed', placeholder='Example: www.example.com')
    input_contents = web_url

elif input_method == 'YouTube URL':
    st.subheader('Enter YouTube URL:▶️️️', divider='gray')
    web_url = st.text_input('Enter YouTube URL', label_visibility='collapsed', placeholder='Example: https://www.youtube.com/watch?v=g84CGmelvSU')
    input_contents = web_url

elif input_method == 'Topic':
    st.subheader('Enter Topic:💬️️', divider='gray')
    topic = st.text_input('Enter the Topic', label_visibility='collapsed', placeholder='Example: Generative AI')
    input_contents = topic

generate  = st.button("Generate", type='primary', icon=":material/summarize:", disabled=not input_contents)

if generate or st.session_state.scope:
    st.session_state.scope = True
    if generate:
        with st.spinner('Generating ...', show_time=True):

            # Extract text from pdf file
            extracted_text = extract_text(input_contents, input_method)

            # Generate summary of the document
            st.session_state.response = generate_summary(extracted_text)

            # Create PDF of generated summary
            st.session_state.pdf_content = create_pdf_from_text(st.session_state.response, st.session_state.design_selection)

            # Create image of generated summary
            st.session_state.image_content = pdf_to_image(st.session_state.pdf_content)

    if st.session_state.response is not None:
        st.subheader('Summary:📄', divider='gray')
        with st.expander("See Summary:", icon=":material/summarize:"):
            with st.container(border=True):
                display_summary(st.session_state.response)

        st.subheader('Preview:🔍', divider='gray')
        col1, col2 = st.columns(2, gap="small", vertical_alignment="top", border=True)

        with col1:
            st.write('***PDF Preview***')
            pdf_viewer(st.session_state.pdf_content)
            st.download_button(label="Download PDF", data=st.session_state.pdf_content, file_name="summary.pdf",
                               mime="application/pdf",
                               icon=":material/picture_as_pdf:")
        with col2:
            st.write('***Image️ Preview***')
            for image in st.session_state.image_content:
                st.image(image)
            st.download_button(label="Download Image", data=st.session_state.image_content[0], file_name="summary.png",
                               mime="image/png",
                               icon=":material/image:")


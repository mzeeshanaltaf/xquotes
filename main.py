import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from util import *

# Page title of the application
page_title = "Summify"
page_icon = "✨"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Session state variables
if "scope" not in st.session_state:
    st.session_state.scope = False
if "response" not in st.session_state:
    st.session_state.response = None
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None
if "image_content" not in st.session_state:
    st.session_state.image_content = None
# Application Title and description
st.title(f'{page_title}{page_icon}')
st.write('***:blue[AI-Powered Summaries – Read Less, Know More!" 🤖📚]***')
st.write("""
*Summify is an AI-powered web app that generates concise and insightful summaries for any topic you enter. 📖✨ 
It lets you download your summary in PDF 📝 or JPEG 🖼️ format, making it easy to save and share. Simplify research, 
boost productivity, and stay informed effortlessly! 🚀💡*
""")

st.subheader('Enter Topic:🗂️', divider='gray')
topic = st.text_input('Enter Topic Title', max_chars=200, label_visibility='collapsed')
generate  = st.button("Generate", type='primary', disabled=not topic, icon=":material/summarize:")
if generate or st.session_state.scope:
    st.session_state.scope = True
    if generate:
        with st.spinner('Generating ...', show_time=True):
            st.session_state.response = generate_summary(topic)
            st.session_state.pdf_content = create_pdf_from_text(st.session_state.response)
            st.session_state.image_content = pdf_to_image(st.session_state.pdf_content)

    if st.session_state.response is not None:
        st.subheader('Summary:📄', divider='gray')
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
            st.image(st.session_state.image_content)
            st.download_button(label="Download Image", data=st.session_state.image_content, file_name="summary.png",
                               mime="image/png",
                               icon=":material/image:")


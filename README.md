# Summify ✨
AI-Powered Summaries – Read Less, Know More!" 🤖📚

Summify is an AI-powered web app that generates concise and insightful summaries for your document. 📖✨ 
It lets you download your summary in PDF 📝 or JPEG 🖼️ format, making it easy to save and share. Simplify research, 
boost productivity, and stay informed effortlessly! 🚀💡

# Application Link
https://summify-st.streamlit.app/

# Technologies Used
* Streamlit -- Front end development
* LangChain -- LLM Orchestration
* Groq -- Chat models
* WeasyPrint -- HTML to PDF Conversion
   
# System Requirements
You must have Python 3.11 or later installed.
You need to have the following tools installed in your system:
* Windows:
  * Poppler -- Get the latest release from [here](https://github.com/oschwartz10612/poppler-windows/releases). Make sure to add the bin/ directory from the extracted Poppler package to your system's PATH environment variable. 
  * WeasyPrint -- Get the latest release from [here](https://github.com/Kozea/WeasyPrint/releases) and install it.
* Linux:
  * `sudo apt-get install libxml2-dev libxslt-dev libffi-dev libcairo2-dev libpango1.0-dev poppler-utils`

# Installation
1. Clone this repository
2. Create a virtual environment
3. Install the necessary python packages:
   `pip install -r requirements.txt`
4. Set `GROQ_API_KEY` and `FIRECRAWL_API_KEY` in `.streamlit/secrets.toml` file
5. Run the application with following command from terminal:

   `streamlit run main.py`

# Screen Shots
![img.png](screenshots/img.png)
![img_2.png](screenshots/img_2.png)
![img_1.png](screenshots/img_1.png)
![img_3.png](screenshots/img_3.png)
![img_4.png](screenshots/img_4.png)
![img_5.png](screenshots/img_5.png)
![img_6.png](screenshots/img_6.png)
![img_7.png](screenshots/img_7.png)

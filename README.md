# QA App

Made with love by Aryaman and Tejas!

Ever encountered a situation where ChatGPT couldn't provide the answers you need because its knowledge cutoff is set to 2021? Our application addresses this challenge by enabling you to query your own documents using the power of OpenAI’s API.

With our application, you can upload a PDF file, enter your OpenAI API key, and get answers to all your queries based on the content of the document.

## Features

- **PDF Document Analysis**: Upload any PDF file and ask questions based on the content.
- **OpenAI Integration**: Utilize OpenAI’s API to get accurate and up-to-date responses directly from your document.
- **Customizable Chunk Processing**: Control how much of the document to process, ensuring efficiency and relevance.
- **User-Friendly Interface**: The application is designed to be intuitive, allowing easy uploads and interaction through a streamlined UI.

## Running the App on Streamlit

In addition to running the application on Google Colab, we now provide a professional and interactive **Streamlit** app version for local use:

### How to Run the Streamlit App:

1. **Ensure Dependencies**: Make sure you have all the necessary libraries installed:
   ```bash
   pip install streamlit langchain openai chromadb pypdf panel

import streamlit as st
import os
from pathlib import Path
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# App Title and Sidebar Setup
st.set_page_config(page_title="Professional QA App", layout="wide")
st.title("📄 Professional Question-Answering App")

st.sidebar.header("Upload Your PDF and API Key")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
chunk_limit = st.sidebar.slider("Number of Relevant Chunks", 1, 20, 5)
chain_type = st.sidebar.selectbox("Select Chain Type", ["stuff", "refine"])

# Main Area for Input and Output
st.write("## Ask Your Question")
question = st.text_input("Enter your question:")

if st.button("Run QA"):
    # Ensure all inputs are provided
    if not uploaded_file or not api_key or not question:
        st.error("Please provide a PDF file, API key, and question to proceed.")
    else:
        try:
            # Save the uploaded file temporarily
            temp_file_path = Path("temp_uploaded_file.pdf")
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Set API Key environment variable
            os.environ["OPENAI_API_KEY"] = api_key

            # Function to load and split documents
            def load_and_process_documents(file_path):
                loader = PyPDFLoader(str(file_path))
                documents = loader.load()
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                chunks = text_splitter.split_documents(documents)
                return chunks

            # Load and process the document
            chunks = load_and_process_documents(temp_file_path)
            chunks = chunks[:chunk_limit]  # Limit the number of chunks

            # Setup embeddings and vectorstore
            embeddings = OpenAIEmbeddings()
            vectorstore = Chroma.from_documents(chunks, embeddings)

            # Load QA chain and run the query
            chain = load_qa_chain(OpenAI(), chain_type=chain_type)
            result = chain.run(input_documents=chunks, question=question)

            # Display the result
            st.success("Answer:")
            st.write(result)

            # Remove the temporary file after processing
            temp_file_path.unlink()

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    </style>
    <footer style="text-align:center;">
        Made with ❤️ by Tejas & Aryaman
    </footer>
    """, unsafe_allow_html=True
)

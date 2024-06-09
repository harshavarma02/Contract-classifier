import os
import streamlit as st
#from llama_index.readers.file import PDFReader
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import streamlit.components.v1 as components
from pypdf import PdfReader

# Download PDFReader
contract_template = PdfReader("Contract-Comparison/Sample-Contract-Agreement-Template-PDF.pdf")
contract_template_text = contract_template.pages[0].extract_text()

contract = PdfReader("Contract-Comparison/Contract document.pdf")
contract_text = contract.pages[0].extract_text()



# Set Google API key
GOOGLE_API_KEY = ""
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = Gemini(model="models/gemini-1.5-flash-latest", temperature=0, embedding=GeminiEmbedding,)

def main():
    '''st.title("Knowledge Graph App")
    
    template = ''
    contract = ''
    # File upload
    uploaded_template_file = st.file_uploader("Upload a template file", type="pdf")
    
    if uploaded_template_file is not None:
        template = parser.load_data(file=uploaded_template_file)

    uploaded_Contract_file = st.file_uploader("Upload the Contract file", type="pdf")
    
    if uploaded_Contract_file is not None:
        contract = parser.load_data(file=uploaded_Contract_file)

    if contract and template:'''
    deviations = llm.complete(f"You are a contract validator, You will be provided a template {contract_template_text}, return the contract {contract_text} in html and color those parts which does not follow the template and mention dates with red color")
    st.write_stream(deviations)


if __name__ == "__main__":
    main()


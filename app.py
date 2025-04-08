import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf_by_sections(pdf_path, sections, output_folder):
    reader = PdfReader(pdf_path)
    for section in sections:
        title = section["title"]
        start_page = section["start_page"] - 1
        end_page = section["end_page"] - 1
        writer = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])
        sanitized_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
        output_path = os.path.join(output_folder, f"{sanitized_title}.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        st.success(f"Saved: {output_path}")

st.title("PDF Splitter For Journal Migration Project")
st.write("Upload a PDF and define sections to split it into smaller PDFs.")

# File upload
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
output_folder = st.text_input("Output Folder", value="Folder_path")

# Section input for json input in the stream lit app
sections = st.text_area(
    "Define Sections (JSON format)",
    value="""[
    {"title": "Section 1", "start_page": 1, "end_page": 5},
    {"title": "Section 2", "start_page": 6, "end_page": 10}
    ]"""
)

if st.button("Split PDF"):
    if uploaded_file and output_folder and sections:
        try:
            sections = eval(sections)  # Convert JSON string to Python list
            os.makedirs(output_folder, exist_ok=True)
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            split_pdf_by_sections("temp.pdf", sections, output_folder)
            st.success("PDF split successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please upload a PDF, specify an output folder, and define sections.")
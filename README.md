# 📄 PDF Section Splitter – A Lightweight PDF Processor

A simple and intuitive **Streamlit-based web application** that allows users to upload a PDF file and split it into smaller PDFs based on custom-defined sections. Perfect for anyone working with large PDFs—whether you're processing academic journals, contracts, reports, or ebooks.

---

## 🚀 Features

- 🖇️ **Split by Section**: Define multiple sections by specifying page ranges and titles.
- 📤 **Web-Based Interface**: Easily upload PDFs and specify outputs via a user-friendly form.
- 📁 **Custom Output Folder**: Choose where the split PDFs will be saved.
- ✅ **Clean Filenames**: Section titles are automatically sanitized for safe file naming.
- ⚙️ **Streamlit-Powered**: Run locally in the browser with minimal setup.

---

## 🛠️ How It Works

1. **Upload your PDF** using the interface.
2. **Specify the output folder** where the split PDFs should be saved.
3. **Define the sections** in JSON format, like this:

```json
[
  {"title": "Chapter 1 - Overview", "start_page": 1, "end_page": 5},
  {"title": "Chapter 2 - Analysis", "start_page": 6, "end_page": 10}
]
```

4. Click **"Split PDF"**, and each section will be saved as an individual PDF.

---

## 🧰 Installation

To run this app locally:

```bash
git clone https://github.com/yourusername/pdf-section-splitter.git
cd pdf-section-splitter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the app:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
pdf-section-splitter/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # Project readme
```

---

## ✅ Requirements

- Python 3.7+
- Streamlit
- PyPDF2

To install manually:

```bash
pip install streamlit PyPDF2
```

---

## 🧠 Use Cases

- Journal and academic paper processing  
- Contract segmentation  
- Chapter-based ebook splitting  
- Report archiving  
- Government or legal document organization  

---

## ⚠️ Note on File Paths

Ensure the specified output folder is valid on your system. If it doesn’t exist, the app will try to create it.

---

## 💡 Future Ideas

- Drag-and-drop section creator  
- Support for bookmarks/table of contents  
- Preview page thumbnails  
- Batch splitting mode  

---

## 🤝 Contributing

Contributions and feedback are welcome! If you’d like to improve this tool, feel free to fork it, open issues, or submit pull requests.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

Built with ❤️ using [Streamlit](https://streamlit.io/) and [PyPDF2](https://pypi.org/project/PyPDF2/).

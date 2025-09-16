# RAG (Retrieval-Augmented Generation) Project

This is my first end-to-end Retrieval-Augmented Generation (RAG) application, built with open-source tools. The project demonstrates how to connect a **Vector Database (ChromaDB)** with a **Transformer-based LLM (Flan-T5 / LLaMA)** to answer questions grounded in custom documents.

---

## 📌 Features
- Load and split documents (PDFs, HR policies, pension docs, university brochures, etc.)
- Generate sentence embeddings using Hugging Face **sentence-transformers**
- Store and query vectors in **ChromaDB**
- Use **Flan-T5 (open)** or **LLaMA (on approval)** for natural language generation
- Interactive **Streamlit UI** for querying
- RAG pipeline that ensures **context-aware answers** and reduces hallucination

---

## 🏗️ Tech Stack
- **Python 3.11**
- **Hugging Face Transformers** (Flan-T5, LLaMA)
- **Sentence Transformers**
- **ChromaDB** (Vector Database)
- **LangChain** (retrieval orchestration)
- **Streamlit** (frontend UI)

---

## 📂 Project Structure
```
RAG-Project/
│── data/                  # PDF documents
│── db/                    # ChromaDB persistence (created on runtime)
│── main.py                # Calls other modules systematically
│── load.py                # Loads PDFs from “/data” folder
│── split.py               # Splits documents and chunks them
│── embed.py               # Embeds chunks and loads them into the vector database
│── generation.py          # Retrieval + LLM generation
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

---

## ⚡ Setup Instructions
```bash
# Clone repo
git clone https://github.com/savarbharadwaj/rag-project.git
cd rag-project

# Create virtual environment
python3 -m venv .venv

# Activate environment
# Mac/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

- Add your documents: place PDFs in the **data/** folder  
- Run the Streamlit app:
```bash
streamlit run main.py
```

---

## 🚀 Usage
1. Enter a query in the Streamlit app  
2. The system retrieves relevant chunks from **ChromaDB**  
3. The **LLM (Flan-T5 / LLaMA)** answers using only the provided context  
4. If context is missing → the model responds with *"I don’t know"*  

---

## 🔮 Future Improvements
- Integrate **LLaMA-2** for stronger answers (GPU required)  
- Support more file types (Word, TXT)  
- Add a **chat-style UI with history**  
- Deploy on cloud (**Streamlit Cloud / Hugging Face Spaces**)  

---

## 👤 Author
**Savar Bharadwaj**  
- 🌍 Passionate about AI/ML, Data Engineering, and Generative AI  
- 💼 Currently expanding skills in **AI Engineering**  

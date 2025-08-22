# UG Student Handbook RAG Chatbot

A local, privacy-first Retrieval-Augmented Generation (RAG) chatbot for answering questions about your university's UG Student Handbook. Powered by Ollama (DeepSeek R1 1.5B), LangChain, and Streamlit.

---

## Features
- **Accurate, handbook-based answers:** Only responds using the provided segmented handbook PDFs.
- **Modern Chat UI:** ChatGPT-style interface via Streamlit.
- **Private & Local:** No data leaves your machine. Runs fully offline with Ollama.
- **No Hallucination:** Strict prompt and retrieval settings to avoid made-up answers.

---

## Quickstart

### 1. Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
- DeepSeek R1 1.5B model pulled: `ollama pull deepseek-r1:1.5b`

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare your data
- Place your segmented UG Student Handbook PDFs in the `data/` folder.
- Remove any unrelated PDFs.

### 4. Populate the database
```bash
python populate_database.py --reset
```

### 5. Start the chat UI
```bash
streamlit run app.py
```
- Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Usage
- Type your question about the UG Handbook in the chat.
- The bot will respond only using information from your handbook PDFs.


---

## Troubleshooting
- **Ollama not found:** Ensure Ollama is installed and running (`ollama serve`).
- **Model not found:** Run `ollama pull deepseek-r1:1.5b`.
- **No answers returned:** Ensure your PDFs are in `data/` and database is populated.
- **Deprecation warnings:** This project uses the latest LangChain packages as of July 2025.

---

## Credits
- Built with [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/), [Streamlit](https://streamlit.io/), [DeepSeek R1 1.5B](https://huggingface.co/deepseek-ai/DeepSeek-V2), and [PyPDF](https://pypdf.readthedocs.io/).

---
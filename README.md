# RAG-Based AI Assistant

An AI-powered question-answering system that retrieves relevant information from video transcripts and generates accurate, context-aware responses — with significantly reduced hallucinations through data grounding.

---

## 🧠 How It Works

```
User Question
     ↓
Semantic Search (bge-m3 embeddings)
     ↓
Retrieve Relevant Transcript Chunks
     ↓
Gemini API generates grounded response
     ↓
Accurate, context-aware answer
```

Traditional LLMs hallucinate because they rely solely on training data. This system grounds every response in real transcript content — the model only answers from what's actually in your documents.

---

## ✨ Features

- **Semantic search** using `bge-m3` vector embeddings — understands meaning, not just keywords
- **Vector similarity retrieval** to fetch the most relevant transcript segments
- **Context-aware response generation** via Gemini API
- **Grounded answers** — dramatically reduced AI hallucinations
- **Video transcript Q&A** — ask anything about long-form video content
- **Scalable RAG pipeline** — easily extend to new document sources

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Embeddings** | bge-m3 |
| **LLM** | Gemini API |
| **Vector Operations** | NumPy, Scikit-learn |
| **Language** | Python |

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/prathamparmar1/RAG-AI-Assistant.git
cd RAG-AI-Assistant

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your Gemini API key
```

---

## 🔑 Environment Variables

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🚀 Usage

```python
# 1. Ingest your transcript
python ingest.py --source transcript.txt

# 2. Ask a question
python query.py --question "What did the speaker say about neural networks?"
```
# How to use this RAG AI Teaching Assistant on your own data

## Step 1 - Collect your videos
Move all your videos files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by running process_vid_to_aud

## Step 3 - Convert mp3 to JSON
Convert all the mp3 files to json by running mp3_to_json

## Step 4 - COnvert the json files to Vectors
Use the file proprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM 
Read the joblib file and load it into the memory. Then create a relavent promptas per the user query and feed it to the LLM. Use file process_incoming for this.

## 📬 Contact

**Pratham Parmar** — [prathamparmar203@gmail.com](mailto:prathamparmar203@gmail.com) · [Portfolio](https://prathamparmar-portfolio.vercel.app/) · [LinkedIn](https://linkedin.com/in/prathamparmar1)

🛰️ Quarry Satellite RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot designed to answer questions about stone quarry detection using satellite imagery and remote sensing concepts.

🚀 Overview

This project combines a local Large Language Model (LLM), a vector database, and a domain-specific knowledge base to answer questions about quarry detection and satellite image analysis.

The chatbot retrieves relevant information from stored documents and uses the retrieved context to generate responses.

✨ Features

- Quarry-specific remote sensing knowledge base
- Text chunking and embedding generation
- Semantic search using ChromaDB
- Local LLM responses using Qwen 2.5 7B through Ollama
- Interactive Streamlit web interface
- Information about Sentinel-2 bands, NDVI, and change detection

🛠️ Tech Stack

- Python
- Ollama
- Qwen 2.5 7B
- Streamlit
- ChromaDB
- Sentence Transformers
- NumPy

📁 Project Structure

satellite-rag/
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── chatbot/
│   └── llm.py
├── data/
│   └── documents/
│       └── quarry_rag_knowledge.txt
├── rag/
│   ├── chunker.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_db.py
└── satellite/

⚙️ Setup and Installation

1. Install Python

Install Python 3.10 or later. A compatible Python version is recommended for the project's dependencies.

2. Install Ollama

Install Ollama from https://ollama.com/

Download the model:

ollama pull qwen2.5:7b

3. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd satellite-rag

4. Install dependencies

python -m pip install -r requirements.txt

5. Prepare the knowledge base

Place the quarry knowledge document inside:

data/documents/

6. Build the vector database

python ingest.py

7. Run the chatbot

python -m streamlit run app.py

Open the local URL displayed in the terminal.

🧠 How It Works

1. Load the quarry knowledge documents.
2. Split the documents into smaller text chunks.
3. Convert the chunks into embeddings.
4. Store the embeddings and text in ChromaDB.
5. Retrieve relevant chunks for a user's question.
6. Pass the retrieved context to Qwen 2.5.
7. Display the generated response through Streamlit.

🛰️ Current Scope

The current implementation is a text-based RAG chatbot for quarry and satellite remote sensing knowledge.

Satellite image classification, quarry segmentation, and automated detection from uploaded imagery are future development goals and are not yet implemented.

🔮 Future Improvements

- Satellite image upload and visualization
- Image preprocessing and spectral index calculation
- Quarry detection using deep learning
- Before-and-after satellite image change detection
- Map-based quarry monitoring

⚠️ Disclaimer

Chatbot responses are informational and should be verified against reliable remote sensing data and domain expertise. Low vegetation index values alone do not confirm the presence of a quarry.

👨‍💻 Author

Developed as a learning project exploring RAG, local language models, and satellite remote sensing.
# RAG_System

A small Retrieval-Augmented Generation (RAG) demo focused on extracting Subnautica wiki content, embedding it with a sentence-transformer, storing vectors in ChromaDB, and answering user questions with an LLM using retrieved context.

## Project Overview

- Scrape selected Subnautica wiki pages into plain text files in `data/`.
- Chunk the scraped text, compute embeddings, and persist them in a local ChromaDB database (`subnautica_db/`).
- Query the vector store to retrieve relevant chunks for a user question and pass the retrieved context to an LLM (via Ollama) to produce an answer constrained to that context.

This project demonstrates a simple, reproducible RAG pipeline using open-source components.

## Repository Structure

- `data/` — scraped plain-text wiki pages (e.g. `seamoth.txt`, `magnetite.txt`).
- `scripts/scraper.py` — scrapes predefined Subnautica wiki pages and saves text to `data/`.
- `scripts/chunking_and_embeddings.py` — chunks the scraped text, creates embeddings (all-MiniLM-L6-v2), and upserts them to ChromaDB.
- `scripts/rag_pipeline.py` — example query flow: retrieve top-k chunks from ChromaDB and call an LLM (Ollama) to answer using only the retrieved context.
- `subnautica_db/` — persistent ChromaDB files (created after running the embeddings script).
- `requirements.txt` — Python dependencies used by the project.
- `analysis.md` — notes on experiments, chunk sizing, and failure cases.

## Quick Start

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Scrape the wiki pages (creates files in `data/`):

```powershell
python scripts\scraper.py
```

3. Create chunks and build the vector DB:

```powershell
python scripts\chunking_and_embeddings.py
```

4. Run the RAG demo (example queries are in the script):

```powershell
python scripts\rag_pipeline.py
```

## Notes & Configuration

- ChromaDB path: `scripts/chunking_and_embeddings.py` and `scripts/rag_pipeline.py` expect a local persistent ChromaDB (by default `./subnautica_db` or `../subnautica_db` depending on how you run the script). Adjust the `PersistentClient(path=...)` call if you want a custom location.
- Embeddings: the pipeline uses `all-MiniLM-L6-v2` via sentence-transformers. Change `model_name` in `chunking_and_embeddings.py` to try other models.
- LLM backend: `rag_pipeline.py` uses the `ollama` client (`ollama.chat`) and specifies `model='llama3.2'`. Ensure Ollama is installed and the model name matches a local Ollama model. If you use a different LLM provider, modify the generation call accordingly.
- Chunk sizing: see `analysis.md` for experiments and recommended chunk_size (the repo uses 1200 chars with overlap 120 to reduce missed facts).
- Safety prompt: `rag_pipeline.py` constrains the LLM to use only retrieved context and to reply with a fallback line if the answer cannot be found in the context.

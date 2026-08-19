import os
import chromadb
from chromadb.utils import embedding_functions

# Initialize Vector Database
chroma_client = chromadb.PersistentClient(path="./subnautica_db")

# Set up the embedding model
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Create a collection for the Subnautica data
collection = chroma_client.get_or_create_collection(
    name="subnautica_knowledge",
    embedding_function=embedding_fn
)

# Chunking function
def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 120):
    """
    Splits the input text into chunks of specified size with a defined overlap.

    Args:
        text (str): The input text to be chunked.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The number of overlapping characters between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# Process the files
documents, ids, metadatas = [], [], []

print("Processing scrapped data...")
for filename in os.listdir("data"):
    if filename.endswith(".txt"):
        with open(os.path.join("data", filename), "r", encoding="utf-8") as f:
            raw_text = f.read()

            # Perform the chunking
            chunks = chunk_text(raw_text)

            # Prepare the chunks for ChromaDB
            for i, chunk in enumerate(chunks):
                doc_id = f"{filename}_chunk_{i}"

                documents.append(chunk)
                ids.append(doc_id)
                metadatas.append({"source": filename})

# Save the database
print(f"Embedding and storing {len(documents)} chunks...")
collection.upsert(
    documents=documents,
    ids=ids,
    metadatas=metadatas
)

print("\nSuccess! All data has been chunked, embedded and stored in ChromaDB.")
import os
import chromadb
from chromadb.utils import embedding_functions
import ollama

# Connect to the existing database
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "subnautica_db")
chroma_client = chromadb.PersistentClient(path=db_path)

# Load embedding model
embdedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Load our data
collection = chroma_client.get_collection(
    name="subnautica_knowledge",
    embedding_function=embdedding_fn
)

def ask_subnautica_ai(question: str):
    print(f"Question: {question}")
    print("Searching the wiki data...\n")

    # Retrieve top-k relevant chunks
    results = collection.query(
        query_texts=[question],
        n_results=3,
        include = ["documents", "distances", "metadatas"]
    )

    retrieved_chunks = results['documents'][0]
    distances = results['distances'][0]

    print("--- Retrieved Chunks & Distances Scores ---")
    for chunk, dist in zip(retrieved_chunks, distances):
        # Print only the first 100 characters of each chunk
        print(f"[Distance: {dist:.4f}] {chunk}...\n")

    # Build the context for the AI model
    context = "\n\n---\n\n".join(retrieved_chunks)

    # Prompt engineering
    prompt = f"""You are an expert Subnautica AI assistant.
    Answer the user's question using ONLY the provided context below.
    If the answer is not in the context, say "I cannot answer this based on the provided information."

    Context:
    {context}

    Question:{question}
    Answer:"""

    print("Generating response...\n")

    # Generate the response
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    print("--- AI Response ---")
    print(response["message"]["content"])
    print("\n" + "=" * 50)

# Testing the AI
if __name__ == "__main__":
    ask_subnautica_ai("What is the maximum depth the Seamoth can reach with upgrades?")
    ask_subnautica_ai("Where can I find Magnetite?")
    ask_subnautica_ai("Can the Seamoth Laser Cannon kill the Reaper Leviathan?")
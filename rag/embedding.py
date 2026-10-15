
from sentence_transformers import SentenceTransformer
from rag.document_loader import load_csv
from rag.text_chunker import create_chunks


# Load dataset
documents = load_csv("data/company-document-text.csv")

# Create chunks
all_chunks = []

for document in documents:
    chunks = create_chunks(document["text"])

    for chunk in chunks:
        all_chunks.append(chunk)

print("Total chunks:", len(all_chunks))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert text into vectors
embeddings = model.encode(all_chunks)

print("Embedding generation completed!")
print("Total embeddings:", len(embeddings))
print("Vector dimensions:", len(embeddings[0]))

print("First embedding:")
print(embeddings[0][:5])

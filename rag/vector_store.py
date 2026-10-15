from sentence_transformers import SentenceTransformer
import chromadb

from rag.document_loader import load_csv
from rag.text_chunker import create_chunks


# Load documents
documents = load_csv("data/company-document-text.csv")

all_chunks = []
chunk_ids = []


# Create chunks
for document in documents:

    chunks = create_chunks(document["text"])

    for i, chunk in enumerate(chunks):

        all_chunks.append(chunk)

        chunk_id = str(document["id"]) + "_" + str(i)
        chunk_ids.append(chunk_id)


print("Total documents:", len(documents))
print("Total chunks:", len(all_chunks))


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(all_chunks)


# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")


# Delete old collection
try:
    client.delete_collection(name="company_documents")
    print("Old collection deleted.")
except Exception:
    print("No old collection found.")


# Create fresh collection
collection = client.create_collection(
    name="company_documents"
)


# Store data
collection.add(
    ids=chunk_ids,
    documents=all_chunks,
    embeddings=embeddings.tolist()
)


print("Data stored successfully!")
print("Total records in database:", collection.count())
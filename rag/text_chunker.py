
from rag.document_loader import load_csv


def create_chunks(text, chunk_size=100, overlap=20):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":

    documents = load_csv("data/company-document-text.csv")

    all_chunks = []

    for document in documents:

        chunks = create_chunks(document["text"])

        for chunk in chunks:

            all_chunks.append({
                "document_id": document["id"],
                "text": chunk
            })

    print("Chunking Successful!")

    print("Total Documents:", len(documents))
    print("Total Chunks:", len(all_chunks))

    print("\nFirst Chunk:")
    print(all_chunks[0]["text"])

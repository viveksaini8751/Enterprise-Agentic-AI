
from rag.document_loader import load_csv
def search_documents(question, n_results=10):

    documents = load_csv("data/company-document-text.csv")

    # Check if the question contains an order ID
    words = question.lower().replace("?", "").split()
    order_id = None

    for i, word in enumerate(words):
        if word in ("order", "invoice") and i + 1 < len(words):
            next_word = words[i + 1].strip(".,:#")

            if next_word == "id" and i + 2 < len(words):
                next_word = words[i + 2].strip(".,:#")

            if next_word.isdigit():
                order_id = next_word
                break

    # Find an exact matching order
    if order_id:
        exact_matches = []

        for document in documents:
            text = document["text"]
            normalized_text = " ".join(text.lower().split())

            if (
                f"order id {order_id} " in normalized_text
                or f"invoice order id {order_id} " in normalized_text
            ):
                exact_matches.append(text)

        if exact_matches:
            return {"documents": [exact_matches[:n_results]]}

    # Use semantic search for other questions
    question_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    return results

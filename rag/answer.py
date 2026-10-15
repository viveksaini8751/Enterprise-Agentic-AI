
from ollama import chat

from rag.retriever import search_documents
from rag.document_loader import load_csv


def get_answer(question):

    # Find an exact order ID in the question
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

    # Find the exact record in the dataset
    if order_id:
        documents = load_csv("data/company-document-text.csv")

        for document in documents:
            text = document["text"]
            normalized_text = " ".join(text.lower().split())

            if (
                f"order id {order_id} " in normalized_text
                or f"invoice order id {order_id} " in normalized_text
            ):

                if "customer" in question.lower():

                    marker = "customer name "
                    start = normalized_text.find(marker)

                    if start != -1:
                        name_start = start + len(marker)

                        # Find the next field after the customer name
                        end = len(normalized_text)

                        for field in [
                            " employee details ",
                            " shipper details ",
                            " order details ",
                            " product details ",
                        ]:
                            field_position = normalized_text.find(
                                field, name_start
                            )

                            if field_position != -1:
                                end = min(end, field_position)

                        name = normalized_text[name_start:end].strip()

                        return (
                            f"The customer for order {order_id} "
                            f"is {name}."
                        )

                break

    # Use RAG and Llama for other questions
    results = search_documents(question)
    relevant_documents = results["documents"][0]

    if not relevant_documents:
        return "Information not found in the context."

    context = "\n\n".join(relevant_documents)

    prompt = f"""
Answer using only the provided context.
Do not guess or invent information.
Copy names, IDs, dates, and prices exactly as written.
If information is missing, say it is not found.

Context:
{context}

Question:
{question}

Answer:
"""

    response = chat(
        model="llama3.2:3b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={"temperature": 0}
    )

    return response["message"]["content"]


if __name__ == "__main__":

    question = input("Ask a question: ")
    answer = get_answer(question)

    print("\nAnswer:")
    print(answer)

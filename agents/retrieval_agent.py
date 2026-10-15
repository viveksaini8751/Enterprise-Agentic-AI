
from rag.retriever import search_documents


def retrieve_information(question):

    results = search_documents(question)

    documents = results["documents"][0]

    if not documents:
        return "No relevant documents found."

    return "\n\n".join(documents)


if __name__ == "__main__":

    question = input("Enter your question: ")

    context = retrieve_information(question)

    print("\nRetrieved Information:")
    print(context)

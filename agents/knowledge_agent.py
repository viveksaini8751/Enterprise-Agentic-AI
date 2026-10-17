
import re

from agents.retrieval_agent import retrieve_information
from agents.answer_agent import generate_answer
from agents.validation_agent import validate_answer


def extract_source_details(context):
    """Extract useful fields from retrieved document text."""
    details = {}

    patterns = {
        "Order ID": r"order id\s+(\d+)",
        "Customer Name": r"customer name\s+(.+?)(?=\s+employee details|\s+employee name|\s+ship address|\s+order date|\s+customer id|$)",
        "Order Date": r"order date\s+(\d{4}-\d{2}-\d{2})",
        "Country": r"ship country\s+([a-zA-Z ]+?)(?=\s+customer details|\s+invoice|\s+page\s+\d+|$)",
        "Total Price": r"total price\s+(?:total price\s+)?(\d+(?:\.\d+)?)",
    }

    for field, pattern in patterns.items():
        match = re.search(pattern, context, re.IGNORECASE)
        if match:
            details[field] = match.group(1).strip()

    return details


def ask_question_with_sources(question):
    # Step 1: Retrieve relevant context
    context = retrieve_information(question)

    if context == "No relevant documents found.":
        return {
            "answer": context,
            "sources": [],
            "source_details": {}
        }

    # Step 2: Generate an answer
    answer = generate_answer(question, context)

    # Step 3: Validate the answer
    validation = validate_answer(answer, context)

    if validation != "Validation passed.":
        answer = validation + "\nGenerated answer: " + answer

    # Step 4: Extract structured source details
    source_details = extract_source_details(context)

    return {
        "answer": answer,
        "sources": [context],
        "source_details": source_details
    }


def ask_question(question):
    # Keep the original function compatible
    result = ask_question_with_sources(question)
    return result["answer"]


if __name__ == "__main__":
    question = input("Ask your question: ")
    result = ask_question_with_sources(question)

    print("\nFinal Answer:")
    print(result["answer"])

    print("\nSource Details:")
    for field, value in result["source_details"].items():
        print(f"{field}: {value}")

    print("\nRetrieved Sources:")
    for source in result["sources"]:
        print(source)

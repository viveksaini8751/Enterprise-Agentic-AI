
from agents.retrieval_agent import retrieve_information
from agents.answer_agent import generate_answer
from agents.validation_agent import validate_answer


def ask_question(question):

    # Step 1: Retrieve information
    context = retrieve_information(question)

    if context == "No relevant documents found.":
        return context

    # Step 2: Generate answer
    answer = generate_answer(question, context)

    # Step 3: Validate the answer
    validation = validate_answer(answer, context)

    if validation != "Validation passed.":
        return validation + "\nGenerated answer: " + answer

    return answer


if __name__ == "__main__":

    question = input("Ask your question: ")

    answer = ask_question(question)

    print("\nFinal Answer:")
    print(answer)

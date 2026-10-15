
from ollama import chat


def generate_answer(question, context):

    prompt = f"""
You are an enterprise knowledge assistant.

Answer the user's question using only the provided context.
Do not invent information.
Keep the answer short and clear.
If the answer is missing, say it is not available in the context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={"temperature": 0}
    )

    return response["message"]["content"]


if __name__ == "__main__":

    question = input("Enter your question: ")

    context = input("Enter context: ")

    answer = generate_answer(question, context)

    print("\nGenerated Answer:")
    print(answer)

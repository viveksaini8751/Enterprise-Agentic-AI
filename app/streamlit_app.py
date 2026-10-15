
import streamlit as st

from agents.knowledge_agent import ask_question


st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Enterprise Agentic AI Knowledge Assistant")

st.write(
    "Ask questions about company documents using RAG and AI agents."
)

st.markdown("---")

# Example questions
st.subheader("Try an example question")

examples = [
    "What is the total price of order 10718?",
    "Who is the customer for order 10718?",
    "What is the order date for order 10718?",
    "What is the shipping country for order 10718?"
]

selected_question = st.selectbox(
    "Choose a question",
    examples
)

if st.button("Use Example"):
    st.session_state["question"] = selected_question

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show previous messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Question input
question = st.chat_input("Ask about a company document...")

if question:

    st.session_state["messages"].append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching documents and generating answer..."):
            answer = ask_question(question)

        st.write(answer)

    st.session_state["messages"].append({
        "role": "assistant",
        "content": answer
    })

# Example question helper
if "question" in st.session_state:
    st.info(
        "Example selected: "
        + st.session_state.pop("question")
    )

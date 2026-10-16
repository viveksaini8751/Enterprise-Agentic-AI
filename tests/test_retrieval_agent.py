
from agents.retrieval_agent import retrieve_information


def test_retrieval_returns_relevant_order():
    result = retrieve_information(
        "Who is the customer for order 10718?"
    )

    assert result != "No relevant documents found."
    assert "10718" in result
    assert "koene" in result.lower()

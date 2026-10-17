
from agents import knowledge_agent


def test_knowledge_agent_returns_answer_and_sources(monkeypatch):
    monkeypatch.setattr(
        knowledge_agent,
        "retrieve_information",
        lambda question: "Order ID 10718. Total price 3463.0."
    )

    monkeypatch.setattr(
        knowledge_agent,
        "generate_answer",
        lambda question, context: "The total price of order 10718 is 3463.0."
    )

    monkeypatch.setattr(
        knowledge_agent,
        "validate_answer",
        lambda answer, context: "Validation passed."
    )

    result = knowledge_agent.ask_question_with_sources(
        "What is the total price of order 10718?"
    )

    assert result["answer"] == "The total price of order 10718 is 3463.0."
    assert result["sources"] == ["Order ID 10718. Total price 3463.0."]


def test_knowledge_agent_returns_validation_error(monkeypatch):
    monkeypatch.setattr(
        knowledge_agent,
        "retrieve_information",
        lambda question: "Order ID 10718. Total price 3463.0."
    )

    monkeypatch.setattr(
        knowledge_agent,
        "generate_answer",
        lambda question, context: "The total price is 9999."
    )

    monkeypatch.setattr(
        knowledge_agent,
        "validate_answer",
        lambda answer, context: "Validation failed: price not found in context."
    )

    result = knowledge_agent.ask_question_with_sources("What is the total price?")

    assert result["answer"].startswith(
        "Validation failed: price not found in context."
    )


def test_knowledge_agent_handles_no_documents(monkeypatch):
    def unexpected_call(*args, **kwargs):
        raise AssertionError("Answer generation should not run without documents")

    monkeypatch.setattr(
        knowledge_agent,
        "retrieve_information",
        lambda question: "No relevant documents found."
    )
    monkeypatch.setattr(knowledge_agent, "generate_answer", unexpected_call)
    monkeypatch.setattr(knowledge_agent, "validate_answer", unexpected_call)

    result = knowledge_agent.ask_question_with_sources(
        "Question about an unavailable document"
    )

    assert result["answer"] == "No relevant documents found."
    assert result["sources"] == []
    assert result["source_details"] == {}


from unittest.mock import patch

from agents.answer_agent import generate_answer


def test_answer_agent_returns_generated_answer():
    expected_answer = "The total price is 3463.0."

    with patch(
        "agents.answer_agent.chat",
        return_value={
            "message": {"content": expected_answer}
        },
    ) as mock_chat:
        result = generate_answer(
            "What is the total price?",
            "Order ID 10718. Total price 3463.0.",
        )

    assert result == expected_answer
    mock_chat.assert_called_once()

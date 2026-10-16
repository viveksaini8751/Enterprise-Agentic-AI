
from agents.validation_agent import validate_answer


def test_validation_passes_when_price_matches():
    context = "Order ID 10718. Total price 3463.0."
    answer = "The total price of order 10718 is 3463.0."

    result = validate_answer(answer, context)

    assert result == "Validation passed."


def test_validation_fails_when_price_is_not_in_context():
    context = "Order ID 10718. Total price 3463.0."
    answer = "The total price of order 10718 is 9999.0."

    result = validate_answer(answer, context)

    assert result == "Validation failed: price not found in context."


def test_validation_passes_for_answer_without_price_claim():
    context = "Order ID 10718."
    answer = "The customer is Königlich Essen."

    result = validate_answer(answer, context)

    assert result == "Validation passed."

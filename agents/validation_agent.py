
import re


def validate_answer(answer, context):
    answer_lower = answer.lower()
    context_lower = context.lower()

    # Check order ID when the answer mentions one
    answer_order_ids = re.findall(
        r"order\s*(?:id)?\s*[:#]?\s*(\d+)",
        answer_lower
    )
    context_order_ids = re.findall(
        r"order\s*(?:id)?\s*[:#]?\s*(\d+)",
        context_lower
    )

    for order_id in answer_order_ids:
        if order_id not in context_order_ids:
            return "Validation failed: order ID not found in context."

    # Check prices when the answer claims a total price
    if "total price" in answer_lower:
        prices = re.findall(r"\d+(?:\.\d+)?", answer)
        context_prices = re.findall(r"\d+(?:\.\d+)?", context)

        if prices:
            for price in prices:
                if price not in context_prices:
                    return "Validation failed: price not found in context."

    return "Validation passed."


if __name__ == "__main__":
    context = "Order ID 10718. Total price 3463.0."
    answer = "The total price of order 10718 is 3463.0."

    print(validate_answer(answer, context))

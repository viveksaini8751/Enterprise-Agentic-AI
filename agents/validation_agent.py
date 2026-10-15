
def validate_answer(answer, context):

    answer_lower = answer.lower()
    context_lower = context.lower()

    # Check whether the answer contains a price
    if "total price" in answer_lower:

        import re

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

    result = validate_answer(answer, context)

    print(result)

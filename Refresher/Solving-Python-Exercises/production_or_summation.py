# Given two integers return their product.
# If product is greater than 1000, then return their sum


def product_sum(num1, num2) -> bool:
    return num1*num2 if (num1 * num2) < 1000 else num1 + num2

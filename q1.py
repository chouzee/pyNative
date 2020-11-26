def multiplication(num1, num2):
    total = num1 * num2
    if total > 1000:
        return num1 + num2
    else:
        return total

print(multiplication(10, 12))

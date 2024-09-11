def factorial(n):
    # Base case
    if n == 0 or n == 1:
        print("Base case: factorial(", n, ") = 1")
        return 1
    # Recursive case
    else:
        result = n * factorial(n - 1)
        print("factorial(", n, ") =", n, "* factorial(", n - 1, ") =", result)
        return result

# Example usage
result = factorial(6)
print("The factorial of 5 is:", result)

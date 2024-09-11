def recursive_sum(n):
    # Base case: sum of 0 is 0
    if n == 0:
        return 0
    # Recursive case: sum(n) = n + sum(n-1)
    else:
        return n + recursive_sum(n - 1)

# Test the recursive_sum function
number = 5
result = recursive_sum(number)
print("The sum of numbers from 1 to", number, "is:", result)

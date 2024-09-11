def factorial(n):
    # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        #This is the base case. If n is 0 or 1, the function returns 1.
        #This is because the factorial of 0 and 1 is defined to be 1.
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the factorial function
number = 5
result = factorial(number)
print("The factorial of " + str(number) + " is: " + str(result))

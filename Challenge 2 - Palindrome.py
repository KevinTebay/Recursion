#In this program, the is_palindrome function checks if a given string s is a palindrome.
#The base case checks if the length of the string is less than or equal to 1 (empty string or single character), in which case it is considered a palindrome.
#In the recursive case, the function checks if the first and last characters of the string are the same and then recursively checks the substring without those characters.

def is_palindrome(s):
    # Base case: an empty string or a single character is a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same
    elif s[0] == s[-1]:
        # Recursively check the substring without the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the is_palindrome function
test_string = str(input("Enter a word here: "))
if is_palindrome(test_string):
    print(test_string + " is a palindrome.")
else:
    print(test_string + " is not a palindrome.")

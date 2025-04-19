"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""# Using string slicing
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Taking user's full name as input
full_name = input("Enter your full name: ")
# Splitting the name into parts and getting the initials
initials = '.'.join([name[0].upper() for name in full_name.split()]) + '.'
print(initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check palindrome
def is_palindrome(string):
    return string == string[::-1]

# Input from the user
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Taking a sentence as input
sentence = input("Enter a sentence: ")
# Counting the number of words
word_count = len(sentence.split())
print(f"The number of words in the sentence is: {word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""# Original string
original_string = "This is a string and it is an example."
# Replacing occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")
print(modified_string)

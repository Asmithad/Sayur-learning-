"""Title Case Conversion:
Write a Python program that converts the first letter of each word in a given sentence to uppercase (title case).
"""
#Code:

# Ask the user to input a sentence
sentence = input("Enter your sentence: ")

# Split the sentence into words
word_list = sentence.split()

# Initialize an empty string to store the capitalized sentence
capitalized_sentence = ""

# Loop through each word in the sentence
for word in word_list:
    # Capitalize the first letter of the word and concatenate with the rest of the word
    capitalized_word = word[0].upper() + word[1:]
    # Append the capitalized word to the sentence with a space
    capitalized_sentence += capitalized_word + " "

# Print the capitalized sentence
print(capitalized_sentence)

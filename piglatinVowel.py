#PigLatin - From the input string, for each word, remove the first chars until a vowel, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

#Code:

# Get a sentence from the user
inputSentence = input("Enter a sentence: ")
if len(inputSentence) == 0:
    print("Please enter a sentence.")
# Define the Pig Latin key and vowels
pigLatinKey = 'ay'
vowels = ['a', 'e', 'i', 'o', 'u']

# Iterate through each word in the sentence
for word in inputSentence.split():
    firstVowelIndex = 0
    
    # Iterate through each character in the word
    for index, char in enumerate(word):
        # Check if the character (ignoring case) is a vowel
        if char.lower() in vowels:
            firstVowelIndex = index
            break
    
    # Construct the Pig Latin version of the word
    word = word[firstVowelIndex+1:] + word[:firstVowelIndex+1] + pigLatinKey
    
    # Print the transformed word, end with a space to separate words
    print(word, end=" ")



# Input is an encrypted  string where there will be chars followed by number. The way to decrypt is to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special chars, all the chars between the number and special char are ignored.eg - ac2bd3 means acacbdbdbd. ac2acc#cd3 acaccdcdcd
#code:
# Take input from the user
string = input("Enter the encrypted string (chars followed by number): ")
# Initialize variables for decrypted string and current sequence of characters
decrypted_string = ''
current_chars = ''
# Iterate through each character in the input string
for char in string:
    # If the character is a letter, add it to the current sequence of characters
    if char.isalpha():
        current_chars += char
    # If the character is a digit, repeat the current sequence of characters by the number of times specified
    elif char.isdigit():
        repeat = int(char)
        decrypted_string += current_chars * repeat
        current_chars = ''  # Reset current_chars for the next sequence of characters
    # If the character is not alphanumeric, reset the current sequence of characters
    elif not char.isalnum():
        current_chars = ''  # Reset current_chars if it encounters any non-alphanumeric character
# Print the decrypted string after processing all characters
print("Decrypted string:", decrypted_string)
# Print the length of the decrypted string
print("Length of decrypted string:", len(decrypted_string))


#String manipulation exercises. Use builtin functions as needed.
#1. Print the level of the password security and if the password is acceptable, Weak - only alphabets or only numbers or only special chars, Ok - at least one alphabet, one number and one special char, strong - at least three alphabets, two numbers and one special char,Very strong - same as strong, but at least 16 count, All passwords must be at least 8 chars long.


#code:
# get password as input
password = input("Enter your password: ")
# Initialize counters for alphabets, numbers, and special characters
alpha_count = 0
num_count = 0
special_count = 0
# Iterate through each character in the password
for char in password:
    # Check if the character is an alphabet
    if char.isalpha():
        alpha_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        num_count += 1
    # If the character is neither alphabet nor digit, consider it as a special character
    else:
        special_count += 1
# Determine the password strength level based on the counts and length
# Check if the length of the password is less than 8 characters
if len(password) < 8:
    print("Weak password. Password is too short. It must be at least 8 characters long.")
# Check if the password meets the criteria for a very strong password
elif alpha_count >= 3 and num_count >= 2 and special_count >= 1 and len(password) >= 16:
    print("Very strong")
# Check if the password meets the criteria for a strong password
elif alpha_count >= 3 and num_count >= 2 and special_count >= 1:
    print("Strong password")
# Check if the password meets the criteria for an okay password
elif alpha_count >= 1 and num_count >= 1 and special_count >= 1:
    print("Ok password")
# If the password doesn't meet any of the above criteria, it's considered weak
else:
    print("Weak - Password does not meet any strong criteria")

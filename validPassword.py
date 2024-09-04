# Prompt the user to enter a password until a valid one is entered
while True:
    # Ask the user to input a password
    user_password = input("Enter your password: ")

    # Check if password meets minimum length requirement
    if len(user_password) >= 8:
        has_digit = False
        has_uppercase = False
        has_lowercase = False
        has_special_char = False
        
        # Define special characters
        special_chars = ["$", "@", "#", "%", "!", "^", "&", "*", "()", "-", "_", "+", "="]
        
        # Check each character in the password
        for char in user_password:
            # Check if password contains a digit
            if char.isdigit():
                has_digit = True
            # Check if password contains an uppercase letter
            if char.isupper():
                has_uppercase = True
            # Check if password contains a lowercase letter
            if char.islower():
                has_lowercase = True
            # Check if password contains a special character
            if char in special_chars:
                has_special_char = True
        
        # Check if all requirements are met
        if has_digit and has_uppercase and has_lowercase and has_special_char:
            print("Valid password")
            break  # Exit the loop if a valid password is entered
        else:
            print("Invalid password. Please make sure your password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.")
    else:
        print("Invalid password. Password must be at least 8 characters long.")



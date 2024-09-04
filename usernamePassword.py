'''Check if the username and password is correct. 
Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
password is the first, third, and last 3 letters of the username followed by the first three letters of the name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
'''
#Code:

# Prompt the user to enter a username
username = input("Enter username:")
# Prompt the user to enter a password
input_password = input("Enter password:")

# Check if the username contains '@' and ends with specific domain extensions
if '@' in username and (username.endswith('.com') or username.endswith('.edu') or username.endswith('.tech') or username.endswith('.org')):
    # Find the index of the '@' symbol in the username
    index_domain = username.index('@')
    
    # Extract the last three digits of the input password
    digit = input_password[-3:]
    
    # Check if the last three characters of the input password are digits
    if digit.isdigit():
        # Derive a password based on specific characters from the username
        password = username[0] + username[2] + username[index_domain-3:index_domain] + username[index_domain+1:index_domain+4] 
        
        # Check if the derived password and the last three digits of the input password are present in the input password
        if password in input_password and digit in input_password:
            print("valid password")
        else:
            print("invalid password")
    else:
        print("invalid password")
else:
    print("invalid username")



#Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).When the customer comes in, vendor asks "What do you want to buy?" .The customer can say "I want apple", or "Apple" or "three apple" or something like that.Your program will find out what fruit the customer is asking. Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).Print the quantity if the customer says the quantity. If not, ask him how much he wants.Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp .You can limit the quantity to single digit number.

#code:

# List of available fruits
fruits = {"apple", "orange", "banana"}

# Infinite loop until the user chooses to exit
while True:
    # Ask the user for their order, and convert it to lowercase for case-insensitive matching
    order = input("What do you want to buy? (Type 'exit' to quit): ").lower()

    # Check if the user wants to exit
    if order == "exit":
        break

    # Split the input into individual words
    words = order.split()

    # Find the fruit name in the order
    fruit_name = None
    for word in words:
        if word in fruits:
            fruit_name = word
            break

    # If the fruit is not available, inform the user and continue to the next iteration
    if fruit_name is None:
        print("Sorry, we don't have that fruit available.")
        continue

    # Find the quantity of the fruit in the order
    quantity = None
    for word in words:
        if word.isdigit():
            quantity = int(word)
            break

    # If quantity is not specified in the order, prompt the user to provide it
    if quantity is None:
        quantity = input(f"How many {fruit_name}s do you want? ")

    # Print the order details
    print(f"You ordered {quantity} {fruit_name}s.")

# Thank the user for shopping
print("Thank you for shopping with us!")

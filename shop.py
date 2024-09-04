'''The user just bought a few things in your  shop. Ask the user what he bought. 
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype
'''
#Code:

# Define prices for each item
OneVadaiPrice = float(30)
OneSodaPrice = float(20)
OneSandwichPrice = float(100)
vadai = 0
soda = 0
sandwich = 0

# Get user input for items and quantities
Things = input("Enter what things you bought: ")
split_Things =  Things.split(" ")
# Calculate the cost of each item and the total cost
for i in split_Things:
    if i == "vadai":
        quantityVadai = int(input("Enter quantity of vadai: "))
        vadai = quantityVadai * OneVadaiPrice
    if i == "soda":
        quantitySoda = int(input("Enter quantity of soda: "))
        soda = quantitySoda * OneSodaPrice
    if i == "sandwich":
        quantitySandwich = int(input("Enter quantity of sandwich: "))
        sandwich = quantitySandwich * OneSandwichPrice
TotalPrice = vadai + soda + sandwich

# Display the total amount to be paid
print("Total Amount is: ", TotalPrice)
print("Please pay the amount")

# Get user input for the amount given
GivenAmount = float(input("Enter money: "))

# Check if the given amount is sufficient
while True:
    if TotalPrice < GivenAmount:
        if GivenAmount >= TotalPrice:
            money = GivenAmount - TotalPrice
        print("Balance amount is ", money)
        break
    else:
        print("Insufficient amount, please pay the current amount")
        GivenAmount = float(input("Enter money: "))




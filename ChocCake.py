##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get a budget from the user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if the shop has it.
#find how many choc and cake the user can buy.

#Code:

# Cost of one chocolate and one cake
oneChocPrice = 200
oneCakePrice = 150

# Get user input for budget and total items
budget = float(input("Enter your budget: "))
totalChoc = int(input("Enter the total number of chocolate in shop: "))
totalCake = int(input("Enter the total number of cake in shop: "))

# Check if no items are available
if totalChoc == 0 and totalCake == 0:
    print("No items available")
else:
    # Calculate the maximum number of chocolates and cakes that can be bought with the budget
    maxChoc = int(budget / oneChocPrice)
    if maxChoc > totalChoc :
        maxChoc = totalChoc
    maxCake = int(budget / oneCakePrice)
    if maxCake > totalCake :
        maxCake = totalCake

    # Display the maximum number of chocolates and cakes that can be bought
    print("You can buy " + str(maxChoc) + " chocolate(s) or " + str(maxCake) + " cake(s)")


#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.


#Code:


total_money = 0  # initializing total money received
asking_attempts = 0  # initializing asking attempts

# Using a for loop for a maximum of 5 attempts
for attempt in range(5):
    money = float(input("Enter the amount your parents gave you: Rs "))
    
    if money <= 0:
        print("Sorry, the amount should be greater than 0. Please try again.")
        continue  # Skip the rest of the loop and start the next iteration
    
    if money <= 10:
        print("Thank you, but this amount is too small. Please try again.")
        continue  # Skip the rest of the loop and start the next iteration
    
    total_money += money  # add money to the total
    asking_attempts += 1  # increment asking attempts
    
    print("Money received so far: Rs", total_money)
    print("Thank you!")

    if total_money >= 1000:
        print("You've collected enough money for the movie!")
        break  # Exit the loop if the total money is sufficient

# Print the total asking attempts
print("Number of times you had to ask your parents:", asking_attempts)


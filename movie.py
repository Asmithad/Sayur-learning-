"""#Ask a first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies do you like ?: ")
#convert movies into a List
#FillinMissingCode
commonMoviewCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input ( )#FillinMissingCode)
    #Check if this movie is in the movie list
    #FillinMissingCode

    #if present, 
    #commonMoviewCount ++
    #check if we reached the max
    if(commmonMovieCount >= 3):
        break
    else:
        print ("Try again")

print () #FillinMissingCode - list all the common movies
"""

#Code:

# Ask friend1 for their list of movies
friend1 = input("Friend 1, tell us your favorite movies (separated by commas) give atleast 3 movie: ")
# Split the input string into a list using ',' as the separator
friend1_movies = friend1.split(',')

# Initialize variables
commonMovieCount = 0

while (True):
    # Ask friend2 for one movie at a time
    movie = input("Friend 2, what movie do you like? (Enter one movie): ")
    
    # Check if this movie is in friend1's list
    if movie in friend1_movies:
        commonMovieCount += 1
        print(f"You both like '{movie}'")
        
        # Check if we reached the minimum required common movies
        if commonMovieCount >= 3:
            break
    else:
        print("Try again")

# Print the list of common movies
# Join the elements of common_movie_list into a string separated by ', ' and print as the final output
print(f"\nCommon movies liked by both friends: {', '.join(friend1_movies)}")


# initializing total as 0
total = 0  
# total number of students
noOfStudents = 5  
# initializing i as 0
i = 0 
# using loop to get mark from 5 students
while i < noOfStudents: 
# getting mark as input from the students
    mark = float(input("Enter the mark for student {}: ".format(i + 1)))  
# calculating the total marks of the students
    total += mark  
# incrementing i by 1 
    i += 1  # incrementing i by 1 
# calculating the average of the total marks
average = total / noOfStudents 
# printing the average
print("Avg is ", average)


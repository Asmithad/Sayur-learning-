"""Get the marks for 3 subjects from the students.
 If the mark is greater than 75 in any two subjects, then print Pass and also print the subject where the marks is > 75
 If the mark is greater than 60 in all three subjects, then print pass.
  If the student scored 100 in any one subject, it is pass.  Print which subject the student scored 100.
 if the above conditions are not met, print fail.
"""
#Code:

# Get input for subject marks
mark1 = int(input("Enter subject1: "))
mark2 = int(input("Enter subject2: "))
mark3 = int(input("Enter subject3: "))
if (mark1 == 100 or mark2 == 100 or mark3 == 100):
    print("Pass")
# check mark1 is equal to 100 then print pass-subject1
    if(mark1 == 100 ):
         print("Pass - Subject 1")
# check mark2 is equal to 100 then print pass-subject2
    if mark2 == 100:
        print("Pass - Subject 2")
# check mark3 is equal to 100 then print pass-subject3
    if mark3 == 100:
        print("Pass - Subject 3")

# Check conditions for passing or failing
elif ((mark1 > 75 and mark2 > 75) or (mark1 > 75 and mark3 > 75) or (mark2 > 75 and mark3 > 75)):
    print("Pass")
    if mark1 > 75:
        print("Pass - Subject 1")
    if mark2 > 75:
        print("Pass - Subject 2")
    if mark3 > 75:
        print("Pass - Subject 3")
elif mark1 > 60 and mark2 > 60 and mark3 > 60:
    print("All pass")
else:
    print("Fail")


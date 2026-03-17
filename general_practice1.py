## using all basics practice 1##

print("Welcome to my 1st mini project")
#empty list
grades = []

#empty list values
total = 0
counter = 0

num_of_grades = int(input("How many grades would you like to enter?: "))

while counter < num_of_grades:
    grade = float(input("Enter a grade: "))
    grades.append(grade)
    total = total + grade
    counter = counter + 1


grade_avg = total / num_of_grades

print(f"Your grade average is: {round(grade_avg , 2)}%")

if grade_avg >= 90:
    print("You have an A in the class")
elif grade_avg >= 80:
    print("You have an B in the class")
elif grade_avg >= 70:
    print("You have an C in the class")
else:
    print("You have an F in the class")




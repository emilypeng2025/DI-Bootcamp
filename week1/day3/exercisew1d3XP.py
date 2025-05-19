#🌟 Exercise 1 : Student Grade Summary
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
student_averages = {} 
for name, grades in student_grades.items():
    average = (grades[0]+grades[1]+grades[2])//3
    student_averages[name] = average

print(student_averages)

student_letter_grades = {}
for name,average in student_averages.items():
    if average >= 90:
        student_letter_grades[name] = "A"
    elif average >= 80:
        student_letter_grades[name] = "B"
    elif average >= 70:
        student_letter_grades[name] = "C"
    elif average >= 60:
        student_letter_grades[name] = "D"
    else:
        student_letter_grades[name] = "F"
print(student_letter_grades)

# Calculate the class average


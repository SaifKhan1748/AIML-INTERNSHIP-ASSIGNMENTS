'''
Assignment (19/02/2026)
Assignment Name : Student Data Manager
Description : Store data for 5 students using dictionaries, print topper, 
class average, and assign grades.
'''



students = {}


for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks


topper = max(students, key=students.get)
print("\nTopper:", topper, "-", students[topper])


total = sum(students.values())
average = total / len(students)
print("Class Average:", average)


print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print(name, ":", grade)
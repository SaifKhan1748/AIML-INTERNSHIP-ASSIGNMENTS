'''
Assignment (12/02/2026)
Assignment Name : Smart Input Program
Description : Build a Python program that takes name, age, hobby 
and prints a personalized message while categorizing age using conditionals.
'''




name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")


if age < 13:
    category = "a Child"
elif age < 20:
    category = "a Teenager"
elif age < 60:
    category = "an Adult"
else:
    category = "a Senior"


print(f"\nHello {name}!")
print(f"You are {age} years old and you are {category}.")
print(f"It's great that you enjoy {hobby}!")
'''
Assignment (17/02/2026)
Assignment Name : Logic Builder
Description : Print numbers 1 - 50 with Fizz/Buzz logic and 
count occurrences using loops and functions.
'''


def fizz_buzz():
    fizz = 0
    buzz = 0
    fizzbuzz = 0

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz += 1
        else:
            print(i)

    print("\nCounts:")
    print("Fizz:", fizz)
    print("Buzz:", buzz)
    print("FizzBuzz:", fizzbuzz)


fizz_buzz()
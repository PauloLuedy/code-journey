# Python Beginner Exercises

# BASIC EXERCISES
# 1. Hello World
print("Hello, World!")

# 2. Variables and Input
name = input("What's your name? ")
print(f"Hello, {name}!")

# 3. Basic Math
a = 10
b = 5
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Division: {a / b}")

# 4. Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year
print(f"You are {age} years old")

# 5. Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# CONDITIONAL EXERCISES
# 6. Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 7. Grade Calculator
score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 8. Password Checker
password = input("Enter password: ")
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# LOOP EXERCISES
# 9. Count to 10
for i in range(1, 11):
    print(i)

# 10. Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 11. Sum of Numbers
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}")

# 12. Factorial
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")

# LIST EXERCISES
# 13. List Operations
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)
print(f"First fruit: {fruits[0]}")
print(f"Number of fruits: {len(fruits)}")

# 14. Find Maximum
numbers = [3, 7, 2, 9, 1, 5]
max_num = max(numbers)
print(f"Maximum: {max_num}")

# 15. List Sum
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum: {total}")

# STRING EXERCISES
# 16. String Length
text = input("Enter a sentence: ")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# 17. Count Vowels
text = input("Enter a word: ")
vowels = "aeiou"
count = 0
for char in text.lower():
    if char in vowels:
        count += 1
print(f"Vowels: {count}")

# 18. Reverse String
text = input("Enter a word: ")
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")

# FUNCTION EXERCISES
# 19. Simple Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 20. Calculator Function
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b

result = calculator(10, 5, "+")
print(f"Result: {result}")

# 21. Prime Number Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

# DICTIONARY EXERCISES
# 22. Student Grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print(students)
print(f"Alice's grade: {students['Alice']}")

# 23. Word Counter
text = "hello world hello"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# PRACTICE PROJECTS
# 24. Number Guessing Game
import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")

# 25. Simple Calculator
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Choose operation: ")
    
    if choice == "5":
        break
    
    if choice in ["1", "2", "3", "4"]:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        
        if choice == "1":
            print(f"Result: {a + b}")
        elif choice == "2":
            print(f"Result: {a - b}")
        elif choice == "3":
            print(f"Result: {a * b}")
        elif choice == "4":
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Cannot divide by zero!")

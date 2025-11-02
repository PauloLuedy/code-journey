# Python Intermediate Exercises

# LIST COMPREHENSIONS
# 1. Square Numbers
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# 3. String Lengths
words = ["python", "java", "javascript", "go"]
lengths = [len(word) for word in words]
print(lengths)

# ADVANCED FUNCTIONS
# 4. Decorator Example
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

# 5. Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x > 2, numbers))
print(f"Squared: {squared}")
print(f"Filtered: {filtered}")

# 6. Recursive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])

# FILE OPERATIONS
# 7. File Reader/Writer
def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

write_file("test.txt", "Hello, World!")
content = read_file("test.txt")
print(content)

# 8. CSV Handler
import csv

def write_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv(filename):
    with open(filename, 'r') as f:
        return list(csv.reader(f))

data = [["Name", "Age"], ["Alice", "25"], ["Bob", "30"]]
write_csv("people.csv", data)
csv_data = read_csv("people.csv")
print(csv_data)

# CLASSES AND OBJECTS
# 9. Basic Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    def birthday(self):
        self.age += 1

person = Person("Alice", 25)
print(person.introduce())
person.birthday()
print(person.introduce())

# 10. Bank Account Class
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    @property
    def balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Balance: ${account.balance}")

# 11. Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())

# ERROR HANDLING
# 12. Exception Handling
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# 13. Custom Exception
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")

# DATA STRUCTURES
# 14. Stack Implementation
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.peek())

# 15. Queue Implementation
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft() if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue("first")
queue.enqueue("second")
print(queue.dequeue())

# ALGORITHMS
# 16. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numbers, 7))

# 17. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers.copy())
print(sorted_numbers)

# GENERATORS
# 18. Generator Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

# 19. Generator Expression
squares_gen = (x**2 for x in range(10))
print(list(squares_gen))

# REGULAR EXPRESSIONS
# 20. Email Validator
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

emails = ["test@example.com", "invalid.email", "user@domain.co.uk"]
for email in emails:
    print(f"{email}: {validate_email(email)}")

# 21. Text Parser
def extract_numbers(text):
    return re.findall(r'\d+', text)

def extract_words(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

text = "I have 5 apples and 10 oranges, total 15 fruits!"
print(f"Numbers: {extract_numbers(text)}")
print(f"Words: {extract_words(text)}")

# ADVANCED DATA MANIPULATION
# 22. Dictionary Merge
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = merge_dicts(dict1, dict2)
print(merged)

# 23. Nested Dictionary Access
def get_nested_value(data, keys):
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

nested_data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 30
        }
    }
}

name = get_nested_value(nested_data, ["user", "profile", "name"])
print(f"Name: {name}")

# CONTEXT MANAGERS
# 24. Custom Context Manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager("temp.txt", "w") as f:
    f.write("Hello from context manager!")

# 25. Threading Example
import threading
import time

def worker(name, delay):
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}", 1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")

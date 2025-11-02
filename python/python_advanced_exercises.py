# Python Advanced Exercises

# METACLASSES
# 1. Custom Metaclass
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# 2. Property Validation Metaclass
class ValidatedMeta(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if hasattr(value, 'validate'):
                attrs[key] = property(value.validate)
        return super().__new__(cls, name, bases, attrs)

class ValidatedField:
    def __init__(self, validator):
        self.validator = validator
    
    def validate(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value: {value}")
        instance.__dict__[self.name] = value

# DESCRIPTORS
# 3. Custom Descriptor
class TypedProperty:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}")
        instance.__dict__[self.name] = value

class Person:
    name = TypedProperty('name', str)
    age = TypedProperty('age', int)

person = Person()
person.name = "Alice"
person.age = 30

# DESIGN PATTERNS
# 4. Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} received: {state}")

subject = Subject()
obs1 = Observer("Observer1")
obs2 = Observer("Observer2")
subject.attach(obs1)
subject.attach(obs2)
subject.set_state("New State")

# 5. Factory Pattern
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {"dog": Dog, "cat": Cat}
        return animals.get(animal_type.lower(), lambda: None)()

dog = AnimalFactory.create_animal("dog")
print(dog.speak())

# 6. Strategy Pattern
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data.copy())

data = [3, 1, 4, 1, 5, 9, 2, 6]
sorter = Sorter(QuickSort())
print(sorter.sort(data))

# ADVANCED DECORATORS
# 7. Parameterized Decorator
def retry(max_attempts=3, delay=1):
    def decorator(func):
        import time
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success"

# 8. Class Decorator
def add_methods(cls):
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
    
    def from_dict(cls, data):
        instance = cls.__new__(cls)
        instance.__dict__.update(data)
        return instance
    
    cls.to_dict = to_dict
    cls.from_dict = classmethod(from_dict)
    return cls

@add_methods
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
data = user.to_dict()
new_user = User.from_dict(data)

# ASYNC PROGRAMMING
# 9. Async/Await
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# 10. Async Context Manager
class AsyncFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    async def __aenter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

async def async_file_example():
    async with AsyncFileManager("async_test.txt", "w") as f:
        f.write("Async file operation")

# ADVANCED DATA STRUCTURES
# 11. Trie Implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))
print(trie.starts_with("ap"))

# 12. LRU Cache Implementation
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        
        self.cache[key] = value
        self.order.append(key)

cache = LRUCache(2)
cache.put(1, "one")
cache.put(2, "two")
print(cache.get(1))
cache.put(3, "three")
print(cache.get(2))  # -1 (evicted)

# MEMORY MANAGEMENT
# 13. Weak References
import weakref

class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)

class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None
    
    def get_parent(self):
        if self.parent:
            return self.parent()
        return None

parent = Parent("Dad")
child = Child("Son")
parent.add_child(child)

# ADVANCED ALGORITHMS
# 14. Dynamic Programming - Fibonacci with Memoization
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

print([fibonacci_memo(i) for i in range(20)])

# 15. Graph Algorithms - DFS and BFS
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result
    
    def bfs(self, start):
        from collections import deque
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.graph.get(vertex, []))
        return result

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
print(f"DFS: {graph.dfs(0)}")
print(f"BFS: {graph.bfs(0)}")

# FUNCTIONAL PROGRAMMING
# 16. Currying
def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
    return curried

@curry
def add_three(a, b, c):
    return a + b + c

add_one = add_three(1)
add_one_two = add_one(2)
result = add_one_two(3)
print(result)  # 6

# 17. Monads (Maybe Pattern)
class Maybe:
    def __init__(self, value):
        self.value = value
    
    def bind(self, func):
        if self.value is None:
            return Maybe(None)
        return Maybe(func(self.value))
    
    def __repr__(self):
        return f"Maybe({self.value})"

def safe_divide(x, y):
    return x / y if y != 0 else None

def add_one(x):
    return x + 1

result = Maybe(10).bind(lambda x: safe_divide(x, 2)).bind(add_one)
print(result)  # Maybe(6.0)

# PERFORMANCE OPTIMIZATION
# 18. Profiling Decorator
import time
import functools

def profile(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@profile
def slow_operation():
    return sum(i**2 for i in range(100000))

# 19. Memory Pool
class MemoryPool:
    def __init__(self, size, obj_class):
        self.size = size
        self.obj_class = obj_class
        self.pool = [obj_class() for _ in range(size)]
        self.available = list(range(size))
    
    def acquire(self):
        if self.available:
            index = self.available.pop()
            return self.pool[index]
        return self.obj_class()
    
    def release(self, obj):
        try:
            index = self.pool.index(obj)
            if index not in self.available:
                self.available.append(index)
        except ValueError:
            pass

class ExpensiveObject:
    def __init__(self):
        self.data = [0] * 1000

pool = MemoryPool(5, ExpensiveObject)
obj = pool.acquire()
pool.release(obj)

# 20. Custom Iterator Protocol
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

for num in FibonacciIterator(10):
    print(num, end=" ")
print()

# ADVANCED TESTING
# 21. Mock and Patch
from unittest.mock import Mock, patch

class EmailService:
    def send_email(self, to, subject, body):
        # Simulate sending email
        return f"Email sent to {to}"

class UserService:
    def __init__(self, email_service):
        self.email_service = email_service
    
    def register_user(self, email):
        # Registration logic
        result = self.email_service.send_email(email, "Welcome", "Welcome to our service")
        return f"User {email} registered. {result}"

# Mock usage
mock_email = Mock()
mock_email.send_email.return_value = "Mock email sent"
user_service = UserService(mock_email)
result = user_service.register_user("test@example.com")

# CONCURRENCY
# 22. Thread Pool Executor
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def cpu_bound_task(n):
    time.sleep(0.1)
    return n ** 2

def run_parallel_tasks():
    numbers = range(10)
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(cpu_bound_task, n): n for n in numbers}
        results = []
        for future in as_completed(futures):
            results.append(future.result())
    return results

# 23. Process Pool
from multiprocessing import Pool

def cpu_intensive_task(n):
    return sum(i * i for i in range(n))

def run_multiprocess():
    with Pool(processes=4) as pool:
        results = pool.map(cpu_intensive_task, [100000, 200000, 300000, 400000])
    return results

# 24. Custom Context Manager with Exception Handling
class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection
        self.transaction = None
    
    def __enter__(self):
        self.transaction = self.connection.begin()
        return self.transaction
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.transaction.commit()
        else:
            self.transaction.rollback()
        return False

# 25. Advanced Generator with Send
def coroutine_example():
    result = None
    while True:
        x = yield result
        if x is not None:
            result = x ** 2

gen = coroutine_example()
next(gen)  # Prime the generator
print(gen.send(5))  # 25
print(gen.send(3))  # 9

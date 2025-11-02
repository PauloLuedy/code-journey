counter = 0
numbers_list = [1, 2, 3, 4, 5]

# While loop example
while counter < 5:
    print("Counting:", counter)
    counter += 1  # increment

# For loop with list
for number in [1, 2, 3, 4]:
    print("Number:", number)

# For loop with range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# For loop with break
for i in range(10):
    if i == 6:
        break  # stops the loop
    print(i)

# For loop with continue
for i in range(5):
    if i == 2:
        continue  # skips 2
    print(i)

# Even/odd check
for number in range(1, 6):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

# Range with step
for i in range(1, 10, 3):
    print(i)  # 1, 3, 5, 7, 9

# Loop with index and value
for i in range(len(numbers_list)):
    print("Index:", i, "Value:", numbers_list[i])
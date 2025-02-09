numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# sec
words = ["hello", "world", "python"]
uppercased = list(map(str.upper, words))
print(uppercased)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# adding lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, list1, list2))
print(summed)  # Output: [5, 7, 9]

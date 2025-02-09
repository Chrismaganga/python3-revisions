# A list with mixed data types
my_list = [1, 2, 3, "apple", 4.5]
print(my_list)  # Output: [1, 2, 3, 'apple', 4.5]

print(my_list[0])  # Output: 1 (first element)
print(my_list[-1]) # Output: 4.5 (last element)

my_list.append(6)      # Adds 6 to the end
my_list.insert(2, "orange")  # Inserts "orange" at index 2
print(my_list)  # Output: [1, 2, 'orange', 3, 'apple', 4.5, 6]

my_list.remove(3)   # Removes the first occurrence of 3
print(my_list)  # Output: [1, 2, 'orange', 'apple', 4.5, 6]


sub_list = my_list[1:4]  # Gets elements from index 1 to 3 (exclusive of 4)
print(sub_list)  # Output: [2, 'orange', 'apple']


squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]


squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]


numbers = [5, 3, 8, 1]
numbers.sort()   # Sorts the list in ascending order
print(numbers)   # Output: [1, 3, 5, 8]

numbers.reverse()   # Reverses the list
print(numbers)      # Output: [8, 5, 3, 1]


nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2]
print(nested_list[1][0])  # Output: 3


import json

# A simple list
my_list = [1, 2, 3, "apple", 4.5]

# Convert list to JSON
list_to_json = json.dumps(my_list)
print(list_to_json)
# Output: '[1, 2, 3, "apple", 4.5]'

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

people_json = json.dumps(people)
print(people_json)
# Output: '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'


import json

# List of data
my_data = [1, 2, 3, "apple", 4.5]

# Write to a JSON file
with open("data.json", "w") as file:
    json.dump(my_data, file)


# Read from a JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

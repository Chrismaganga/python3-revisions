person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# accessing values
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25

# adding values
person["job"] = "Engineer"  # Adding a new key
person["age"] = 26  # Updating an existing key
print(person)


del person["city"]
# OR: person.pop("city")
print(person)

for key, value in person.items():
    print(f"{key}: {value}")


squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2
print(merged)
# Output: {'a': 1, 'b': 3, 'c': 4}

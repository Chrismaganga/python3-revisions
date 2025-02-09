# With multiple elements
my_tuple = (1, 2, 3, "hello", True)
print(my_tuple)  # Output: (1, 2, 3, 'hello', True)

# With one element (MUST include a comma!)
single_element_tuple = (5,)
print(single_element_tuple)  # Output: (5,)


print(my_tuple[0])   # Output: 1 (first element)
print(my_tuple[-1])  # Output: True (last element)

for item in my_tuple:
    print(item)


t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(t1 + t2)  # Output: (1, 2, 3, 4, 5, 6)
print(t1 * 3)   # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


print(2 in t1)   # Output: True
print(10 in t1)  # Output: False

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)


numbers = (10, 20, 30, 40)
print(len(numbers))  # Output: 4
print(min(numbers))  # Output: 10
print(max(numbers))  # Output: 40


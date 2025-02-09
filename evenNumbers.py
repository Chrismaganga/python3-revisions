def is_even(number):
    return number % 2 == 0

# Example usage
num = 100
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# sec
even_numbers = list(range(2, 21, 2))  # Generates even numbers from 2 to 20
print(even_numbers)
# third

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# Example usage
p = Person("Chris", 45)
p.greet()  # Output: Hello, my name is Chris, and I'm 45 years old.

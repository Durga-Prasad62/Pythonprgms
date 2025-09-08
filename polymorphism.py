#overcoming method overloading
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))


class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior overriding
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

#operator overloading
# print(5 + 10)  # Integer addition
# print("Hello " + "World!")  # String concatenation
# print([1, 2] + [3, 4])  # List concatenation
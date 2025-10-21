# String Reverse

# Using slicing
str1 = "HELLO"
str1 = str1[::-1]
print("Reversed using slicing:", str1)

# Using iteration
def reverse_string(name):
    rev = ""
    for ch in name:
        rev = ch + rev
    return rev

print("Reversed using iteration:", reverse_string("HELLO"))
print("Reversed using iteration:", reverse_string("WORLD"))

# Using range
def reverse_string_range(name):
    rev = ""
    for i in range(len(name)-1, -1, -1):
        rev += name[i]
    return rev

print("Reversed using range:", reverse_string_range("HELLO"))
print("Reversed using range:", reverse_string_range("WORLD"))
print()


# Sum of digits of each number in the list
def sum_of_digits(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    return total

numbers = [123, 456, 789, 45, 334, 566]
sum_list = [sum_of_digits(n) for n in numbers]
print("Sum of digits for each number:", sum_list)
print()


# Find max digit in a given number
def max_digit(num):
    maximum = 0
    for ch in str(num):
        if int(ch) > maximum:
            maximum = int(ch)
    return maximum

print("Max digit in numbers:")
print(max_digit(123689753))
print(max_digit(12342246373))
print()


# Find max digit for every number in a list
def max_digit_list(lst):
    return [max_digit(n) for n in lst]

print("Max digit for each number in list:", max_digit_list(numbers))

# Assignment 

# Print first n natural numbers using recursion.

def natural(n):
    if n == 0:
        return 
    print(n)
    natural(n-1)

natural(5)

# # N natural numbers using recursion in reverse order
def natural(n):
    if n == 0:
        return
    natural(n-1)
    print(n)

natural(10)

# First n even numbers using recursion

def even_number(n):
    if n == 0:
        return
    even_number(n-1)
    if n&1==0:
     print(n)
even_number(10)
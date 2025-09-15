# string Reverse
# slicing
str1 = "HELLO"
str1 = str1[::-1]
print(str1)
#insert not in str
#we cant do swapping in str because item reassignment is not possible so  way is we need to change to str to list swap will work
def Reverse (name):
    rev = ""
    for i in name:
        rev=i+rev
    print(rev)
Reverse("HELLO")
Reverse("WORLD")

#using range
def Reverse (name):
    rev = ""
    for i in range(len(name)-1,-1,-1):
        rev+=name[i]
    print(rev)
Reverse("HELLO")
Reverse("WORLD")

def individual_sum (num):
    sum = 0
    while(num!=0):
        rem = num%10
        sum += rem
        num//=10    
    return sum
ls = [123,456,789,45,334,566]
new_list = []
for i in range(len(ls)):
      new_list.append(individual_sum(ls[i]))
print(new_list)

#Find max digit in the given number
def max_digit(num):
    max = 0
    for i in str(num):
        if int(i) > max:
            max = int(i)
    print("max=", max)
max_digit(123689753)
max_digit(12342246373)
    
#Find max digit for every number in the given list
def individual_max(num):
     max=0
     for i in str(num):
           if int(i) > max:
            max = int(i)
     return max        
ls = [123,456,789,45,334,566]
new_list = []
for i in range(len(ls)):
      new_list.append(individual_max(ls[i]))
print(new_list)
 
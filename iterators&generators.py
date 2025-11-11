# Iterable - list tuple str etc
# ls = [1,2,3,4,5,6,7]
# for i in ls:
#     print(i)
# Iterator:
# using 1 in next  part of code
# using 2 in next  part of code
# using 3 in next  part of code etc

# ls  = [10,20,40,50,60]
# iter1 = iter(ls)
# print(next(iter1))
# print("random things happen")
# print(next(iter1))
# print("random things happen")
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1)) # stop  iteration


# Even Iterator
class EvenIterator():
    def __init__(self,limit):
        self.current = 0
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.limit:
            raise StopIteration
        temp = self.current
        self.current+=2
        return temp
e = EvenIterator(20)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
# print(next(e)) # stop iteration
# Range Iterator
class EvenIterator():
    def __init__(self,start,end):
        self.current = start
        self.limit = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.limit:
            raise StopIteration
        temp = self.current
        self.current+=1
        return temp
e = EvenIterator(0,7)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
# print(next(e))# stop iteration

# Generators
def gen1():
    yield 1
    yield 2
    yield 3
    yield 4
var1 = gen1()
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
# print(next(var1)) #iteration stop

def gen2(limit):
    num1 = 0
    while num1<=limit:
        temp = num1
        num1+=2
        yield temp
var2 = gen2(10)
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
# print(next(var2))#stop iteration

#   Range like generator and Infinite fibnocci generator



#fibonacci using genarator
def gen_fibonacci(n):
    a,b= 0,1
    for i in range(n):
        yield(a)
        a,b=b,a+b
var3=gen_fibonacci(10)
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))







      



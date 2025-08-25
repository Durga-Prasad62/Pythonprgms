#set inbuilt methods
#ADD
s1={1,2,3,4}
s1.add(5)
print(s1)
# {1, 2, 3, 4, 5}

#remove
s2={1,55,6,4,6}
s2.clear()
print(s2)

# set()
#edge case
# s3={1,5,6,4,6}
# s3.remove()
# print(s3)
# TypeError: set.remove() takes exactly one argument (0 given)
s3={1,5,6,4,6}
s3.remove(6)
print(s3)
# {1, 4, 5}
#pop edge case
# s4={1,3,4,5,6,8}
# s4.pop(4)
# print(s4)
# TypeError: set.pop() takes no arguments (1 given)
s4={1,3,4,5,6,8}
s4.pop()
print(s4)
# {3, 4, 5, 6, 8}   its pops  1 any element

s5={1,3,4,5,6,7,8,8}
s5.discard(6)
print(s5)
# {1, 3, 4, 5, 7, 8}

s6={1,2,3,4,5,6}
s6.copy()
print(s6)
# {1, 2, 3, 4, 5, 6}
s7={1,2}
s8={7,8}
res=s7.union(s8)
print(res)
# {8, 1, 2, 7}

s7={1,2,7}
s8={6,7,7}
res=s7.intersection(s8)
print(res)
# {7}
s8={1,2,3,4,5,5,6,6,7,8}
s9=(3,5,7,7,8,9.1)
res=s8.difference(s9)
print(res)
# {1, 2, 4, 6}

s9={1,2,3,4}
s10={1,3,5,5,6}
res=s9.isdisjoint(s10)
print(res)
# False


s11={1,4,56,67,7,7}
s12={1,3,4,5,6,7,8}
res=s11.issubset(s12)
print(res)
# False
s11={1,4,56,67,7,7}
s12={1,3,4,5,6,7,8}
res=s11.issuperset(s12)
print(res)
# False

s13={1,3,44,5,6}
s14={1,4,5,6,7,8,8,9}
res=s13.symmetric_difference(s14)
print(res)
# {3, 4, 7, 8, 9, 44}

s14={1,5,6,6}
s15={13}
s14.update(s15)
print(s14)
# {1, 13, 5, 6}


# frozenset inbuilt
fs1=frozenset([1,5,6,67,7])
f2=frozenset([1,5,6,7,7])
fs1.union(f2)
print(fs1)
# frozenset({1, 67, 5, 6, 7})


#frozen set accept set operations like union intersection disjoint etc  
# but it not perform  add(),remove(),pop() etc


# edge cases

# fs1=frozenset([1,3,4,5,5])
# print(fs1.add([1,7,8,89,9]))
# AttributeError: 'frozenset' object has no attribute 'add'
# fs1=frozenset([1,3,4,5,5])
# print(fs1.update([1,7,8,89,9]))
# AttributeError: 'frozenset' object has no attribute 'update'

# fs1=frozenset([1,3,4,5,5])
# fs1.append(5)
# print(fs1)
# AttributeError: 'frozenset' object has no attribute 'append'






#APPEND
#its add the element in last
# list1=[1,2,3,4,5]
# list1.append(7)
# list1.append([5,5,6,6])
# print(list1)
# [1, 2, 3, 4, 5, 7, [5, 5, 6, 6]]

#Edge Cases-append
# list2=[4,6,7,7,9]
# list2.append(4,5,6,6)
# print(list2)
# TypeError: list.append() takes exactly one argument (4 given)

# list2=[4,6,7,7,9]
# list2.append([4,5,6,6],[4,6,7])
# print(list2)
# TypeError: list.append() takes exactly one argument (2 given)

# list2=[3,5,6,7]
# list2.append()
# print(list2)
# TypeError: list.append() takes exactly one argument (0 given)
# list2=[6,7,78] #classic  Edge Case
# print(list2.append(5))
#It returns None


#Extend
list3=[1,3,6,7]
list3.extend([1,4,5,7])
print(list3)
# [1, 3, 6, 7, 1, 4, 5, 7]
list3=[1,3,6,7]
list3.extend([[1,4,5,7]])
print(list3)
# [1, 3, 6, 7, [1, 4, 5, 7]]

# list3=[1,2,3,4,5]
# list3.extend(1,5,6)
# print(list3)
# TypeError: list.extend() takes exactly one argument (3 given)
# list3=[1,3,6,7]
# list3.extend()
# print(list3)
# TypeError: list.extend() takes exactly one argument (0 given)
# list3=[1,3,4,5,6]
# list3.extend(10)
# print(list3)
# # TypeError: 'int' object is not iterable
# list3=[1,3,4,5,6]
# print(list3.extend(10))
# TypeError: 'int' object is not iterable
# list3=[1,3,4,5,6]
# print(list3.extend(10.5))
# float' object is not iterable

#insert
list4=[1,3,4,5,6,6]
list4.insert(2,6)
print(list4)
# [1, 3, 6, 4, 5, 6, 6]
list4=[1,3,4,5,6,6]
list4.insert(-4,8)
print(list4)
# [1, 3, 8, 4, 5, 6, 6]

list4=[1,3,4,5,6,6]
list4.insert(8,7)
print(list4)
# [1, 3, 4, 5, 6, 6, 7] #it prints in last index
#EDGE CASES-Insert
# list4=[1,3,4,5,6,6]
# list4.insert()
# print(list4)
# # TypeError: insert expected 2 arguments, got 0
# list4=[1,3,4,5,6,6]
# list4.insert(1)
# print(list4)
# TypeError: insert expected 2 arguments, got 1
# list4=[1,2,3,4,4]
# list4.insert(1,'a','b')
# print(list4)
# TypeError: insert expected 2 arguments, got 3
# list4=[1,3,4,5,6,7]
# list4.insert(1.5,5)
# print(list4)
# TypeError: 'float' object cannot be interpreted as an integer

#index
list5=[4,5,6,7,5]
res=list5.index(5)
print(res)
# 1
list5=[3,4,5,6,7,3]
print(list5.index(5,1))
# 2
list5=[3,4,5,6,7,3]
print(list5.index(5,1,5))
# 2
#Edge cases-Index
# list5=[3,4,5,6,6,7,3]
# print(list5.index(9))
# ValueError: 9 is not in list
# list5=[3,4,5,6,7,3]
# print(list5.index(5,3))
# ValueError: 5 is not in list
# list5=[3,4,5,6,7,3]
# print(list5.index(3))
# 0  its give duplicate first index
# list5=[]
# print(list5.index(1))
# ValueError: 1 is not in list
# list5=[3,4,5,6,7,3,4]
# print(list5.index(4,2))
# 6 its gives index after2
#remove

list6=[1,3,4,5,56,6]
list6.remove(1)
print(list6)
# [3, 4, 5, 56, 6]
#EDGE CASE OF REMOVE
# list6=[1,3,4,5,56,6]
# list6.remove(1,5)
# print(list6)
# TypeError: list.remove() takes exactly one argument (2 given)
# list6=[]
# list6.remove(1)
# print(list6)
# ValueError: list.remove(x): x not in list
# list6=[1.4,6,7,8,9,6,6]
# print(list6.remove(6))
# None
# list6=[1.4,6,7,8,9,6,6]
# list6.remove(6)
# print(list6)
# [1.4, 7, 8, 9, 6, 6] only first 6 was removed
# nested=[[1,2],[1,2]]
# nested.remove([1,2])
# print(nested)
# [[1, 2]]

#Reverse
# rev_list=[1,3,4,56,4,6,6]
# rev_list.reverse()
# print(rev_list)
# [6, 6, 4, 56, 4, 3, 1]
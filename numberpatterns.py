#Increasing Number Triangle
n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


#Repeating Row Numbers
n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows,end=" ")
    print()

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# Continuos Number Triangle
n=5
num=1
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(num,end=" ")
        num+=1
    print()

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


#Reverse Row Pattern
n=5
for rows in range(1,n+1):
    for cols in range(rows,0,-1):
        print(cols,end=" ")
    print()
# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1


#Inverted number Triangle
n=5
for rows in range(n,0,-1):
    for cols in range(rows,0,-1):
        print(cols,end=" ")
    print()

# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1

#Right Aligned Number Triangle()
n=5
for rows in range(1,n+1):
    for spaces in range(n-rows):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()

#         1 
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5



#Pyramid Number Pattern
n=5
for rows in range(1,n+1):
    for spaces in range(n-rows):
        print(" ",end=" ")
    for cols in range(1,(2*rows-1)+1):
          if rows<cols:
               print( rows+rows-cols,end=" ")                                #or we can write 2*rows-cols
          else:
               
               print(cols,end=" ")     
    print()

#         1 
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

#Even Triangle
n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
           print(cols*2,end=" ")
    print()

# 2 
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10


#Odd Triangle
n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
           print(cols*2-1,end=" ")
    print()

# 1 
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

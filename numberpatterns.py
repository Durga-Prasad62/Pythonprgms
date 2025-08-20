# Increasing Number Triangle
# n=5
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print(cols,end=" ")
#     print()

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


# Continuos Number Triangle
# n=5
# num=1
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print(num,end=" ")
#         num+=1
#     print()


#Reverse Row Pattern
# n=5
# for rows in range(1,n+1):
#     for cols in range(rows,0,-1):
#         print(cols,end=" ")
#     print()


#Inverted number Triangle
# n=5
# for rows in range(n,0,-1):
#     for cols in range(rows,0,-1):
#         print(cols,end=" ")
#     print()

#Right Aligned Number Triangle()
# n=5
# for rows in range(1,n+1):
#     for spaces in range(n-rows):
#         print(" ",end=" ")
#     for cols in range(1,rows+1):
#         print(cols,end=" ")
#     print()


#Pyramid Number Pattern
# n=5
# for rows in range(1,n+1):
#     for spaces in range(n-rows):
#         print(" ",end=" ")
#     for cols in range(1,(2*rows-1)+1):
#           if rows<cols:
#                print( rows+rows-cols,end=" ")                                #or we can write 2*rows-cols
#           else:
               
#                print(cols,end=" ")     
#     print()


#Even Triangle
# n=5
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#            print(cols*2,end=" ")
#     print()
#

#Odd Triangle
# n=5
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#            print(cols*2-1,end=" ")
#     print()

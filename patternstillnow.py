# for my understanding i did this further we can optimize this



# m=3        #Square Box
# n=5
# for rows in range(1,m+1):
#     for cols in range(1,n+1):
#         print("*",end=" ")
#     print()
# # * * * * * 
# # * * * * * 
# # * * * * * 




# #RIGHT ANGLE TRIANGLE(Aligned Left)
# n=4                                                
# for rows in range(1,n+1):  
#     for cols in range(1,rows+1):
#         print("*",end=" ")  
#     print() 
# # * 
# # * * 
# # * * * 
# # * * * *     



# # ALIGNED (Right)     RIGHT ANGLE TRIANGLE
# n=5                                               
# for rows in range(1,n+1): 
#   for space in range(n-rows):
#         print(" ",end=" ")  
#   for cols in range(rows):
#          print("*",end=" ") 
#   print() 
# #         * 
# #       * *
# #     * * *
# #   * * * *
# # * * * * *






# #PYRAMID TRIANGLE or CENTERED PYRAMID TRIANGLE
# n = 5
# for i in range(1,n+1):
#    # for spaces
#     spaces=""
#     for j in range(i,n):
#        spaces+=" "
#     # for stars
#     stars=""
#     for j in range(i):
#        stars+="* "
#     print(spaces+stars)
# #     * 
# #    * *
# #   * * *
# #  * * * *
# # * * * * *

# #INVERTED RIGHT ANGLE(LEFT ALIGNED)
# n=5
# for rows in range(n,0,-1):
#     for cols in range(rows,0,-1):
#         print("*",end=" ")
#     print()
# # * * * * * 
# # * * * *
# # * * *
# # * *
# # *



# #INVERTED RIGHT ANGLE RIGHT ALIGNED
# n=5
# for rows in range(n,0,-1):
#     #for spaces
#     for space in range(n-rows):
#         print(" ",end=" ")
#     for cols in range(rows,0,-1):
#         print("*",end=" ")
#     print()
# # * * * * * 
# #   * * * *
# #     * * *
# #       * *
# #         *


# # PYRAMID (1,3,5,7)
# n=4
# for rows in range(1,n+1):
#     #for spaces
#     for spaces in range(n-rows):
#         print(" ",end=" " ) 
#     #for stars
#     for cols in range(0,2*rows-1):
#         print("*",end=" ")  
#     print()  
# #       * 
# #     * * *
# #   * * * * *
# # * * * * * * *  



# #Inverted Pyramid(7,5,3,1)
# n=4
# for rows in range(n,0,-1):
#     #for spaces
#     for spaces in range(n-rows):
#         print(" ",end=" " ) 
#     #for stars
#     for cols in range(0,2*rows-1):
#         print("*",end=" ")  
#     print()
# #  * * * * * * * 
# #    * * * * *
# #      * * *
# #        *


# # DIAMOND PATTERN
# # upper part
# n=4
# for rows in range(1,n+1):
#     #for spaces
#     for spaces in range(n-rows):
#         print(" ",end=" " ) 
#     #for stars
#     for cols in range(0,2*rows-1):
#         print("*",end=" ")  
#     print() 
# # # Lowerpart
# for rows in range(n-1,0,-1):
#     #for spaces
#     for spaces in range(n-rows):
#         print(" ",end=" " ) 
#     #for stars
#     for cols in range(0,2*rows-1):
#         print("*",end=" ")  
#     print()  

# #       * 
# #     * * *
# #   * * * * *
# # * * * * * * *
# #   * * * * *
# #     * * *
# #       *


# #LEFT ALIGNED HALF DIAMOND
# n=4
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print("*",end=" ")
#     print()
# n=3
# for rows in range(n,0,-1):
#     for cols in range(1,rows+1):
#         print("*",end=" ")
#     print()

# # * 
# # * *
# # * * *
# # * * * *
# # * * *
# # * *
# # *


# #RIGHT ALIGNED HALF DIAMOND
# n=4
# for rows in range(1,n+1):
#     #for spaces
#     for spaces in range(n-rows):
#         print(" ",end=" ")
#         #for stars
#     for cols in range(rows):
#             print("*",end=" ")
#     print() 
# n=4
# for rows in range(n-1,0,-1):
#     #for spaces
#     for spaces in range(n-rows):
#         print(" ",end=" ")
#         #for stars
#     for cols in range(rows):
#             print("*",end=" ")
#     print()   

# #       * 
# #     * *
# #   * * *
# # * * * *
# #   * * *
# #     * *
# #       *

# #Butterfly Pattern 
# # Upper Part
# n=3
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print("*",end=" ")
#     #for spaces
#     for spaces in range(2*(n-rows)):              
#         print(" ",end=" ")
#     for cols2 in range(rows):
#         print("*",end=" ")
#     print()
# #Lower part
# for rows in range(n-1,0,-1):
#     for cols in range(1,rows+1):
#      print("*",end=" ")
#     for spaces in range(2*(n-rows)):
#         print(" ",end=" ")
#     for cols2 in range(rows):
#         print("*",end=" ")
#     print()

# # *         * 
# # * *     * * 
# # * * * * * *
# # * *     * *
# # *         *



# # SAND GLASS PATTERN
# n=4
# for rows in range(n,0,-1):
#    for spaces in range(n-rows):
#       print(" ",end=" ")
#    for cols in range(rows):
#       print("*",end=" ")
#    print()
# for rows in range(2,n+1):
#    for spaces in range(n-rows):
#       print(" ",end=" ")
#    for cols in range(1,rows+1):
#       print("*",end=" ")
#    print()

# # * * * * 
# #   * * *
# #     * *
# #       *
# #     * *
# #   * * *
# # * * * *

# # HOURGLASS
# # upper part
# # n=5
# for rows in range(n,0,-1):
#     #for spaces
#     for space in range(n-rows):
#         print("",end=" ")
#     for cols in range(rows,0,-1):
#         print("*",end=" ")
#     print()
#     #lowerpart
# for rows in range(2,n+1):
#     #for spaces
#     for space in range(n-rows):
#         print("",end=" ")
#     for cols in range(1,rows+1):
#         print("*",end=" ")
#     print()
   
# # * * * * * 
# #  * * * *
# #   * * *
# #    * *
# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *



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

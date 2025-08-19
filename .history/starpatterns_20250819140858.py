m=3        #Square Box
n=5
for rows in range(1,m+1):
    for cols in range(1,n+1):
        print("*",end=" ")
    print()
# * * * * * 
# * * * * * 
# * * * * * 




#RIGHT ANGLE TRIANGLE(Aligned Left)
n=4                                                
for rows in range(1,n+1):  
    for cols in range(1,rows+1):
        print("*",end=" ")  
    print() 
# * 
# * * 
# * * * 
# * * * *     



# ALIGNED (Right)     RIGHT ANGLE TRIANGLE
n=5                                               
for rows in range(1,n+1): 
  for space in range(n-rows):
        print(" ",end=" ")  
  for cols in range(rows):
         print("*",end=" ") 
  print() 
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *






#PYRAMID TRIANGLE or CENTERED PYRAMID TRIANGLE
n = 5
for i in range(1,n+1):
   # for spaces
    spaces=""
    for j in range(i,n):
       spaces+=" "
    # for stars
    stars=""
    for j in range(i):
       stars+="* "
    print(spaces+stars)
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

#INVERTED RIGHT ANGLE(LEFT ALIGNED)
n=5
for rows in range(n,0,-1):
    for cols in range(rows,0,-1):
        print("*",end=" ")
    print()
# * * * * * 
# * * * *
# * * *
# * *
# *



#INVERTED RIGHT ANGLE RIGHT ALIGNED
n=5
for rows in range(n,0,-1):
    #for spaces
    for space in range(n-rows):
        print(" ",end=" ")
    for cols in range(rows,0,-1):
        print("*",end=" ")
    print()
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *


# PYRAMID (1,3,5,7)
n=4
for rows in range(1,n+1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        print("*",end=" ")  
    print()  
#       * 
#     * * *
#   * * * * *
# * * * * * * *  



#Inverted Pyramid(7,5,3,1)
n=4
for rows in range(n,0,-1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        print("*",end=" ")  
    print()
#  * * * * * * * 
#    * * * * *
#      * * *
#        *


# DIAMOND PATTERN
# upper part
n=4
for rows in range(1,n+1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        print("*",end=" ")  
    print() 
# # Lowerpart
for rows in range(n-1,0,-1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        print("*",end=" ")  
    print()  

#      * 
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *


#LEFT ALIGNED HALF DIAMOND
n=4
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()
n=3
for rows in range(n,0,-1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()

# * 
# * *
# * * *
# * * * *
# * * *
# * *
# *


#RIGHT ALIGNED HALF DIAMOND
n=4
for rows in range(1,n+1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" ")
        #for stars
    for cols in range(rows):
            print("*",end=" ")
    print() 
n=4
for rows in range(n-1,0,-1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" ")
        #for stars
    for cols in range(rows):
            print("*",end=" ")
    print()   

#       * 
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *

#Butterfly Pattern 
# Upper Part
n=3
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    #for spaces
    for spaces in range(2*(n-rows)):              
        print(" ",end=" ")
    for cols2 in range(rows):
        print("*",end=" ")
    print()
#Lower part
for rows in range(n-1,0,-1):
    for cols in range(1,rows+1):
     print("*",end=" ")
    for spaces in range(2*(n-rows)):
        print(" ",end=" ")
    for cols2 in range(rows):
        print("*",end=" ")
    print()

# *         * 
# * *     * * 
# * * * * * *
# * *     * *
# *         *



# SAND GLASS PATTERN
n=4
for rows in range(n,0,-1):
   for spaces in range(n-rows):
      print(" ",end=" ")
   for cols in range(rows):
      print("*",end=" ")
   print()
for rows in range(2,n+1):
   for spaces in range(n-rows):
      print(" ",end=" ")
   for cols in range(1,rows+1):
      print("*",end=" ")
   print()

# * * * * 
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *

# HOURGLASS
# upper part
# n=5
for rows in range(n,0,-1):
    #for spaces
    for space in range(n-rows):
        print("",end=" ")
    for cols in range(rows,0,-1):
        print("*",end=" ")
    print()
    #lowerpart
for rows in range(2,n+1):
    #for spaces
    for space in range(n-rows):
        print("",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()
   
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *





#INCREASING WIDTH TRIANGLE
n=4
for rows in range(1,n+1):
    #for spaces
    for spaces in range(n-rows):
        print("  ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        print("*",end=" ")  
    print()

#          * 
#       * * *
#    * * * * *
# * * * * * * *



#DECREASING WIDTH TRIANGLE
n=4
for rows in range(n,0,-1):
    #for spaces
    for spaces in range(n-rows):
        print("  ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        print("*",end=" ")  
    print()

# * * * * * * * 
#    * * * * *
#       * * *
#          *

#RIGHT-ALIGNED HILL PATTERN
n=4                                            
for rows in range(1,n+1): 
  for space in range(n-rows):
        print(" ",end=" ")  
  for cols in range(rows):
         print("*",end=" ") 
  print() 
#       * 
#     * *
#   * * *
# * * * *



#HOLLOW SQUARE PATTERN
n=4
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==1 or rows==n or cols==1 or cols==n:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
# * * * * 
# *     *
# *     *
# * * * *

#HOLLOW RECTANGLE PATTERN
m=4
n=5
for rows in range(1,m+1):
    for cols in range(1,n+1):
        if rows==1 or rows==m or cols==1 or cols==n:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# * * * * * 
# *       *
# *       *
# * * * * *




#HOLLOW RIGHT ANGLE TRIANGLE(LEFT-ALIGNED)
n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
    
        if cols==1 or rows==n or cols==rows:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# * 
# * *
# *   *
# *     *
# * * * * *

#HOLLOW RIGHT ANGLE TRIANGLE(RIGHT-ALIGNED)
n=5                                               
for rows in range(1,n+1): 
  for space in range(n-rows):
        print(" ",end=" ")  
  for cols in range(rows):
          if cols==0 or rows==n or cols==rows-1: 
           print("*",end=" ") 
          else:
              print(" ",end=" ")
#   print() 

#         * 
#       * *
#     *   *
#   *     *
# * * * * *





# HOLLOW INVERTED RIGHT ANGLE(LEFT ALIGNED)
n=5
for rows in range(n,0,-1):
    for cols in range(rows,0,-1):
        if rows==n or cols==1 or cols==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * 
# *     *
# *   *
# * *
# *


# HOLLOW INVERTED RIGHT ANGLE(RIGHT ALIGNED)
n=5
for rows in range(n,0,-1):
    #for spaces
    for space in range(n-rows):
        print(" ",end=" ")
    for cols in range(rows,0,-1):
        if rows==n or cols==1 or  rows==cols:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * 
#   *     *
#     *   *
#       * *
#         *


#HOLLOW PYRAMID PATTERN
n=4
for rows in range(1,n+1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        if cols==0 or rows==n or cols==2*rows-2:
         print("*",end=" ")  
        else:
           print(" ",end=" ")
    print() 


#       * 
#     *   *
#   *       *
# * * * * * * *





# #HOLLOW DIAMOND PATTERN
# # upper part
n=4
for rows in range(1,n+1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        if cols==0 or cols==2*rows-2:
         print("*",end=" ")  
        else:
            print(" ",end=" ")
    print() 
    #LOWER PART
for rows in range(n-1,0,-1):
    #for spaces
    for spaces in range(n-rows):
        print(" ",end=" " ) 
    #for stars
    for cols in range(0,2*rows-1):
        if cols==0 or cols==2*rows-2:
         print("*",end=" ") 
        else:
           print(" ",end=" ") 
    print()

#       * 
#     *   *
#   *       *
# *           *
#   *       *
#     *   *
#       *   

#HOLLOW HOUR GLASS PATTERN
# Upper Part
n=5
for rows in range(n,0,-1):
    #for spaces
    for space in range(n-rows):
        print("",end=" ")
    for cols in range(rows,0,-1):
        if rows==n or cols==1 or rows==cols:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
# LOWER PART
for rows in range(2,n+1):
    #for spaces
    for space in range(n-rows):
        print("",end=" ")
    for cols in range(1,rows+1): 
        if cols==1 or rows==cols or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * 
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# * * * * *


#Hollow Butterfly Pattern
n = 5

# Upper part
for rows in range(1, n + 1):
    # Left wing
    for cols in range(1, rows + 1):
        if cols == 1 or cols == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    # Spaces between wings
    for spaces in range(2 * (n - rows)):
        print(" ", end=" ")
    
    # Right wing
    for cols2 in range(1, rows + 1):
        if cols2 == 1 or cols2 == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower part
for rows in range(n, 0, -1):
    # Left wing
    for cols in range(1, rows + 1):
        if cols == 1 or cols == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    # Spaces between wings
    for spaces in range(2 * (n - rows)):
        print(" ", end=" ")
    
    # Right wing
    for cols2 in range(1, rows + 1):
        if cols2 == 1 or cols2 == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# *                 * 
# * *             * * 
# *   *         *   * 
# *     *     *     * 
# *       * *       * 
# *       * *       * 
# *     *     *     * 
# *   *         *   *
# * *             * *
# *                 *






    

             


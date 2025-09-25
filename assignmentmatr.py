#Basic Matrix Programs

#addition of two matrices
A = [[1,2],
     [3,4]]
B = [[5,6],
     [7,8]]
C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        res=(A[i][j]+B[i][j])
        row.append(res)
    C.append(row)  
print(C)
# [[6, 8], [10, 12]]

#substraction of two matrices
A = [[9,8],
     [7,6]]
B = [[1,2],
     [3,4]]
C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        res = (A[i][j]-B[i][j])
        row.append(res)
    C.append(row)
    
print(C)
# [[8, 6], [4, 2]]

#Transpose of matrix
A = [[1,2],
     [3,4],
     [5,6]]
T = []
for i in range(len(A[0])):
    C = []
    for j in range(len(A)):
       C.append(A[j][i])
    T.append(C)
    
print(T)
# [[1, 3, 5], [2, 4, 6]]
rows,cols = map(int,input().split())
mat = []
for _ in range (rows):
    row = list(map(int,input().split()))
    mat.append(row)
left_sum = 0
right_sum = 0 
for i  in range(rows):
    for j in range(cols):
        if i == j:
            left_sum += mat[i][j]
        if i+j == cols-1:
         right_sum += mat[i][j]
print("left diagonal sum",left_sum)
print("right diagonal sum",right_sum)


m = [[1,0,0],
     [0,1,0],
     [0,0,1]]
is_identity= True
for i in range(len(m)):
    for j in range(len(m[i])):
        if  ((i==j and m[i][j]!=1) or  (i!=j  and m[i][j]!=0)):
            is_identity = False
            break
if is_identity:
    print("Identity")
else:
     print("not")

           




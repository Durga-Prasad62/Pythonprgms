# Today's dashboard agenda  : write a code to convert diagonal elements to zero (left diagonal elements and right diagonal elements too ).
#using one loop
m=[[1,2,3,5],
   [4,5,6,7],
   [7,8,9,8]
   ]
rows = len(m)
cols = len(m[0])
for i in range(min(rows,cols)):
    m[i][i] = 0
    m[i][cols-1-i]  = 0 
print(m)




m=[[1,2,3,5],
   [4,5,6,7],
   [7,8,9,8]
   ]
rows = len(m)
cols = len(m[0])
for i in range(rows):
    for j in range(cols):
        if i==j:
            m[i][j]=0
        if j == cols-i-1:
            m[i][j]=0
print(m)

rows = len(m)
cols = len(m[0])
i = 0
while  i< rows  and i < cols:
       m[i][i] = 0
       m[i][cols-1-i]  = 0 
       i += 1
print(m)
    
   



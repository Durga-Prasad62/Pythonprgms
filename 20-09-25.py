m = [[1,2,3],
    [4,5,6 ],
    [7,8,9,10]]
n = []
sum = 0
for i in range(len(m)):  #for indices
    for j in m[i]:       # for items 
        sum += j
n.append(sum)
print(n)


l = [202,89,112,88]
nl=[]
for i in l:
    m = str(i)
    found = False
    for j in range(len(m)):
        for k in range(j+1, len(m)):
            if m[j] == m[k]:
                found = True
                break
        if found:
            break
    nl.append(found)
print(nl)
   


 




  


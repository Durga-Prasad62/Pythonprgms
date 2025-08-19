def Prime_num(m,n):
    
    for i in range(m,n+1):
        if i<2:
            continue
        count=0
        
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                count+=1
                break
        if count==0:
            print(i,end=" ")
    print()
Prime_num(1,100)
Prime_num(100,500)
Prime_num(500,1000)
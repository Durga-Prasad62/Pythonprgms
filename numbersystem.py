#even digit in a number for 2541  so 2,4 is even digits
num=int(input("enter a number:"))
temp=num
rev=0
while(temp!=0):
    rem=temp%10
    if rem&1==0:
        print("even digit is",rem)
    temp//=10


num=int(input("enter a number:"))
temp=num
while(temp!=0):
    rem=temp%10
    is_prime=True
    if rem<2:
        is_prime=False
    else:
     for i in range(2,int(rem*0.5)+1):
        if rem%i==0:
            is_prime=False
            break
    if is_prime:
        print("prime is",rem)
    temp//=10



#perfect number 6 factor 1 2 3  (1+2+3)   6 ==6 
# 28(1,2,4,7,14)==28

def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    print("perfect number") if sum==num else print("not a perfect number")
perfect_number(6)
perfect_number(24)
perfect_number(28)


#within the range
def perfect_number(num):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i
    return sum==num
start=int(input("enter starting number:"))
end=int(input("enter ending number:"))
for j in range(start,end+1):
    if perfect_number(j):
            print(j)








    

# #strong number 145!=1+24+120
# num=int(input("enter a number:"))
# temp=num
# sum=0
# while(temp!=0):
#     rem=temp%10
#     temp//=10
#     fact=1
#     for i in range(1,rem+1):
#         fact*=i 
#     sum+=fact
# if sum==num:
#     print("strong number")
# else:
#     print("weak number")

def strong_check(num):
    temp=num
    sum=0
    while(temp!=0):
        rem=temp%10
        temp//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i 
        sum+=fact
    return sum==num
start=int(input("enter a starting number"))
end=int(input("enter a ending number"))
for i in range(start,end+1):
    if strong_check(i):
        print(i)
     
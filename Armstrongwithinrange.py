# m=1
# n=500
# for i in range(m,n+1):
#   updated=i
#   arm=0
#   length=len(str(i))
#   while(i!=0):
#       rem=i%10
#       arm=arm+rem**length
#       i//=10
#   if updated==arm:
#    print(arm,end=" ")


# def Armstrong_within_range(m,n):
#     for i in range(m,n+1):
#      updated=i
#      arm=0
#      length=len(str(i))
#      while(i!=0):
#         rem=i%10
#         arm=arm+rem**length
#         i//=10
#      if updated==arm:
#        print(arm,end=" ")
# Armstrong_within_range(1,1000)


# print("\n") # i used this for the new sepearation between two functions
#for safer use temp=i
# def Armstrong_within_range(m,n):
#     for i in range(m,n+1):
#      updated=i
#      arm=0
#      length=len(str(i))
#      temp=i
#      while(temp!=0):
#         rem=temp%10
#         arm=arm+rem**length
#         temp//=10
#      if updated==arm:
#        print(arm,end=" ")
# Armstrong_within_range(1,1000)



#without using len() function
def Armstrong_within_range(m,n):
    for i in range(m,n+1):
     updated=i
     arm=0
     count=0
     temp=i 
     while(i<0):
        count+=1
      print("count",count)
     while(temp!=0):
        rem=temp%10
        arm=arm+rem**count
        temp//=10
     if updated==arm:
       print(arm,end=" ")
Armstrong_within_range(1,1000)

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


def Armstrong_within_range(m,n):
    for i in range(m,n+1):
     updated=i
     arm=0
     length=len(str(i))
     while(i!=0):
        rem=i%10
        arm=arm+rem**length
        i//=10
     if updated==arm:
       print(arm,end=" ")
Armstrong_within_range(1,1000)

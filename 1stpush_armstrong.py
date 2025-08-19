def Armstrong_num(num):
     updated=num  
     arm=0
     length=len(str(num))
     while(num!=0):
        rem=num%10
        arm=arm+rem**length
        num//=10
     if updated==arm:
         return 'Armstrong Number'
     else:
          return 'Not a Armstrong Number'
print(Armstrong_num(1))
print(Armstrong_num(22))
print(Armstrong_num(153))
print(Armstrong_num(157))
print(Armstrong_num(1634))
print(Armstrong_num(1646))

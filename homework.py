#Even or Odd
def EvenODD(n):
   return "EVEN" if n & 1 == 0 else "ODD"
print(EvenODD(8))
print(EvenODD(7))
print(EvenODD(25))

#Maxmimun Minimum
def MaxMin(arr):
   maxi = float("-inf")
   mini = float("inf")
   for i in arr:
      if i>maxi:
         maxi = i
      if i<mini:
         mini = i
   print("maximum is",maxi)
   print("minimum is",mini)
MaxMin([1,2,3,4,5,6,7,-8])
MaxMin([7,8,2,3,5,6,1,0,9])

#reverse of string without using slicing
def Rev_string(str1):
   rev=""
   for i in str1:
      rev=i+rev
   return rev
print(Rev_string("Hello"))
print(Rev_string("Python"))
print(Rev_string("Ajay Babu"))

#String Palindrome using Two Pointers
def str_pal(str1):
    low = 0
    high = len(str1)-1
    while(low < high):
        if str1[low] != str1[high]:
            return False
        else:
            low += 1
            high-= 1
    return True
print(str_pal("kerala"))
print(str_pal("malayalam"))
print(str_pal("hyderabad"))
print(str_pal("racecar"))



def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact =fact*i
    return fact
print(factorial(5))
print(factorial(4))
print(factorial(10))

# frequency of string
def Frequency(str1):
    dict={}
    for i in str1:
        if i not  in dict:
            dict[i]=1
        else:
            dict[i]+=1
    print(dict)
Frequency("banana")
Frequency("babu")
Frequency("Laptop")
Frequency("Coding")


# Second Maxmimum
def MaxMin(arr):
   maxi = float("-inf")
   smaxi = float("-inf")
   for i in arr:
      if i>maxi: # check for max and smax
         smaxi = maxi
         maxi = i
      elif i<maxi and i>smaxi:
         smaxi=i     
   print("secondmaximum is",smaxi)
MaxMin([1,2,3,4,5,6,7,-8])
MaxMin([7,8,2,3,5,6,1,0,9])

# #vowels and consonants
def vowel_consonent(str1):
    vowel_count = 0
    consonent_count= 0
    str1=str1.lower()
    for i in str1:
        if i.isalpha(): # i use built in here without  we have to use one condition check small and capital with using or
         if i in ['a','e','i','o','u']:
            vowel_count +=1
         else:
            consonent_count+=1
    print("vowelcount:",vowel_count)
    print("consonentcount:",consonent_count)
vowel_consonent("hello123")

#sum of digits  123 =6
def sum_of_digit(n):
    temp = n
    sum = 0
    while temp!=0:
        rem = temp%10
        sum += rem
        temp //= 10
    print("sum of digits:",sum)  
sum_of_digit(123)   
sum_of_digit(345)  
sum_of_digit(467) 

#Multiplication table
def multable(n):
    for i in range(1,13):
        print(f"{n} X {i} = {n*i}")
multable(5)
multable(6)
multable(10)

# sentence i love python largest is python
def largest(str1):
    word = ""
    largest = ""
    str1+=" "
    for  i in str1:
        if i != " ":
            word+=i
        else:
            if len(largest)<len(word):
                largest = word
            word=""
    print(largest)
largest("I Love Python")
largest("I Love Python Programming")
largest("Happy Dushera to Everyone")


#Remove Duplicates  [1,2,3,4,4,3,2] output[1,2,3,4]
def Remove_Duplicates(arr):
    duplicates=[]
    for i in arr:
        if i not in duplicates:
            duplicates.append(i)
    print(duplicates)
Remove_Duplicates([1,2,3,4,4,2,5,6,5,1])
Remove_Duplicates([1,2,3,4,4,3,2])


#modified insertion  sort without using built in
def sorting(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
sorting([4,6,7,8,1,2,3])
sorting([6,7,9,0,1,2,3,4,5,8])
sorting([])


#merge two list into  single
list1 = [1,3,4,5,8]
list2 = [3,4,5,6,7,8]
list3 = list1+list2
list3.sort()
print(list3)

list1 = [1,3,4,5,8]
list2 = [3,4,5,6,7,8]
list3 = list(zip(list1,list2))
print(list3)

def Prime(n):
    if n<2:
        return "Not Prime"
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return "Not Prime"
    return "Prime"
print(Prime(1))
print(Prime(7))
print(Prime(2))
print(Prime(5))
print(Prime(9))
print(Prime(49))
print(Prime(15))

    

#MEDIUM QUESTIONS
#Target pair 
def TargetPair(arr,target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if  arr[i]+arr[j]== target:
                pairs.append((arr[i],arr[j]))
    return pairs
print(TargetPair([0,1,2,3,4,2,3,6,7],6))
       


#Rotation Of List
def Rotation(arr,k):
    if len(arr)==1 or 0:
        return arr
    k = k % 10
    print(arr[k:]+arr[:k])
Rotation([1,2,3,4,5,6],1)
Rotation([1,2,3,4,5,6],2)
Rotation([1,2,3,4,5,6],3)
Rotation([1,2,3,4,5,6],4)

#Missing Number
def MissingNumber(arr):
    minimum = min(arr)
    maximum = max(arr)
    missing=[]
    for i in range(minimum,maximum+1):
        if i not in arr:
            print(i)
        if i not in missing:
           missing.append(i)
    return missing
print(MissingNumber([1,2,3,4,6,8]))

#count the words
def largest(str1):
    word = ""
    str1 += " "
    count = 0
    for  i in str1:
        if i != " ":
            word+=i
        else:
           if word:
               count+=1
    print(count)

largest("I Love Python")
largest("I Love Python Programming")
largest("Happy Dushera to Everyone")
largest("wish you a happy dusshera")

#bubble sort
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(BubbleSort([9,5,3,1,4,7]))
print(BubbleSort([6,7,8,1,2,3,4,5]))

#intersection of lists
def intersection(ls1,ls2):
    nls=[]
    for i in range(len(ls1)):
        for j in range(len(ls2)):
            if  ls1[i]==ls2[j]:
                nls.append(ls2[j])     
    return(sorted(set(nls)))
print(intersection([1,2,3,4,5],[1,3,2,6,7,7]))

# anagram ex listen silent 
def clean_string(s):
    """Remove spaces and special characters, keep only alphanumeric, and lowercase.""" 
    cleaned = ""
    for ch in s:
        if ch.isalnum():   # keep only letters & digits
            cleaned += ch.lower()
    return cleaned 
def Anagram(str1,str2):
    str1=clean_string(str1)
    str2=clean_string(str2)
    ls1=list(str1)
    ls2=list(str2)
    if len(str1)!=len(str2):
        print("This is not a Anagram")
    else:
        for i in range(len(ls1)):
            for j in range(i+1,len(ls1)):
             if ord(ls1[i])>ord(ls1[j]):
                ls1[i],ls1[j]=ls1[j],ls1[i]
        for i in range(len(ls2)):
            for j in range(i+1,len(ls2)):
             if ord(ls2[i])> ord(ls2[j]):
                ls2[i],ls2[j]=ls2[j],ls2[i]
        if ls1==ls2:
         print("it is a Anagram ")
        else:
            print("it is not  a Anagram ")
Anagram("listen!","silent!")
Anagram("hello","world")
Anagram("evil",'vile')
Anagram("java","python")

def invert_dic(dict):
    return{values:keys for keys,values in dict.items()}
print(invert_dic({"a":1,"b":2,"c":3}))



def Transpose_of_matrix(arr):
    for i in range(len(arr)):
        for j in range(i):
           arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    return arr
print(Transpose_of_matrix([[1,2,3],[4,5,6],[7,8,9]]))

#swiss first non repeating character is w
def non_repeating_char(str1):
    for i in str1:
        count = 0
        for j in str1:
            if i == j:
                count+=1
        if count == 1:
            return i
print(non_repeating_char("swiss"))
print(non_repeating_char("happy"))
            
#longest word
def largest(str1):
    word = ""
    largest = ""
    str1+=" "
    for  i in str1:
        if i != " ":
            word+=i
        else:
            if len(largest)<len(word):
                largest = word
            word=""
    print(largest)
largest("I Love Python")
largest("I Love Python Programming")
largest("Happy Dushera to Everyone")

#second min
def secondMin(arr):
   mini = smini = float("inf")
   for i in arr:
      if i<mini:
         smini=mini
         mini=i
      elif i < smini:
         smini = i
   return smini
print(secondMin([1,2,3,4,5,6]))


def Armstrong(n):
    temp = n
    arm = 0
    while temp!=0:
        rem = temp%10
        arm = arm+rem**len(str(n))
        temp //= 10
    return "Armstrong " if n == arm else "Not Armstrong"
print(Armstrong(24))
print(Armstrong(143))
print(Armstrong(153))
print(Armstrong(1))
  
  



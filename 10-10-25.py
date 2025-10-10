# REVERSE OF STRING
# #reverse of string without using slicing
def Rev_string(str1):
   rev=""
   for i in str1:
      rev=i+rev
   return rev
print(Rev_string("Hello"))
print(Rev_string("Python"))
print(Rev_string("Ajay Babu"))

# USING SLICING
def rev_slicing(str1):
    str1 = str1[::-1]
    return str1
print(rev_slicing("hello"))
print(rev_slicing("prasad"))
print(rev_slicing("majji"))

# range from last
def Rev_string(str1):

   for i in  range(len(str1)-1,-1,-1):
      print(str1[i],end="")
   print()  
(Rev_string("Hello"))
(Rev_string("Python"))
(Rev_string("Ajay Babu"))


#Using recursion
def  string_reverse(str1):
   if len(str1) == 0:
      return str1
   return str1[-1] + string_reverse( str1[:-1])
print(string_reverse("hello"))










#'(a+b-c*[e/f])' Remove brackets from string
#a+b-c*e/f

str1 = "(a+b-c*[e/f])"
new = ""
for i in str1:
    if i in ("()[]"):
        continue
    else:
        new += i
print(new)



# vowel, consonant, spaces count in a string
def vowel_consonent(str1):
    vowel_count = 0
    consonent_count= 0
    space_count = 0
    str1=str1.lower()
    for i in str1:
        if i == " ":
           space_count+=1
        if i.isalpha(): # i use built in here without  we have to use one condition check small and capital with using or
         if i in ['a','e','i','o','u']:
            vowel_count +=1
         else:
            consonent_count+=1
    print("spaceount",space_count)
    print("vowelcount:",vowel_count)
    print("consonentcount:",consonent_count)
vowel_consonent("hello 123")
vowel_consonent("hello")
vowel_consonent("iam going to village")




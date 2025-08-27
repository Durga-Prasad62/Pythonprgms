str1="Iam Prasad"
print(str1.upper())
# IAM PRASAD
print(str1.lower())
# iam prasad
print(str1.startswith("I"))
# True
print(str1.endswith("I"))
# False
print(str1.endswith("d"))
# True
print(str1.replace("Iam","hey"))
# hey Prasad
print(str1.swapcase())
# iAM pRASAD
print(str1.isdigit())
# False
str2="abc"
print(str2.isalpha())
# True
str2="a b c"
print(str2.isalpha())
# False  because space is there
str3="  happy   "
print(str3.strip())
# happy
str3="  ha,pp,y   "
print(str3.split(","))
# ['  ha', 'pp', 'y   ']
str4="hello iam python"
print(str4.find('h'))
# 0
str4="hello iam python"
print(str4.capitalize())
# Hello iam python
print(str4.title())
# Hello Iam Python
str5="walker"
print(str5.count('j'))
# 0
str6="hello i"
print(str6.isascii())
# True
str7="hello i am"
print(str7.isdecimal())
# False
str7="hello i am raju"
print(str7.index('m'))
# 9
str7="HellO i am RajU rani"
print(str7.casefold())
# hello i am raju rani
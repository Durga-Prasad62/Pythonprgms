# open the file
f =open('prime.py','r')
# read the file
print(f.read()) 
print(f.read(5))  # the cursor moves to last
# tells where is cursor is there
print(f.tell())
# cursor moves to top
f.seek(0)
# read one line
print(f.readline())
# read all lines and gives in list format
print(f.readlines())
# closing file
f.close()

f = open("new.py",'w')
# existing file is erased and write content
print(f.write("Hi Iam Learning FILE HANDLING"))
print(f.write("\nSOME OPERATIONS ARE THERE LIKE READ WRITE APPEND "))
f.close()

g = open('prime.py','a')
# append the content at the end
print(g.write("this is prime program"))
g.close()

h = open("new.py",'r+')
# combination of read and write 
print(h.read())
print(h.write("hello this is new file in the python"))
h.close()

k = open("new.py",'w+')
# combination of write and read
print(k.write("hello this is new file in the python"))
print(k.read())
k.close()

k = open("new.py",'a+')
# combination of append and read
print(k.write("hello this is new file in the python"))
print(k.read())
k.close()
# it creates a new file
n = open("hello.txt","x")   


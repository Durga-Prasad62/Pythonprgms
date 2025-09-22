# #  3. Matrix addition using range.

# # m=[]
# # rows,cols = map(int,input().split())
# # for i in range(rows):
# #     row = list(map(int,input().split()))
# #     m.append(row)
# # sum=0
# # tsum=[]
# # for i in range(rows):
# #     for j in range(rows):
# #         sum+=m[i][j]
# #     tsum.append(sum)
# # print(tsum)


# # 2. Find the missing numbers. Input: 34571  	Output : 26 missing
# num1 = 34751
# # list1 =  list(num1)# int directly convert to list so we use list comphrension
# list1 = [int(digit) for digit in str(num1)]
# print(list1)
# newlist=[]
# list_min = min(list1)
# list_max = max(list1)
# for i in range(list_min,list_max+1):
#     if i not  in list1:
#         print(i)
#     if i not  in newlist:
#         newlist.append(i)
# print(newlist)

#third Question
# 1. "Given a list where each element represents the color of a sock, e.g., ['red', 'green', 'red', 'purple', 'green', 'black', 'red'], how many days can I sustain if I can wear only one matching pair of socks per day and each pair can be used only once?"

ls =  ['red', 'green', 'red', 'purple', 'green', 'black', 'red']
sockcfreq = {}
for i in ls:
    if i not in sockcfreq:
        sockcfreq[i] = 1
    else:
        sockcfreq[i]+=1
for key,values in sockcfreq.items():
    count=values//2
    if count == 1:
      print(key,"its  use for only one day")
    



        





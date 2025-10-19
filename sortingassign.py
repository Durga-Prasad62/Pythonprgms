# def BubbleSort (arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] < arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     print(arr)
       

# BubbleSort( [1,3,4,5,6,2,9,0,7])
# BubbleSort( [67,0,67,-7,3,2,1,7,999])
# BubbleSort( ["apple","bat","car","dog","elephant","fan"])

#if we sort the strings if we give the answer based on the dictionary order


# bubble  sort based on the length
# def BubbleSort (arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#            if len(arr[j])> len(arr[j+1]):
#               arr[j],arr[j+1]=arr[j+1],arr[j]
#     print(arr)      
# BubbleSort( ["apple","bat","car","dog","elephant","fan"])

#bubble sort Can you sort nested lists based on the first element of each nested list.

def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j][0] > arr[j+1][0]:
                # Swap entire sublists
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

# Test
BubbleSort([[1,56,56],[90,79,98],[78,86,72],[6,13,42],[89,7,5]])






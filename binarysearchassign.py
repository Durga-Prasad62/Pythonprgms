# Assignemnt question:
# Count the number of swaps performed by bubble sort while sorting an array.
# Apply binary search in only first half of the list. (Search only in first half)
def BubbleSort(arr):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                count+=1
    print("number of swaps:",count)
BubbleSort([5,6,7,8,1,4,3])
#T.C=O(n*n)
#S.C=O(1)



def BinarySearch (arr,search):
    low = 0
    high = (len(arr)-1)//2
    while(low<=high):
        mid = (low+high)//2  #it check only first half
        if arr[mid]==search:
            return mid
        elif arr[mid]<search:
            low = mid+1
        else:
            high = mid-1
    return -1
print(BinarySearch([2,4,6,7,8,9],4))

#T.C:O(log n)
#S.C:O(1)


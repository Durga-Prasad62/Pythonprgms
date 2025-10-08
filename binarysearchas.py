def Binary(arr,search):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid] == search:
            return mid
        elif arr[mid]<search:
           low = mid+1
        else:
            high = mid-1
    
    return-1
print(Binary([1,3,5,7,9],3))

# Time Complexity: O(log n)

# Space Complexity: O(1)
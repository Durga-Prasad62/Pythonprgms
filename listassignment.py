def list_max_min_sum (arr):
    if not arr:
        print("empty list")
    else:
         max_element = arr[0]
         min_element = arr[0]
         sum=0
         for i in arr:
            sum+=i
        #    store the max element
            if i > max_element:
                max_element = i
            #   store the min element
            if i < min_element:
                min_element = i
         print("max:",max_element)
         print("min:",min_element)
         print("sum is:",sum)
list_max_min_sum([-1,-8,-7,-6])
list_max_min_sum([1,2,4,5,6,7,8,5,3])
list_max_min_sum([])



def list_max_min_sum (arr):
    if not arr:
        print("empty list")
    else:
         max_element = 0
         min_element = arr[0]
         for i in arr:
            #if all are in negative items [-1,-8,-7,-6]
            # -1>0(false) so  it include for all element in array
            if i > max_element:
                max_element = i
            if i < min_element:
                min_element = i
         print("max:",max_element)
         print("min:",min_element)
list_max_min_sum([-1,-8,-7,-6])
list_max_min_sum([1,2,4,5,6,7,8,5,3])
list_max_min_sum([])


def list_max_min_sum (arr):
    if not arr:
        print("empty list")
    else:
         max_element = arr[3]
         min_element = arr[3]
         sum=0
         for i in arr:
            sum+=i
            #We Can Check With any item
            #why means  -1>-6  updated (max=-1)  -8>-1(false) it includes all item
            if i > max_element:
                max_element = i            
            if i < min_element:
                min_element = i
         print("max:",max_element)
         print("min:",min_element)
         print("sum is:",sum)
list_max_min_sum([-1,-8,-7,-6])
list_max_min_sum([1,2,4,5,6,7,8,5,3])
list_max_min_sum([])

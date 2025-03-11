import math

arr = []
start = 0
for i in range(1024):
    arr.append(i)

end = len(arr) - 1
target = 800

def binarysearch(arr, start, end, target):
    # Condition to return False when target is not present in the array
    if(start > end):
        return False
    
    midIndex = math.floor((start + end)/2)
    
    # Condition to check if mid value is our target
    if(arr[midIndex] == target):
        return True
    
    if(arr[midIndex] > target):
        # Target is lower that our mid index hence is target is in the left side. So we on search from start to the midIndex
        return binarysearch(arr, start, midIndex - 1, target)
    else:
        # Target is higher that our mid index hence is target is in the right side. So we on search from midIndex to end
        return binarysearch(arr, midIndex + 1, end, target)
    
print(binarysearch(arr, start, end, target))
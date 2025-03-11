import math

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    middleIndex = math.floor(len(arr)/2)
    leftArr = arr[:middleIndex]
    rightArr = arr[middleIndex:]
    
    return merge(mergeSort(leftArr), mergeSort(rightArr))

def merge(leftarr, rightarr):
    resultarr = []
    leftIndex = 0
    rightIndex = 0
    
    while (leftIndex < len(leftarr) and rightIndex < len(rightarr)):
        if (leftarr[leftIndex] < rightarr[rightIndex]):
            resultarr.append(leftarr[leftIndex])
            leftIndex += 1
        else:
            resultarr.append(rightarr[rightIndex])
            rightIndex += 1
    
    resultarr.extend(leftarr[leftIndex:])
    resultarr.extend(rightarr[rightIndex:])
    return resultarr


print(mergeSort([3,12,5,16,10,20]))

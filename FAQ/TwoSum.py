'''
Write a program to find all pairs of integers whose sum is equal to a given number. 
double loop (O(n^2)) and an optimized hash-map approach (O(n))
For example, if the input integer array is {2, 6, 3, 9, 11} and the given sum is 9, the output should be {6,3}.
'''

# Implementation with o(n^2) complexity
def two_sum_brute_force(arr, sum):
    temparr = []
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if(arr[i]+arr[j] == sum):
                temparr.append((arr[i],arr[j]))
    return temparr

print(two_sum_brute_force([2, 6, 3, 9, 11], 9))
print(two_sum_brute_force([2, 4, 3, 5, 7, 8, 9], 7))
print(two_sum_brute_force([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
    
    
# Implementation with o(n) complexity
def two_sum_hashmap(nums, target):
    num_map = {}  # Dictionary to store seen numbers
    result = []
    
    for num in nums:
        complement = target - num
        if complement in num_map:
            result.append((complement, num))  # Store the pair
        num_map[num] = True  # Store number in hash map
    
    return result  # Return all pairs that satisfy the condition

print(two_sum_hashmap([2, 6, 3, 9, 11], 9))
print(two_sum_hashmap([2, 4, 3, 5, 7, 8, 9], 7))
print(two_sum_hashmap([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
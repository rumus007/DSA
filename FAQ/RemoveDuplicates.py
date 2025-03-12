'''
Given an integer array nums sorted in non-decreasing (ascending) order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.

Return k.
'''

def removeDuplicates(nums):
    if not nums:
        return 0 # case when array is empty
    
    k = 1 # set inital index of unique number to 1
    
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]: #  check if current i index is same as previous index for duplicates
            nums[k] = nums[i]
            k += 1 # increment the unique index by one
    
    return k
    
            

# Test cases
test_cases = [
    ([1, 1, 2], [1, 2]),  # Simple case with duplicates
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),  # Standard case
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # No duplicates
    ([1, 1, 1, 1], [1]),  # All elements are the same
    ([10, 10, 10, 20, 20, 30, 30, 30, 30, 40], [10, 20, 30, 40]),  # Mixed duplicates
    ([5], [5]),  # Single element array
    ([], []),  # Empty array
]

# Run assertions
for nums, expected in test_cases:
    nums_copy = nums[:]  # Make a copy to preserve the original input
    k = removeDuplicates(nums_copy)
    assert k == len(expected), f"Failed: Expected length {len(expected)}, got {k}"
    assert nums_copy[:k] == expected, f"Failed: Expected {expected}, got {nums_copy[:k]}"
    print(f"Test passed for input: {nums} -> Output: {nums_copy[:k]}")

print("All test cases passed successfully!")
# Compute the sum of an array (linear time).
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(array_sum([1,2,3,4,5,6]))

# Check for duplicates in an array by brute force vs. using a set (O(n^2) vs. O(n)).

# Brute Force Approach (O(n²))
# The brute force approach checks each element against every other element, leading to a time complexity of O(n^2)

arr = [1,2,3,4,5,6,7,8,8]

def has_duplicates_brute_force(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False

print(has_duplicates_brute_force(arr))

# Set-Based Approach (O(n))
# Using a set, we can check for duplicates in linear time O(n). If an element is already in the set, we return True.

def has_duplicates_set(arr):
    seen = []
    x = 0
    for num in arr:
        x += 1
        if num in seen:
            print(x)
            return True
        seen.append(num)
    return False

print(has_duplicates_set(arr))
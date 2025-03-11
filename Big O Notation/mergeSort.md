Merge Sort Explanantion with O (n log(n)) Complexity

We have an Array of N length that needs to sort, we use the merge sort to implement divide and conquer

Divide the the array into two halfes from the index

* left half = array[:middleindex]
* right half = array[middleindex:]

Call a helper function with recursive to the left and right array

`return helper(mergesort(left), mergesort(right))`

Helper function takes left and right and compare each elements pushing the smallest to result array and adding the left or right index which ever element was smaller until index exceeds the array lenght. 

Finally return a concatinated array of the resut array, left array starting from the left index and right index starting from right index. 

The function recursively divides the array into halves until each half has only one element.
It then merges the sorted halves back together.
The splitting takes 
𝑂
(
log
⁡
𝑛
)
O(logn) time because we repeatedly divide the array.
The merging takes 
𝑂
(
𝑛
)
O(n) time at each level of recursion.
This results in a total complexity of 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
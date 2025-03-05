* Theory – Algorithmic Complexity: Learn how to analyze time and space complexity using Big-O notation. 

* Understand common complexities (constant O(1), logarithmic O(log n), linear O(n), quadratic O(n^2), exponential O(2^n), etc.) and why they matter in optimizing code​.

* Practice evaluating the complexity of simple algorithms and recognize patterns (loop = linear, nested loops = quadratic, divide & conquer = logarithmic). 

* O (n) complexity is explained as function the that have a linear (single loop) execution
```
def function_one(n):
    for i in range(n):
        # your code over here
        return
```

* O (n^2) complexity is explained as function the that have a qudratic (two loops) execution
```
def function_two(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
```

* O (n^3) complexity is explained as function the that having three loops execution
```
def function_three(n):
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    print(i,j)
```

* O (log(n)) complexity is explained as function having iternation or recursion with the value for log(n). i.e. log(8) = 3 so total iterations is three
```
def function_four(n):
    if n == 0:
        return "Done"
    n = math.floor(n/2)
    return function_four(n)
```
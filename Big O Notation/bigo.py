import math
# Funtion definiation of O(n) complexity
def function_one(n):
    for i in range(n):
        print("code execution")
        

# Funtion definiation of O(n^2) complexity
def function_two(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
            
# Funtion definiation of O(n^2) complexity
def function_two(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# Funtion definiation of O(n^3) complexity            
def function_three(n):
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    print(i,j)
                       
# Funtion definiation of O(log(n)) complexity
def function_four(n):
    if n == 0:
        return "Done"
    n = math.floor(n/2)
    return function_four(n)

# Funtion definiation of O(nlog(n)) complexity
def function_five(n):
    y = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(1, y+1):
            print(i)  

# Funtion definiation of O(2^n) complexity
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Funtion definiation of O(n!) complexity
def f(n):
    if n == 0:
        print("********")
        return
    
    for i in range(n):
        f(n-1)
        


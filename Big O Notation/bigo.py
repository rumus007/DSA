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

    

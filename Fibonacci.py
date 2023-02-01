""" Recursive method """
def fibonacci_find(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_find(n-1) + fibonacci_find(n-2)

        
# Test Cases 
test1 = fibonacci_find(5)
print(test1)
test2 = fibonacci_find(27)
print(test2)
test3 = fibonacci_find(0)
print(test3)


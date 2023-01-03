import random


def BinarySearch(target, start, end, arr):
    if start > end:
        return 'Not found'
    
    middle = (start + end) // 2
    
    if arr[middle] == target:
        return f'{target} was found at index {middle}'
        

if __name__ == '__main__':
    array = [random.randrange(1, 50) for i in range(10)]
    lookfor = int(input("Please input a number: "))
    BinarySearch(lookfor, 0, len(array), array)
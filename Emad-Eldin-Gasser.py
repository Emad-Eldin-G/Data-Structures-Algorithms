# Declaring array with name arr (of 10 elements)
from time import sleep


def bubbleSort(arr):
    queryLength = len(arr)
    for i in range(queryLength):
        for j in range(queryLength-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
print(arr)
sleep(0.5)
print(bubbleSort(arr))
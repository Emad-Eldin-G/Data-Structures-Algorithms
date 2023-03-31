def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1 
    return arr


if __name__ == '__main__':
    oldArray = [3,2,5,7,8,1,4,6]
    print(f'Old array:{oldArray}')
    new = insertionSort(oldArray)
    print(f'Sorted:{new}')
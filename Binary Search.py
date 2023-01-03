# The condition to perform a Binary Search
# is to insure that the list is sorted

def BinarySearch(target, start, end, arr):
    if start > end:
        return 'Not found'
    # Declaring middle index by finding the avg of the start and end
    middle = (start + end) // 2
    # Base condition | eventually comes here if target is in arr
    if arr[middle] == target:
        return f'{target} was found at index {middle}'

    elif target > arr[middle]:
        return BinarySearch(target, middle+1, end, arr)

    elif target < arr[middle]:
        return BinarySearch(target, start, middle-1, arr)


if __name__ == '__main__':
    array = [x for x in range(20)]
    lookfor = int(input("Please input a number: "))
    result = BinarySearch(lookfor, 0, len(array), array)
    print(result)

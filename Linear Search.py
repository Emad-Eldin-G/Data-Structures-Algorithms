from random import randint
from time import sleep

#declaring a 1D list with 10 elements randomly generated and added to a list
arrayData = [randint(1, 50) for _ in range(10)]

def linear_search(target):
    ub = len(arrayData)
    lb = 0
    index = 0
    while lb < ub:
        sleep(1)
        if arrayData[index] == target:
            print(f'{target} was found at index ({index}) of the list')
            return target
        else: 
            lb += 1
            index += 1
            print(f'Target not found at index ({index})')

#Startsup when calling the file using the terminal
if __name__ == "__main__":
    print('Please input a number: ')
    number = input()
    sleep(0.5)
    print(f'Finding {number} in the array....')
    answer = linear_search(number)
    print(answer)



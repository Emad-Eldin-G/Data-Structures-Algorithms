from random import randrange


arr = [[randrange(1, 100) for j in range(10)] for i in range(10)]

def bubble_sort(arr):
    query_length = len(arr)
    for j in arr:
        for i in range(query_length):
            for z in range(query_length -1):
                if j[z] > j[z+1]:
                    j[z], j[z+1] = j[z+1], j[z] 
    return arr

# Outputing original vs sorted    
print(arr)
print('\n')
query = bubble_sort(arr)

for i in query:
    for j in i:
        print(j, end=" | ")
    print('\n')

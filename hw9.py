    #davaleba1
import random

random_list_of_numbers = [random.randint(1, 100) for _ in range(10)]

random_list_of_numbers.sort()

print(random_list_of_numbers)







    #davaleba2
import random

random_list_of_numbers = [random.randint(1, 100) for _ in range(10)]

sorted_list = sorted(random_list_of_numbers, reverse=True)

print(sorted_list)







    #davaleba3
import random
import time

def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

for size in [1000, 2000, 3000]:
    random_list = generate_random_list(size)
    
        #Bubble Sort
    bubble_list = random_list.copy()
    start_time = time.time()
    bubble_sort(bubble_list)
    end_time = time.time()
    bubble_time = end_time - start_time
    
        #Selection Sort
    selection_list = random_list.copy()
    start_time = time.time()
    selection_sort(selection_list)
    end_time = time.time()
    selection_time = end_time - start_time
    
    print(f"List size: {size}")
    print(f"Bubble Sort time: {bubble_time} seconds")
    print(f"Selection Sort time: {selection_time} seconds")
    print()

    #selection metodi ufro efeqturia
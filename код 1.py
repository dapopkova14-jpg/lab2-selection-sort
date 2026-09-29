import random

def selection_sort_ascending(arr):
    """Функция сортировки выбором по возрастанию"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

random_array = [random.randint(2, 103) for _ in range(10)]

print("Исходный массив:", random_array)
sorted_array = selection_sort_ascending(random_array)
print("Отсортированный массив (по возрастанию):", sorted_array)

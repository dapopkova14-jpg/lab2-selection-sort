import random

def selection_sort_descending(arr):
    """Функция сортировки выбором по убыванию"""
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

random_array = [random.randint(0, 100) for _ in range(10)]

print("Исходный массив:", random_array)
sorted_array = selection_sort_descending(random_array)
print("Отсортированный массив (по убыванию):", sorted_array)

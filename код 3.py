def selection_sort_strings(arr):
    """Функция сортировки выбором для строк (телефонов)"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

phones = [
    "45-67-89",
    "12-34-56",
    "99-88-77",
    "23-45-67",
    "50-50-50",
    "11-22-33"
]

print("Исходный список телефонов:", phones)
sorted_phones = selection_sort_strings(phones)
print("Отсортированный список (по возрастанию):", sorted_phones)

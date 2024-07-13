import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для запуску і вимірювання часу сортування
def measure_sorting_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    end_time = timeit.default_timer()
    return end_time - start_time

# Генерація даних для тестування
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Основна функція для виконання тестів і виведення результатів
def main():
    data_sizes = [1000, 10000, 100000]
    for size in data_sizes:
        data = generate_data(size)

        # Вимірювання часу для сортування злиттям
        merge_sort_time = measure_sorting_time(merge_sort, data.copy())
        print(f'Merge Sort Time for {size} elements: {merge_sort_time:.6f} seconds')

        # Вимірювання часу для сортування вставками
        insertion_sort_time = measure_sorting_time(insertion_sort, data.copy())
        print(f'Insertion Sort Time for {size} elements: {insertion_sort_time:.6f} seconds')

        # Вимірювання часу для Timsort (вбудоване сортування Python)
        timsort_time = measure_sorting_time(sorted, data.copy())
        print(f'Timsort Time for {size} elements: {timsort_time:.6f} seconds')

if __name__ == "__main__":
    main()

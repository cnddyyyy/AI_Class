from bisect import bisect_left, bisect_right

def count_occurrences_and_indices(A, u):
    # Sort the list to use binary search
    A_sorted = sorted(A)
    

    left_index = bisect_left(A_sorted, u)
    right_index = bisect_right(A_sorted, u)
    
    if left_index == right_index:
        return f"{u} tidak ditemukan dalam list."
    
    count = right_index - left_index
    indices = [i for i, value in enumerate(A) if value == u]
    
    return f"Angka {u} muncul sebanyak {count} kali pada indeks {indices}"

#memanggil 
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
u = 1
result = count_occurrences_and_indices(A, u)
print(result)

A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
u = 2
result = count_occurrences_and_indices(A, u)
print(result)

A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
u = 3
result = count_occurrences_and_indices(A, u)
print(result)

A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
u = 5
result = count_occurrences_and_indices(A, u)
print(result)

A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
u = 7
result = count_occurrences_and_indices(A, u)
print(result)

A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
u = 10
result = count_occurrences_and_indices(A, u)
print(result)
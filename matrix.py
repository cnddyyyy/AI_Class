# Cindy Amelia_ F55123098 

# Menggunakan Library Numpy
import numpy as np

print("Hasil Menggunakan Library")

# Mendefinisikan matriks
A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Perkalian Matriks A * C
try:
    A_C_multiplication = A @ C
    print("Matriks A * C:\n", A_C_multiplication)
except ValueError as e:
    print("Error pada perkalian matriks A * C:", e)

# Perkalian Matriks A * D (yang seharusnya error)
try:
    A_D_multiplication = A @ D
    print("Matriks A * D:\n", A_D_multiplication)
except ValueError as e:
    print("Error pada perkalian matriks A * D:", e)

# Penjumlahan Matriks D + E
try:
    D_E_addition = D + E
    print("Matriks D + E:\n", D_E_addition)
except ValueError as e:
    print("Error pada penjumlahan matriks D + E:", e)

# Pengurangan Matriks D - E
try:
    D_E_subtraction = D - E
    print("Matriks D - E:\n", D_E_subtraction)
except ValueError as e:
    print("Error pada pengurangan matriks D - E:", e)



# Tanpa Library Numpy

print("Hasil Tanpa Library")

# Mendefinisikan matriks
A = [[3, 0], [-1, 2], [1, 1]]
B = [[4, -1], [0, 2]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

# Fungsi untuk perkalian matriks
def matrix_multiply(X, Y):
    # Cek apakah jumlah kolom X sama dengan jumlah baris Y
    if len(X[0]) != len(Y):
        raise ValueError("Ukuran matriks tidak sesuai untuk perkalian.")
    return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

# Fungsi untuk penjumlahan matriks
def matrix_add(X, Y):
    # Cek apakah ukuran matriks X dan Y sama
    if len(X) != len(Y) or len(X[0]) != len(Y[0]):
        raise ValueError("Ukuran matriks tidak sesuai untuk penjumlahan.")
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk pengurangan matriks
def matrix_subtract(X, Y):
    # Cek apakah ukuran matriks X dan Y sama
    if len(X) != len(Y) or len(X[0]) != len(Y[0]):
        raise ValueError("Ukuran matriks tidak sesuai untuk pengurangan.")
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Perkalian Matriks A * C
try:
    A_C_multiplication = matrix_multiply(A, C)
    print("Matriks A * C:\n", A_C_multiplication)
except ValueError as e:
    print("Error pada perkalian matriks A * C:", e)

# Perkalian Matriks A * D (yang seharusnya error)
try:
    A_D_multiplication = matrix_multiply(A, D)
    print("Matriks A * D:\n", A_D_multiplication)
except ValueError as e:
    print("Error pada perkalian matriks A * D:", e)

# Penjumlahan Matriks D + E
try:
    D_E_addition = matrix_add(D, E)
    print("Matriks D + E:\n", D_E_addition)
except ValueError as e:
    print("Error pada penjumlahan matriks D + E:", e)

# Pengurangan Matriks D - E
try:
    D_E_subtraction = matrix_subtract(D, E)
    print("Matriks D - E:\n", D_E_subtraction)
except ValueError as e:
    print("Error pada pengurangan matriks D - E:", e)


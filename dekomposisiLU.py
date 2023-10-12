import numpy as np # Mengimpor pustaka NumPy untuk digunakan dalam pemrosesan matriks

# Membuat fungsi LU_decomposition yang menerima matriks A dan ukuran n sebagai argumen
def LU_decomposition(A, n):
# Menginisialisasi matriks L dan U dengan nol, yang akan menyimpan hasil dekomposisi LU
    L = np.empty((n, n))
    U = np.empty((n, n))

    for i in range(n): # Memulai iterasi untuk setiap baris i dari matriks
        L[i, i] = 1  # Inisialisasi elemen diagonal matriks L dengan 1
        for j in range(i, n): # Memulai iterasi untuk setiap kolom j mulai dari i hingga akhir matriks
            U[i, j] = A[i, j] # Menyalin nilai elemen matriks A ke matriks U
            for k in range(i): # Menghitung elemen matriks U dengan mengurangkan hasil perkalian elemen-elemen matriks L dan U
                U[i, j] -= L[i, k] * U[k, j]
        for j in range(i+1, n): # Melanjutkan iterasi untuk setiap kolom j mulai dari i + 1
            L[j, i] = A[j, i] # Menyalin nilai elemen matriks A ke matriks L
            for k in range(i): # Menghitung elemen matriks L dengan mengurangkan hasil perkalian elemen-elemen matriks L dan U sesuai dengan rumus dekomposisi LU
                L[j, i] -= L[j, k] * U[k, i]
            L[j, i] /= U[i, i] # Normalisasi elemen L dengan membaginya dengan elemen diagonal dari U

    return L, U # Mengembalikan matriks L dan U yang berisi hasil dekomposisi LU

# Memasukkan matriks contoh A dan ukuran n ke dalam fungsi LU_decomposition
A = np.array([[4, 3, 2],
              [2, 2, 3],
              [3, 5, 5]])
n = 3
L, U = LU_decomposition(A, n)

# Mencetak hasil
print("Matriks L:")
print(L)
print("Matriks U:")
print(U)

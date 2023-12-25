import numpy as np

# Fungsi untuk eliminasi Gauss parsial pada sistem persamaan linear Ax = b
def gaussian_partial(A, b):
    n = A.shape[0]
    C = np.c_[A, b.reshape(-1, 1)]  # Menggabungkan matriks A dan b menjadi matriks gabungan C
    flag = 0  # Penanda untuk solusi tidak unik atau sistem tak terhingga

    for i in range(n-1):
        max_c, chosen_k  = 0, i
        
        # Memilih baris dengan elemen terbesar pada kolom i
        for k in range(i, n):
            if np.abs(C[k, i]) > max_c:
                max_c = np.abs(C[k, i])
                chosen_k = k

        if max_c == 0:
            flag = 1  # Solusi tidak unik atau sistem tak terhingga
            break

        # Menukar baris ke-i dengan baris terpilih (chosen_k)
        if chosen_k != i:
            temp = C[i, :].copy()
            C[i, :] = C[chosen_k, :]
            C[chosen_k, :] = temp

        # Menggunakan eliminasi Gauss untuk menghasilkan matriks segitiga atas T
        for j in range(i+1, n):
            c = C[j, i] / C[i, i]
            C[j, :] = C[j, :] - c * C[i, :]

    return C, flag

# Fungsi untuk substitusi mundur pada matriks segitiga atas T
def backsubstitution(T):
    flag = 0  # Penanda untuk solusi tidak unik
    n = T.shape[0]
    X = np.zeros((n))

    if T[n-1, n-1] == 0:
        flag = 1  # Solusi tidak unik
    else:
        # Menghitung solusi menggunakan substitusi mundur
        X[n-1] = T[n-1, n] / T[n-1, n-1]

        for i in range(n-2, -1, -1):
            s = 0
            for j in range(i+1, n):
                s += T[i, j] * X[j]

            X[i] = (T[i, n] - s) / T[i, i]

    return X, flag

# Meminta input matriks A dari pengguna
n = int(input("Masukkan ukuran matriks (n x n): "))
A = []
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(elem)
    A.append(row)

# Meminta input matriks b dari pengguna
b = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    b.append([elem])

# Menjalankan metode eliminasi Gauss parsial
T, err = gaussian_partial(np.array(A), np.array(b))

if err:
    print('Solusi tidak unik atau sistem tak terhingga')
else:
    # Menjalankan substitusi mundur untuk mendapatkan solusi
    X, err = backsubstitution(T)
    if err:
        print('Solusi tidak unik')
    else:
        # Menampilkan solusi sistem persamaan linear
        print('Solusi:')
        for i, val in enumerate(X):
            print(f"X{i+1} = {val}")

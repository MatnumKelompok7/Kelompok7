import numpy as np

def metode_bisection(fungsi, a, b, tol=1e-6, max_iter=100):

    # Mengecek tanda fungsi pada batas interval
    if fungsi(a) * fungsi(b) >= 0:
        raise ValueError("Metode bisection memerlukan nilai f(a) dan f(b) yang berlawanan tanda pada interval [a, b]")

    iterasi = 0
    while (b - a) / 2 > tol and iterasi < max_iter:
        # Menghitung titik tengah interval
        c = (a + b) / 2

        # Jika nilai fungsi di titik tengah adalah 0, maka akar ditemukan secara tepat
        if fungsi(c) == 0:
            return c, iterasi

        # Menyesuaikan batas interval berdasarkan tanda fungsi di titik tengah
        elif fungsi(c) * fungsi(a) < 0:
            b = c
        else:
            a = c

        # Menambah jumlah iterasi
        iterasi += 1

    # Menghitung akar sebagai nilai tengah interval
    akar = (a + b) / 2
    return akar, iterasi

# Contoh penggunaan metode bisection dengan NumPy
def contoh_fungsi(x):
    return x**3 - x**2 - 1

# Konversi fungsi ke bentuk fungsi NumPy
fungsi_np = np.vectorize(contoh_fungsi)

# Tentukan interval awal [a, b]
a = 1.0
b = 2.0

# Panggil metode bisection
akar, iterasi = metode_bisection(fungsi_np, a, b)

# Tampilkan hasil
print("Akar:", akar)
print("Jumlah Iterasi:", iterasi)

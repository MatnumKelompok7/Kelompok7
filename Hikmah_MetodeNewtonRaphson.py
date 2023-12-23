import math
import matplotlib.pyplot as plt
import numpy as np

# Fungsi yang ingin dicari akarnya
def f(x):
    return math.exp(x) - x

# Turunan pertama dari fungsi f(x)
def df(x):
    return math.exp(x) - 1

# Meminta input dari pengguna untuk nilai awal (x0)
x0 = float(input("Masukkan nilai awal (x0): "))

# Meminta input dari pengguna untuk akurasi
tolerance = float(input("Masukkan akurasi (contoh: 1e-6): "))

# Maksimum iterasi
max_iterations = 100

# Inisialisasi list untuk menyimpan nilai-nilai x dan f(x) selama iterasi
x_values = []
f_values = []

for i in range(max_iterations):
    x_values.append(x0)
    f_values.append(f(x0))
    x1 = x0 - f(x0) / df(x0)
    if abs(f(x1)) < tolerance:
        break
    x0 = x1

print("Akar yang ditemukan:", x1)

# Membuat array x untuk plotting
x = np.linspace(min(x_values) - 1, max(x_values) + 1, 100)
y = [f(xi) for xi in x]

# Membuat plot untuk fungsi f(x) dan akarnya
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = exp(x) - x')
plt.scatter(x1, 0, c='green', marker='o', label='Akar')  # Menampilkan akar yang ditemukan
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik Fungsi dan Akar Menggunakan Metode Newton-Raphson')
plt.legend()
plt.grid(True)
plt.show()

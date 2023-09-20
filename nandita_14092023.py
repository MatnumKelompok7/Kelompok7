import numpy as np # Mengimpor pustaka NumPy untuk operasi numerik
import matplotlib.pyplot as plt # Mengimpor pustaka Matplotlib untuk plotting

# Definisi fungsi metode Bagi Dua
def bisection_method(f, a, b, tol, max_iter):
    # Memeriksa apakah tanda fungsi pada ujung-ujung interval a dan b sama
    if f(a) * f(b) >= 0:
        raise ValueError("Tidak ada akar pada interval [a, b]") # Raise exception jika tanda sama

    # Melakukan iterasi hingga jumlah iterasi maksimum tercapai
    for iteration in range(1, max_iter + 1):
        c = (a + b) / 2 # Menghitung titik tengah c dari interval

        # Memeriksa apakah c adalah akar atau toleransi terpenuhi
        if f(c) == 0 or (b - a) / 2 < tol:
            print(f"Program berhenti di iterasi ke-{iteration}") # Mencetak pesan iterasi berhenti ke-i
            return c

        # Memeriksa tanda fungsi pada interval [a, c]
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    # Jika mencapai sini, berarti tidak konvergen
    print(f"Program berhenti setelah mencapai iterasi maksimum ({max_iter} iterasi)")
    raise Exception("Metode bisection tidak konvergen") # Raise exception jika tidak konvergen

# Fungsi utama
def main():
    user_input = input("Masukkan fungsi sebagai string (contoh: x**3 - 2*x - 5): ")
    f = lambda x: eval(user_input) # Membuat fungsi yang dapat dievaluasi dari string input

    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    tol = float(input("Masukkan galat (toleransi): "))
    max_iter = int(input("Masukkan iterasi maksimum: "))

    akar = bisection_method(f, a, b, tol, max_iter) # Memanggil metode bisection untuk mencari akar

    print(f"Akar yang ditemukan: {akar}")

    # Membuat plot fungsi dan menandai akar
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y, label="Fungsi")
    plt.axvline(x=akar, color='r', linestyle='--', label="Akar")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main() # Memanggil fungsi main jika program dijalankan sebagai script utama

# Fungsi untuk menghitung integral menggunakan metode trapesium
def hitung_integral_trapesium(fungsi, batas_bawah, batas_atas, n):
    # Menghitung lebar interval
    h = (batas_atas - batas_bawah) / n
    
    # Menghitung nilai integral dengan menambahkan nilai fungsi di kedua ujung interval
    integral = (fungsi(batas_bawah) + fungsi(batas_atas)) / 2

    # Menggunakan loop untuk menambahkan nilai fungsi di setiap titik tengah interval
    for i in range(1, n):
        x = batas_bawah + i * h
        integral += fungsi(x)

    # Mengalikan dengan lebar interval h
    integral *= h
    return integral

def fungsi_input(x):
    return eval(input(f'Masukkan fungsi dalam bentuk Python (contoh: x**2 + 2*x + 1): '))

batas_bawah = float(input('Masukkan batas bawah integral: '))
batas_atas = float(input('Masukkan batas atas integral: '))
n = int(input('Masukkan jumlah subinterval: '))

# Hitung integral menggunakan metode trapesium
hasil_integral = hitung_integral_trapesium(fungsi_input, batas_bawah, batas_atas, n)
print(f'Hasil integral metode trapesium: {hasil_integral}')

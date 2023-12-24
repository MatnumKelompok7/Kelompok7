# Fungsi untuk menghitung integral menggunakan metode titik tengah
def hitung_integral_titik_tengah(fungsi, batas_bawah, batas_atas, n):
    # Menghitung lebar interval
    h = (batas_atas - batas_bawah) / n
    
    # Inisialisasi nilai integral
    integral = 0

    # Menggunakan loop untuk menambahkan nilai fungsi pada titik tengah setiap subinterval
    for i in range(n):
        x_mid = batas_bawah + (i + 0.5) * h
        integral += fungsi(x_mid)

    # Mengalikan dengan lebar interval h
    integral *= h
    return integral

def fungsi_input(x):
    return eval(input(f'Masukkan fungsi dalam bentuk Python (contoh: x**2 + 2*x + 1): '))

# Input dari pengguna
batas_bawah = float(input('Masukkan batas bawah integral: '))
batas_atas = float(input('Masukkan batas atas integral: '))
n = int(input('Masukkan jumlah subinterval: '))

# Hitung integral menggunakan metode titik tengah
hasil_integral = hitung_integral_titik_tengah(fungsi_input, batas_bawah, batas_atas, n)
print(f'Hasil integral metode titik tengah: {hasil_integral}')

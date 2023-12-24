def hitung_integral_simpson13(fungsi, batas_bawah, batas_atas, n):
    h = (batas_atas - batas_bawah) / n
    integral = fungsi(batas_bawah) + fungsi(batas_atas)

    for i in range(1, n):
        x = batas_bawah + i * h
        koefisien = 4 if i % 2 == 1 else 2
        integral += koefisien * fungsi(x)

    integral *= h / 3
    return integral

def fungsi_input(x):
    return eval(input(f'Masukkan fungsi dalam bentuk Python (contoh: x**2 + 2*x + 1): '))

# Masukkan batas bawah, batas atas, dan jumlah subinterval
batas_bawah = float(input('Masukkan batas bawah integral: '))
batas_atas = float(input('Masukkan batas atas integral: '))
n = int(input('Masukkan jumlah subinterval (harus genap): '))

# Hitung integral menggunakan metode Simpson 1/3
hasil_integral = hitung_integral_simpson13(fungsi_input, batas_bawah, batas_atas, n)
print(f'Hasil integral metode Simpson 1/3: {hasil_integral}')

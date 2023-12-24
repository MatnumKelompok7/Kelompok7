# Fungsi untuk menghitung turunan menggunakan metode selisih maju
def hitung_turunan_selisih_maju(fungsi, nilai_x, h):
    # Menggunakan rumus turunan selisih maju: (f(x + h) - f(x)) / h
    turunan = (fungsi(nilai_x + h) - fungsi(nilai_x)) / h
    return turunan

# Fungsi untuk menghitung turunan menggunakan metode selisih mundur
def hitung_turunan_selisih_mundur(fungsi, nilai_x, h):
    # Menggunakan rumus turunan selisih mundur: (f(x) - f(x - h)) / h
    turunan = (fungsi(nilai_x) - fungsi(nilai_x - h)) / h
    return turunan

# Fungsi untuk menghitung turunan menggunakan metode selisih nilai tengah
def hitung_turunan_selisih_tengah(fungsi, nilai_x, h):
    # Menggunakan rumus turunan selisih nilai tengah: (f(x + h) - f(x - h)) / (2 * h)
    turunan = (fungsi(nilai_x + h) - fungsi(nilai_x - h)) / (2 * h)
    return turunan

# Contoh fungsi polinom
def polinom(x):
    return x**2 + 3*x + 2

# Nilai x yang ingin dihitung turunannya
x = 2

# Nilai h (langkah)
h = 0.0001

# Hitung turunan menggunakan metode selisih maju
turunan_selisih_maju = hitung_turunan_selisih_maju(polinom, x, h)
print(f'Turunan Selisih Maju di {x} adalah {turunan_selisih_maju}')

# Hitung turunan menggunakan metode selisih mundur
turunan_selisih_mundur = hitung_turunan_selisih_mundur(polinom, x, h)
print(f'Turunan Selisih Mundur di {x} adalah {turunan_selisih_mundur}')

# Hitung turunan menggunakan metode selisih nilai tengah
turunan_selisih_tengah = hitung_turunan_selisih_tengah(polinom, x, h)
print(f'Turunan Selisih Tengah di {x} adalah {turunan_selisih_tengah}')

import math # Mengimpor pustaka matematika untuk menggunakan fungsi eksponen e^x

# Definisi fungsi f(x) = e^x - x
def fungsi_dua(x):
    return math.exp(x) - x

# Definisi metode Bagi Dua untuk mencari akar fungsi
def metode_bagi_dua_fungsi_dua(a, b, toleransi):
    # Memeriksa apakah tanda fungsi pada ujung-ujung interval a dan b sama
    if fungsi_dua(a) * fungsi_dua(b) >= 0:
        print("Metode Bagi Dua tidak berlaku pada interval ini.")  # Cetak pesan jika tanda sama
        return None

    # Melakukan iterasi hingga selisih antara b dan a lebih kecil daripada toleransi
    while (b - a) / 2.0 > toleransi:
        c = (a + b) / 2.0  # Menghitung titik tengah c dari interval

        if fungsi_dua(c) == 0.0:  # Memeriksa apakah c adalah akar
            return c
        elif fungsi_dua(a) * fungsi_dua(c) < 0:  # Memeriksa tanda fungsi pada interval [a, c]
            b = c
        else:
            a = c

    return (a + b) / 2.0  # Mengembalikan akar yang ditemukan

batas_bawah2 = 0      # Batas bawah interval
batas_atas2 = -122    # Batas atas interval
toleransi2 = 0.01     # Toleransi error

akar2 = metode_bagi_dua_fungsi_dua(batas_bawah2, batas_atas2, toleransi2)  # Memanggil metode Bagi Dua
print("Akar dari f(x) = e^x - x adalah:", akar2)  # Menampilkan akar yang ditemukan

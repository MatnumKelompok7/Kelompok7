# Definisi fungsi f(x) = x^3 - 2x + 1
def fungsi_satu(x):
    return x**3 - 2*x + 1

# Definisi metode Bagi Dua untuk mencari akar fungsi
def metode_bagi_dua_fungsi_satu(a, b, toleransi):
    # Memeriksa apakah tanda fungsi pada ujung-ujung interval a dan b sama
    if fungsi_satu(a) * fungsi_satu(b) >= 0:
        print("Metode Bagi Dua tidak berlaku pada interval ini.")  # Cetak pesan jika tanda sama
        return None

    # Melakukan iterasi hingga selisih antara b dan a lebih besar daripada toleransi
    while (b - a) / 2 > toleransi:
        c = (a + b) / 2  # Menghitung titik tengah c dari interval

        if fungsi_satu(c) == 0: # Memeriksa apakah c adalah akar
            return c
        elif fungsi_satu(a) * fungsi_satu(c) < 0: # Memeriksa tanda fungsi pada interval [a, c]
            b = c
        else:
            a = c

    return (a + b) / 2 # Mengembalikan akar yang ditemukan

batas_bawah1 = 3    # Batas bawah interval
batas_atas1 = -2    # Batas atas interval
toleransi1 = 0.1    # Toleransi error

akar1 = metode_bagi_dua_fungsi_satu(batas_bawah1, batas_atas1, toleransi1) # Memanggil metode Bagi Dua
print("Akar dari f(x) = x^3 - 2x + 1 adalah:", akar1) # Menampilkan akar yang ditemukan

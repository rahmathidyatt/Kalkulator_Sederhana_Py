def penjumlahan(a, b):
    return a + b 

def pengurangan(a, b):
    return a - b

def perkalian (a, b):
    return a * b 

def pembagian (a, b):
    if b != 0:
        return a / b
    else:
        return "error: pembagian tidak bisa dibagi nol"

print("___!Kalkulator Sederhana___")
print("___________________________") 

while True:
    print("Pilih Operasi")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan Pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Anda Keluar Dari Kalkulator")
        break

    angka1 = float(input("Masukkan Angka Pertama: "))
    angka2 = float(input("Masukkan Angka Kedua: "))

    if pilihan =='1':
        hasil = penjumlahan(angka1, angka2)
        print("Hasil Penjumlahan = ", hasil)
    elif pilihan =='2':
        hasil = pengurangan(angka1, angka2)
        print("Hasil Pengurangan = ", hasil)
    elif pilihan =='3':
        hasil = perkalian(angka1, angka2)
        print("Hasil Perkalian=", hasil)
    elif pilihan =='4':
        hasil = pembagian(angka1, angka2)
        print("Hasil Pembagian=", hasil)
    else:
        print("Anda Tidak Memasukkan Pilihan.")
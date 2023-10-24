# Nomor 1
motor1 = ["B123L","Thunder",125, "hitam"]
motor1.append(2000000)
motor1.append(2)
motor1.insert(2, "Suzuki")
motor1.insert(3, "Kendaraan Bermotor")
print("Kode Kendaraan  : ", motor1[0])
print("Nama Kendaraan  : ", motor1[1])
print("Merk Kendaraan  : ", motor1[2])
print("Jenis Kendaraan : ", motor1[3])
print("CC Kendaraan    : ", motor1[4])
print("Warna Kendaraan : ", motor1[5])
print("harga           : Rp.","{:,}".format(motor1[6]))
print("Jumlah Ban      : ", motor1[7])

# nomor 3
# pilihan  = int(input("""Silahkan pilih nomor dibawah ini 
# untuk menggunakan tools dibawah ini
# ==================================
# Pilihan 
# ==================================
# 1. menghitung luas persegi
# 2. menghitung luas lingkaran
# 3. menghitung luas segitiga
# =================================
# Pilihan mu? """))
# match pilihan:
#     case 1:
#         print ("kamu memilih 1 untuk menghitung luas persegi")
#         sisi = int(input ("masukan sisi ?"))
#         luasP = sisi * sisi
#         print ("luas persegi yang sisinya ", sisi, " adalah ",luasP)
#     case 2:
#         print ("kamu memilih 2 untuk menghitung luas lingkaran")
#         jari2 = float(input ("masukan jari2 ?"))
#         luasL = 3.14 * jari2 * jari2
#         print ("luas lingkaran yang jari2nya ", jari2, " adalah ",int(luasL))
#     case 3:
#         print ("kamu memilih 3 untuk menghitung luas segitiga")
#         alas = int(input ("masukan alas ?"))
#         tinggi = int(input ("masukan tinggi ?"))
#         luasS = 0.5 * alas * tinggi
#         print ("luas segitiga yang alasnya ", alas, " dan tingginya",tinggi , " adalah ",int(luasS))
#     case _:
#         print("salah memilih pilihan")
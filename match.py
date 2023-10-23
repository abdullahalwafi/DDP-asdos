pilihan = input("""Silahkan pilih tools dibawah ini dengan mengirimkan yang dikurung
==============================
Tools yang tersedia
==============================
1. Menghitung luas persegi (persegi)
2. Menghitung luas lingkaran (lingkaran)
3. Menghitung luas segitiga (segitiga)
==============================
Pilihanmu? """)

match pilihan:
    case "persegi":
        print("kamu memilih menghitung luas persegi")
        sisi = int(input("sisi = "))
        LuasPersegi = sisi * sisi
        print("Luas persegi untuk persegi dengan sisi", sisi, "adalah", LuasPersegi)
    case "lingkaran":
        print("kamu memilih menghitung luas lingkaran")
        r = int(input("jari jari = "))
        LuasL = 3.14 * r * r
        print("Luas lingkaran untuk lingkaran dengan jari jari", r, "adalah", LuasL)
    case "segitiga":
        print("kamu memilih menghitung luas segitiga")
        alas = int(input("alas = "))
        tinggi = int(input("tinggi = "))
        LuasS = 0.5 * alas * tinggi
        print("Luas segitiga untuk segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", LuasS)
    case _:
        print("pilihan tidak ada")    

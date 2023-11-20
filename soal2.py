def nilai_kelulusan(nilai):
    if nilai >=60 and nilai<=100:
        print(f"Nilai kamu {nilai} kamu lulus")
    elif nilai < 60 and nilai >= 0:
        print(f"Nilai kamu {nilai} kamu tidak lulus")
    else:
        print("data ditemukan")
nilai_kelulusan(10)
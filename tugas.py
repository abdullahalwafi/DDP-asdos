TB = 175/100
BB = 60
BMI = BB/(TB**2)

print("BMI anda adalah", BMI)


if BMI < 18.5:
    print("status Berat badan anda adalah Kekurangan berat badan")
elif BMI >= 18.5 and BMI <= 24.9:
    print("status Berat badan anda adalah Ideal")
elif BMI >= 25.0 and BMI <= 29.9:
    print("status Berat badan anda adalah Kelebihan berat badan")
elif BMI >= 30.0:
    print("status Berat badan anda adalah Obesitas")
else:
    print('data tidak ditemukan')
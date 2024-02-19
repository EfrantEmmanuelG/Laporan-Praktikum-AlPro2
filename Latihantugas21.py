BMI = eval(input("BMI yang diharapkan(kg): "))
tinggi = eval(input("Tinggi anda(cm): "))
print('BMI yang anda harapkan yaitu: ', BMI)
tinggi = tinggi / 100
berat = BMI * (tinggi **2)
print('Jika dalam meter, tinggi anda: ', tinggi)
print('berat badan yang anda perlukan adalah: ', berat, "kg")

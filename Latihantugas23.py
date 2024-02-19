gaji = eval(input("Gaji yang diinginkan per jam: "))
jumlah_waktu = eval(input("Jumlah jam kerja yang akan dilakukan dalam seminggu: "))

pendapatantotal = gaji * jumlah_waktu
print("Pendapatan Budi selama libur musim panas tanpa pajak yaitu: Rp", pendapatantotal)

pendapatanbersih = pendapatantotal - (pendapatantotal * 0.14)
print("Pendapatan budi setelah membayar pajak: Rp", pendapatanbersih)

aksesoris = pendapatanbersih * 0.10
print("Jumlah uang yang dihabiskan Budi untuk aksesoris yaitu: Rp", aksesoris)

alat_tulis = pendapatanbersih * 0.01
print("Jumlah uang yang dihabiskan Budi untuk alat tulis yaitu: Rp", alat_tulis)

sedekah = (pendapatanbersih - aksesoris - alat_tulis) * 0.25
print("Jumlah uang yang dihabiskan Budi untuk sedekah yaitu: Rp", sedekah)

pendapatanyatim = ((pendapatanbersih - aksesoris - alat_tulis - sedekah)/1000) * 0.3
print("Jumlah uang yang diterima oleh anak yatim yaitu: Rp", pendapatanyatim)

kaum = (pendapatanbersih - aksesoris - alat_tulis - sedekah - pendapatanyatim)
print("Jumlah uang yang diterima oleh kaum dhuafa yaitu: Rp", kaum)



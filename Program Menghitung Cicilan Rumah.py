# Membuat Program Cicilan Rumah
harga_jual = float(input("Masukkan Harga Jual Rumah : "))
harga_asal = float(input("Masukkan Harga Asal Rumah : "))
print("pilih lama cicilan : \n20 tahun \n15 tahun \n10 tahun \n5 tahun")
lama_cicilan = int(input("Masukkan Lama Tahun Cicilan : "))
if lama_cicilan in [20, 15, 10, 5] :
    for tahun in range(1, lama_cicilan + 1) :
        cicilan = (harga_jual - harga_asal) / lama_cicilan
        print("Tahun :", tahun, "Cicilan:", cicilan, "rupiah")
else :
    print("cicilan tidak berlaku pada lama tahun tersebut")


from collections import deque

antrian_darurat = deque()
antrian_umum = deque()

n = int(input("Jumlah pasien: "))

for i in range(n):

    data = input(
        "Masukkan Nama dan Jenis (Umum/Darurat): "
    ).split()

    nama = data[0]
    jenis = data[1].lower()

    if jenis == "darurat":
        antrian_darurat.append(nama)

    else:
        antrian_umum.append(nama)

print("\nUrutan Pelayanan:")

while antrian_darurat or antrian_umum:

    if antrian_darurat:
        print(antrian_darurat.popleft())

    elif antrian_umum:
        print(antrian_umum.popleft())
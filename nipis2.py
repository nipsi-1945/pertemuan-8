from collections import deque

antrian = deque()

n = int(input("Masukkan jumlah pelanggan: "))

for i in range(n):
    nama = input(f"Nama pelanggan ke-{i+1}: ")
    antrian.append(nama)   

if antrian:
    dilayani = antrian.popleft()   
    print("\nPelanggan dilayani:", dilayani)

print("\nSisa antrean:")
for pelanggan in antrian:
    print(pelanggan)
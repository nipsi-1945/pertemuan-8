stack_buku = []

n = int(input("masukan jumlah buku: "))

for i in range (n):
    judul = input (f"judul buku ke - {i+1}: ")
    stack_buku.append(judul )

    print ("\n isi stack :")
    for buku in reversed (stack_buku):
        print (buku)

    if stack_buku :
        buku_diambil = stack_buku.pop()
        print ( "\n Buku yang diambil:", buku_diambil)

    print("\n isi stack setelah pop :")
    for buku in reversed (stack_buku):
        print(buku)
from collections import deque

# =========================
# DATA
# =========================
history = []                 # Stack untuk browser history
download_queue = deque()     # Queue untuk download

total_kunjungan = 0
download_selesai = 0


# =========================
# FUNGSI BROWSER HISTORY
# =========================
def kunjungi_halaman():
    global total_kunjungan

    url = input("Masukkan URL halaman: ")
    history.append(url)
    total_kunjungan += 1

    print(f"Berhasil membuka {url}")


def back():
    if history:
        halaman = history.pop()
        print(f"Kembali dari {halaman}")
    else:
        print("History kosong!")


def tampilkan_history():
    if history:
        print("\n=== HISTORY BROWSER ===")

        for i in range(len(history)-1, -1, -1):
            print(history[i])

    else:
        print("Tidak ada history!")


# =========================
# FUNGSI DOWNLOAD MANAGER
# =========================
def tambah_download():
    file = input("Masukkan nama file: ")
    download_queue.append(file)

    print(f"{file} ditambahkan ke antrian download")


def proses_download():
    global download_selesai

    if download_queue:
        file = download_queue.popleft()
        download_selesai += 1

        print(f"Download selesai: {file}")

    else:
        print("Tidak ada antrian download!")


def tampilkan_download():
    if download_queue:
        print("\n=== ANTRIAN DOWNLOAD ===")

        for file in download_queue:
            print(file)

    else:
        print("Antrian download kosong!")


# =========================
# FUNGSI STATISTIK
# =========================
def statistik():
    print("\n=== STATISTIK SISTEM ===")
    print(f"Jumlah halaman pernah dikunjungi : {total_kunjungan}")
    print(f"Jumlah history tersimpan         : {len(history)}")
    print(f"Jumlah download selesai         : {download_selesai}")
    print(f"Jumlah download menunggu        : {len(download_queue)}")


# =========================
# MENU UTAMA
# =========================
while True:

    print("\n===== MENU =====")
    print("1. Kunjungi Halaman")
    print("2. Back")
    print("3. Tampilkan History")
    print("4. Tambah Download")
    print("5. Proses Download")
    print("6. Tampilkan Queue Download")
    print("7. Statistik")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kunjungi_halaman()

    elif pilihan == "2":
        back()

    elif pilihan == "3":
        tampilkan_history()

    elif pilihan == "4":
        tambah_download()

    elif pilihan == "5":
        proses_download()

    elif pilihan == "6":
        tampilkan_download()

    elif pilihan == "7":
        statistik()

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
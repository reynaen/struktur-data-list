log_tidur = []

def tambah_tidur(tanggal, jam_tidur):
    log_tidur.append([tanggal, jam_tidur])
    print(f"Data jam tidur pada {tanggal} dicatat: {jam_tidur} jam.")

def tampilkan_log():
    if not log_tidur:
        print("Tidak ada data tidur yang dicatat.")
    else:
        print("\nLog Jam Tidur:")
        for data in log_tidur:
            print(f"{data[0]}: {data[1]} jam")

def rata_tidur():
    if not log_tidur:
        print("Tidak ada data tidur untuk dihitung.")
    else:
        total = sum([data[1] for data in log_tidur])
        print(f"\nRata-rata tidur: {total / len(log_tidur):.2f} jam")

def tidur_extrem():
    if not log_tidur:
        print("Tidak ada data tidur untuk dianalisis.")
    else:
        jam_list = [data[1] for data in log_tidur]
        max_jam = max(jam_list)
        min_jam = min(jam_list)
        hari_max = [data[0] for data in log_tidur if data[1] == max_jam][0]
        hari_min = [data[0] for data in log_tidur if data[1] == min_jam][0]
        print(f"Tidur terlama: {max_jam} jam pada {hari_max}")
        print(f"Tidur tersingkat: {min_jam} jam pada {hari_min}")

def tidur_7_hari_terakhir():
    if len(log_tidur) < 7:
        print("Data tidur kurang dari 7 hari.")
    else:
        print("\nJam Tidur 7 Hari Terakhir:")
        for data in log_tidur[-7:]:
            print(f"{data[0]}: {data[1]} jam")

def menu():
    while True:
        print("\n--- Tracker Jam Tidur ---")
        print("1. Tambah Data Jam Tidur")
        print("2. Tampilkan Log Jam Tidur")
        print("3. Hitung Rata-rata Jam Tidur")
        print("4. Tampilkan Tidur Terlama dan Tersingkat")
        print("5. Tampilkan 7 Hari Terakhir")
        print("6. Keluar")

        pilihan = input("Pilih nomor menu (1-6): ")

        if pilihan == '1':
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            jam_tidur = float(input("Masukkan jam tidur (dalam jam): "))
            tambah_tidur(tanggal, jam_tidur)

        elif pilihan == '2':
            tampilkan_log()

        elif pilihan == '3':
            rata_tidur()

        elif pilihan == '4':
            tidur_extrem()

        elif pilihan == '5':
            tidur_7_hari_terakhir()

        elif pilihan == '6':
            print("Terima kasih telah menggunakan aplikasi Tracker Jam Tidur!")
            break

        else:
            print("Pilihan tidak valid, silakan pilih antara 1-6.")

menu()

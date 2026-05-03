def input_angka(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 0:
                print("Input ga boleh kurang dari 0")
            else:
                return nilai
        except ValueError:
            print("Input nya harus pake angka")

def input_nama(pesan):
    while True:
        nama = input(pesan)
        if nama.replace(" ", "").isalpha():
            return nama
        else:
            print("Nama nya harus pake huruf")

def bubble_sort(nama_pemain, jumlah_gol):
    n = len(jumlah_gol)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if jumlah_gol[j] < jumlah_gol[j+1]:
                jumlah_gol[j], jumlah_gol[j+1] = jumlah_gol[j+1], jumlah_gol[j]
                nama_pemain[j], nama_pemain[j+1] = nama_pemain[j+1], nama_pemain[j]

def tampilkan_data(nama_pemain, jumlah_gol):
    print("\nDaftar Pemain Berdasarkan Jumlah Gol Terbanyak:")
    for i in range(len(nama_pemain)):
        print(f"{i+1}. {nama_pemain[i]} - {jumlah_gol[i]} gol")

n = input_angka("Masukkan jumlah pemain sesuai selera: ")

nama_pemain = []
jumlah_gol = []

for i in range(n):
    print(f"\nData pemain ke-{i+1}")
    nama = input_nama("Nama pemain: ")
    gol = input_angka("Jumlah gol: ")

    nama_pemain.append(nama)
    jumlah_gol.append(gol)

bubble_sort(nama_pemain, jumlah_gol)
tampilkan_data(nama_pemain, jumlah_gol)
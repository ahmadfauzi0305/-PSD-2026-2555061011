while True:
    try:
        n = int(input("Masukkan jumlah pemain: "))
        if n <= 0:
            print("Jumlah pemain harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input harus berupa angka!")

nama_pemain = []
jumlah_gol = []

for i in range(n):
    print(f"\nData pemain ke-{i+1}")

    while True:
        nama = input("Nama pemain: ")
        if nama.isalpha():
            break
        else:
            print("Nama harus berupa huruf!")

    while True:
        try:
            gol = int(input("Jumlah gol: "))
            if gol < 0:
                print("Jumlah gol tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Jumlah gol harus berupa angka!")

    nama_pemain.append(nama)
    jumlah_gol.append(gol)

for i in range(n-1):
    for j in range(0, n-i-1):
        if jumlah_gol[j] < jumlah_gol[j+1]:
            jumlah_gol[j], jumlah_gol[j+1] = jumlah_gol[j+1], jumlah_gol[j]
            nama_pemain[j], nama_pemain[j+1] = nama_pemain[j+1], nama_pemain[j]

print("\nDaftar Pemain Berdasarkan Jumlah Gol (Terbanyak):")
for i in range(n):
    print(f"{nama_pemain[i]} - {jumlah_gol[i]} gol")
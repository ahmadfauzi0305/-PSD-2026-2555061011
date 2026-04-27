class Mobil:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None
        self.next = None

class Parkiran:
    def __init__(self):
        self.head = None

    def tambah_mobil(self, plat):
        mobil_baru = Mobil(plat)

        if self.head is None:
            self.head = mobil_baru
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = mobil_baru
        mobil_baru.prev = temp

    def keluar_mobil(self, plat):
        temp = self.head

        while temp:
            if temp.plat == plat:
                if temp.prev is None:
                    self.head = temp.next
                    if temp.next:
                        temp.next.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev

                print("Mobil berhasil keluar dari parkiran")
                return

            temp = temp.next

        print("Mobil tidak ditemukan")

    def tampilkan(self):
        if self.head is None:
            print("Parkiran kosong")
            return

        temp = self.head
        while temp:
            print(temp.plat, end=" <-> ")
            temp = temp.next
        print("None")

    def cari_mobil(self, plat):
        temp = self.head
        posisi = 1

        while temp:
            if temp.plat == plat:
                print("Mobil ditemukan di posisi", posisi)
                return
            temp = temp.next
            posisi += 1

        print("Mobil tidak ditemukan di parkiran")

    def jumlah_mobil(self):
        temp = self.head
        jumlah = 0

        while temp:
            jumlah += 1
            temp = temp.next

        print("Jumlah mobil di parkiran:", jumlah)

parkir = Parkiran()

while True:
    print("\n=== MENU PARKIR MOBIL ===")
    print("1. Tambah Mobil")
    print("2. Mobil Keluar")
    print("3. Tampilkan Parkiran")
    print("4. Cari Mobil")
    print("5. Jumlah Mobil")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        plat = input("Masukkan nama / plat mobil: ")
        parkir.tambah_mobil(plat)

    elif pilihan == "2":
        plat = input("Masukkan mobil yang keluar: ")
        parkir.keluar_mobil(plat)

    elif pilihan == "3":
        parkir.tampilkan()

    elif pilihan == "4":
        plat = input("Masukkan mobil yang dicari: ")
        parkir.cari_mobil(plat)

    elif pilihan == "5":
        parkir.jumlah_mobil()

    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
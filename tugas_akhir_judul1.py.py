# Membuat node untuk setiap mobil
class Mobil:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None
        self.next = None


# Membuat doubly linked list untuk parkiran
class Parkiran:
    def __init__(self):
        self.head = None

    # Menambahkan mobil ke parkiran
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

    # Menghapus mobil dari parkiran
    def keluar_mobil(self, plat):
        temp = self.head

        while temp:
            if temp.plat == plat:
                # jika mobil di depan
                if temp.prev is None:
                    self.head = temp.next
                    if temp.next:
                        temp.next.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next

    # Menampilkan antrian mobil
    def tampilkan(self):
        temp = self.head
        while temp:
            print(temp.plat, end=" <-> ")
            temp = temp.next
        print("None")


# Contoh penggunaan
parkir = Parkiran()

parkir.tambah_mobil("Mobil A")
parkir.tambah_mobil("Mobil B")
parkir.tambah_mobil("Mobil C")
parkir.tambah_mobil("Mobil D")

print("Antrian parkir:")
parkir.tampilkan()

print("\nMobil B keluar dari parkiran")
parkir.keluar_mobil("Mobil B")

print("Antrian parkir sekarang:")
parkir.tampilkan()
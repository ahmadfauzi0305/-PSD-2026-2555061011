class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.kode_barang = None
        self.stok = None
        self.state = SlotState.EMPTY


class HashMapStokBarang:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, kode_barang):
        return (kode_barang % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, kode_barang, stok):
        idx = self.hash_function(kode_barang)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].kode_barang == kode_barang:
                    self.table[i].stok = stok
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].kode_barang = kode_barang
                self.table[i].stok = stok
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def search(self, kode_barang):
        idx = self.hash_function(kode_barang)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].kode_barang == kode_barang):
                return self.table[i]

        return None

    def remove_barang(self, kode_barang):
        entry = self.search(kode_barang)

        if entry is None:
            return False

        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nData Stok Barang Minimarket")
        print("-" * 35)

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("KOSONG")

            elif self.table[i].state == SlotState.DELETED:
                print("DIHAPUS")

            else:
                print(
                    f"Kode Barang: {self.table[i].kode_barang}, "
                    f"Stok: {self.table[i].stok}"
                )


def main():
    stok_barang = HashMapStokBarang()

    stok_barang.insert(101, 50)   
    stok_barang.insert(111, 30)   
    stok_barang.insert(121, 25)   
    stok_barang.insert(102, 40)   

    print("Data Stok Barang:")
    stok_barang.display()

    kode_cari = int(input("\nMasukkan kode barang yang ingin dicari: "))

    hasil = stok_barang.search(kode_cari)

    if hasil is not None:
        print("\nBarang ditemukan!")
        print(f"Kode Barang : {hasil.kode_barang}")
        print(f"Jumlah Stok : {hasil.stok}")
    else:
        print("\nBarang tidak ditemukan.")

if __name__ == "__main__":
    main()
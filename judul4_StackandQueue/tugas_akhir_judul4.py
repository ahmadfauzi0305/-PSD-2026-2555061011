class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print(f"\n[SUKSES] Nomor antrean {x} berhasil dibuat.")

    def dequeue(self):
        if self.is_empty():
            print("\n[INFO] Antrean kosong. Tidak ada nasabah yang menunggu.")
            return None
        temp = self.front_ptr
        print(f"\n[PANGGILAN] Nomor antrean {temp.data}, silakan menuju ke Loket Kasir!")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None
        return temp.data

    def peek(self):
        if self.is_empty():
            print("\n[INFO] Antrean kosong.")
            return
        print(f"\n[INFO] Nasabah berikutnya yang akan dipanggil: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("\n[INFO] Antrean saat ini kosong.")
            return
        print("DAFTAR ANTREAN SAAT INI")
        print("Depan (Loket) -> ", end="")
        current = self.front_ptr
        while current is not None:
            print(f"[{current.data}]", end=" ")
            current = current.next
        print("<- Belakang")


def main():
    queue = QueueLinkedList()
    pilih = 0
    nomor_urut = 1 
    
    while pilih != 5:
        print("   SISTEM ANTREAN BANK CENTRAL   ")
        print("1. Ambil Nomor Antrean (Nasabah Baru)")
        print("2. Panggil Nasabah (Proses Loket)")
        print("3. Lihat Antrean Berikutnya")
        print("4. Tampilkan Seluruh Antrean")
        print("5. Tutup Bank & Selesai")
        
        try:
            pilih = int(input("Pilih Menu (1-5): "))
        except ValueError:
            print("\n[ERROR] Input harus berupa angka!")
            continue
            
        if pilih == 1:
            kode_antrean = f"B-{nomor_urut:03d}"
            queue.enqueue(kode_antrean)
            nomor_urut += 1 
            
        elif pilih == 2:
            queue.dequeue()
            
        elif pilih == 3:
            queue.peek()
            
        elif pilih == 4:
            queue.display()
            
        elif pilih == 5:
            if not queue.is_empty():
                print("\n[PERINGATAN] Menghabiskan sisa antrean sebelum menutup bank...")
                while not queue.is_empty():
                    queue.dequeue()
            print("\nBank telah resmi ditutup. Terima kasih!")
            
        else:
            print("\n[ERROR] Pilihan menu tidak tersedia!")


if __name__ == "__main__":
    main()
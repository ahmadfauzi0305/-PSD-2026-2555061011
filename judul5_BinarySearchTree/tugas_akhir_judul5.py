class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None


class BSTNilaiSiswa:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nilai):
        if root is None:
            return Node(nilai)

        if nilai < root.nilai:
            root.left = self.insert_node(root.left, nilai)
        elif nilai > root.nilai:
            root.right = self.insert_node(root.right, nilai)

        return root

    def insert(self, nilai):
        self.root = self.insert_node(self.root, nilai)

    # Mencari nilai siswa
    def search_node(self, root, nilai):
        if root is None:
            return False

        if root.nilai == nilai:
            return True

        if nilai < root.nilai:
            return self.search_node(root.left, nilai)

        return self.search_node(root.right, nilai)

    def search(self, nilai):
        return self.search_node(self.root, nilai)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.nilai, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.nilai, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.nilai, end=" ")

    def find_min(self, root):
        if root is None:
            return None

        current = root
        while current.left is not None:
            current = current.left

        return current.nilai

    def find_max(self, root):
        if root is None:
            return None

        current = root
        while current.right is not None:
            current = current.right

        return current.nilai

    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0

        return root.nilai + self.sum_nodes(root.left) + self.sum_nodes(root.right)

    def average(self):
        jumlah_siswa = self.count_nodes(self.root)

        if jumlah_siswa == 0:
            return 0

        total_nilai = self.sum_nodes(self.root)
        return total_nilai / jumlah_siswa


def main():
    bst = BSTNilaiSiswa()

    while True:
        print("\n===== SISTEM DAFTAR NILAI SISWA =====")
        print("1. Tambah Nilai Siswa")
        print("2. Cari Nilai Siswa")
        print("3. Tampilkan Nilai (Inorder)")
        print("4. Tampilkan Nilai (Preorder)")
        print("5. Tampilkan Nilai (Postorder)")
        print("6. Nilai Terendah")
        print("7. Nilai Tertinggi")
        print("8. Jumlah Siswa")
        print("9. Total Nilai")
        print("10. Rata-rata Nilai")
        print("11. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            try:
                nilai = int(input("Masukkan nilai siswa: "))
                bst.insert(nilai)
                print(f"Nilai {nilai} berhasil ditambahkan.")
            except ValueError:
                print("Nilai harus berupa angka!")

        elif pilih == 2:
            try:
                nilai = int(input("Masukkan nilai yang dicari: "))
                if bst.search(nilai):
                    print(f"Nilai {nilai} ditemukan.")
                else:
                    print(f"Nilai {nilai} tidak ditemukan.")
            except ValueError:
                print("Nilai harus berupa angka!")

        elif pilih == 3:
            print("Daftar nilai (urut dari terkecil ke terbesar):")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Preorder:")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Postorder:")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            nilai_min = bst.find_min(bst.root)

            if nilai_min is not None:
                print("Nilai terendah:", nilai_min)
            else:
                print("Data nilai masih kosong.")

        elif pilih == 7:
            nilai_max = bst.find_max(bst.root)

            if nilai_max is not None:
                print("Nilai tertinggi:", nilai_max)
            else:
                print("Data nilai masih kosong.")

        elif pilih == 8:
            print("Jumlah siswa:", bst.count_nodes(bst.root))

        elif pilih == 9:
            print("Total nilai seluruh siswa:", bst.sum_nodes(bst.root))

        elif pilih == 10:
            print("Rata-rata nilai siswa:", round(bst.average(), 2))

        elif pilih == 11:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia!")


if __name__ == "__main__":
    main()
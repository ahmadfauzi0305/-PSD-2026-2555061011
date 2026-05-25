# Datar Nilai Siswa Dengan Menggunakan BST
<br></br>

## Penjelasan Program
Program ini itu merupakan implementasi Binary Search Tree (BST) untuk mengelola data nilai siswa. Setiap nilai siswa itu disimpan dalam sebuah node, lalu kemudian ditempatkan berdasarkan aturan BST, yaitu nilai yang lebih kecil disimpan di subpohon kiri dan nilai yang lebih besar disimpan di subpohon kanan. Program ini juga menyediakan fitur untuk menambahkan nilai siswa, mencari nilai tertentu, serta menampilkan data menggunakan traversal inorder, preorder, dan postorder.

Selain itu, program juga bisa digunakan untuk memperoleh informasi dari data nilai yang tersimpan, seperti mencari nilai tertinggi dan terendah, menghitung jumlah siswa, menghitung total seluruh nilai, dan juga menentukan rata-rata nilai siswa. Dengan menggunakan BST, proses pencarian dan pengelolaan data nilai jadi lebih terstruktur dan efisien dibandingkan penyimpanan data secara acak atau pencarian satu per satu pada daftar biasa.
<br></br>
## Source Code
<img width="718" height="754" alt="Screenshot 2026-05-25 131922" src="https://github.com/user-attachments/assets/3b8b8de2-ca0d-47c4-8033-d4474fe43d46" />
<img width="627" height="683" alt="Screenshot 2026-05-25 131941" src="https://github.com/user-attachments/assets/1a4a1f2f-4afd-4a9b-aafc-8ee7df21b9a5" />
<img width="923" height="709" alt="Screenshot 2026-05-25 131956" src="https://github.com/user-attachments/assets/c8b3ba01-897a-4bab-9489-b1dc0f9fa832" />
<img width="770" height="709" alt="Screenshot 2026-05-25 132046" src="https://github.com/user-attachments/assets/668d5ac3-17e1-4b10-ac69-20046231d0eb" />
<img width="724" height="748" alt="Screenshot 2026-05-25 132104" src="https://github.com/user-attachments/assets/057a674c-90cb-4128-b3cc-b9cbefe3e878" />
<img width="676" height="726" alt="Screenshot 2026-05-25 132118" src="https://github.com/user-attachments/assets/19c1717c-cfe2-4f63-9511-d1b0e0df16e5" />

<br></br>
## Penjelasan Code
### Class `Node`
`class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None`
Class `Node` digunakan untuk membuat setiap simpul (node) pada Binary Search Tree. Setiap node menyimpan satu data berupa nilai siswa (`nilai`) serta memiliki dua pointer yaitu `left` untuk anak kiri dan right untuk anak kanan. Saat node pertama kali dibuat, kedua pointer tersebut bernilai `None`.

### Class `BSTNilaiSiswa`
`class BSTNilaiSiswa:
    def __init__(self):
        self.root = None`
Class ini berfungsi buat mengelola seluruh operasi BST. Variabel `root` itu digunakan sebagai akar pohon. Awalnya BST itu masih kosong jadi `root` nya itu ernilai `None`

### Function `insert_node()`
`def insert_node(self, root, nilai):`
Function ini digunakan buat nambahin nilai siswa ke dalam BST secara rekursif. jika data node itu kosong, maka akan dibuat node baru. nika nilai lebih kecil dari node saat ini, data tempatkan ke subtree kiri. kalau lebih besar, data akan ditempatkan ke subtree kanan

### Function `inser()`
`def insert(self, nilai):`
Function ini merupakan pembungkur dari `insert_node()`. Tujuannya itu agar si pengguna nya cukup memanggil `insert(nilai)` tanpa perlu memasuka parameter root secara manual

### Function `search_node()`
`def search_node(self, root, nilai):`
Function ini digunakan buat mencari nilai siswa dalam BST secara rekursif. jika nilai ditemukan makan akan mengembalikan `True`, sedangkan jika ga ditemukan maka akan mengembaikan `False`

### Function `search`
`def search(self, nilai):`
Function ini memanggil `search_node()` mulai dari root BST sehingga si pengguna na cuman perlu memasukan nilai yang pengen dicari

### Function `inorder()`
`def inorder(self, root):`
Function ini akan melakukan traversal inorder dengan urutan: Left --> root --> right.
Hasil traversal inorder pada BST akan selalu menghasilkan data yang terurut dari yang kecil ke yang besar

### Function `preorder()`
`def preorder(self, root):`
Function ini akan melakukan traversal preorder dengan urutan: root --> left --> right.
Traversal ini sering digunakan buat menyalin atau merepresentasikan struktur pohon

### Function `postorder()`
`def postorder(self, root):`
Function ini melakukan traversal postorder dengan urutan: left --> right --> root
trversal ini sering digunakan buat menghapus pohon atau memproses node dari bawah

### function `find_me()`
`def find_me(self, root):`
Function ini digunakan untuk mencari nilai terendah dalam BST. Karena nilai terkecil selalu berada pada node paling kiri, maka program terus bergerak ke kiri sehingga tidak ada lagi anak kiri.

### `function find_max()`
`def find_max(self, root):`
Function ini digunakan buat mencari nilai paling tinggi dalam BST. Program akan bergerak terus ke kanan sehingga mencapai node paling kanan

### `function count_nodes()`
` def count_nodes(self, root):`
FUnction ini untuk menghitung jumlah seluruh node atau jumlah siswa yang tersimpan di dalam BST dengan menggunakan teknis rekursif

### `function `sum_nodes()`
`def sum_nodes(self, root):`
Function ini untuk menghitung totoal seluruh nilai siswa yang tersimpan di dalam BST

### function `average()`
`def average(self):`
function ini buat menghitung rata rata nilai siswa. Program ini membagi total nilai (`sum_nodes`) dengan jumlah siswa (`count_nodes`)

### function `main`
`def main():`
function utama yang digunakan buat menjalankan program. functio ini menampilkan menu, menerima inputdari pengguna, dan memanggil function yang sesuai dengan pilihan pengguna seperti menambah nilai, mencari nilai, menampilkan traversal, menghitung jumlah siswa, total nilai, dan rata rata nilai
<br></br>
## Source Output
<img width="504" height="542" alt="Screenshot 2026-05-25 140254" src="https://github.com/user-attachments/assets/d490ede5-f50e-4420-b234-88bcfb3aa66f" />
<img width="456" height="527" alt="Screenshot 2026-05-25 140312" src="https://github.com/user-attachments/assets/682af932-83de-4f3c-881d-2b63d4c64b14" />
<img width="479" height="282" alt="Screenshot 2026-05-25 140323" src="https://github.com/user-attachments/assets/e4e28c35-58c8-40f9-ba09-4ba613a69c1a" />
<img width="326" height="274" alt="Screenshot 2026-05-25 140337" src="https://github.com/user-attachments/assets/45e4a922-b89d-4669-bfc7-0cf0d1b230e7" />
<img width="378" height="290" alt="Screenshot 2026-05-25 140349" src="https://github.com/user-attachments/assets/bc9528a4-e297-4732-aef5-9a9d25a0c13d" />
<img width="358" height="261" alt="Screenshot 2026-05-25 140400" src="https://github.com/user-attachments/assets/32d4cfa4-efc8-4a81-b2c1-7eb67db3b10e" />
<img width="375" height="267" alt="Screenshot 2026-05-25 140410" src="https://github.com/user-attachments/assets/89bef885-7cf9-475d-b1c9-59e2907a2319" />
<img width="387" height="264" alt="Screenshot 2026-05-25 140421" src="https://github.com/user-attachments/assets/825770b6-e657-4f40-8509-7a4ed09e95a7" />
<img width="424" height="271" alt="Screenshot 2026-05-25 140432" src="https://github.com/user-attachments/assets/b8867874-5a7b-44ec-b77b-7b8ddddf1a73" />
<img width="360" height="267" alt="Screenshot 2026-05-25 140445" src="https://github.com/user-attachments/assets/4c7702bc-5540-4dce-9fbb-96868c9f5b9f" />
<img width="334" height="272" alt="Screenshot 2026-05-25 140518" src="https://github.com/user-attachments/assets/aeaf1568-bd62-447a-89eb-212d37c144b2" />

<br></br>
## Penjelasan Output
### Menu Tambah Nilai Siswa
Ketika pengguna memasukkan nilai siswa, program akan menampilkan pesan bahwa nilai tersebut berhasil ditambahkan ke dalam BST. Output ini menunjukkan bahwa data telah berhasil disimpan dan akan digunakan dalam proses pencarian maupun traversal selanjutnya.

### Menu Cari Nilai Siswa
Saat pengguna mencari suatu nilai, program akan menampilkan informasi apakah nilai tersebut ditemukan atau tidak ditemukan. Jika nilai ada dalam BST, program akan memberikan pesan bahwa nilai berhasil ditemukan. Sebaliknya, jika nilai tidak ada dalam BST, program akan menampilkan pesan bahwa nilai tersebut tidak ditemukan.

### Menu Inorder
Menu inorder menampilkan seluruh nilai siswa yang tersimpan dalam BST secara terurut dari nilai terkecil hingga terbesar. Hal ini karena traversal inorder pada BST selalu mengunjungi subtree kiri, root, lalu subtree kanan sehingga menghasilkan urutan data yang terurut.

### Menu Preorder
Menu preorder menampilkan nilai siswa dengan urutan root terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan. Output ini menggambarkan struktur BST dimulai dari akar pohon sebelum mengunjungi node-node lainnya.

### Menu Postorder
Menu postorder menampilkan nilai siswa dengan urutan subtree kiri, subtree kanan, kemudian root. Output ini menunjukkan bahwa node akar ditampilkan paling akhir setelah seluruh node anak selesai dikunjungi.

### Menu Nilai Tertinggi
Menu ini menghasilkan nilai siswa yang paling besar di dalam BST. Program menemukannya dengan menelusuri node paling kanan karena pada BST nilai terbesar selalu berada pada cabang kanan paling ujung.

### Menu Jumlah Siswa
Menu jumlah siswa menampilkan banyaknya data nilai yang tersimpan dalam BST. Program menghitung seluruh node yang ada sehingga hasilnya menunjukkan jumlah siswa yang datanya telah dimasukkan.

### Menu Total Nilai
Menu total nilai menampilkan hasil penjumlahan seluruh nilai siswa yang tersimpan dalam BST. Output ini memberikan informasi mengenai akumulasi nilai dari seluruh siswa.

### Menu Rata Rata Nilai
Menu rata-rata nilai menghasilkan nilai rata-rata siswa yang diperoleh dari pembagian total nilai dengan jumlah siswa yang tersimpan dalam BST. Output ini digunakan untuk mengetahui gambaran umum performa nilai seluruh siswa yang telah dimasukkan ke dalam sistem.
<br></br>
## Link Youtube
https://youtu.be/6KLSPpbXPlA?si=ThoaEt95KxCmVbuH
<br></br>

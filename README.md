Program ini seperti parkiran mobil berderet, nah Program ini juga memungkinkan pengguna untuk menambahkan mobil
yang masuk ke parkiran, mengeluarkan mobil juga di parkiran, menampilkan urutan mobil yang lagi parkir, mencari 
nobil, serta menghitung mobil yang ada di parkiran. Dengan adanya menu menu itu, user bisa mengelola data mobil 
yang parkir secara teratur sesuai urutan kedatangan nya

Algoritma struktur data yang di terapkan pada program ini adalah Doubly Linked List. Pada struktur data ini, setiap node 
atau kendaraan memiliki dua penunjuk yaitu prev yang menunjkan node sebelumnya dan next yang menunjuk ke node berikutnya.
Dengan konsep ini, data mobil dapat di tambahkan, dihapus atau juga bisa di cari dengan flexibel tanpa harus memindahkan
seluruh data yang ada. Struktur ini cocok digunakan buat menggambarkan kondisi parkiran yang berderet, karena setiap 
kendaraan punya hubungan dengan kendaraan di depan dan kendaraan yang ada di belakang nya


## Source code
<img width="1408" height="792" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/d30b7e99-284d-4e9a-9fd0-8c814c0386a2" />
<br></br>

<img width="1350" height="1007" alt="Screenshot (22)" src="https://github.com/user-attachments/assets/d569e1f0-a0c5-4469-bfee-1550671e56a0" />
<br></br>

<img width="1326" height="1080" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/fc89d58d-fd08-434a-a49e-81d70ba7f296" />
<br></br>

<img width="1368" height="986" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/6b4bd368-e4ea-463a-86c3-a51e7c54a9f1" />
<br></br>


## Penjelasan code

### 1. Class Mobil
Class `Mobil` digunakan untuk merepresentasikan satu mobil dalam parkiran. Setiap mobil dianggap sebagai node dalam struktur Doubly Linked List.

Atribut yang dimiliki:
- `plat` → menyimpan nama atau nomor plat mobil
- `prev` → menunjuk ke mobil sebelumnya
- `next` → menunjuk ke mobil berikutnya
<br></br>

### 2. Class Parkiran

Class Parkiran berfungsi untuk mengelola seluruh mobil yang ada di parkiran.

Atribut utama:

- `head` → menunjuk ke mobil pertama dalam parkiran

Jika `head` bernilai `None`, berarti parkiran masih kosong.
<br></br>

### 3.Tambah Mobil

Fungsi `tambah_mobil()` digunakan untuk menambahkan mobil baru ke parkiran.

Proses yang dilakukan:

Membuat node mobil baru
- Jika parkiran kosong, mobil menjadi head
- Jika tidak kosong, mobil ditambahkan di posisi terakhir
<br></br>

### 4. Keluar Mobil
Fungsi `keluar_mobil()` digunakan untuk menghapus mobil dari parkiran berdasarkan plat mobil.

Proses yang dilakukan:

- Mencari mobil dengan plat yang sesuai
- Jika ditemukan, node akan dihapus dari linked list
- Jika tidak ditemukan, program menampilkan pesan bahwa mobil tidak ada
<br></br>

### 5. Tampilkan Parkiran
Fungsi `tampilkan()` digunakan untuk menampilkan seluruh mobil yang sedang parkir.
<br></br>

### 6. Cari Mobil
Fungsi `cari_mobil()` digunakan untuk mencari mobil berdasarkan plat.

Program akan menelusuri linked list dan menampilkan posisi mobil jika ditemukan.
<br></br>

### 7. Jumlah Mobil
Fungsi `jumlah_mobil()` digunakan untuk menghitung jumlah mobil yang sedang parkir.

Program akan menelusuri seluruh node dan menghitung jumlahnya.
<br></br>

### 8. Menu Program
Program menyediakan menu interaktif yang memungkinkan pengguna melakukan beberapa operasi
<br></br>

## Output Program
1. Tambah Mobil
<img width="1920" height="1080" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/3b39329a-e2ee-4d0d-94b5-888bd0997417" />
<br></br>

2. Mobil Keluar
<img width="1920" height="1080" alt="Screenshot (26)" src="https://github.com/user-attachments/assets/f6140b32-321d-4d6d-8ab1-3fdde0a4769d" />
<br></br>

3. Tampilkan Parkiran
<img width="1920" height="1080" alt="Screenshot (28)" src="https://github.com/user-attachments/assets/290f441b-8082-4be8-a6a4-34f95b26ad6c" />
<br></br>

4. Cari Mobil
<img width="1920" height="1080" alt="Screenshot (28)" src="https://github.com/user-attachments/assets/9ebd1adb-d2fa-480c-8d1c-04afcce6b89a" />
<br></br>

5. Jumlah Mobil
<img width="1920" height="1080" alt="Screenshot (30)" src="https://github.com/user-attachments/assets/a57408b3-a68c-47c3-8420-03dbccb81d43" />
<br></br>

6. Keluar
<img width="1920" height="1080" alt="Screenshot (31)" src="https://github.com/user-attachments/assets/1778b06e-b7b6-405e-914d-98d90eedabc2" />
<br></br>

## Penjelasan Output 
### 1. Tambah Mobil
Ketika pengguna memasukkan plat atau nama mobil, mobil tersebut akan ditambahkan ke dalam daftar parkiran. 
Mobil akan disimpan secara berurutan sesuai urutan kedatangan
<br></br>

### 2. Mobil Keluar
Jika pengguna memasukkan plat mobil yang ada di parkiran, mobil tersebut akan dihapus dari daftar dan program menampilkan pesan
"Mobil berhasil keluar dari parkiran". Jika tidak ditemukan, akan muncul pesan "Mobil tidak ditemukan"
<br></br>

### 3. Tampilkan Parkiran
Program menampilkan semua mobil yang sedang terparkir dalam bentuk urutan seperti:
`Mobil1 <-> Mobil2 <-> Mobil3 <-> None`
Jika tidak ada mobil, akan muncul pesan "Parkiran kosong"
<br></br>

### 4. Cari Mobil
Program mencari mobil berdasarkan plat atau nama yang dimasukkan. Jika ditemukan, program menampilkan posisi mobil di parkiran, misalnya
"Mobil ditemukan di posisi 2". Jika tidak ditemukan, akan muncul pesan bahwa mobil tidak ada di parkiran.
<br></br>

### 5. Jumlah Mobil
Program menghitung dan menampilkan jumlah mobil yang sedang terparkir, misalnya "Jumlah mobil di parkiran: 3".
<br></br>

### 5. Keluar
Program akan berhenti dan menampilkan pesan "Program selesai".










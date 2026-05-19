# Program Antrian Bank Dengan Menggunakan Metode Queue
<br></br>
## Penjelasan Program
Sistem yang dibuat merupakan gambaran dari sistem antrean pada bank menggunakan bahasa pemrograman Python dengan penerapan struktur data Queue yang bekerja berdasarkan prinsip FIFO (First In First Out). Pada sistem ini, nasabah yang datang lebih dulu akan dilayani lebih dulu oleh loket kasir. Implementasi antrean dilakukan menggunakan Linked List, di mana setiap data antrean disimpan dalam sebuah node yang berisi nomor antrean dan penunjuk ke node berikutnya. Program memiliki dua pointer utama yaitu front_ptr yang menunjuk ke antrean paling depan dan rear_ptr yang menunjuk ke antrean paling belakang, sehingga proses penambahan dan penghapusan antrian dapat dilakukan secara efisien.

Melalui menu yang tersedia, pengguna itu bisa melakukan beberapa operasi utama seperti mengambil nomor antrean (enqueue) untuk menambahkan nasabah baru ke dalam antrean, memanggil nasabah (dequeue) buat melayani nasabah yang ada di posisi paling depan, melihat antrean berikutnya tanpa menghapusnya dari sistem, serta menampilkan seluruh daftar antrean yang sedang menunggu layanan. Nomor antrean juga dibuat secara otomatis dengan format tertentu agar lebih terstruktur. Dengan adanya sistem ini, proses pengelolaan antrian dapat disimulasikan secara sederhana namun tetap menggambarkan mekanisme antrian yang umum digunakan pada layanan perbankan.
<br></br>
## Source Code
<img width="950" height="726" alt="Screenshot 2026-05-19 073541" src="https://github.com/user-attachments/assets/5e942f14-85fb-4bf4-9708-360586c6a019" />
<img width="970" height="672" alt="Screenshot 2026-05-19 073600" src="https://github.com/user-attachments/assets/810551b8-73e3-4c00-85bb-c2d81aff8076" />
<img width="811" height="708" alt="Screenshot 2026-05-19 073633" src="https://github.com/user-attachments/assets/635c967c-7640-4866-9d9a-4d46cef739a7" />
<img width="1045" height="432" alt="Screenshot 2026-05-19 073650" src="https://github.com/user-attachments/assets/3eaf8a53-df88-4cab-9a76-0d553913fa59" />
<br></br>

## Penjelasan kode
### 1. `Class Node`
Class Node digunakan untuk membuat node atau elemen pada linked list. Setiap node menyimpan dua hal, yaitu data dan referensi ke node berikutnya.

- `self.data = data`
Menyimpan nilai data, dalam program ini berupa nomor antrean nasabah.
- `self.next = None`
Menyimpan alamat atau referensi ke node berikutnya. Awalnya bernilai None karena node belum terhubung dengan node lain.

### 2. `Class QueueLinkedList`
Class ini digunakan untuk mengelola struktur antrean menggunakan linked list.

- front_ptr > menunjuk elemen paling depan dalam antrean (nasabah yang akan dipanggil terlebih dahulu).
- rear_ptr > menunjuk elemen paling belakang dalam antrean (nasabah yang terakhir masuk).
Jika keduanya bernilai None, berarti antrean masih kosong.

### Fungsi `is_empty()`
Fungsi ini digunakan untuk mengecek apakah antrean kosong atau tidak.

Jika `front_ptr` bernilai `None`, berarti tidak ada data dalam antrean.
Fungsi akan mengembalikan nilai True jika kosong, dan False jika ada data.

### Fungsi `enqueue()`
Fungsi ini digunakan untuk menambahkan data ke dalam antrean.
`new_node = Node(x)`
Membuat node baru yang berisi nomor antrean.

Jika antrean masih kosong:
Node baru akan menjadi depan sekaligus belakang antrean.

Jika antrean sudah ada isinya:

Node baru ditambahkan di belakang antrean.
Node belakang sebelumnya dihubungkan dengan node baru.

Menampilkan pesan bahwa nomor antrean berhasil dibuat.

### Fungsi `dequeue()`
Fungsi ini digunakan untuk mengeluarkan data dari antrean.
`if self.is_empty():` Jika antrean kosong:
Program akan menampilkan pesan bahwa tidak ada nasabah yang menunggu.

`temp = self.front_ptr` Menyimpan data node paling depan ke variabel sementara.

`self.front_ptr = self.front_ptr.next` Memindahkan posisi front ke node berikutnya.
<br></br>

## Source Output
<br></br>

## Penjelasan Output
<br></br>

## Link Youtube
<br></br>

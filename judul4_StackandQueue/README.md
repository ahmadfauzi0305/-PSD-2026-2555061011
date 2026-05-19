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
Class Node digunakan untuk merepresentasikan satu elemen pada struktur data linked list. Setiap node menyimpan dua bagian utama yaitu data yang berisi nomor antrean nasabah dan next yang merupakan penunjuk ke node berikutnya. Dengan adanya next, setiap node dapat saling terhubung sehingga membentuk sebuah antrean.

### 2. `Class QueueLinkedList`
Class ini digunakan untuk mengelola sistem antrean menggunakan konsep queue dengan linked list. Di dalam class ini terdapat dua pointer yaitu `front_ptr` yang menunjuk ke elemen paling depan antrean dan `rear_ptr` yang menunjuk ke elemen paling belakang antrean. Class ini juga berisi beberapa function yang digunakan untuk mengatur operasi pada antrean seperti menambah, menghapus, melihat, dan menampilkan data antrean.

### 3. Fungsi `is_empty()`
Function ini digunakan untuk mengecek apakah antrean kosong atau tidak. Pengecekan dilakukan dengan melihat apakah `front_ptr` bernilai `None`. Jika bernilai `None`, berarti tidak ada nasabah dalam antrean.

### 4. Fungsi `enqueue(x)`
Function ini berfungsi untuk menambahkan nomor antrean baru ke dalam queue. Program akan membuat node baru yang berisi nomor antrean. Jika antrean masih kosong, node tersebut akan menjadi elemen pertama sehingga `front_ptr` dan `rear_ptr` menunjuk ke node tersebut. Jika antrean sudah berisi data, node baru akan ditambahkan di bagian belakang antrean.

### 5. Fungsi `dequeue()`
Function ini digunakan untuk memanggil atau menghapus antrean yang berada di posisi paling depan. Jika antrean kosong, program akan menampilkan pesan bahwa tidak ada nasabah yang menunggu. Jika ada data, maka nomor antrean paling depan akan dipanggil dan pointer `front_ptr` akan dipindahkan ke node berikutnya.

### 6. `peek()`
Function ini digunakan untuk melihat nomor antrean yang berada di posisi paling depan tanpa menghapusnya dari antrean. Function ini berguna untuk mengetahui nasabah yang akan dipanggil selanjutnya.

### 7, `display()`
Function ini digunakan untuk menampilkan seluruh daftar antrean yang sedang menunggu. Program akan menelusuri setiap node mulai dari `front_ptr` hingga node terakhir dan menampilkan nomor antrean secara berurutan.

### 8. `main()`
Function ini merupakan fungsi utama yang menjalankan sistem antrean bank. Di dalamnya terdapat menu interaktif yang memungkinkan pengguna memilih berbagai operasi seperti mengambil nomor antrean, memanggil nasabah, melihat antrean berikutnya, menampilkan semua antrean, dan menutup bank.
<br></br>

### Alur Program
- Program dimulai dari fungsi `main()`.
- Sistem membuat objek antrean dari `class QueueLinkedList`.
- Program menampilkan menu sistem antrean bank.
- Pengguna memasukkan pilihan menu.
- Jika memilih 1, program membuat nomor antrean baru dan menambahkannya ke antrean menggunakan `enqueue()`.
- Jika memilih 2, program memanggil nasabah paling depan menggunakan `dequeue()`.
- Jika memilih 3, program menampilkan antrean paling depan menggunakan `peek()`.
- Jika memilih 4, program menampilkan seluruh daftar antrean menggunakan `display()`.
- Menu akan terus ditampilkan selama pengguna belum memilih 5.
- Jika memilih 5, program akan menghabiskan sisa antrean lalu menutup sistem.
<br></br>

## Source Output
<img width="472" height="402" alt="Screenshot 2026-05-19 102107" src="https://github.com/user-attachments/assets/a23e7754-8259-4a62-9285-92c5a8e160a6" />
<img width="628" height="192" alt="Screenshot 2026-05-19 102148" src="https://github.com/user-attachments/assets/4e927832-158a-4650-a2ea-5e17db6d8ded" />
<img width="610" height="197" alt="Screenshot 2026-05-19 102202" src="https://github.com/user-attachments/assets/ecd0b34b-8348-4303-8467-02b487f88648" />
<img width="522" height="342" alt="Screenshot 2026-05-19 102225" src="https://github.com/user-attachments/assets/13d9c05b-beee-4592-aa3f-b0a2ec95392b" />
<img width="742" height="397" alt="Screenshot 2026-05-19 102239" src="https://github.com/user-attachments/assets/41426d51-17ff-4084-9eed-993aabbd2b43" />
<br></br>

## Penjelasan Output
### 1. Menu Utama
Program akan menampilkan menu utama sistem antrean bank setiap kali dijalankan atau setelah suatu proses selesai dilakukan. Menu ini berisi beberapa pilihan yang dapat dipilih oleh pengguna, yaitu mengambil nomor antrean, memanggil nasabah, melihat antrean berikutnya, menampilkan seluruh antrean, dan menutup bank. Pengguna kemudian diminta memasukkan angka pilihan dari 1 sampai 5 untuk menjalankan fungsi yang diinginkan.

### 2. Mengambil Nomor Antrian
Jika pengguna memilih menu 1 (Ambil Nomor Antrean), program akan membuat nomor antrean baru dengan format seperti B-001, B-002, B-003, dan seterusnya. Setelah nomor antrean berhasil dibuat dan dimasukkan ke dalam sistem, program akan menampilkan pesan output seperti:
[SUKSES] Nomor antrean B-001 berhasil dibuat.

### 3. Memanggil Nasabah
Jika pengguna memilih menu 2 (Panggil Nasabah), program akan mengambil nomor antrean yang berada di posisi paling depan dan menampilkannya sebagai nasabah yang dipanggil ke loket. Output yang muncul contohnya:
[PANGGILAN] Nomor antrean B-001, silakan menuju ke Loket Kasir!
Setelah dipanggil, nomor antrean tersebut akan dihapus dari daftar antrean.

### 4. Melihat Antrian Berikutnya
Jika pengguna memilih menu 3 (Lihat Antrean Berikutnya), program akan menampilkan nomor antrean yang berada di posisi paling depan tanpa menghapusnya dari antrean. Output yang ditampilkan misalnya:
[INFO] Nasabah berikutnya yang akan dipanggil: B-002

### 5, Menampilkan Antrian berikutnya
Jika pengguna memilih menu 4 (Tampilkan Seluruh Antrean), program akan menampilkan semua nomor antrean yang sedang menunggu secara berurutan dari depan hingga belakang. Outputnya akan terlihat seperti berikut:
Depan (Loket) -> [B-002] [B-003] [B-004] <- Belakang

### 5. Bank Tutup Atau Selesai
Jika pengguna memilih menu 5 (Tutup Bank & Selesai), program akan memeriksa apakah masih ada antrean yang tersisa. Jika masih ada, sistem akan memanggil semua nasabah yang tersisa hingga antrean kosong. Setelah itu program akan menampilkan pesan:
Bank telah resmi ditutup. Terima kasih!

### 6. Inputan Eror
Selain itu, jika pengguna memasukkan input yang tidak sesuai seperti huruf atau angka di luar pilihan menu, program akan menampilkan pesan error seperti:
[ERROR] Input harus berupa angka! atau
[ERROR] Pilihan menu tidak tersedia!
<br></br>

## Link Youtube
<br></br>

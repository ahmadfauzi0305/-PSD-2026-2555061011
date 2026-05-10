# Program Mencari Nama di Kontak Handphone Dengan Menggunakan Sequential Search
<br></br>
## Penjelasan Program
Program ini dibuat untuk mencari nama kontak dalam sebuah daftar kontak. Program menerapkan algoritma Sequential Search, yaitu metode pencarian yang dilakukan dengan memeriksa setiap data secara berurutan dari awal hingga akhir. Data kontak disimpan dalam sebuah list yang berisi beberapa dictionary, dimana setiap data memiliki atribut nama dan nomor telepon. Saat program dijalankan, pengguna diminta memasukkan nama kontak yang ingin dicari. Program kemudian akan memeriksa setiap kontak dalam daftar menggunakan perulangan dan membandingkannya dengan nama yang dimasukkan pengguna. Jika kontak ditemukan, program akan menampilkan nama dan nomor teleponnya serta menghitung jumlah kemunculan kontak tersebut. Jika tidak ditemukan, program akan menampilkan pesan bahwa kontak yang dicari tidak ada dalam daftar.
<br></br>
## Source Code
<br></br>
## Penjelasan Code
### 1. Fungsi `sequential_search()`
Fungsi `sequential_search()` digunakan untuk melakukan proses pencarian nama kontak dalam daftar kontak menggunakan metode Sequential Search. Fungsi ini bekerja dengan cara memeriksa setiap data kontak secara berurutan dari indeks pertama hingga indeks terakhir. Parameter fungsi nya itu:
- `Kontak`, yang merupakan list yang berisi data kontak berupa nama dan nomor telepon.
- `n`, Menunjukkan jumlah total data kontak yang ada dalam list.
- `target`, Merupakan nama kontak yang ingin dicari oleh pengguna.
Cara kerja fungsi ini yaitu:
- Fungsi menginisialisasi variabel `i` sebagai indeks awal untuk menelusuri data kontak.
- Variabel counter digunakan untuk menghitung jumlah kontak yang ditemukan.
- Fungsi melakukan perulangan selama `i < n`, sehingga seluruh data dalam list akan diperiksa.
- Pada setiap perulangan, program membandingkan nama kontak dengan nilai target.
- Jika nama kontak sama dengan `target`, program akan Menampilkan nama dan nomor telepon kontak tersebut dan Menambah nilai counter.
- Setelah seluruh data diperiksa, fungsi akan mengembalikan nilai counter yang menunjukkan jumlah kontak yang ditemukan.

### 2. `Fungsi `main()`
Fungsi `main()` merupakan fungsi utama yang mengatur jalannya program secara keseluruhan. Cara kerja fungsi ini itu yaitu:
- Program membuat daftar kontak yang disimpan dalam bentuk list of dictionary yang berisi nama dan nomor telepon.
- Program menghitung jumlah data kontak menggunakan fungsi `len()` dan menyimpannya ke dalam variabel `n`.
- Program menampilkan seluruh daftar kontak yang tersedia.
- Program meminta pengguna memasukkan nama kontak yang ingin dicari.
- Program memanggil fungsi `sequential_search()` untuk melakukan proses pencarian kontak.
- Setelah fungsi selesai dijalankan, program akan menampilkan hasil pencarian yaitu Jika kontak ditemukan, program menampilkan jumlah kontak yang ditemukan dan Jika tidak ditemukan, program menampilkan pesan bahwa kontak tidak ditemukan.
<br></br>

## Penjelasan Output
## Link Youtube
## Link Rumus

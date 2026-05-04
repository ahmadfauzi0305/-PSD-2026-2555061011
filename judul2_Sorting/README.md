# Program Mengurutkan Pemain Bola Berdasarkan Jumlah Gol Dengan Metode Bubble Sort
<br></br>

## Penjelasan Program

Program ini merupakan program sederhana menggunakan bahasa pemrograman Python yang berfungsi untuk mengelola data pemain bola berdasarkan jumlah gol yang dicetak. Pengguna diminta untuk memasukkan jumlah pemain, nama pemain, serta jumlah gol yang dicetak oleh masing-masing pemain. Program juga dilengkapi dengan validasi input, sehingga jika pengguna memasukkan data yang tidak sesuai (misalnya memasukkan huruf ketika diminta angka atau sebaliknya), program tidak akan berhenti dan akan meminta input ulang sampai data yang dimasukkan benar.

Setelah semua data pemain dimasukkan, program akan mengurutkan daftar pemain berdasarkan jumlah gol terbanyak menggunakan metode Bubble Sort. Metode ini bekerja dengan cara membandingkan dua data yang bersebelahan lalu menukarnya jika urutannya tidak sesuai. Hasil akhirnya adalah daftar pemain yang sudah terurut dari jumlah gol paling banyak hingga paling sedikit, kemudian ditampilkan ke layar agar pengguna dapat melihat peringkat pemain berdasarkan jumlah gol yang dicetak.
<br></br>

## Struktur Program

### 1. Fungsi `input_angka()`

Fungsi ini digunakan untuk menerima input berupa angka (integer) dari pengguna.
Cara Kerja
- Program meminta pengguna memasukkan angka.
- Jika pengguna memasukkan huruf atau karakter lain, program akan menampilkan pesan kesalahan.
- Program akan terus meminta input sampai pengguna memasukkan angka yang benar.

### 2. Fungsi `input_nama()`
Fungsi ini digunakan untuk menerima input berupa nama pemain.
- Program meminta pengguna memasukkan nama pemain.
- Program akan memeriksa apakah input hanya berisi huruf.
- Jika pengguna memasukkan angka atau karakter lain, program akan meminta input ulang.

### 3. Fungsi `bubble_sort()`
Fungsi ini digunakan untuk **mengurutkan data pemain berdasarkan jumlah gol** menggunakan algoritma **Bubble Sort**.
Cara Kerja
1. Program membandingkan dua data yang bersebelahan.
2. Jika jumlah gol pemain pertama lebih kecil dari pemain kedua, maka kedua data akan ditukar.
3. Proses ini dilakukan berulang sampai semua data terurut dari **gol terbanyak ke gol paling sedikit**.
Karena program menggunakan dua list (`nama_pemain` dan `jumlah_gol`), maka saat jumlah gol ditukar, nama pemain juga harus ditukar agar data tetap sesuai.

### 4. Fungsi `tampilkan_data()`
Fungsi ini digunakan untuk menampilkan data pemain yang sudah diurutkan.
- Program melakukan perulangan pada seluruh data pemain.
- Setiap pemain ditampilkan bersama jumlah golnya.
<br></br>

## Alur Program Utama

1. Program meminta pengguna memasukkan **jumlah pemain**.
2. Program melakukan perulangan sebanyak jumlah pemain.
3. Pengguna diminta memasukkan:
   - Nama pemain
   - Jumlah gol pemain
4. Data disimpan dalam dua list:
   - `nama_pemain`
   - `jumlah_gol`
5. Program menjalankan fungsi **Bubble Sort** untuk mengurutkan data berdasarkan jumlah gol.
6. Program menampilkan daftar pemain yang sudah diurutkan.

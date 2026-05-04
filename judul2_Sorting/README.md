# Program Mengurutkan Pemain Bola Berdasarkan Jumlah Gol Dengan Metode Bubble Sort

Program ini merupakan program sederhana dengan menggunakan bahasa pemrograman Python yang berfungsi untuk mengelola data pemain bola berdasarkan jumlah gol yang dicetak. Pengguna diminta buat masukin jumlah pemain, nama pemain, serta jumlah gol yang dicetak oleh masing-masing pemain. Program ini juga dilengkapi dengan validasi input, sehingga jika pengguna memasukkan data yang tidak sesuai misalnya memasukkan huruf ketika diminta angka atau sebaliknya, program tidak akan berhenti dan akan meminta input ulang sampai data yang dimasukkan benar.
Setelah semua data pemain dimasukkan, nah nanti program akan mengurutkan daftar pemain berdasarkan jumlah gol terbanyak menggunakan metode Bubble Sort. Metode ini juga bekerja dengan cara membandingkan dua data yang bersebelahan lalu menukarnya jika urutannya tidak sesuai. Hasil akhirnya atau output nya adalah daftar pemain yang sudah terurut dari jumlah gol paling banyak hingga paling sedikit, kemudian ditampilkan di terminal agar pengguna bisa ngeliat peringkat pemain berdasarkan jumlah gol yang dicetak.
<br></br>

## Source Code
<img width="1920" height="1080" alt="Screenshot (33)" src="https://github.com/user-attachments/assets/4d3fdb70-55f5-476e-83df-d5c41a020b55" />
<img width="1920" height="1080" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/ce055fd4-da7c-48ab-86db-3a04b80bc44e" />
<br></br>

## Penjelasan Code
### 1. Fungsi `input_angka()`

Fungsi ini digunakan untuk menerima input berupa angka atau integer dari pengguna.
Cara Kerja nya:
- Program meminta pengguna memasukkan angka.
- Jika pengguna memasukkan huruf atau karakter lain, program akan menampilkan pesan kesalahan.
- Program akan terus meminta input sampai pengguna memasukkan angka yang benar.

### 2. Fungsi `input_nama()`
Fungsi ini digunakan untuk menerima input berupa nama pemain.
Cara kerja nya:
- Program meminta pengguna atau user masukin nama pemain.
- Program akan memeriksa apakah input hanya berisi huruf.
- Jika pengguna memasukkan angka atau karakter lain, program akan meminta input ulang.

### 3. Fungsi `bubble_sort()`
Fungsi ini digunakan untuk mengurutkan data pemain berdasarkan jumlah gol menggunakan algoritma Bubble Sort.
Cara Kerja
1. Program membandingkan dua data yang bersebelahan.
2. Jika jumlah gol pemain pertama lebih kecil dari pemain kedua, maka kedua data akan ditukar.
3. Proses ini dilakukan berulang sampai semua data terurut dari gol terbanyak ke gol paling sedikit.
Karena program menggunakan dua list (`nama_pemain` dan `jumlah_gol`), maka saat jumlah gol ditukar, nama pemain juga harus ditukar agar data tetap sesuai.

### 4. Fungsi `tampilkan_data()`
Fungsi ini digunakan untuk menampilkan data pemain yang sudah diurutkan.
- Program melakukan perulangan pada seluruh data pemain.
- Setiap pemain ditampilkan bersama jumlah golnya.
<br></br>

## Alur Program Utama

1. Program meminta pengguna memasukkan jumlah pemain.
2. Program melakukan perulangan sebanyak jumlah pemain.
3. Pengguna diminta memasukkan:
   - Nama pemain
   - Jumlah gol pemain
4. Data disimpan dalam dua list:
   - `nama_pemain`
   - `jumlah_gol`
5. Program menjalankan fungsi Bubble Sort untuk mengurutkan data berdasarkan jumlah gol.
6. Program menampilkan daftar pemain yang sudah diurutkan.
<br></br>

## Output Program
<img width="1920" height="1080" alt="Screenshot (35)" src="https://github.com/user-attachments/assets/7609ec4b-3abe-437a-adea-8e80e64657ff" />

Output dari program ini adalah nama nama pemain bola yang telah diurutkan berdasarkan jumlah gol terbanyak. Setelah itu pengguna memasukkan nama pemain dan jumlah gol, program akan memproses data tersebut menggunakan algoritma Bubble Sort.
Hasilnya akan ditampilkan dalam bentuk daftar peringkat, yang di mana pemain dengan jumlah gol paling banyak berada di urutan pertama, diikuti pemain dengan jumlah gol yang lebih sedikit seperti yang ada di contoh gambar output
<br></br>

## Link Youtube



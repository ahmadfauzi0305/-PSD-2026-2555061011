## Program Mengurutkan Pemain Bola Berdasarkan Jumlah Gol Dengan Metode Bubble Sort

### Penjelasan Program

Program ini merupakan program sederhana menggunakan bahasa pemrograman **Python** yang berfungsi untuk mengelola data pemain bola berdasarkan jumlah gol yang dicetak. Pengguna diminta untuk memasukkan jumlah pemain, nama pemain, serta jumlah gol yang dicetak oleh masing-masing pemain. Program juga dilengkapi dengan **validasi input**, sehingga jika pengguna memasukkan data yang tidak sesuai (misalnya memasukkan huruf ketika diminta angka atau sebaliknya), program tidak akan berhenti dan akan meminta input ulang sampai data yang dimasukkan benar.

Setelah semua data pemain dimasukkan, program akan mengurutkan daftar pemain berdasarkan jumlah gol terbanyak menggunakan metode **Bubble Sort**. Metode ini bekerja dengan cara membandingkan dua data yang bersebelahan lalu menukarnya jika urutannya tidak sesuai. Hasil akhirnya adalah daftar pemain yang sudah terurut dari jumlah gol paling banyak hingga paling sedikit, kemudian ditampilkan ke layar agar pengguna dapat melihat peringkat pemain berdasarkan jumlah gol yang dicetak.


### Fitur Program

* Meminta pengguna memasukkan **jumlah pemain**.
* Memvalidasi input agar:

  * Jumlah pemain harus berupa **angka**.
  * Nama pemain harus berupa **huruf**.
  * Jumlah gol harus berupa **angka dan tidak boleh negatif**.
* Menyimpan data pemain ke dalam **list**.
* Mengurutkan pemain berdasarkan **jumlah gol terbanyak** menggunakan algoritma **Bubble Sort**.
* Menampilkan hasil pengurutan pemain dan jumlah golnya.

### Alur Program

1. **Input jumlah pemain**

   * Program meminta jumlah pemain.
   * Jika input bukan angka atau kurang dari sama dengan 0, program akan meminta input ulang.

2. **Input data pemain**

   * Pengguna memasukkan:

     * Nama pemain
     * Jumlah gol pemain
   * Program akan mengecek validitas input:

     * Nama harus huruf.
     * Gol harus angka dan tidak boleh negatif.

3. **Penyimpanan data**

   * Nama pemain disimpan dalam list `nama_pemain`.
   * Jumlah gol disimpan dalam list `jumlah_gol`.

4. **Proses pengurutan**

   * Data diurutkan menggunakan algoritma **Bubble Sort**.
   * Pengurutan dilakukan dari **jumlah gol terbesar ke terkecil**.

5. **Menampilkan hasil**

   * Program menampilkan daftar pemain yang sudah diurutkan berdasarkan jumlah gol terbanyak.

### Contoh Output

```
Daftar Pemain Berdasarkan Jumlah Gol Yang Terbanyak:
Messi - 30 gol
Ronaldo - 25 gol
Neymar - 18 gol
```

### Konsep yang Digunakan

* Perulangan (`while`, `for`)
* Percabangan (`if`)
* Exception Handling (`try` dan `except`)
* List pada Python
* Algoritma Sorting **Bubble Sort**

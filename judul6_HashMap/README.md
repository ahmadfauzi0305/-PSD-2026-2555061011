## Stok Barang di Minimarket Menggunakan HashMap
<br></br>
## Penjelasan Program
Program ini dibuat untuk mensimulasikan pengelolaan stok barang di minimarket menggunakan struktur data Hash Map dengan metode Open Addressing (Linear Probing). Setiap barang memiliki kode barang sebagai kunci (key) dan jumlah stok sebagai nilai (value). Data barang disimpan ke dalam tabel hash menggunakan fungsi hash yang menghitung posisi penyimpanan berdasarkan kode barang. Jika terjadi tabrakan data atau collision karena dua kode barang memiliki indeks yang sama, program akan mencari posisi kosong berikutnya secara berurutan hingga menemukan tempat yang tersedia.

Selain menyimpan data, program juga menyediakan fitur untuk mencari barang berdasarkan kode yang dimasukkan oleh pengguna. Ketika pengguna memasukkan kode barang, program akan menelusuri tabel hash dan menampilkan informasi stok jika barang tersebut ditemukan. Program juga memiliki fungsi untuk memperbarui data barang yang sudah ada, menghapus barang dari tabel, serta menampilkan seluruh data stok yang tersimpan. Dengan adanya fitur-fitur tersebut, program dapat membantu menggambarkan bagaimana sistem pencarian dan pengelolaan data barang pada minimarket dapat dilakukan secara cepat dan efisien menggunakan Hash Map.
<br></br>
## Source Code
<img width="616" height="651" alt="Screenshot 2026-06-08 164115" src="https://github.com/user-attachments/assets/310a6f93-47c4-4cfa-baf6-87c2a43532c6" />
<img width="622" height="756" alt="Screenshot 2026-06-08 164132" src="https://github.com/user-attachments/assets/dc5ee756-9198-4846-aaef-0e28228c76aa" />
<img width="681" height="753" alt="Screenshot 2026-06-08 164147" src="https://github.com/user-attachments/assets/1470d030-7b04-4aa5-8532-afc42fd79c3e" />
<img width="578" height="245" alt="Screenshot 2026-06-08 164157" src="https://github.com/user-attachments/assets/c74dfc1e-8e5c-4dd2-b07b-f8c11f9efad2" />
<br></br>
## Penjelasan Code
### 1. Class `SlotState`
Class `SlotState` digunakan untuk memberikan status pada setiap slot yang ada di dalam hash table. Terdapat tiga status yang digunakan, yaitu `EMPTY` untuk slot yang masih kosong, `OCCUPIED` untuk slot yang sedang menyimpan data, dan `DELETED` untuk slot yang datanya sudah dihapus. Status ini membantu program membedakan kondisi setiap slot saat melakukan proses pencarian, penyisipan, maupun penghapusan data.

### 2. Class `Entry`
Class `Entry` berfungsi sebagai wadah untuk menyimpan satu data pada hash table. Setiap objek `Entry` memiliki atribut `kode_barang`, `stok`, dan `state`. Atribut `kode_barang` digunakan sebagai kunci data, `stok` digunakan untuk menyimpan jumlah stok barang, sedangkan `state` digunakan untuk menunjukkan kondisi slot tersebut apakah kosong, terisi, atau telah dihapus.

### 3. Class `HashMapStokBarang`
Class `HashMapStokBarang` merupakan class utama yang mengelola seluruh operasi hash map. Class ini berisi ukuran hash table dan kumpulan fungsi yang digunakan untuk menambah, mencari, menghapus, dan menampilkan data barang. Saat objek dibuat, program akan membuat sejumlah slot kosong sesuai ukuran yang telah ditentukan.

### 4. Function `__init__(self, size=10)`
Function constructor ini dijalankan saat objek `HashMapStokBarang` dibuat. Fungsinya adalah menentukan ukuran hash table dan membuat daftar slot kosong menggunakan objek `Entry`. Secara default, hash table memiliki kapasitas sebanyak 10 slot.

### 5. Function `hash_function(self, kode_barang)`
Function ini digunakan untuk menentukan posisi penyimpanan suatu barang pada hash table. Perhitungan dilakukan menggunakan operasi modulus (`%`) antara kode barang dengan ukuran tabel. Hasil perhitungan tersebut menjadi indeks awal tempat data akan disimpan atau dicari.

### 6. Function `insert(self, kode_barang, stok)`
Function `insert()` digunakan untuk menambahkan data barang baru ke dalam hash table. Program terlebih dahulu menghitung indeks menggunakan fungsi hash. Jika slot tujuan masih kosong, data langsung disimpan. Namun jika slot sudah terisi oleh data lain, program akan melakukan Linear Probing, yaitu mencari slot kosong berikutnya secara berurutan hingga menemukan tempat yang tersedia. Jika kode barang yang dimasukkan sudah ada, maka data stok akan diperbarui.

### 7. Function `search(self, kode_barang)`
Function `search()` digunakan untuk mencari data barang berdasarkan kode barang yang dimasukkan pengguna. Program akan menghitung indeks awal menggunakan fungsi hash, kemudian memeriksa slot tersebut. Jika data tidak ditemukan karena adanya collision, program akan terus memeriksa slot berikutnya menggunakan metode Linear Probing sampai data ditemukan atau sampai mencapai slot kosong.
Nilai yang dikembalikan berupa objek `Entry` jika barang ditemukan, dan `None` jika barang tidak ada di dalam hash table.

### 8. Function `remove_barang(self, kode_barang)`
Function `remove_barang()` digunakan untuk menghapus data barang dari hash table. Program akan mencari terlebih dahulu data yang sesuai menggunakan function `search()`. Jika data ditemukan, status slot akan diubah menjadi `DELETED`. Cara ini digunakan agar proses pencarian data lain yang mengalami collision tetap dapat berjalan dengan benar.

### 9. Function `display(self)`
Function `display()` digunakan untuk menampilkan seluruh isi hash table. Program akan memeriksa setiap slot satu per satu dan menampilkan statusnya. Jika slot kosong akan ditampilkan "KOSONG", jika telah dihapus akan ditampilkan "DIHAPUS", dan jika berisi data maka akan ditampilkan kode barang beserta jumlah stoknya.

### 10. Function `main()`
Function `main()` merupakan pusat jalannya program. Pada function ini dibuat objek hash map, kemudian beberapa data barang dimasukkan ke dalam tabel menggunakan function `insert()`. Setelah itu program menampilkan seluruh data yang tersimpan dan meminta pengguna memasukkan kode barang yang ingin dicari. Selanjutnya function `search()` dijalankan untuk menemukan data yang sesuai, lalu hasil pencarian ditampilkan kepada pengguna. Function ini menghubungkan seluruh function lain sehingga program dapat berjalan sesuai tujuan pengelolaan stok barang minimarket.
<br></br>

## Source Output
<img width="585" height="365" alt="Screenshot 2026-06-08 164235" src="https://github.com/user-attachments/assets/6002ebbc-5dce-4ad6-921c-77ed652b08ba" />
<br></br>

## Penjelasan Output
Saat program dijalankan, pertama kali akan muncul tampilan seluruh data stok barang yang telah dimasukkan ke dalam hash table. Setiap baris menunjukkan posisi indeks pada tabel serta informasi kode barang dan jumlah stok yang tersimpan. Tampilan ini menunjukkan bagaimana data ditempatkan dalam hash table berdasarkan hasil perhitungan fungsi hash dan proses linear probing jika terjadi collision.
Kemudian setelah pengguna memasukkan kode barang yang ingin dicari, program akan menghasilkan salah satu dari dua kemungkinan output. Jika kode barang ditemukan, program menampilkan pesan bahwa barang berhasil ditemukan beserta kode barang dan jumlah stoknya. Contohnya, jika pengguna memasukkan kode 121, maka output yang muncul adalah informasi bahwa barang dengan kode tersebut memiliki stok sebanyak 25. Namun jika pengguna memasukkan kode yang tidak tersedia, misalnya 150, maka program akan menampilkan pesan "Barang tidak ditemukan", yang menunjukkan bahwa kode tersebut tidak tersimpan dalam hash table.
<br></br>

## Link Youtube
https://youtu.be/q_F2XQtyMeE?si=NSRgNz_bb-FAdFFd
<br></br>

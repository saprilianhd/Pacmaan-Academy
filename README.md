# Python Project : Super Cashier

**A. Background**

Super Cashier adalah sebuah mesin cashier self-service yang dimiliki sebuah supermarket, sehingga para customer yang tidak berada di kota tersebut dapat membeli dari supermarket tersebut.
Dimana terdapat beberapa fitur, seperti `Tambahkan Barang Belanjaan`, `Hapus Barang Belanjaan`, `Cek Order`, `Update Barang yang Dibeli`, `Hitung Total Harga`, dan `Hapus Transaksi`.

![image](https://user-images.githubusercontent.com/63135748/232187068-6250b7e5-7e10-4b73-b7e4-2338c0922ea0.png)


**B. Tools**

- Python

**C. Library**

1. Tabulate
2. DataClass

**D. Objective**

Learning Objective :
- Create Super Cashier using Python
- Using OOP to create Python program
- Appy PEP8 principles to write clean Python program

Program Objective :
- Adding Item information to Super Cashier
- Deleting Item inputed in Super Cashier
- Displaying/Checking the whole order infromation in Super Cashier, consisting of Item Names, Item Quantity, Price, and Total Price
- Updating Item informations in Super Cashier
- Displaying the total price before and after discount
- Clearing all transaction order information to Super Cashier

**E. Program Description**
Create functions for each features

![image](https://user-images.githubusercontent.com/63135748/232187114-721659ee-df83-4f25-9ec3-8f2a4f1e4260.png)
![image](https://user-images.githubusercontent.com/63135748/232187126-b9fd608d-aacc-47ae-8c7c-6e100c1fa949.png)


**F. Guide to Try it by yourself**
  1. Clone/downlaod this git repository into your local computer. It should contain:
![image](https://user-images.githubusercontent.com/63135748/232190381-4118f639-842a-420f-a5d8-12c808f9cadf.png)

  2. Open terminal > go to git repository file on your local computer
  3. Execute "python main.py" file on your terminal. Refer to screenshot below:

![image](https://user-images.githubusercontent.com/63135748/232190444-7e7d51b6-d7c2-4302-9255-3cd0583abd1b.png)

 
**G. Test Cases & Results**

-Test case 1:
Customer ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut :
  - Nama item : Ayam Goreng, QTY : 2, Harga : 20000
  - Nama item : Pasta gigi, QTY : 3, Harga : 15000
Expected output:

![image](https://user-images.githubusercontent.com/63135748/232187338-1771b016-91e6-44c0-8bb9-19d5ab1cdff3.png)

![image](https://user-images.githubusercontent.com/63135748/232187369-d6ab5d04-d4e8-4065-b643-dd94829cf5e5.png)

-Test case 2:
Ternyata customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan maka customer menggunakan method `delete_item()` untuk menghapus item. Item yang ingin dihapus adalah **Pasta Gigi**.

Expected Output:

![image](https://user-images.githubusercontent.com/63135748/232187485-64e5bb9c-5e30-431d-94b2-b0298aaffb22.png)

- Test case 3
Ternyata setelah dipikir pikir customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapus satu satu, maka customer cukup menggunakan method `rest_tyransaction()`untuk menghapus semua item yang sudah ditambhakan. 

Expected Output :

![image](https://user-images.githubusercontent.com/63135748/232189788-4f9367e7-b2a2-4cb3-af03-9148940151bf.png)

-Test case 4:
Setelah customer selesai belanja akan menghitung total belanja yang akan dibayarkan menggunakan method `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan itm item yang dibeli.

![image](https://user-images.githubusercontent.com/63135748/232190250-817e4145-d054-4098-8d0d-9326f6993eda.png)

**Improvement Suggestions**
  1. Membjuat program lebih advance seperti menambahkan warna.
  2. Menambahkan syntax clear ketika satu program telah selesai dijalankan, jadi ketika ingin memilih fitur lainnya output pada terminal hanya menampilkan program yang sedang dijalankan.
  3. Perbaikan lainnya yang mungkin ditemukan setelah program digunakan oleh beberapa user.

**Author** Copyright (c) 2023 *Saprilian Hidayat*


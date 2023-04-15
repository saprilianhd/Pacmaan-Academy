'''Ini adalah program utama untuk menjalan super cashier'''
  
from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Transaction:
    name_item: str
    numb_item: int
    price: int
    transaction_list: list = None

    def check_order(self):
        if self.numb_item is not None or self.price is not None:
            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            if len(self.transaction_list) > 1:
                headers = headers[:4] + [''] * 2 + [headers[-1]]
            rows = [[t.name_item, t.numb_item, t.price, t.numb_item * t.price] for t in self.transaction_list]
            print(tabulate(rows, headers=headers))
        else:
            print("Maaf, keranjang anda sedang kosong")

    def update_item(self, new_name_item, new_numb_item, new_price):
        for transaction in self.transaction_list:
            #if transaction.name_item == name_item:
                self.name_item = new_name_item
                self.numb_item = new_numb_item
                self.price = new_price
                break
    
    @classmethod
    def add_item(cls, item_list):
        return cls(*item_list)

    def delete_item(self, name_item):
        for transaction in self.transaction_list:
            if transaction.name_item == name_item:
                self.transaction_list.remove(transaction)
                break
    
    @classmethod
    def total_price_all(cls, transaction_list):
        total_price = sum([t.numb_item * t.price for t in transaction_list])
        print(f'Total Price for all transactions: {total_price}')
        if total_price > 500_000:
            print('10% Discount Applied')
            total_price *= 0.9
        elif total_price > 300_000:
            print('8% Discount Applied')
            total_price *= 0.92
        elif total_price > 200_000:
            print('5% Discount Applied')
            total_price *= 0.95
        print(f'Total Price after Discount: {total_price}')

    def reset_transaction(self):
        self.transaction_list.clear()
        print('Transaksi berhasil di hapus')

# example usage:
def main_menu():
    transaction_list = []
    print("-------------------------------")
    print("Selamat Datang di Super Cashier")
    print("-------------------------------\n")
    
    while True:
        print('1. Tambahkan Item')
        print('2. Hapus Item')
        print('3. Cek Order')
        print('4. Perbaharui Item')
        print('5. Lihat Total Harga')
        print('6. Hapus Transaksi')
        print('7. Keluar')
        choice = input('Enter choice: ')

        if choice == '1':
            try:
                name_item = input('Masukkan nama Item: ')
                numb_item = int(input('Masukkan jumlah Item: '))
                price = int(input('Masukkan harga per Item: '))
                trnsct = Transaction(name_item, numb_item, price, transaction_list)
                transaction_list.append(trnsct)
                print(f"Item {name_item} berhasil ditambahkan\n")
            except ValueError:
                print('Input salah. Silakan masukkan angka pada harga dan kuantitas')

        elif choice == '2':
            name_item = input('Masukkan nama Item yang ingin di hapus: ')
            for transaction in transaction_list:
                if transaction.name_item == name_item:
                    transaction_list.remove(transaction)
                    print(f'Item {name_item} berhasil dihapus\n')
                    break
            else:
                print(f'Item {name_item} tidak ditemukan di dalam list transaksi')

        elif choice == '3':
            trnsct.check_order()
            print('\n')

        elif choice == '4':
            name_item = input('Masukkan nama item yang mau di update: ')
            new_name_item = input('Masukkan nama item yang baru: ')
            new_numb_item = int(input('Masukkan jumlah item yang baru: '))
            new_price = int(input('Masukkan harga item yang baru'))
            for transaction in transaction_list:
                if transaction.name_item == name_item:
                  transaction.update_item(new_name_item, new_numb_item, new_price)
                  print(f'Item {name_item} berhasil di perbarui\n')
                  break
            else:
                print(f'Item {name_item} tidak ditemukan didalam list transaksi')

        elif choice == '5':
            Transaction.total_price_all(transaction_list)
                
        elif choice == '6':
            trnsct.reset_transaction()

        elif choice == '7':
            print('\nTerima kasih sudah menggunakan layanan super cashier')
            print('----------------------------------------------------\n')
            keluar = input("Apakah anda yakin ingin keluar dari program ? (Y/N): ").lower()
            if keluar == 'y':
                break
            else:
                main_menu()

        else:
            print('Pilihan tidak tersedia, silakan coba lagi!')
            main_menu()

if __name__ == '__main__':
    main_menu()
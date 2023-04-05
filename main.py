from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Transaction:
    name_item: str
    numb_item: int
    price: int
    transaction_list: list = None

    #sudah dihapus karena mengakibatkan outputnya double
    #def __post_init__(self):
        #if self.transaction_list is None:
            #self.transaction_list = []
        #self.transaction_list.append(self)

    def check_order(self):
        if self.numb_item is not None or self.price is not None:
            print("Your order is correct")
            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            if len(self.transaction_list) > 1:
                headers = headers[:4] + [''] * 2 + [headers[-1]]
            rows = [[t.name_item, t.numb_item, t.price, t.numb_item * t.price] for t in self.transaction_list]
            print(tabulate(rows, headers=headers))
        else:
            print("Your ordering input is incorrect")

    #masi bermaslah belum bisa update  (solve)
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
        print('Semua item berhasil di delete')

# example usage:
def main_menu():
    transaction_list = []

    while True:
        print('1. Add Item')
        print('2. Delete Item')
        print('3. Check Order')
        print('4. Update Item')
        print('5. Total Price')
        print('6. Hapus Transaksi')
        print('7. Exit')
        choice = input('Enter choice: ')

        if choice == '1':
            try:
                name_item = input('Enter name of item: ')
                numb_item = int(input('Enter quantity of item: '))
                price = int(input('Enter price of item: '))
                trnsct = Transaction(name_item, numb_item, price, transaction_list)
                transaction_list.append(trnsct)
            except ValueError:
                print('Input salah. Silakan masukkan angka pada harga dan kuantitas')

        elif choice == '2':
            name_item = input('Enter name of item to be deleted: ')
            for transaction in transaction_list:
                if transaction.name_item == name_item:
                    transaction_list.remove(transaction)
                    break
            else:
                print(f'Item {name_item} not found in transaction list')

        elif choice == '3':
            trnsct.check_order()

        elif choice == '4':
            name_item = input('Enter name of item to be updated: ')
            new_name_item = input('Enter new name of item: ')
            new_numb_item = int(input('Enter new quantity of item: '))
            new_price = int(input('Enter new price of item'))
            for transaction in transaction_list:
                if transaction.name_item == name_item:
                  transaction.update_item(new_name_item, new_numb_item, new_price)
                  break
            else:
                print(f'Item {name_item} not found in transaction list')

        elif choice == '5':
            Transaction.total_price_all(transaction_list)
                
        elif choice == '6':
            trnsct.reset_transaction()

        elif choice == '7':
            break

        else:
            print('Invalid choice, please try again')
            main_menu()

if __name__ == '__main__':
    main_menu()
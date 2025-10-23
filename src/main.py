"""
main.py
Command-line interface for the refactored banking system.
"""
from . import services as svc
from .models import Customer, Transaction, User

def admin_menu_loop(admin_name):
    while True:
        print(f"\n=== ADMIN: {admin_name} ===")
        print("1. Create NEW Profile\n2. Search Customer Data\n3. Search Customer Transaction\n4. Log Out")
        choice = input('Select (1-4): ').strip()
        if choice == '1':
            cid = input('New customer ID: ').strip()
            name = input('Name: ').strip()
            addr = input('Address: ').strip()
            phone = input('Phone: ').strip()
            pwd = input('Password: ').strip()
            balance = int(input('Initial balance (integer): ').strip() or '0')
            cust = Customer(cid, name, pwd, addr, phone)
            svc.add_customer(cust, balance)
            print('Customer created.')
        elif choice == '2':
            cid = input('Customer ID to search: ').strip()
            c = svc.find_customer(cid)
            if c:
                print('FOUND:', c)
            else:
                print('Customer not found.')
        elif choice == '3':
            cid = input('Customer ID to view transactions: ').strip()
            txs, bal = svc.get_transactions(cid)
            print('Transactions:')
            for t in txs:
                print(t['type'], t['amount'])
            print('Current balance:', bal)
        elif choice == '4':
            break
        else:
            print('Invalid choice.')

def customer_menu_loop(customer_id):
    while True:
        print(f"\n=== CUSTOMER: {customer_id} ===")
        print('1. Deposit\n2. Withdraw\n3. View Transactions\n4. Logout')
        choice = input('Select (1-4): ').strip()
        if choice == '1':
            amt = int(input('Amount to deposit: ').strip())
            svc.add_transaction(Transaction(customer_id, amt, 'Deposit'))
            print('Deposit recorded.')
        elif choice == '2':
            amt = int(input('Amount to withdraw: ').strip())
            svc.add_transaction(Transaction(customer_id, -amt, 'Withdrawal'))
            print('Withdrawal recorded.')
        elif choice == '3':
            txs, bal = svc.get_transactions(customer_id)
            for t in txs:
                print(t['type'], t['amount'])
            print('Balance:', bal)
        elif choice == '4':
            break
        else:
            print('Invalid choice.')

def main_menu():
    while True:
        print('\n**** WELCOME TO REFACTORED ONLINE BANK ****')
        print('1. Admin\n2. Customer\n3. First Time User\n4. Exit')
        choice = input('Select (1-4): ').strip()
        if choice == '1':
            aid = input('Admin ID: ').strip()
            pwd = input('Password: ').strip()
            ok, name = svc.authenticate_admin(aid, pwd)
            if ok:
                print('Welcome,', name)
                admin_menu_loop(name)
            else:
                print('Invalid admin credentials.')
        elif choice == '2':
            cid = input('Customer ID: ').strip()
            pwd = input('Password: ').strip()
            if svc.authenticate_customer(cid, pwd):
                print('Welcome,', svc.find_customer(cid)['name'])
                customer_menu_loop(cid)
            else:
                print('Invalid customer credentials.')
        elif choice == '3':
            cid = input('Please enter new Admin ID: ').strip()
            pwd = input('Please enter new Admin password: ').strip()
            name = input('Please enter new Admin name: ').strip()
            first_admin = User(cid, name, pwd)
            svc.add_admin(first_admin)
            print(F'New admin {name} created.')
        elif choice == '4':
            print('Goodbye.')
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main_menu()

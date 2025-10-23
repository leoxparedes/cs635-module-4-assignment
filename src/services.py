"""
services.py
Business logic separated from the UI.
"""
from . import database as db
from .models import Customer, Transaction, User

CUSTOMER_FILE = 'customer_db.txt'
TRANSACTION_FILE = 'transaction_db.txt'
ADMIN_FILE = 'admin_db.txt'

def load_customers():
    rows = db.read_csv(CUSTOMER_FILE)
    customers = {}
    for r in rows:
        # expected: id,name,address,phone,password,balance
        if len(r) < 6: 
            continue
        cid, name, addr, phone, pwd, bal = r[:6]
        customers[cid] = {'id': cid, 'name': name, 'address': addr, 'phone': phone, 'password': pwd, 'balance': int(bal)}
    return customers

def find_customer(customer_id):
    customers = load_customers()
    return customers.get(customer_id)

def authenticate_customer(customer_id, password):
    c = find_customer(customer_id)
    return c and c['password'] == password

def add_customer(customer: Customer, initial_balance=0):
    db.append_csv(CUSTOMER_FILE, customer.to_row(initial_balance))
    # record initial deposit transaction
    db.append_csv(TRANSACTION_FILE, Transaction(customer.id, initial_balance, 'Deposit').to_row())

def add_admin(admin: User):
    db.append_csv(ADMIN_FILE, admin.to_row())

def add_transaction(transaction: Transaction):
    db.append_csv(TRANSACTION_FILE, transaction.to_row())

def get_transactions(customer_id):
    rows = db.read_csv(TRANSACTION_FILE)
    txs = []
    balance = 0
    for r in rows:
        if len(r) < 3: 
            continue
        cid, amt, typ = r[:3]
        if cid == customer_id:
            amt_int = int(amt)
            balance += amt_int
            txs.append({'type': typ, 'amount': amt_int})
    return txs, balance

def authenticate_admin(admin_id, password):
    rows = db.read_csv(ADMIN_FILE)
    for r in rows:
        if len(r) < 3: 
            continue
        aid, name, pwd = r[0], r[1], r[2]
        if aid == admin_id and pwd == password:
            return True, name
    return False, None

import pytest
from src import services as svc
from src.models import Customer, Transaction, User
import tempfile, os

#Test creating temporary database files
@pytest.fixture
def temp_db_files(tmp_path, monkeypatch):
    #Temporary file paths
    cust_file = tmp_path / "customer_db.txt"
    tx_file = tmp_path / "transaction_db.txt"
    admin_file = tmp_path / "admin_db.txt"
    #Use patch constants in services module
    monkeypatch.setattr(svc, "CUSTOMER_FILE", cust_file.name)
    monkeypatch.setattr(svc, "TRANSACTION_FILE", tx_file.name)
    monkeypatch.setattr(svc, "ADMIN_FILE", admin_file.name)
    return cust_file, tx_file, admin_file

#Test to authenticate admin
def test_admin_auth(temp_db_files):
    #Create initial admin
    admin_test = User("admin","Administrator","adminpass")
    svc.add_admin(admin_test)
    #Check using correct credentials
    ok, name = svc.authenticate_admin("admin", "adminpass")
    assert ok and name == "Administrator"
    #Check using incorrect credentials
    ok, name = svc.authenticate_admin("admin", "wrong")
    assert not ok and name is None

#Test to add customer and find them in database
def test_add_customer_and_find(temp_db_files):
    cfile, tfile, afile = temp_db_files
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, initial_balance=100)
    found = svc.find_customer("001")
    assert found['name'] == "Alice"
    assert found['balance'] == 100

#Test to duplicate customer and check if they are in database
def test_duplicate_customer(temp_db_files):
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, 100)
    #Add same ID again
    cust2 = Customer("001","Alice2","pass456","456 St","555-222")
    svc.add_customer(cust2, 50)
    #Should have correct last added balance should in file
    customers = svc.load_customers()
    assert customers["001"]["name"] == "Alice2"

#Test to authenticate customer
def test_authenticate_customer(temp_db_files):
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, 100)
    #Correct credentials
    assert svc.authenticate_customer("001","pass123")
    #Incorrect credentials
    assert not svc.authenticate_customer("001","wrong")
    #Incorrect credentials
    assert not svc.authenticate_customer("999","pass123")

#Test transactions for withdrawals, deposits, and checking balance
def test_transactions(temp_db_files):
    cust = Customer("005","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, 100)
    #Deposit 50
    svc.add_transaction(Transaction("005",50,"Deposit"))
    txs, bal = svc.get_transactions("005")
    assert bal == 150
    assert txs[-1]['type'] == "Deposit"
    #Withdrawal 30
    svc.add_transaction(Transaction("005",-30,"Withdrawal"))
    txs, bal = svc.get_transactions("005")
    assert bal == 120
    assert txs[-1]['amount'] == -30
    #Reset customer
    svc.add_transaction(Transaction("005",-120,"Withdrawal"))

#Test edge cases of bad user id and empty transaction file
def test_edge_cases(temp_db_files):
    #Introduce a messed up line in customer_db.txt
    cfile, tfile, afile = temp_db_files
    cfile.write_text("bad,line\n010,Alice,pass123\n")
    customers = svc.load_customers()
    #Try empty transaction file
    tfile.write_text("")
    txs, bal = svc.get_transactions("010")
    assert txs == [] and bal == 0

import pytest
from src import services as svc
from src.models import Customer, Transaction
import tempfile, os

@pytest.fixture
def temp_db_files(tmp_path, monkeypatch):
    # temporary file paths
    cust_file = tmp_path / "customer_db.txt"
    tx_file = tmp_path / "transaction_db.txt"
    admin_file = tmp_path / "admin_db.txt"
    # create initial admin
    admin_file.write_text("admin,Administrator,adminpass\n")
    # patch constants in services module
    monkeypatch.setattr(svc, "CUSTOMER_FILE", cust_file.name)
    monkeypatch.setattr(svc, "TRANSACTION_FILE", tx_file.name)
    monkeypatch.setattr(svc, "ADMIN_FILE", admin_file.name)
    return cust_file, tx_file, admin_file

def test_admin_auth(temp_db_files):
    ok, name = svc.authenticate_admin("admin", "adminpass")
    assert ok and name == "Administrator"
    ok, name = svc.authenticate_admin("admin", "wrong")
    assert not ok and name is None

def test_add_customer_and_find(temp_db_files):
    cfile, tfile, afile = temp_db_files
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, initial_balance=100)
    found = svc.find_customer("001")
    assert found['name'] == "Alice"
    assert found['balance'] == 100

def test_duplicate_customer(temp_db_files):
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, 100)
    # add same ID again
    cust2 = Customer("001","Alice2","pass456","456 St","555-222")
    svc.add_customer(cust2, 50)
    # last added balance should be reflected in CSV file
    customers = svc.load_customers()
    assert customers["001"]["name"] == "Alice2"

def test_authenticate_customer(temp_db_files):
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, 100)
    assert svc.authenticate_customer("001","pass123")
    assert not svc.authenticate_customer("001","wrong")
    assert not svc.authenticate_customer("999","pass123")

def test_transactions(temp_db_files):
    cust = Customer("001","Alice","pass123","123 St","555-111")
    svc.add_customer(cust, 100)
    # deposit 50
    svc.add_transaction(Transaction("001",50,"Deposit"))
    txs, bal = svc.get_transactions("001")
    assert bal == 150
    assert txs[-1]['type'] == "Deposit"
    # withdrawal 30
    svc.add_transaction(Transaction("001",-30,"Withdrawal"))
    txs, bal = svc.get_transactions("001")
    assert bal == 120
    assert txs[-1]['amount'] == -30

def test_edge_cases(temp_db_files):
    # malformed line in customer_db.txt
    cfile, tfile, afile = temp_db_files
    cfile.write_text("bad,line\n001,Alice,pass123\n")
    customers = svc.load_customers()
    # should skip bad line and load valid
    assert "001" in customers
    # empty transaction file
    tfile.write_text("")
    txs, bal = svc.get_transactions("001")
    assert txs == [] and bal == 0

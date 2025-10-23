import pytest
from refactored_bank.models import Customer, Transaction

def test_customer_dataclass():
    c = Customer("001","Alice","pass123","123 St","555-111")
    assert c.id == "001"
    assert c.to_row(100) == ["001","Alice","123 St","555-111","pass123","100"]

def test_transaction_dataclass():
    t = Transaction("001", 500, "Deposit")
    assert t.to_row() == ["001","500","Deposit"]

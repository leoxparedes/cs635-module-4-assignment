"""
Data models for the banking system
"""
from dataclasses import dataclass

#User model
@dataclass
class User:
    id: str
    name: str
    password: str

    def to_row(self):
        return [self.id, self.name, self.password]

#Customer model
@dataclass
class Customer(User):
    address: str = ''
    phone: str = ''

    def to_row(self, balance=0):
        return [self.id, self.name, self.address, self.phone, self.password, str(balance)]

#Transaction model
@dataclass
class Transaction:
    customer_id: str
    amount: int
    type: str

    def to_row(self):
        return [self.customer_id, str(self.amount), self.type]

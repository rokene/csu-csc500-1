#!/usr/bin/env python3

from datetime import datetime
from typing import List

class Transaction:
    def __init__(self, date: datetime, description: str, amount: float, balance: float):
        self.date: datetime = date
        self.description: str = description
        self.amount: float = amount
        self.balance: float = balance

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} | {self.description} | {self.amount:.2f} | {self.balance:.2f}"

class BankLedger:
    balance: float = 0.0
    overdraft_fee: float = -45.0

    def __init__(self, initial_balance: float=0):
        self.transactions: List[Transaction] = []
        self.add_transaction("Initial Account Deposit", initial_balance)

    def add_transaction(self, description: str, amount: float):
        self.balance = round(self.balance + amount, 2)
        self.transactions.append(Transaction(datetime.now(), description, amount, self.balance))

        if amount < 0 and self.balance < 0:
            self.balance = round(self.balance - self.overdraft_fee, 2)
            self.transactions.append(Transaction(datetime.now(), "Overdraft Fee", self.overdraft_fee, self.balance))

    def display_ledger(self):
        print("Date       | Description      | Amount | Balance")
        print("------------------------------------------------")
        for transaction in self.transactions:
            print(transaction)

ledger = BankLedger(200)
ledger.add_transaction("House Payment", -1200.53)
ledger.add_transaction("Lottery Winning", 100000000.00)
ledger.add_transaction("Lambo Payment", -345132.13)
ledger.add_transaction("House Payment", -545132.13)
ledger.display_ledger()

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:53:16 2023

@author: user
"""

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount"

    def get_balance(self):
        return self.balance


class CurrentAccount(Account):
    def __init__(self, account_number, balance, cheque_count=0):
        super().__init__(account_number, balance)
        self.cheque_count = cheque_count

    def issue_cheque(self):
        self.cheque_count += 1
        return f"Cheque issued. Total cheques issued: {self.cheque_count}"


class DepositAccount(Account):
    def __init__(self, account_number, balance, withdrawal_limit, interest_rate):
        super().__init__(account_number, balance)
        self.withdrawal_limit = withdrawal_limit
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance and amount <= self.withdrawal_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds, invalid withdrawal amount, or exceeded withdrawal limit"

    def calculate_interest(self):
        return (self.balance * self.interest_rate) / 100


class RestrictedAccount(CurrentAccount):
    def __init__(self, account_number, balance, cheque_count=0, max_withdrawal_limit=1000):
        super().__init__(account_number, balance, cheque_count)
        self.max_withdrawal_limit = max_withdrawal_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance and amount <= self.max_withdrawal_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds, invalid withdrawal amount, or exceeded maximum withdrawal limit"


class AccountWithOverdraft(CurrentAccount):
    def __init__(self, account_number, balance, cheque_count=0, overdraft_limit=0):
        super().__init__(account_number, balance, cheque_count)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or exceeded overdraft limit"

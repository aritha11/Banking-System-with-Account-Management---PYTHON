# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:42:09 2023

@author: user
"""

from Account_class import Account

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
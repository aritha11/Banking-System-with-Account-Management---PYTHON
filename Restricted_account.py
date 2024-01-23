# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:48:42 2023

@author: user
"""

from Current_account import CurrentAccount

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
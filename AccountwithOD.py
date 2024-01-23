# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:50:33 2023

@author: user
"""

from Current_account import CurrentAccount

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
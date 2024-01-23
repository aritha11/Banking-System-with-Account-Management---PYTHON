# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:36:15 2023

@author: user
"""

from Account_class import Account

class CurrentAccount(Account):
    def __init__(self, account_number, balance, cheque_count=0):
        super().__init__(account_number, balance)
        self.cheque_count = cheque_count

    def issue_cheque(self):
        self.cheque_count += 1
        return f"Cheque issued. Total cheques issued: {self.cheque_count}"

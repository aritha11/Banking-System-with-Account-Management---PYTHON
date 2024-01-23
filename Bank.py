# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:08:33 2023

@author: user
"""


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def withdraw_from_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            result = account.withdraw(amount)
            return result
        else:
            return "Account not found"
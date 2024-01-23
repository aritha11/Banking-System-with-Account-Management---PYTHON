# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:20:35 2023

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

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount"

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

# Create a Bank instance
bank = Bank()

while True:
    print("\nBanking System Menu:")
    print("1. Add Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        account_type = input("Enter account type (Current/Deposit/Restricted/Overdraft): ").capitalize()

        if account_type == 'Current':
            cheque_count = int(input("Enter initial cheque count: "))
            account = CurrentAccount(account_number, balance, cheque_count)
        elif account_type == 'Deposit':
            withdrawal_limit = float(input("Enter withdrawal limit: "))
            interest_rate = float(input("Enter interest rate (%): "))
            account = DepositAccount(account_number, balance, withdrawal_limit, interest_rate)
        elif account_type == 'Restricted':
            max_withdrawal_limit = float(input("Enter maximum withdrawal limit: "))
            account = RestrictedAccount(account_number, balance, max_withdrawal_limit=max_withdrawal_limit)
        elif account_type == 'Overdraft':
            overdraft_limit = float(input("Enter overdraft limit: "))
            account = AccountWithOverdraft(account_number, balance, overdraft_limit=overdraft_limit)
        else:
            print("Invalid account type. Account not added.")
            continue

        bank.add_account(account)
        print(f"Account {account_number} added.")

    elif choice == '2':
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        result = bank.withdraw_from_account(account_number, amount)
        print(result)

    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        result = bank.withdraw_from_account(account_number, amount)
        print(result)

    elif choice == '4':
        print("Exiting the banking system. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Balans kifayət qədər deyil.")

    def display_balance(self):
        print(f"Hesab nömrəsi: {self.account_number}, Balans: {self.balance}")

class CreditAccount(BankAccount):
    def __init__(self, account_number, balance, credit_amount):
        super().__init__(account_number, balance)
        self.credit_amount = credit_amount

    def give_credit(self):
        self.balance += self.credit_amount

    def pay_credit(self):
        monthly_payment = self.credit_amount / 12
        self.balance -= monthly_payment
        print(f"Aylıq kredit ödənişi: {monthly_payment}")


bank_acc = BankAccount(123456, 1000)
bank_acc.display_balance()  
bank_acc.deposit(500)
bank_acc.display_balance()  
bank_acc.withdraw(200)
bank_acc.display_balance()  

credit_acc = CreditAccount(987654, 2000, 10000)
credit_acc.display_balance()  
credit_acc.give_credit()
credit_acc.display_balance()  
credit_acc.pay_credit()  
credit_acc.display_balance()  

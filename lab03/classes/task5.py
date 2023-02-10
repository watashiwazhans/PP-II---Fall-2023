class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def check_balance(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited. Balance is {self.balance}")


    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawal is unavaliable. Balance is low")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from the deposit. Balance is {self.balance}")

ba1 = Account("Beket")
ba2 = Account("Medeu")

ba1.check_balance()
ba1.withdrawal(1000)
ba1.deposit(1000)
ba1.withdrawal(500)
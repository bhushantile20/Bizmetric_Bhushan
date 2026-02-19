class Account:
    def __init__(self, id, balance=0, name=""):
        try:
            self.id = id
            self.balance = float(balance)
            self.name = name[:30]
        except:
            self.id = ""
            self.balance = 0.0
            self.name = ""

    def deposit(self, amt):
        try:
            amt = float(amt)
            if amt <= 0:
                return "Invalid amount"
            self.balance += amt
            return f"Deposited ₹{amt:.2f} | Balance ₹{self.balance:.2f}"
        except:
            return "Invalid amount"

    def withdraw(self, amt):
        try:
            amt = float(amt)
            if amt <= 0:
                return "Invalid amount"
            if amt > self.balance:
                return "Insufficient balance"
            self.balance -= amt
            return f"Withdrew ₹{amt:.2f} | Balance ₹{self.balance:.2f}"
        except:
            return "Invalid amount"

class Wallet:
    def __init__(self,amount):
        self.amount = amount

    def __add__(self,other):
        return Wallet(self.amount + other.amount)
    
    def __sub__(self,other):
        return Wallet(self.amount - other.amount)
    
    def __muL__(self,factor):
        return Wallet(self.amount * factor)
    
    def __truediv__(self,factor):
        return Wallet(self.amount / factor)
    
    def __repr__(self):
        return f"Wallet(amount={self.amount})"

Wallet1 = Wallet(100)
Wallet2 = Wallet(50)

wallet3 = Wallet1 + Wallet2
print(wallet3)

wallet4 = Wallet1 - Wallet2
print(wallet4)
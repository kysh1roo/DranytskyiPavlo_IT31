class Wallet:
    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner
        self.__balance = round(balance, 2)

    @property
    def balance(self):
        return self.__balance

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("--- case 1: del wallet ---")
wallet = Wallet("Pavlo Dranytskyi", 2000)
del wallet
print("after del")

print("--- case 2: two references ---")
wallet = Wallet("Pavlo Dranytskyi", 2000)
other = wallet
del wallet
print("after del wallet (other still references the object)")
del other
print("after del other")

print("--- case 3: end of program ---")
last = Wallet("Pavlo Dranytskyi", 2000)
print("program finished")

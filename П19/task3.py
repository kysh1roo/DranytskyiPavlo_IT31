class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner        # викликає сетер owner
        self.balance = balance    # викликає сетер balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value or not value.strip():
            raise ValueError("owner name can not be empty")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.__balance == 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("not enough money")
        self.balance = self.__balance - amount


if __name__ == "__main__":
    wallet = Wallet("Pavlo Dranytskyi", 2000)
    print(wallet.balance)
    wallet.balance = 1200.555
    print(wallet.balance)
    print("is_empty:", wallet.is_empty)

    try:
        wallet.balance = -50
    except ValueError as e:
        print("balance = -50 ->", e)

    try:
        wallet.owner = ""
    except ValueError as e:
        print("owner = '' ->", e)

    try:
        wallet.is_empty = True
    except AttributeError as e:
        print("is_empty = True ->", e)

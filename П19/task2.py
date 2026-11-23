class Wallet:
    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("not enough money")
        self.__balance = round(self.__balance - amount, 2)

    def show(self):
        return f"{self.owner}: {self.__balance:.2f}"


if __name__ == "__main__":
    wallet = Wallet("Pavlo Dranytskyi", 2000)
    wallet.deposit(500)
    print(wallet.show())
    wallet.withdraw(300)
    print(wallet.show())

    try:
        wallet.withdraw(5000)
    except ValueError as e:
        print("withdraw(5000) failed:", e)

    try:
        print(wallet.__balance)
    except AttributeError as e:
        print("wallet.__balance ->", e)

    print("wallet._Wallet__balance ->", wallet._Wallet__balance)
    print("wallet.__dict__ ->", wallet.__dict__)

    # Це не повний захист: значення можна змінити через змангльоване ім'я.
    wallet._Wallet__balance = -1
    print("after hack:", wallet.show())

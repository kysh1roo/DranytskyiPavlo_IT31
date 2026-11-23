class Wallet:
    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner
        self.balance = round(balance, 2)


if __name__ == "__main__":
    wallet = Wallet("Pavlo Dranytskyi", 2000)
    print(f"created: {wallet.owner}, balance {wallet.balance:.2f}")

    for owner, balance in (("", 500), ("Pavlo Dranytskyi", -100)):
        try:
            Wallet(owner, balance)
        except ValueError as e:
            print(f"Wallet({owner!r}, {balance}) failed: {e}")

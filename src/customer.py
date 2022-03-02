class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def can_afford_drink(self, drink):
        if self.wallet >= drink:
            return True

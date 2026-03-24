class Money:
    def __init__(self, amount, currency='KGS'):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"<Money obj amount={self.amount} currency={self.currency}>"

    # equal
    def __eq__(self, other):
        print("OTHER in eq:", other)
        if self.amount == other.amount:
            return True
        else:
            return False

    # gt -> greater than ">"
    # gte -> greater than or equal ">="
    # lt -> less than "<"
    # lte -> less than or equal "<="
    def __gt__(self, other):
        print("OTHER in gt:", other)
        if self.amount > other.amount:
            return True
        else:
            return False
        ### one line ###
        # return self.amount > other.amount

    def __add__(self, other):
        new_amount = self.amount + other.amount
        new_money = Money(new_amount, other.currency)
        return new_money

money_igor = Money(100)
money_artur = Money(200)
print(money_igor)
print(money_igor == money_artur)
print(money_artur > money_igor)
total_money = money_igor + money_artur
print(total_money)

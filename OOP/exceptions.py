class Wallet:
    def __init__(self, currency: str, balance: int):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif currency != currency.upper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        elif other.currency != self.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.currency

    def __add__(self, other):
        if not isinstance(other, Wallet) or other.currency != self.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or other.currency != self.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - other.balance)


wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
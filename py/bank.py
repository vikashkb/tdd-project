from money import Money

class Bank:
    def __init__(self):
        self.exchangeRates = {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + "->" + currencyTo
        self.exchangeRates[key] = rate

    # a money needs to be converted to a currency
    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)

        key = aMoney.currency + "->" + aCurrency
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurrency)

        raise Exception(key)

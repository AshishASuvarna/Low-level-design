from Currency import Currency

class Conversion:
    _exchange_rates = {
        (Currency.DOLLAR, Currency.RUPEE): 83,
        (Currency.RUPEE, Currency.DOLLAR): 1 / 83,
        (Currency.DOLLAR, Currency.YEN): 145,
        (Currency.YEN, Currency.DOLLAR): 1 / 145,
        (Currency.RUPEE, Currency.YEN): 1.75,
        (Currency.YEN, Currency.RUPEE): 1 / 1.75,
    }

    @classmethod
    def convert(cls, amount, from_currency: Currency, to_currency: Currency) -> float:
        if from_currency == to_currency:
            return amount

        rate = cls._exchange_rates.get((from_currency, to_currency), None)
        if rate is None:
            raise ValueError(f"Conversion rate from {from_currency} to {to_currency} not available.")

        return amount * rate
__author__ = 'Dale'


class Error(Exception):
    def __init__(self, value):
        super().__init__(value)


class Country():
    def __init__(self, name, currency_code, currency_symbol):
        # Defining Values
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def __str__(self):
        # Returns string of form Country, Code, Symbol
        return '{} {} {}'.format(self.name, self.currency_code, self.currency_symbol)

    def format_amount(self, amount):
        formated_amount = self.currency_symbol + str(format(float(amount), '.1f'))
        return formated_amount


class Details():
    pass


print(Country('Germany', 'EUR', '€'))

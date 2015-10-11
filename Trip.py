__author__ = 'Dale Muccignat'


class Error(Exception):
    def __init__(self, value):
        super().__init__(value)


class Country:
    def __init__(self, name, currency_code, currency_symbol):
        # Defining Values
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def __str__(self):
        # Returns string of form Country, Code, Symbol
        return '{} {} {}'.format(self.name, self.currency_code, self.currency_symbol)

    def format_amount(self, amount):
        if amount < 0:
            raise Error("Amount can't be less than 0.")
        formated_amount = self.currency_symbol + str(format(float(amount), '.1f'))
        return formated_amount


class Details:

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        # Date string is expect to be of format YYYY/MM/DD
        details_tuple = (country_name, start_date, end_date)
        if details_tuple in self.locations:
            raise Error("Trip already recorded.")
        if start_date > end_date:
            raise Error("Trip can't start after it ends.")
        # Add list to location list.
        self.locations.append(details_tuple)

    def current_country(self, date_string):

# print(Country('Germany', 'EUR', '€'))
# print(Country('Germany', 'EUR', '€'))

details = Details()

details.add("Australia", "1990/05/10", "1999/05/10")
details.add("Australia", "2000/05/11", "2005/05/10")
# details.add("Australia", "1990/05/10", "1980/05/10")
print(details.locations)


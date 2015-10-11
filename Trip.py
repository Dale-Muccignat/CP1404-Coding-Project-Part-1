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
        # Returns a string that begins with the country's currency symbol followed by the amount to 1 decimal place
        return self.currency_symbol + str(format(float(amount), '.1f'))


class Details:

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        # Checking if date string is of format YYYY/MM/DD
        # Split dates into lists
        date_split_list = [start_date.split("/"), end_date.split("/")]
        # Check if all characters is a digit
        for item in date_split_list:
            for part in item:
                for char in part:
                    if not char.isdigit():
                        raise Error("Not a valid date!")
            # Check if dates are right format
            if len(item[0]) != 4 or len(item[1]) != 2 or len(item[2]) != 2:
                raise Error("Not a valid date!")
        details_tuple = (country_name, start_date, end_date)
        # If trip already recorded, raise error
        if details_tuple in self.locations:
            raise Error("Trip already recorded.")
        # If trip starts after it finished, raise an error
        if start_date > end_date:
            raise Error("Trip can't start after it ends.")
        # Add list to location list.
        self.locations.append(details_tuple)

    def current_country(self, date_string):
        current_country = ""
        # for each list item in locations, check if date_string is in between start and end dates.
        for item in self.locations:
            if item[1] < date_string < item[2]:
                current_country = item[0]
        # If current_country is still an empty strip, raise error
        if current_country == "":
            raise Error("Not currently in a recorded country.")
        else:
            return current_country

    def is_empty(self):
        # Returns true if list is empty
        return self.locations == []


# Various trial print statements
# print(Country('Germany', 'EUR', '€').format_amount(100))
# print(Country('Germany', 'EUR', '€'))

# details = Details()

# details.add("Germany", "1990/05/10", "1999/05/10")
# details.add("Australia", "2000/05/11", "2005/05/10")
# details.add("Australia", "1990/05/10", "1980/05/10")
# print(details.locations)
# print(details.current_country("2015/05/10"))


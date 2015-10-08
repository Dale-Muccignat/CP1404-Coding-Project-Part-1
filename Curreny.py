__author__ = 'Dale'
import web_utility


def convert(amount, from_currency_code, too_currency_code):
    # Customizable url which takes into account convert paramaters
    url_string = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(from_currency_code) +\
                 "&to=" + str(too_currency_code)
    result = web_utility.load_page(url_string)
    # Print result section of the web_utility module.
    #TODO Truncate result
    truncated_string = result[result.index("result"):]
    truncated_string = truncated_string.split()
    return truncated_string


def get_details(country_name):
    # Variables to be used later in code
    country_details = ()
    # Format is like: CountryName,Code,Symbol
    currency_details = open("currency_details.txt", mode="r", encoding="UTF-8")

    # FOR LOOP TEST
    for line in currency_details.readlines():
        parts = line.strip().split(",")
        if parts[0] == str(country_name.title()):
            country_details = tuple(parts)
    currency_details.close()
    if country_details == ():
        return "Country doesn't exist."
    else:
        return country_details

# Test functions
# print(convert(input("Amount to convert: "), input("Convert From: "), input("Convert Too: ")))
print(get_details(input("Enter Country: ")))


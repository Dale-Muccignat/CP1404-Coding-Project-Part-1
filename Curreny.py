__author__ = 'Dale'
import web_utility


def convert(amount, from_currency_code, too_currency_code):
    try:
        # Test if amount is a number, produces an error
        float(amount)
        # Customizable url which takes into account convert paramaters
        url_string = "https://www.google.com/finance/converter?a={}&from={}&to={}".format(str(amount), from_currency_code.upper(), too_currency_code.upper())
        result = web_utility.load_page(url_string)
        # Print result section of the web_utility module.
        truncated_string = result[result.index("result"):]
        # Seperates with >
        truncated_string = truncated_string.split(">")
        truncated_string = truncated_string[2].split(" ")
        return truncated_string[0]
    except:
        return -1

def get_details(country_name):
    # Variables to be used later in code
    country_details = ()
    # Format is like: CountryName,Code,Symbol
    currency_details = open("currency_details.txt", mode="r", encoding="UTF-8")

    for line in currency_details.readlines():
        # Split line into three parts.
        parts = line.strip().split(",")
        if parts[0] == str(country_name.title()):
            # Save to tuple
            country_details = tuple(parts)
    currency_details.close()

    # If country_details is still empty return and error
    if country_details == ():
        return "Country doesn't exist."
    else:
        return country_details

# Test functions
# print(convert(input("Amount to convert: "), input("Convert From: "), input("Convert Too: ")))
# print(get_details(input("Enter Country: ")))


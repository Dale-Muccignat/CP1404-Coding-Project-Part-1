__author__ = 'Dale Muccignat'
import web_utility


def convert(amount, from_currency_code, too_currency_code):
    try:
        # Test if amount is a number, produces an error
        float(amount)
        # Customizable url which takes into account convert parameters
        url_string = "https://www.google.com/finance/converter?a=" \
                     "{}&from={}&to={}".format(str(amount), from_currency_code.upper(), too_currency_code.upper())
        result = web_utility.load_page(url_string)
        truncated_string = result[result.index("result"):]
        # Separates with >
        truncated_string = truncated_string.split(">")
        # Separates with " "
        truncated_string = truncated_string[2].split(" ")
        # Returns the amount as a float, if amount is not a number, functions returns -1.
        return format(float(truncated_string[0]), '.2f')
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

# Test print statements
# print(convert(input("Amount to convert: "), input("Convert From: "), input("Convert Too: ")))
# print(get_details(input("Enter Country: ")))


__author__ = 'Dale'
import web_utility


def convert(amount, from_currency_code, too_currency_code):
    # Customizable url which takes into account convert paramaters
    url_string = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(from_currency_code) +\
                 "&to=" + str(too_currency_code)
    result = web_utility.load_page(url_string)
    # Print result section of the web_utility module.
    print(result[result.index("result"):])
    return


def get_details(country_name):
    # Variables to be used later in code
    document_end = ""
    country_details = ""
    line_count = 0
    # Format is like: CountryName,Code,Symbol
    currency_details = open("currency_details.txt", mode="r", encoding="utf-8")

    while document_end == "":
        line = currency_details.readline()
        # Formats the string with .title and checks if in document
        if str(country_name.title()) in line:
            document_end = "True"
            currency_details.close()
            # Had to close and open the docunment to reset the curser
            currency_details = open("currency_details.txt", mode="r", encoding="utf-8")
            country_details = currency_details.readlines()
            currency_details.close()
        elif line == "":
            # A blank line exists at the end of the docunment which is used to stop the while loop
            document_end = "True"
        else:
            # Line count to be used later to call line form a list
            line_count += 1

    if country_details == "":
        # If country_details is still empty, means country wasn't found.
        # print("Country does not exist.")    # Debugging
        country_details_tuple = ()
        return country_details_tuple
    else:
        # Turns string into a list of strings
        parts = country_details[line_count].split(",")
        # String into tuple
        country_details_tuple = ([part for part in parts])
        #TODO Remove \n from tuple
        return country_details_tuple
        # print(country_details_tuple)    # Debugging


# Test functions
# convert(input("Amount to convert: "), input("Convert From: "), input("Convert Too: "))
print(get_details(input("Enter Country: ")))


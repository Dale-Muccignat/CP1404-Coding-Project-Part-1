__author__ = 'Dale'
import web_utility

def convert(amount, home_currency_code, location_currency_code):
    #Customizable url which takes into account convert paramaters
    url_string = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code)
    result = web_utility.load_page(url_string)
    #Print result section of the web_utility module.
    print(result[result.index("result"):])
    return

def get_details(country_name):
    document_end = ""
    country_details = ""
    line_count = 0
    #Format is like: CountryName,Code,Symbol
    currency_details = open("currency_details.txt", mode="r", encoding="utf-8")

    while document_end == "":
        line = currency_details.readline()
        if str(country_name.title()) in line:   #formats the string with .capatilize and checks if in document
            document_end = "True"
            currency_details.close()
            currency_details = open("currency_details.txt", mode="r", encoding="utf-8")
            country_details = currency_details.readlines()
        elif line == "":
            document_end = "True"
        else:
            line_count += 1

    if country_details == "":
        print("Country does not exist.")
    else:
        print(country_details[line_count])
    currency_details.close()

#Test functions
# convert(input("Amount to convert: "), input("Convert From: "), input("Convert Too: "))
get_details(input("Enter Country: "))


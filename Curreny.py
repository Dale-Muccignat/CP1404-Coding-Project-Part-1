__author__ = 'Dale'
import web_utility

def convert(amount, home_currency_code, location_currency_code):
    #Customizable url which takes into account convert paramaters
    url_string = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code)
    result = web_utility.load_page(url_string)
    #Print result section of the web_utility module.
    print(result[result.index('result'):])
    return

def get_details(country_name):
    country_details = ""
    currency_details = open('currency_details.txt', mode='r', encoding='utf-8')
    #Stores file's contents for use.
    file_contents = currency_details.read()
    print(file_contents)
    #TODO Count how many lines, check each line and return that line as a tuple.
    currency_details.close()

#Test code
# convert(1, 'AUD', 'JPY')
currency_details = open('currency_details.txt', mode='r', encoding='utf-8')
country_name = input("Country Name: ")
#TODO Count how many lines, check each line and return that line as a tuple.

document_end = ""
country_details = ""
line_count = 0
while document_end == "":
    if country_name in currency_details.readline():
        document_end = "True"
        currency_details.close()
        currency_details = open('currency_details.txt', mode='r', encoding='utf-8')
        country_details = currency_details.readlines()
    else:
        line_count += 1

if country_details == "":
    print("Country does not exist.")
else:
    print(country_details[line_count])

currency_details.close()

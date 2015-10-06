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

#Testing get_details
currency_details = open('currency_details.txt', mode='r', encoding='utf-8')
#Stores file's contents for use.
file_contents = currency_details.read()
print(file_contents)
#TODO Count how many lines, check each line and return that line as a tuple.
currency_details.close()

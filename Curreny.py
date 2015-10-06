__author__ = 'Dale'
import web_utility

def convert(amount, home_currency_code, location_currency_code):
    #Customizable url which takes into account convert paramaters
    url_string = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code)
    result = web_utility.load_page(url_string)
    #Print result section of the web_utility module.
    print(result[result.index('result'):])
    return

convert(1, 'AUD', 'JPY')

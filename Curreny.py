__author__ = 'Dale Muccignat'
import web_utility


def convert(amount, from_currency_code, to_currency_code):
    try:
        # Test if amount is a number, produces an error
        float(amount)
        # Customizable url which takes into account convert parameters, which are converted to uppercase for now
        url_string = "https://www.google.com/finance/converter?a={}&from={}&to={}"\
            .format(str(amount), from_currency_code.upper(), to_currency_code.upper())
        result = web_utility.load_page(url_string)
        truncated_string = result[result.index("result"):]
        truncated_string = truncated_string.split(">")
        truncated_string = truncated_string[2].split(" ")
        # Returns the amount as a float, if amount is not a number, functions returns -1.
        return float(truncated_string[0])
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
    return country_details

# print(get_details(input("Enter Country Name: ")))
# print(convert(input("Amount: "), input("From: "), input("To: ")))

def main():
    test1 = convert(1, "AUD", "AUD")
    test2 = convert(1, "JPY", "ABC")
    test3 = convert(1, "ABC", "USD")
    test4 = convert(10.95, "AUD", "JPY")
    test5 = convert(943.18, "JPY", "AUD")
    test6 = convert(10.95, "AUD", "BGN")
    test7 = convert(13.62, "BGN", "AUD")
    test8 = convert(200.15, "BGN", "JPY")
    test9 = convert(13859.49, "JPY", "BGN")
    test10 = convert(100, "JPY", "USD")
    test11 = convert(0.83, "USD", "JPY")
    test12 = convert(19.99, "USD", "BGN")
    test13 = convert(34.58, "BGN", "USD")
    test14 = convert(19.99, "USD", "AUD")
    test15 = convert(27.8, "AUD", "USD")
    test16 = get_details("Unknown")
    test17 = get_details("Japanese")
    test18 = get_details("")
    test19 = get_details("Australia")
    test20 = get_details("Japan")
    test21 = get_details("Hong Kong")
    print(format("invalid conversion", ">30") + format("1.00", ">10") + format("AUD->AUD", "^20") + str(format(test1, '<10.2f')))
    print(format("invalid conversion", ">30") + format("1.00", ">10") + format("JPY->ABC", "^20") + str(format(test2, '<10.2f')))
    print(format("invalid conversion", ">30") + format("1.00", ">10") + format("ABC->USD", "^20") + str(format(test3, '<10.2f')))
    print(format("valid conversion", ">30") + format("10.95", ">10") + format("AUD->JPY", "^20") + str(format(test4, '<10.2f')))
    print(format("valid conversion reverse", ">30") + format("943.18", ">10") + format("JPY->AUD", "^20") + str(format(test5, '<10.2f')))
    print(format("valid conversion", ">30") + format("10.95", ">10") + format("AUD->BGN", "^20") + str(format(test6, '<10.2f')))
    print(format("valid conversion reverse", ">30") + format("13.62", ">10") + format("BGN->AUD", "^20") + str(format(test7, '<10.2f')))
    print(format("valid conversion", ">30") + format("200.15", ">10") + format("BGN->JPY", "^20") + str(format(test8, '<10.2f')))
    print(format("valid conversion reverse", ">30") + format("13859.49", ">10") + format("JPY->BGN", "^20") + str(format(test9, '<10.2f')))
    print(format("valid conversion", ">30") + format("100.00", ">10") + format("JPY->USD", "^20") + str(format(test10, '<10.2f')))
    print(format("valid conversion reverse", ">30") + format("0.83", ">10") + format("USD->JPY", "^20") + str(format(test11, '<10.2f')))
    print(format("valid conversion", ">30") + format("19.99", ">10") + format("USD->BGN", "^20") + str(format(test12, '<10.2f')))
    print(format("valid conversion reverse", ">30") + format("34.58", ">10") + format("BGN->USD", "^20") + str(format(test13, '<10.2f')))
    print(format("valid conversion", ">30") + format("19.99", ">10") + format("USD->AUD", "^20") + str(format(test14, '<10.2f')))
    print(format("valid conversion reverse", ">30") + format("27.80", ">10") + format("AUD->USD", "^20") + str(format(test15, '<10.2f')))
    print(format("invalid details Unknown", "<30") + str(test16))
    print(format("invalid details Japanese", "<30") + str(test17))
    print(format("invalid details", "<30") + str(test18))
    print(format("  valid details Australia", "<30") + str(test19))
    print(format("  valid details Japan", "<30") + str(test20))
    print(format("  valid details Hong Kong", "<30") + str(test21))

if __name__ == "__main__":
    main()



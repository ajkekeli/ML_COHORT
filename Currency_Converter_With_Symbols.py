# Simple Currency Converter by [GROUP 8]
# This program converts an amount from one currency to another using fixed rates as of MAY 2025.

# Currency exchange rates are stored in a dictionary.
exchange_rates = {
    'USD': {'EUR': 0.91, 'GBP': 0.78, 'INR': 83.2, 'GHS':13.5},
    'EUR': {'USD': 1.10, 'GBP': 0.86, 'INR': 91.4, 'GHS':14.8},
    'GBP': {'USD': 1.28, 'EUR': 1.16, 'INR': 106.3, 'GHS':17.2},
    'INR': {'USD': 0.012,'EUR': 0.011, 'GBP': 0.0094, 'GHS':0.16},
    'GHS': {'USD': 0.074,'EUR': 0.067, 'GBP': 0.058, 'INR': 6.2}
}

# Currency symbols for display
currency_symbols = {
    'USD': '$',
    'EUR': '€',
    'GBP': '£',
    'INR': '₹',
    'GHS': '₵'
}

# This function performs the conversion.
def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        result = amount * rate
        return result
    else:
        return None

# Main program starts here
print("Welcome to the Currency Converter!")
print("Supported currencies: USD, EUR, GBP, INR, GHS")

while True:
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Convert from (e.g., USD): ").upper()
        to_currency = input("Convert to (e.g., EUR): ").upper()

        converted = convert_currency(amount, from_currency, to_currency)

        if converted is not None:
            from_symbol = currency_symbols.get(from_currency, '')
            to_symbol = currency_symbols.get(to_currency, '')
            print(f"{from_symbol}{amount:.2f} {from_currency} = {to_symbol}{converted:.2f} {to_currency}")
        else:
            print("Sorry, currency not supported or invalid input.")

    except ValueError:
        print("Please enter a valid number for the amount.")

    again = input("Do you want to convert another amount? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for using the Currency Converter. Goodbye!")
        break

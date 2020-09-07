# this file contains functions that flash messages from handlers.py

from flask import Flask, flash
from forex_python.converter import CurrencyRates, Decimal, CurrencyCodes


# flashes all errors in the 'errors' list

def flash_errors(errors):
    for error in errors:
        flash(error, 'danger')


# flashes the new converted value with two decimal points and the new currency's symbol on the left

def flash_conversion(firstCurr, secondCurr, amount):
    s = CurrencyCodes()
    c = CurrencyRates()

    symbol = s.get_symbol(secondCurr)
    result = c.convert(firstCurr, secondCurr, Decimal(amount))
    formatted_result = "{:,.2f}".format(result)

    flash_message = f'{symbol} {formatted_result}'
    flash(flash_message, 'success')

# this file contains functions that check the validity of currency codes and amounts

from flask import Flask, request


# a list of all the valid currency codes from forex_python.converter

RATES = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD',
         'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']


# checks to see if the 'amount' value is a float

def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# ensures that the 'amount' value is valid - if not, flash the appropriate error message
# return 'errors' for testing purposes

def handle_amount(errors, amount):

    if type(amount) is int or type(amount) is float:
        return errors
    elif is_float(amount) or amount.isnumeric():
        amount = float(amount)
    else:
        amountError = f'Not a valid amount: {amount}'
        errors.append(amountError)
    return errors


# ensures that the 'firstCurr' value is valid - if not, flash the appropriate error message
# return 'errors' for testing purposes

def handle_firstCurr(errors, firstCurr):
    if firstCurr not in RATES:
        fromError = f'Not a valid code: {firstCurr}'
        errors.append(fromError)
    return errors


# ensures that the 'secondCurr' value is valid - if not, flash the appropriate error message
# return 'errors' for testing purposes

def handle_secondCurr(errors, secondCurr):
    if secondCurr not in RATES:
        toError = f'Not a valid code: {secondCurr}'
        errors.append(toError)
    return errors

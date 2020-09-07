from flask import Flask, request, render_template, jsonify, flash, redirect
from handlers import handle_amount, handle_firstCurr, handle_secondCurr
from flashers import flash_conversion, flash_errors


# the main app for the currency converter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey'


# render index.html when in the root route

@app.route('/')
def home():
    return render_template('index.html')


# make a post request with the convertFrom, convertTo & amount values from the form.

@app.route('/conversion', methods=['POST'])
def convert():
    errors = []

    firstCurr = request.form.get('convertFrom')
    secondCurr = request.form.get('convertTo')
    amount = request.form.get('amount')

    # check to see if all values are valid - if not, redirect and flash appropriate error message(s).
    handle_amount(errors, amount)
    handle_firstCurr(errors, firstCurr)
    handle_secondCurr(errors, secondCurr)

    # if all values are valid, redirect and flash the new converted value.
    if len(errors) > 0:
        flash_errors(errors)
    else:
        flash_conversion(firstCurr, secondCurr, amount)
    return redirect('/')

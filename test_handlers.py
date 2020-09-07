from handlers import handle_amount, handle_firstCurr, handle_secondCurr, RATES
from unittest import TestCase

# Unit tests for handlers.py


class HandlersTest(TestCase):

    # tests that currency amounts are handled correctly
    def test_handle_amount(self):

        # tests that the correct error message will be appended to the errors list if the 'amount' value is not numeric
        errors = []
        amount = 'hello'
        self.assertEquals(handle_amount(errors, amount),
                          [f"Not a valid amount: {amount}"])

        # tests that no error message will be appended to the errors list if the 'amount' value is an int
        errors2 = []
        amount2 = 250
        self.assertEquals(handle_amount(errors2, amount2), [])

        # tests that no error message will be appended to the errors list if the 'amount' value is a float
        errors3 = []
        amount3 = 250.00
        self.assertEquals(handle_amount(errors3, amount3), [])

        # tests that no error message will be appended to the errors list if the 'amount' value is a numeric string
        errors4 = []
        amount4 = '345'
        self.assertEquals(handle_amount(errors4, amount4), [])

    # tests the handle_firstCurr() function
    def test_handle_firstCurr(self):

        # tests that the correct error message will be appended to the errors list if the 'firstCurr' value is not
        # a valid currency
        errors = []
        firstCurr = 'ZZZ'
        self.assertEquals(handle_firstCurr(errors, firstCurr),
                          [f"Not a valid code: {firstCurr}"])

        # tests that no error message will be appended to the errors list if the 'firstCurr' value is a valid currency
        errors2 = []
        firstCurr2 = 'USD'
        self.assertEquals(handle_firstCurr(errors2, firstCurr2), [])

    # tests the handle_secondCurr() function
    def test_handle_secondCurr(self):

        # tests that the correct error message will be appended to the errors list if the 'secondCurr' value is not
        # a valid currency
        errors = []
        secondCurr = 'ZZZ'
        self.assertEquals(handle_secondCurr(errors, secondCurr),
                          [f"Not a valid code: {secondCurr}"])

        # tests that no error message will be appended to the errors list if the 'secondCurr' value is a valid currency
        errors2 = []
        secondCurr2 = 'USD'
        self.assertEquals(handle_secondCurr(errors2, secondCurr2), [])

from app import app
from unittest import TestCase
from forex_python.converter import CurrencyCodes

# Integration tests for app.py


class AppTestCase(TestCase):

    # tests that the user is redirected after making a post request to '/conversion'
    def test_redirect(self):
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'USD', 'convertTo': 'USD', 'amount': '20'})

            # tests that the status code of the response is 302 (redirect)
            self.assertEqual(res.status_code, 302)

            # tests that the location for the redirect is the localhost
            self.assertEqual(res.location, 'http://localhost/')

    # tests that the redirect is successful
    def test_redirect_followed(self):

        # tests for a successful redirect with a successful currency conversion
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'USD', 'convertTo': 'USD', 'amount': '20'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            # tests that the status code of the response after following the redirect is 200 (ok)
            self.assertEqual(res.status_code, 200)

            # tests that an appropriate flash is shown after the redirect is followed (and that the converted
            # number is a float with 2 decimal places)
            self.assertIn(
                f'<div class="alert alert-success" role="alert">{CurrencyCodes().get_symbol("USD")} 20.00</div>', html)

        # same as the above test, but ensures that we will get the same result if the amount entered already has 2 decimal places
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'USD', 'convertTo': 'USD', 'amount': '20.00'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            # tests that the status code of the response after following the redirect is 200 (ok)
            self.assertEqual(res.status_code, 200)

            # tests that an appropriate flash is shown after the redirect is followed
            self.assertIn(
                f'<div class="alert alert-success" role="alert">{CurrencyCodes().get_symbol("USD")} 20.00</div>', html)

        # tests that the 'convertTo' currency symbol preceeds the new amount
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'USD', 'convertTo': 'INR', 'amount': '10'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            # tests that the status code of the response after following the redirect is 200 (ok)
            self.assertEqual(res.status_code, 200)

            # tests that an appropriate flash is shown after the redirect is followed
            self.assertIn(
                f'<div class="alert alert-success" role="alert">{CurrencyCodes().get_symbol("INR")} 734.51</div>', html)

    # tests for different circumstances in which the converstion is unsuccessful
    def test_unsuccessful_conversion(self):

        # tests that the correct is flash is shown when the 'convertFrom' value is not a valid code
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'ZZZ', 'convertTo': 'USD', 'amount': '100'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertIn(
                '<div class="alert alert-danger" role="alert">Not a valid code: ZZZ</div>', html)

        # tests that the correct is flash is shown when the 'convertTo' value is not a valid code
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'QQQ', 'convertTo': 'SSS', 'amount': '100'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertIn(
                '<div class="alert alert-danger" role="alert">Not a valid code: QQQ</div>', html)
            self.assertIn(
                '<div class="alert alert-danger" role="alert">Not a valid code: SSS</div>', html)

        # tests that the correct is flash is shown when the 'amount' value is not a number
        with app.test_client() as client:
            res = client.post(
                '/conversion', data={'convertFrom': 'USD', 'convertTo': 'JPY', 'amount': 'hello'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertIn(
                '<div class="alert alert-danger" role="alert">Not a valid amount: hello</div>', html)

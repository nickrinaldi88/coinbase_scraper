import dotenv
import selenium
import coinbase
import requests
from coinbase.wallet.client import Client
from dotenv import load_dotenv
import os
import sys
from twilio.rest import Client as twilioClient

sys.path.insert(0, os.environ['USERPROFILE'])

dotenv_path = os.environ['USERPROFILE'] + '\prod.env'
load_dotenv(dotenv_path, override=True)

# SET UP ENV VARIABLES

# COIN BASE

api_key = os.getenv('coinbase_api_key')
api_secret = os.getenv('coinbase_api_secret')

# TWILIO

account_sid = os.getenv('twilio_account_sid')
auth_token = os.getenv('twilio_auth_token')
twilio_number = os.getenv('twilio_number')

# Clients

coinbase_client = Client(api_key, api_secret)
twilio_client = twilioClient(account_sid, auth_token)

# user = coinbase_client.get_current_user()
accounts = coinbase_client.get_accounts()
currencies = coinbase_client.get_currencies()
# print(currencies)  # print(accounts)
# stop

# get_sell_price = client.get_sell_price()
# print(get_sell_price)


class Price:

    def __init__(self, accounts):
        self.accounts = accounts

    def get_current_price(self, ticker):

        for coin in accounts['data']:
            if coin['currency'] == ticker:
                value = "$" + str(coin['native_balance']['amount'])

        self.value = value

        return self.value

    def send_notification(self):

        price = self.get_current_price('LRC')

        self.message = twilioClient.messages.create(
            body='The price of your portfolio is currently: ' + str(price),
            from_=twilio_number,
            to='+8458250826')

        # set up twilio, to end notification when price is below certain amount

    def execute_trade(self):

        pass

        # based on SMS response, method executes trade


if __name__ == "__main__":

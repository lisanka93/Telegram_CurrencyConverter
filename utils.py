import requests
from config import *
import pandas as pd

currency_df = pd.read_csv("physical_currency_list.csv")
digital_df = pd.read_csv("digital_currency_list.csv")
physical_currency_list = currency_df.currency_code.tolist()
digital_currency_list = digital_df.currency_code.tolist()
currency_list = digital_currency_list + physical_currency_list


#helperfunction

def fmtpairs(mylist):
    """
    printing out currencies with country name and flag
    """

    pairs = zip(mylist[::2],mylist[1::2])
    return '\n'.join('\t \t'.join(i) for i in pairs)



class CurrencyException(Exception):
    pass


class CurrencyConverter:

    @staticmethod
    def convert(message):

        bug = False   #api has bug so need to fix it manually

        tokens = message.split()
        if len(tokens) != 3:
            raise CurrencyException("invalid input, please provide 2 currencies and the amount you want to convert")

        if tokens[0].upper() not in currency_list or tokens[1].upper() not in currency_list:
            raise CurrencyException("sorry but we dont support these currencies")
        try:
            money_amount = float(tokens[2])
        except ValueError:
            raise CurrencyException("please provide a valid money amount")

        curr1 = tokens[0].upper()
        curr2 = tokens[1].upper()
        amount = tokens[2]

        """
        The API has a bug and doesnt convert physical to crypto
        """

        if curr1 in physical_currency_list and curr2 in digital_currency_list:
            temp = curr1
            curr1 = curr2
            curr2 = temp
            bug = True

        querystring = {"from_currency":"","function":"CURRENCY_EXCHANGE_RATE","to_currency":""}
        querystring["from_currency"] = curr1
        querystring["to_currency"] =curr2

        response = requests.request("GET", url, headers=headers, params=querystring)
        r = response.json()
        rate = r["Realtime Currency Exchange Rate"]['5. Exchange Rate']

        if bug == True:

            new_amount =  (1/float(rate)) *float(amount)   #reverse exchange rate
            new_amount = round(new_amount,5)

            bot_response = f"{amount} {curr2} are {new_amount} {curr1}"

        else:

            new_amount =  float(rate)*float(amount)
            new_amount = round(new_amount,5)

            bot_response = f"{amount} {curr1} are {new_amount} {curr2}"

        return bot_response

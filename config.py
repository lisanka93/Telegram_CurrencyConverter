from keys import *

API_KEY =  telegramAPI_key

#rapidAPI
headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

headers['x-rapidapi-key'] = rapidAPI_key

CONTENT_TYPES = [ "audio", "document", "photo", "stricker", "video", "video_note", "voice", "location", "contact"]

PCURRENCIES = ["π¬π§ Pound Sterling", "GBP", "πͺπΊ Euro", "EUR", "πΊπΈ US Dollar", "USD", "π¨π³ Chinese Yuan", "CNY", "π―π΅ Japanese Yen", "JPY", "π΅π± Polish Zloty", "PLN", "π·πΊ Russian Ruble", "RUB", "π¨π­ Swiss Franc", "CHF", "πΊπ¦ Ukraininan Hryvnia", "UAH"]

DCURRENCIES = ["Bitcoin", "BTC", "Ethereum", "ETH", "Litecoin", "LTC", "Tether", "USDT", "Binance Coin", "BNB", "Doge Coin", "DOGE", "Solana", "SOL", "Cardano", "ADA", "Polygon", "MATIC"]


url = "https://alpha-vantage.p.rapidapi.com/query"

****************************** FOR SKILLFACTORY MENTOR ****************************

The bot is currently live on telegram! It is called @sf_cc_bot - check it out!




# Telegram Digital & Physical Currency Converter

Telegram Bot using RapidAPI Alpha Vantage to get real time currency exchange rates (digital and physical). It supports English and Russian.

### In order to create a local server for the bot on your *local machine*
- (1) make sure to create a bot instance on telegram and get an API key
- (2) create an account on rapidapi and check out the following documentation https://rapidapi.com/alphavantage/api/alpha-vantage/
- (3) store the telegram bot API key and the rapid-api key in a keys.py file in the same directory (which will be ignored if you ever push your code to git) - never leave keys in your public code!


### In order to deploy your bot on *Digital Ocean*
- (1) create an account https://www.digitalocean.com (it will cost you 5$)
- (2) create a droplet
- (3) open a console or ssh into the server via terminal (if using linux or mac) and clone this repository
- (4) create the keys.py file
- (5) run the bot via screen (to keep it running once you close the console)


TODO:
- store user_id in redis database and not python dictionary






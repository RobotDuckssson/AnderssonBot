# AnderssonBot
This small app fetches data from my solar panels and current weather.
The app Tweets information on its own Twitter account.
This app will probably by automated some time in the future.

The app uses a config file to get api keys and other private data.

For Twitter it uses the Tweepy API. 
pip install tweepy

The solar panel data is fetched from my Solar Edge account via the provided API: 
https://monitoringapi.solaredge.com

The weather forecast is collected from Open Weather Map: 
https://api.openweathermap.org/

Add the following file:
config.py

```python
#!/usr/bin/python

###############################
# settings                    #
###############################

# Solar Edge API keys
solar_api_key = "YOUR_API_KEY" 
solar_site_id = "YOUR_SITE_ID"

# Twitter app keys
TWEET__CONSUMER_API_KEY ="YOUR_CONSUMER_APPI_KEY"
TWEET__CONSUMER_API_SECRET = "YOUR_CONSUMER_API_SECRET"
TWEET__ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
TWEET__ACCESS_TOKEN_SECRET = "YOUR_TOKEN_SECRET"

# Weather Object
weather_api_key = "YOUR_API_KEY"
```

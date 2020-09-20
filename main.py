import tweepy
import datetime
import time
from TweetConfig import create_api
from Weather import forecast
from SolarInfo import SolarInfo
from config import print_out


def main():
    # Classes
    weather_forecast = forecast()
    solar = SolarInfo()

    celsius = u'\u2103'
    daily_tweet = (f"Energy produced so far today: {solar.get_current_energy_production()}. Temperature in Lerberget at the moment: {weather_forecast.temprature()}{celsius}  and {weather_forecast.sky_formation()}")
    monthly_tweet = (f"Energy produced last month: {solar.get_last_month_energy_production() }.")
    savings_tweet = (f"Total CO2 saved: {solar.get_total_co2()}kg")
    lifetime_tweet = (f"Energy produced since October 1st 2019: {solar.get_lifetime_energy_production()}")

    # print outs    
    if print_out : print(daily_tweet)
    if datetime.datetime.today().day == 27:
        if print_out : print(monthly_tweet)

    if print_out : print(savings_tweet)
    if print_out : print(lifetime_tweet) 
    
    '''
    api = create_api()
    api.update_status(daily_tweet)

    api = create_api()
    api.update_status(monthly_tweet)

    api = create_api()
    api.update_status(savings_tweet)
    '''
    '''
    api = create_api()
    api.update_status(lifetime_tweet)
    '''
    
if __name__ == "__main__":
    main()
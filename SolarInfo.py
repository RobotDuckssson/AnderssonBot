#!/usr/bin/python

import requests
import datetime
import time
from config import solar_api_key
from config import solar_site_id


class SolarInfo(object):
        
    def get_last_month_energy_production(self):
        now = time.localtime()
        last = datetime.date(now.tm_year, now.tm_mon, 1) - datetime.timedelta(1)
        first = last.replace(day=1)

        json_link = f"https://monitoringapi.solaredge.com/site/{solar_site_id}/timeFrameEnergy?startDate={first}&endDate={last}&api_key={solar_api_key}"
        my_json = requests.get(json_link).json()
        return self.__change_value(format(int(my_json["timeFrameEnergy"]["energy"]), "4,d"))


    def get_current_energy_production(self):
        json_link = f"https://monitoringapi.solaredge.com/site/{solar_site_id}/overview.json?api_key={solar_api_key}"
        my_json = requests.get(json_link).json()
        return self.__change_value(format(int(my_json["overview"]["lastDayData"]["energy"]), "4,d"))

    def get_lifetime_energy_production(self):
        json_link = f"https://monitoringapi.solaredge.com/site/{solar_site_id}/overview.json?api_key={solar_api_key}"
        my_json = requests.get(json_link).json()
        return self.__change_value(format(int(my_json["overview"]["lifeTimeData"]["energy"]), "4,d"))

    def get_total_co2(self):
        json_link = f"https://monitoringapi.solaredge.com/site/{solar_site_id}/envBenefits?systemUnits=Metrics&api_key={solar_api_key}"
        my_json = requests.get(json_link).json()
        return round(my_json["envBenefits"]["gasEmissionSaved"]["co2"])


    def __change_value(self, energy_kwh):
        energy_kwh = energy_kwh.lstrip()
        kWh_to_show = ""
        
        if len(energy_kwh) > 3:
            str_split = energy_kwh.split(",")
            str_first = str(int(str_split[0]))
            str_second = str(round(int(str_split[1]), -2))
            
            kWh_to_show = f"{str_first},{str_second[0]} "

            if len(energy_kwh) > 6:
                kWh_to_show += "MWh"
            else :
                kWh_to_show += "kWh"

        else :
            kWh_to_show = f"{energy_kwh } Wh" 
        return kWh_to_show
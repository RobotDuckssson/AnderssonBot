#!/usr/bin/python

class WeatherObject:

    def __init__(self, temp, temp_max, temp_min, sky):
        self.temp = temp
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.sky = sky
  

    def temprature(self):
        return round(self.temp, 1)

    def temprature_min(self):
        return round(self.temp_min, 1)

    def temprature_max(self):
        return round(self.temp_max, 1)

    def sky_formation(self):
        return self.sky
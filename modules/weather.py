#!/usr/bin/python

import ConfigParser
import time
import feedparser
import os

from core.voicesynthetizer import VoiceSynthetizer

class Weather(object):

    def __init__(self, voicesynthetizer):

        self.conf = ConfigParser.ConfigParser()
        self.path = "configuration/general.configuration"
        self.conf.read(self.path)

        self.speaker = voicesynthetizer

    def parser(self):

        cityid = self.conf.get("weather", "cityid")
        self.url = "http://weather.yahooapis.com/forecastrss?w=" + cityid  + "&u=c"

        data = feedparser.parse(self.url)

        # {'city': u'Guadalajara', 'region': u'JA', 'country': u'Mexico'}
        # {'pressure': u'1015.92', 'rising': u'1', 'visibility': u'12.87', 'humidity': u'46'}
        # {'sunset': u'6:57 pm', 'sunrise': u'7:11 am'}
        
        self.location = data.feed.yweather_location
        self.atmosphere = data.feed.yweather_atmosphere
        self.astronomy = data.feed.yweather_astronomy

        sunrise=self.astronomy['sunrise']
        sunset=self.astronomy['sunset']

        summary=data.entries[0].summary
        temp=summary.split("High: ")
        temp=temp[1].split(" Low: ")
        self.high=temp[0]
        self.low=temp[1].split("<br />")[0]
        return

    def report(self):
	try:
                self.parser()
                self.speaker.speechit("Reporte del clima en la ciudad de " + self.location['city'] + ", " + self.location['country'])
                self.speaker.speechit("Temperatura maxima, " + self.high + " grados centigrados")
                self.speaker.speechit("Temperatura minima, " + self.low + " grados centigrados")
                self.speaker.speechit("Humedad, " + self.atmosphere['humidity'] + " por ciento")
                self.speaker.speechit("El Sol se oculta a las " + self.astronomy['sunset'].replace(":", " ") + " de la tarde")
	except:
                return

if __name__ == '__main__':

    test = Weather("temp")
    test.report()

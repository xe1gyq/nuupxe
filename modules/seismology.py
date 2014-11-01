#!/usr/bin/python

import re

from core.twitterc import TwitterC

state = {'CHIS': 'Chiapas', 'NL': 'Nuevo Leon', 'VER': 'Veracruz',
	'JAL': 'Jalisco', 'OAX': 'Oaxaca'}

class Seismology(object):

    def __init__(self, voicesynthetizer):

	self.twitterc = TwitterC()

        self.voicesynthetizer = voicesynthetizer

    def SismologicoMX(self):
        print '[Cancun] Seismology'
        self.voicesynthetizer.speechit('Servicio Sismologico Nacional, Universidad Nacional Autonoma de Mexico')

        tstatus = self.twitterc.timeline('SismologicoMX', 3)
        sismo = 'False'
        for status in tstatus:
            if status.text.partition(' ')[0] == 'SISMO':
                status.text = status.text.replace("Loc", "Localizacion")
                status.text = status.text.replace("CD", "Ciudad")
                status.text = status.text.replace("Lat", "Latitud")
                status.text = status.text.replace("Lon", "Longitud")
                status.text = status.text.replace("Pf", "Profundidad")
                pattern = re.compile(r'\b(' + '|'.join(state.keys()) + r')\b')
                status.text = pattern.sub(lambda x: state[x.group()], status.text)
                self.voicesynthetizer.speechit(status.text)
                sismo = 'True'
        if sismo == 'False':
            self.voicesynthetizer.speechit("No se encontraron sismos en las ultimas horas")

if __name__ == '__main__':

    mytest = SeismologyC("google")
    mytest.sismologicomx()
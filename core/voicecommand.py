#!/usr/bin/python

import commands

from core.speechrecognition import SpeechRecognition
from core.pushtotalk import PushToTalk

class VoiceCommand(object):

    def __init__(self, voicesynthetizer):

	self.output = ""
        self.agent = "google"
        self.audiofilewav = "voicecommand.wav"
        self.audiofilewavcompand = "voicecommandc.wav"
        self.audiofilewavnoise = "voicecommandn.wav"
        self.audiofileflac = "voicecommand.flac"
        self.voicesynthetizer = voicesynthetizer
        self.pushtotalk = PushToTalk()
        self.speechrecognition = SpeechRecognition()

    def __del__(self):

        status, output = commands.getstatusoutput("rm " + self.audiofilewav)
        status, output = commands.getstatusoutput("rm " + self.audiofileflac)

    def record(self, seconds):

        print '[Cancun] Voice Command Record'

        if self.agent == 'nexiwave':
                status, output = commands.getstatusoutput("arecord -vv -f cd -d " + seconds + " " + self.audiofilewav)
        elif self.agent == 'google':
                status, output = commands.getstatusoutput("arecord -d " + seconds + " -t wav -f S16_LE -r48000 " + self.audiofilewav)
                #status, output = commands.getstatusoutput("sox " + self.audiofilewav + " " + self.audiofilewavcompand + " compand 0.02,0.20 5:-60,-40,-10 -5 -90 0.1")
                #status, output = commands.getstatusoutput("sox " + self.audiofilewav + " -n remix 1 trim 0 1 noiseprof noise.prof")
                #status, output = commands.getstatusoutput("sox " + self.audiofilewav + " " + self.audiofilewavnoise + " remix 1 noisered noise.prof")
                status, output = commands.getstatusoutput("flac -f -o " + self.audiofileflac + " --channels=1 --sample-rate=48000 " + self.audiofilewav)

    def decode(self, speech):

        print '[Cancun] Voice Command Decode'

	if speech == 'True':
                self.voicesynthetizer.speechit("Estamos procesando tu respuesta")
                self.pushtotalk.openport()
                status, output = commands.getstatusoutput("aplay " + self.audiofilewav)
                #status, output = commands.getstatusoutput("aplay " + self.audiofilewavcompand)
                #status, output = commands.getstatusoutput("aplay " + self.audiofilewavnoise)
                self.pushtotalk.closeport()

        if self.agent == 'nexiwave':
                self.output = self.speechrecognition.nexiwave(self.audiofilewav)
                print self.output
        elif self.agent == 'google':
                self.output = self.speechrecognition.google(self.audiofileflac)
                print self.output

        return self.output

if __name__ == '__main__':

    mytest = Command()
    mytest.record()
    mytest.play()

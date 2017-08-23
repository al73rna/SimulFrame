__author__ = 'mohammadreza'
from main import *

class xa (Agent):
    def behavior(self,signal,args=None):

        signal.attributes["yes ?"] = "yes"
        return signal
class ya (Agent):
    def behavior(self,signal,args=None):

        signal.attributes["yes ?"] = "no"
        return signal
class za (Agent):
    def behavior(self,signal,args=None):
        return signal





x = xa("ali")
y = ya("jj")
z = za("pp")

creator = Emitter()
recorder = Receiver()

class en1 (Environment):
    def setEnvironment(self):

        creator.sendTo(x)
        x.sendTo(y)
        y.sendTo(z)
        z.sendTo(recorder)
        creator.busyTime=0
        x.setBusyTime(4)
        y.setBusyTime(1)
        z.setBusyTime(3)
    def getStat(self):
        print("terminal signals")
        for i in self.receivers :
            print(len(i.receivedSingals))
            for j in i.receivedSingals :
                print(j.attributes["yes ?"])
        print("agents process delays")
        for j in self.agents :
            print(j.processDelay)
        print("emitter process delays")
        for j in self.emitters :
            print(j.processDelay)


en = en1()
en.agents = [x,y,z]
en.emitters = [creator]
en.receivers = [recorder]

en.start()
en.getStat()

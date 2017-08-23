__author__ = 'mohammadreza'
from main import *
import random



#rn =  RNG.RandomNumberGenerator()

class c(Creator):
    def action(self,e):
        e.atts["rnd"] = random.randrange(0,100)
        return e
crt = c(Signal,"creator1")
crt.setBusyTime(0)


dsp = Disposer("dsp1")


class p1(Agent):
    def behavior(self,ent):
        ent.atts["1"] = "self"
        return ent
selfserv = p1("selfservice")
selfserv.setBusyTime(0)


class p2(Agent):
    def behavior(self,ent):
        self.instances -= 1
        if (self.instances) == 1 :
            self.instances = 3
        ent.atts["1"] = "sell"
        return ent
seller = p2("sellers")
seller.instances = 3
seller.setBusyTime(0)
seller.MAXUTIL = 60

class p3(Agent):
    def behavior(self,ent):
        ent.atts["2"] = "cash"
        return ent
cashier = p3("cashier")
cashier.setBusyTime(0)
cashier.MAXUTIL = 90

class dc(Decide):
    def condition(self,t):
        return (t.atts["rnd"]>40)
decider = dc()

RESULTS = []
TRES = []
class enviro(Environment):
    def setEnv(self):
        crt.sendTo(decider)
        decider.sendtoF(selfserv)
        decider.sendtoT(seller)
        selfserv.sendTo(cashier)
        seller.sendTo(cashier)
        cashier.sendTo(dsp)
        self.addAgent([seller,cashier,selfserv,decider,crt,dsp])

    def getStat(self):
        sell = 0
        cash = 0

        for i in self.PQ :
            if isinstance(i,Disposer):
                if len(i.innerQ)>0:
                    for j in i.innerQ :
                        if(j.atts["1"]) == "sell" :
                            sell+=1
                        if(j.atts["2"]) == "cash" :
                            cash+=1
        print(sell/seller.MAXUTIL)
        print(cash/cashier.MAXUTIL)



myEnnviro = enviro()
myEnnviro.setNumberOfTrials(80)
myEnnviro.start()
myEnnviro.getStat()
print(len(RESULTS))

print()
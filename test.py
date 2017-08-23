__author__ = 'mohammadreza'
from main import *
import random



#rn =  RNG.RandomNumberGenerator()

class c(Creator):
    def action(self,e):
        e.atts["total"] = 90
        return e
crt = c(Entity,"creator1")
crt.setBusyTime(0)


dsp = Disposer("dsp1")


class p1(Process):
    def action(self,ent):
        day = self.env.enVars["day"]
        rnd = random.randrange(0,100)
        tmp = None
        if day == "good":
            if 0<rnd<10 :
                tmp = 60
            elif 10<rnd<50 :
                tmp = 70
            else:
                tmp = 100
        elif day == "fair":
            if 0<rnd<10 :
                tmp = 40
            elif 10<rnd<50 :
                tmp = 50
            else:
                tmp = 60
        else:
            if 0<rnd<10 :
                tmp = 20
            elif 10<rnd<50 :
                tmp = 30
            else:
                tmp = 40
        ent.atts["demand"] = tmp
        ent.atts["day"] = day
        return ent
seller = p1("seller")
seller.setBusyTime(0)


class p2(Process):
    def action(self,ent):
        ent.atts["scraped"] = ent.atts["total"]-ent.atts["demand"]
        ent.atts["shortage"] = 0
        return ent
scraper = p2("scraper")
scraper.setBusyTime(0)

class p3(Process):
    def action(self,ent):
        ent.atts["scraped"] = 0
        ent.atts["shortage"] = ent.atts["demand"] - ent.atts["total"]
        return ent
lostchecker = p3("lostchecker")
lostchecker.setBusyTime(0)


class dc(Decide):
    def condition(self,t):
        return (t.atts["total"] - t.atts["demand"] < 0)
decider = dc()

RESULTS = []
TRES = []
class enviro(Environment):
    def setEnv(self):
        crt.sendTo(seller)
        seller.sendTo(decider)
        seller.env = self
        decider.sendtoF(scraper)
        decider.sendtoT(lostchecker)
        scraper.sendTo(dsp)
        lostchecker.sendTo(dsp)
        self.addProcess([seller,scraper,lostchecker,decider,crt,dsp])
    def action(self):
        rnd = random.randrange(1,100)
        if 1<rnd<35 :
            self.addVar("day","good")
        elif 35<rnd<80 :
            self.addVar("day","fair")
        else :
            self.addVar("day","poor")
    def getStat(self):
        n = 0
        total_salary = 0
        total_lost = 0
        total_scrape = 0
        for i in self.PQ :
            if isinstance(i,Disposer):
                for j in i.innerQ :
                    RESULTS.append(j.atts)
        for d in RESULTS :
            n += 1
            if d["total"] - d["demand"] > 0 :
                d["revenue"] =( d["demand"] ) * 0.17
                d["lostprofit"] = 0


            else:
                d["revenue"] = d["total"] * 0.17
                d["lostprofit"] = (d["demand"] - d["total"]) * 0.17
            if d["scraped"] != 0 :
                d["salvage"] = d["scraped"] * 0.05
            else:
                d["salvage"] = 0
            d["profit"] = d["revenue"] + d["salvage"] - d["lostprofit"]

            total_salary += d["revenue"]/n
            total_lost += d["lostprofit"]/n
            total_scrape += d["salvage"]/n
            d["AVG REV"] = total_salary
            d["AVG LOSS"] = total_lost
            d["AVG SLVG"] = total_scrape


myEnnviro = enviro()
myEnnviro.setNumberOfTrials(10)
myEnnviro.start()
myEnnviro.getStat()
print(len(RESULTS))

print()
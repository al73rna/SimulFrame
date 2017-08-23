__author__ = 'mohammadreza'
from main import *
import matplotlib.pyplot as plt
import random
from rp.report import *

class cell(ActiveAgent):
    def behavior(self,signal,args=None):
        #print(len(self.pendingSingals),len(self.signalReceivers))

        # if self.firstTime :
        #     print("r")
        #     p = Signal()
        #     p.attributes["state"] = self.attributes["state"]
        #     self.firstTime=False
        #     if self.attributes["state"]=="sick":
        #         self.attributes["ttl"]=3
        #     return p

        sickNeighbours = 0
        if len(signal)==0 :
            self.attributes["ttl"]=3
            self.attributes["t"] = self.attributes["ttl"]
        else:
            for s in signal :
                if s.attributes["state"] == "sick" :
                    sickNeighbours +=1
        print(self.attributes["ttl"])
        diseaseChance = random.randrange(100)

        if self.attributes["state"]=="alive" and diseaseChance<sickNeighbours*12:
            self.attributes["state"] = "sick"
            self.attributes["ttl"] = random.randrange(2,5)
            self.attributes["t"] = self.attributes["ttl"]
        elif self.attributes["state"]=="sick":
            if self.attributes["ttl"] <= 0 :
                rn= random.randrange(100)
                if rn>70:
                    self.attributes["state"]="dead"
                else:
                    self.attributes["state"]="immune"
            self.attributes["ttl"]-=1

        p = Signal()
        p.attributes["state"] = self.attributes["state"]
        #print(p.attributes["state"])
        return p

def makeGridNetwork(X,Y):
    network = []

    for j in range(Y):
        row = []
        for i in range(X):
            t = cell("")
            t.attributes["state"]="alive"
            t.setBusyTime(0)
            row.append(t)
        network.append(row)


    for row_index in range(Y) :
        for cell_index in range(X) :
            if (0<row_index<Y-1) and (0<cell_index<X-1):
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index-1])
            #========================================================================== +

            elif row_index == 0 and cell_index ==0 :
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index+1])

            elif row_index == 0 and cell_index ==X-1 :
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index-1])

            elif row_index == Y-1 and cell_index ==0 :
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index+1])

            elif row_index == Y-1 and cell_index ==X-1:
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index-1])
            #========================================================================== +

            elif row_index == 0 :
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index-1])

            elif row_index == Y-1:
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index+1])

            elif cell_index == 0 :
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index+1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index+1])

            elif cell_index == X-1 :
                network[row_index][cell_index].signalReceivers.append(network[row_index][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index])
                network[row_index][cell_index].signalReceivers.append(network[row_index-1][cell_index-1])
                network[row_index][cell_index].signalReceivers.append(network[row_index+1][cell_index-1])


    return network

tt = makeGridNetwork(25,25)


tt[6][6].attributes["state"]="sick"
tt[5][5].attributes["state"]="sick"
tt[6][7].attributes["state"]="sick"
tt[7][5].attributes["state"]="alive"
reporter = Reports_and_Results()
class env(Environment):
    def getStat(self):
        dead=0
        alive=0
        immune=0
        ttl ={}
        for i in self.agents:
            if i.attributes["state"]=="dead":
                dead+=1
            elif i.attributes["state"]=="immune":
                immune+=1
            elif i.attributes["state"]=="alive":
                alive+=1
            if "t" in i.attributes.keys() :
                if(i.attributes["t"] in ttl.keys()):
                    ttl[i.attributes["t"]]+= 1
                else :
                    ttl[i.attributes["t"]] = 1
        label=["immune","dead","alive"]
        values=[immune,dead,alive]
        reporter.add_text("THE DISEASE SPREAD SIMULATION")

        reporter.add_text("pie CHART")
        reporter.add_chart("pie",label,values)

        reporter.add_text("line CHART")
        reporter.add_chart("line",label,values)

        l = []
        v = [[]]
        vt=[]
        for i in ttl.keys():
            l.append(str(i))
        for i in ttl.values():
            v[0].append(str(i))
            vt.append(int(i))
        reporter.add_table(l, v)

        reporter.add_text("Bar CHART")
        reporter.add_chart("bar",l,vt)

        reporter.add_text("Area CHART")
        reporter.add_chart("area",l,vt)

        reporter.generate_reports_and_results()
    def update(self):
        #time.sleep(0.3)
        plt.clf()
        #plt.pause(0.00001)
        drawTable =[]
        for i in range(len(tt)):
            row = []
            for j in range(len(tt[i])) :
                if tt[i][j].attributes["state"]=="alive":
                    plt.scatter(j, i , s=256 , color="green")
                elif tt[i][j].attributes["state"]=="dead":
                    plt.scatter(j, i, s=256 , color="black")
                elif tt[i][j].attributes["state"]=="sick":
                    plt.scatter(j, i, s=256 , color="red")
                elif tt[i][j].attributes["state"]=="immune":
                    plt.scatter(j, i, s=256 , color="blue")
            drawTable.append(row)
        plt.draw()
        #plt.pause(0.0000001)


table = env()
table.agents = []
table.clockLimit = 40
axis = [0, len(tt)+2, 0, len(tt[0])+2]
plt.axis(axis)
plt.ion()
plt.show()
mng = plt.get_current_fig_manager()
mng.resize(800,800)


for i in tt :
    for j in i :
        table.agents.append(j)

table.start()
table.getStat()

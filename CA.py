__author__ = 'mohammadreza'
from main import *
import matplotlib.pyplot as plt
import gc

class cell(ActiveAgent):
    def behavior(self,signal,args=None):
        #print(len(self.pendingSingals),len(self.signalReceivers))

        #if self.firstTime :
        aliveNeighbours = 0
        r = ""
        if len(signal)==0 :
            aliveNeighbours = 2
        else:
            for s in signal :
                r+=str(s.attributes["state"])
                if s.attributes["state"] == "alive" :
                    aliveNeighbours +=1
                if s.attributes["state"] == "dead" :
                    pass

        #print(aliveNeighbours,"nb",r)
        if ((aliveNeighbours < 2) or (aliveNeighbours>3)) and self.attributes["state"]=="alive":
            self.attributes["state"] = "dead"
        elif(aliveNeighbours==2 or aliveNeighbours==3) and (self.attributes["state"] == "alive"):
            self.attributes["state"] = "alive"
        elif (aliveNeighbours==3) and (self.attributes["state"] == "dead") :
            self.attributes["state"] = "alive"

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
            t.attributes["state"]="dead"
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

tt = makeGridNetwork(15,15)


tt[6][6].attributes["state"]="alive"
tt[5][5].attributes["state"]="alive"
tt[6][7].attributes["state"]="alive"
tt[7][5].attributes["state"]="alive"
class env(Environment):
    def getStat(self):
        pass
    def update(self):

        plt.clf()

        drawTable =[]
        for i in range(len(tt)):
            row = []
            for j in range(len(tt[i])) :
                if tt[i][j].attributes["state"]=="alive":
                    plt.scatter(j, i , s=256 , color="green")
                elif tt[i][j].attributes["state"]=="dead":
                    plt.scatter(j, i, s=256 , color="pink")
            drawTable.append(row)
        plt.draw()
        plt.pause(0.0000001)


table = env()
table.agents = []
table.clockLimit = 30
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


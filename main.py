__author__ = 'mohammadreza'




class Environment :
    def __init__(self):
        self.agents = []
        self.emitters = []
        self.receivers = []
        self.CLOCK = 0
        self.environmentVariables = {}
        #---------
        self.setEnvironment()
        self.clockLimit = 30

    def addVariable(self,_key,_value):
        self.environmentVariables[_key] = _value
    def update(self):
        pass
    def setclockLimit(self,x):
        self.clockLimit = x
    def start(self):
        while (self.CLOCK < self.clockLimit) :
            # set the environment :
            self.update()

            # get the current signals :
            #-------------------------

            # agents

            for agent in self.agents :
                if agent.remainingTime <= 0 :
                    agent.getSignals()
                    tttt=""
                    for i in agent.pendingSingals :
                        tttt+=str(i.attributes["state"]) + "-"
                    #print(tttt)


            # receivers
            for receiver in self.receivers :
                receiver.getSignals()

            # set the next state :
            #-------------------------

            # agents
            for agent in self.agents :
                if agent.remainingTime<=0 :
                    agent.update()

                else :
                    for i in  agent.signalQueue :
                        t = i.queueDelay
                        if agent.name in t.keys():
                            t[agent.name] +=1
                        else:
                            t[agent.name] = 1
                agent.remainingTime -= 1
            # emitters
            for emitter in self.emitters:

                emitter.remainingTime -= 1
                if emitter.remainingTime <= 0 :
                    #print(self.CLOCK,"EMITTERs WORK :")
                    emitter.update()


            self.CLOCK += 1


    def setEnvironment(self):
        pass
    def envEvents(self):
        pass
    def addAgent(self,x):
        self.agents.extend(x)
    def getStat(self):
        pass



class Signal :
    def __init__(self):
        self.attributes = {}
        self.queueDelay = {}
    def ret(self):
        e = Signal()
        e.attributes = self.attributes.copy()
        e.queueDelay = self.queueDelay.copy()
        return e



class Agent :
    def __init__(self,_name,_environment = None):
        self.name = _name
        self.signalQueue = []
        self.signalReceivers = []
        self.firstTime = True
        self.busyTime = 4
        self.remainingTime = 0
        self.processDelay = {}
        self.environment = _environment
        self.pendingSingals = []
        self.signalCount = 1

        self.attributes={}
    def sendTo(self,_destination):
        self.signalReceivers.append(_destination)
    def getBusy(self):
        self.remainingTime = self.busyTime
        if self.busyTime in self.processDelay.keys() :
            self.processDelay[self.busyTime] += 1
        else:
            self.processDelay[self.busyTime] = 1

    def setBusyTime(self,x):
        self.busyTime = x

    def update(self):
        processedSignals = []
        if len(self.pendingSingals) != 0 :
            #print(self.name)
            for signal in self.pendingSingals :
                processedSignals.append(self.behavior(signal).ret())
            self.pendingSingals = []
            for receiver in self.signalReceivers :
                receiver.signalQueue.extend(processedSignals)
            self.getBusy()

    def behavior(self,signal,args=None):
        return (signal)
            
    def getSignals(self):
        if len(self.signalQueue)!= 0 :
            if self.signalCount == "inf":
                self.pendingSingals = self.signalQueue
                self.signalQueue = []
            else:
                for i in range(int(self.signalCount)):
                    t = self.signalQueue.pop(0)
                    self.pendingSingals.append(t)
class ActiveAgent(Agent):
    def update(self):
        processedSignals = []
        #print(self.name)
        processedSignals.append(self.behavior(self.pendingSingals))
        self.pendingSingals = []
        for receiver in self.signalReceivers :
            receiver.signalQueue.extend(processedSignals)

        self.getBusy()

    def getSignals(self):
        if len(self.signalQueue)!= 0 :
            self.pendingSingals = self.signalQueue
            self.signalQueue = []

# the receiver class
class Receiver:
    def __init__(self):
        self.signalQueue = []
        self.receivedSingals = []
    def getSignals(self):
        if len(self.signalQueue)!= 0 :
            self.receivedSingals.extend(self.signalQueue)
            self.signalQueue = []

# the emitter class
class Emitter :
    def __init__(self):
        self.remainingTime = 0
        self.busyTime = 10
        self.signalReceivers = []
        self.processDelay = {}
        self.count = 1

    def getBusy(self):
        self.remainingTime = self.busyTime
        if self.busyTime in self.processDelay.keys() :
            self.processDelay[self.busyTime] += 1
        else:
            self.processDelay[self.busyTime] = 1

    def setBusyTime(self,x):
        self.busyTime = x

    def update(self):
        processedSignals = []
        for i in range(self.count) :
            processedSignals.append(self.behavior().ret())

        for receiver in self.signalReceivers :
            receiver.signalQueue.extend(processedSignals)
        self.getBusy()

    def behavior(self,args=None):
        signal = Signal()
        signal.attributes["isOK"] = "yoloooo"
        return (signal)

    def sendTo(self,_destination):
        self.signalReceivers.append(_destination)


# 
# class Decide :
#     def __init__(self):
#         self.remainingTime = 0
#         self.signalQueue = []
#         self.sendToTrue = None
#         self.sendToFalse = None
#         self.name = "decide"
#         self.processDelay = "decide"
#     def condition(self,t):
#         return True
#     def sendtoT(self,dst):
#         self.sendToTrue = dst
#     def sendtoF(self,dst):
#         self.sendToFalse = dst
#     def update(self):
#         if len(self.signalQueue)>0:
#             t = self.signalQueue.pop(0)
#             if (self.condition(t)) :
#                 self.sendToTrue.signalQueue.append(t.ret())
#             else:
#                 self.sendToFalse.signalQueue.append(t.ret())




# from scipy.stats import bernoulli, binom, poisson, rv_discrete
#
# class RandomNumberGenerator:
#
#     def __init__(self):
#         pass
#
#     def Bernoulli(self, p, size=1):
#         return bernoulli.rvs(p, size=size)
#
#     def Binomial(self, n, p, size=1):
#         return binom.rvs(n, p, size=size)
#
#     def Poisson(self, mu, size=1):
#         return poisson.rvs(mu, size=size)
#
#     def Discrete(self, values, probabilities, size=1):
#         distribute = rv_discrete(values=(values, probabilities))
#         return distribute.rvs(size=size)


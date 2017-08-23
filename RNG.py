__author__ = 'mohammadreza'



from scipy.stats import bernoulli, binom, poisson, rv_discrete

class RandomNumberGenerator:

    def __init__(self):
        pass

    def Bernoulli(self, p, size=1):
        return bernoulli.rvs(p, size=size)

    def Binomial(self, n, p, size=1):
        return binom.rvs(n, p, size=size)

    def Poisson(self, mu, size=1):
        return poisson.rvs(mu, size=size)

    def Discrete(self, values, probabilities, size=1):
        distribute = rv_discrete(values=(values, probabilities))
        return distribute.rvs(size=size)

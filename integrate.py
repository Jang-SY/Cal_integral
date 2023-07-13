from scipy.integrate import quad
import numpy as np
from numpy import sqrt, pi
import math

def integrand(x):
    return np.exp(x**2)*(1+math.erf(x))


if __name__== "__main__":
    top = np.loadtxt("top.txt", dtype=np.double)
    bot = np.loadtxt("bot.txt", dtype=np.double)
    
    for i in range(290):
        I = quad(integrand, bot[i], top[i], limit=100000)
        answer = 0.004 + (0.001 * sqrt(pi) * I[0])
        print(1/answer)
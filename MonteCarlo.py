import numpy as np
import random 
import math

#n represents the dimension of the volume
#N represents the total number of points generated
#r represents the 'radius' of the volume
#P is a matrix of random vectors to be sampled
#M represents the total number of points inside the volume

def AnalyticVolume(r, n):
    if n%2 == 0:
        return ((math.pi**(n/2))/math.factorial(int(n/2)))*r**n
    else:
        return ((2*math.factorial(int((n-1)/2))*(4*math.pi)**((n-1)/2))/math.factorial(n))*r**n

n = 2
N = 100000
r = 2
P = np.random.rand(n,N)*r
M = 0

for i in range(N):
    M += (np.sum(np.square(P[:,i]))<r**2)

#Estimated Volume
V_e = (M/N) * (2*r)**n
print("Estimated Volume: ",V_e)

#Analytic Volume
V_a = AnalyticVolume(r,n)
print("Analytic Volume: ",V_a)

#Error
print("Percentage Error: ", (abs(V_a-V_e)/V_a)*100,"%")
def wallis(n):
    pi = 0.0   
    for i in range(1, n):
        numerator = 4 * (i ** 2)   #lim(m→∞) ∏((2 n**2)/((2(n**2))-1))
        denominator = numerator - 1
        x = float(numerator) / float(denominator)
        if (i == 1):
            pi = x
        else:
            pi *= x
    pi *= 2
    return pi

print(wallis(1000000))



import random
from math import sqrt
#the number of darts thrown
n= 200000000
def monte_carlo(n):
    point = 0
    
    for i in range(1, n+1):
        x = random.random()
        y = random.random()
        
        if sqrt(x**2 + y**2) <= 1:
            point += 1
    pi = 4*(point/n)
    return pi

print(monte_carlo(n))   



from PrimeC import *
import math

def PrimeLoop(l, m=math.inf):
    count = 0
    mi = max(l) + 1
    primelist = l

    try:
        while count < m+1:
            if PrimeC(mi, primelist):
                primelist.append(mi)
                count += 1

            mi += 1

    except KeyboardInterrupt:
        return primelist
    return primelist

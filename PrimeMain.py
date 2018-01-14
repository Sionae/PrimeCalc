from PrimeLoop import *
import os

os.chdir("C:/Users/samco/Desktop/Code/Maths/PrimeFinder")

def l2str(l):
    s = ""

    for elt in l:
        s += str(elt) + " "

    return s

def str2l(s):
    """Split returning integers"""
    l = s.split()
    splitedList = []

    for elt in l:
        splitedList.append(int(elt))

    return splitedList

with open("primes.txt", "r+") as f:
    data = f.readlines()

    if len(data) == 0:
        primelist = [2, 3, 5, 7, 9, 11, 13]
        data = [""]

    else:
        primelist = str2l(data[0])

    primelist = PrimeLoop(primelist, 100000)
    data[0] = l2str(primelist)
    f.writelines(data)

    print("Done")
    print("Total number of prime numbers : {}".format(len(primelist)))

#Security closing
f.close()

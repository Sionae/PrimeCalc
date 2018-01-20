from PrimeLoop import *
import os

os.chdir("C:\\Users\\samco\\Desktop\\Code\\Python\\PrimeCalc")

def l2str(l):
    s = ""

    for elt in l:
        s += str(elt) + " "

    return s

def delAncient(l, lengthi):
    count = 0
    while count < lengthi:
        del l[0]
        count += 1

    return l


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
        data.append("")

    else:
        primelist = str2l(data[0])



    lengthi = len(primelist)

    primelist = PrimeLoop(primelist, 1000)
    if lengthi != 7:
        primelist = delAncient(primelist, lengthi)
    data[0] = l2str(primelist)
    f.writelines(data)

    print("Done")
    print("Total number of prime numbers : {}".format(len(primelist)))
    print("Highest prime number : {}".format(primelist[-1]))

#Security closing
f.close()

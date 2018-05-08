import matplotlib.pyplot as plt
import numpy as np
import math

x, y = np.loadtxt('dataA.txt', delimiter=',', unpack=True)
x1, y1 = np.loadtxt('dataB.txt', delimiter=',', unpack=True)

sizeJ = x.shape[0] + x1.shape[0]
margin = np.zeros(sizeJ)

print "Masukkan persamaan garis : (w1x1 + w2x2 + b = 0)"
w1 = input("Masukkan nilai w1 : ")
w2 = input("Masukkan nilai w2 : ")
b = input("Masukkan nilai b : ")

def countMargin(w1, w2, b, x, y, x1, y1):
    for i in range(0, x.shape[0]):
        margin[i] = (w1*x[i] + w2*y[i] + b) / math.sqrt(w1**2 + w2**2)
    
    for j in range(0,x1.shape[0]):
        margin[j+x.shape[0]] = abs((w1*x1[j] + w2*y1[j] + b) * -1) / math.sqrt(w1**2 + w2**2)
    
    print margin
    print "Nilai margin = ", np.amin(margin)
    return

countMargin(w1, w2, b, x, y, x1, y1)

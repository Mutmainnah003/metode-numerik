# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:48:48 2020

@author: ASUS
"""


import math 
 
def f(x):     
    return math.exp(x) - 5*x**2 
 
a = 0 
b = 1 
e = 0.000001 
N = 100 
iterasi = 0 

print ("========================")
print (' c          f(c)')
print ("========================")


while True:
    iterasi +=1
    c=(a+b)/2
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
    print('{:7.5f}\t{:15.10f}'.format(c, f(c)))
    if abs(f(c))< e or iterasi >= N:
       break

print ("========================")
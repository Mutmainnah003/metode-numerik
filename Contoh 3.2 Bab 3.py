# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:20:28 2020

@author: ASUS
"""


import math 
 
def f(x):     
    return x**3-10*x**2+5  
 
a = 1
b = 3
e = 0.000001 
N = 100 
iterasi = 0 
 
print('=========================') 
print('   c        f(c)')
print('=========================')

while True:
    iterasi +=1
    c= (b-f(b)*(b-a)/(f(b)-f(a)))
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
    print('{:7.5f}\t{:15.10f}'.format(c, f(c)))
    if abs(f(c))< e or iterasi >= N:
       break
   
print('========================')
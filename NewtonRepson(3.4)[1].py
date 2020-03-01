# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 00:01:15 2020

@author: User
"""

#metode neowton untuk mencari akar
#fungsi fx=x^2-16

import math
iterasi= 20
x=5    #nilai tebakan
fx=x**3 - 30
batas=0.001
i=0

while (i<=iterasi and abs (fx)>batas):
    fx=x**3 - 30
    ft=3**3 + 3
    x=x-(fx/ft)
    print ('x =',x,      'fx = ',fx)
    i=i+1
print ('akarnya adalah',x,'dengan iterasi sebanyak',i,'kali')
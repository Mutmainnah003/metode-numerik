import math 
def f(x): 
    return math.exp(x) - 5*x**2 


a = 0 
b = 1 
e = 0.000001 
N = 100 
iterasi = 0
print('==================================') 
print(' c                      f(c)') 
print('==================================') 
while True: 
    iterasi += 1 
    c = (a + b)/2 
    if f(a)*f(c) < 0: 
        b = c 
    else: 
        a = c 
    print('{:7.5f} \t {:+15.10f}'.format(c, f(c))) 
    if abs(f(c)) < e or iterasi >= N: 
        break 
print('==================================')

# a. Input taksiran awal yang mengurung akar dapat dilakukan secara interaktif, diinput dari keyboard
def f(x): 
    return math.exp(x) - 5*x**2 

a = 0 
b = 1 
e = 0.000001 
N = 100
iterasi = 1
print('==================================') 
print(' f(a)                   f(b)') 
print('==================================') 
while True: 
    iterasi += 0
    # c = (a + b)/2 
    if f(a)*f(b) < 0: 
        # b = c 
        print('mengurung akar {:7.5f} \t {:+15.10f}'.format(f(a), f(b)))  
    else: 
        # a = c
        # print('{:7.5f} \t {:+15.10f}'.format(c, f(c))) 
        if abs(f(a) and f(b)) < e or iterasi >= N: break 
    print('==================================')
 
# b. Program dapat mendeteksi jika taksiran awal tidak mengurung akar.

def f(x): 
    return math.exp(x) - 5*x**2 
a = 0 
b = 1 
e = 0.000001 
N = 100 
iterasi = 1
print('==================================') 
print('                  f(a)                   f(c)') 
print('==================================') 
while True: 
    iterasi += 1
    c = (a + b)/2 
    if f(a)*f(b) < 0: 
        b = c 
        print(' mengurung akar       {:7.5f} \t {:+15.10f}'.format(f(a), f(c)))  
    else: 
        a = c 
        print(' tidak mengurung akar {:7.5f} \t {:+15.10f}'.format(c, f(c))) 
        if abs(f(a) and f(b)) < e or iterasi >= N: break 
    print('==================================')
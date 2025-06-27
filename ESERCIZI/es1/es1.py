import numpy as np

#1
a = []
for i in range(10):
    a.append(i)
    
b = []
for i in range(10):
    if i % 2 == 0:
        b.append(i)

b2 = [i for i in range(10) if i % 2 == 0]

c = []
for i in range(10):
    c.append(i*2)

c2 = [i*2 for i in range(10)]

#2
p = np.array([1,2,3,5,7])

print(len(p))
print(p.size)
print(p.dtype)

def is_prime(n):
    if n < 2: return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

primi2 = np.array([i for i in range(11) if is_prime(i)])
print(primi2)

#3
a = np.arange(1,6)     
b = a[1:4]             
c = a[::-1]            
print(a/c)

al = [1,2,3,4,5]
bl = al[1:4]
cl = al[::-1]
divl = [x/y for x,y in zip(al,cl)]
print(divl)
from Crypto.Util.number import getPrime
from gmpy2 import next_prime
from random import getrandbits

flag = b'1'

p=getPrime(1024)
print(p)
q=next_prime(p+(p&((1<<600)-1))^getrandbits(200))
print(q)
n=p*q
e=65537
eular=(p-1)*(q-1)
d=pow(e, -1, eular)
print(d)
print((e*d)%eular)
print(pow(n,0.3))
m=int(flag.hex(),16)
assert m<n
c=pow(m,e,n)
with open("output.txt","w") as f:
    f.write("n = "+str(n)+"\nc = "+str(c))

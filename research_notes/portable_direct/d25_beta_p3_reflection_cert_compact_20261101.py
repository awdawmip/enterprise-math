#!/usr/bin/env python3
"""D25 original signed beta-tail p^3 test; author-side, NOT native H0/B0."""
from math import isqrt, comb

def primes(n):
 a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
 for d in range(2,isqrt(n)+1):
  if a[d]:a[d*d:n+1:d]=b'\0'*((n-d*d)//d+1)
 return [p for p in range(5,n+1) if a[p]]

def beta(p,m):
 v=1;arr=[]
 for k in range(p):
  arr.append(v)
  if k+1<p:v=v*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,m)%m
 return arr

def tail(b,p,m):
 s=[0]*(p+1);v=[0]*(p+1)
 for k in range(p-1,-1,-1):
  s[k]=(s[k+1]+b[k])%m;v[k]=(v[k+1]+k*b[k])%m
 return sum(b[i]*((8*i+1)*s[p-i]+8*v[p-i]) for i in range(p))%m

def reflected(p):
 t=(p-3)//8; b=q=1;S=M=U=0
 for i in range(1,t+1):
  if i>1:
   r=i-2;q=q*576*(r+1)**2*pow((8*r+13)*(8*r+15),-1,p)%p
  S=(S+q)%p;M=(M+(i-1)*q)%p
  k=i-1;b=b*(8*k+1)*(8*k+3)*pow(576*i*i,-1,p)%p
  U=(U+b*((8*i-7)*S-8*M))%p
 return U*6*pow(35,-1,p)%p

def Bsum(p,m):
 b=1;ans=0
 for k in range(p):
  ans=(ans+(8*k+1)*b)%m
  if k+1<p:b=b*(4*k+1)*(2*k+1)*(4*k+3)*pow(288*(k+1)**3,-1,m)%m
 return ans

nt=nr=nraw=0
for p in primes(3000):
 if p%8!=3:continue
 m=p**3;b=beta(p,m);u=reflected(p);T=tail(b,p,m)
 assert T==p*p*u and b[-1]//(p*p)%p==3*pow(35,-1,p)%p
 t=(p-3)//8
 for k in range(p):
  v=0 if k<=t else 1 if k<=3*t+1 else 2
  assert b[k]%p**v==0 and b[k]%p**(v+1)!=0
 g=sum(b)%m;h=sum((16*k+1)*x for k,x in enumerate(b))%m
 B=Bsum(p,m);chi=1 if p%3==1 else -1
 assert B==(p*chi)%m and (g*h-T)%m==B
 if p%24==19:
  assert g%p==0 and h%p!=0
  assert g//p%p**2==(1+p*u)*pow(h,-1,p*p)%(p*p)
  nr+=1
 else:
  assert p%24==11 and h%p==0 and g%p!=0
  assert h//p%p**2==(-1+p*u)*pow(g,-1,p*p)%(p*p)
 if p in (11,19,43,67,139):
  for k in range(p):
   z=1
   for j in range(k):z=z*(8*j+1)*(8*j+3)%m
   assert b[k]==z*pow(576**k*__import__('math').factorial(k)**2,-1,m)%m
   nraw+=1
  direct=sum((8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,m) for k in range(p))%m
  assert B==direct
  print('sample',p,'U',u,'T',T,'G',g,'H',h)
 nt+=1
print('PASS p=3 mod8',nt,'primes <=3000; p19 target',nr,'; direct beta checks',nraw)

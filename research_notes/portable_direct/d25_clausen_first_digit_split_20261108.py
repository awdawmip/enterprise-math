#!/usr/bin/env python3
"""Exact independent finite-field regression: original W216 versus Clausen Gauss factors."""
from math import isqrt
def primes(n):
 s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
 for q in range(2,isqrt(n)+1):
  if s[q]:s[q*q:n+1:q]=b'\x00'*((n-q*q)//q+1)
 return [p for p in range(7,n+1) if s[p]]
def W(p):
 a=1;out=0;d=pow(216,-1,p)
 for n in range(p):
  out=(out+(6*n+1)*a)%p
  if n+1<p:
   a=a*(2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3)*pow(n+1,-5,p)*d%p
 return out
def FG(p):
 k=(p-1)//6
 assert p==6*k+1 and p>3
 a=1;f=0;g=0
 for n in range(k+1):
  f=(f+a)%p;g=(g+(1+12*n)*a)%p
  if n<k:a=a*(n-k)*(n-2*k)*pow(2,-1,p)*pow(n+1,-2,p)%p
 return f,g
def chi(p):
 a=pow(-6%p,(p-1)//2,p)
 assert a in (1,p-1)
 return 1 if a==1 else -1
def main():
 z={v:[0,0,0] for v in (1,7,13,19)}
 for p in primes(10000):
  if p%6!=1:continue
  f,g=FG(p); w=W(p)
  assert w==f*g%p==0,(p,w,f,g)
  assert (f==0 and g!=0) if chi(p)==-1 else (g==0 and f!=0),(p,f,g)
  r=z[p%24];r[0]+=1;r[1]+=f==0;r[2]+=g==0
 assert sum(r[0] for r in z.values())==611
 print('CHECKED 611 primes p=1 mod6 through 10000: all exact tests passed')
 for k,v in z.items():print(k,v)
 for p in (7,13,19,31,37,373):print('witness',p,FG(p),W(p))
 print('CM factor classification is finite conjectural evidence, not a universal proof')
if __name__=='__main__':main()

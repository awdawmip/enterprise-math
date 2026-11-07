#!/usr/bin/env python3
"""D25: exact modular 216/2304 source-strata checks, author-side only."""
from math import comb,isqrt,factorial
def primes(n):
 s=bytearray(b'\1')*n;s[:2]=b'\0\0'
 for d in range(2,isqrt(n-1)+1):
  if s[d]:s[d*d::d]=b'\0'*len(s[d*d::d])
 return [p for p in range(5,n) if s[p]]
def sums(p,e=3,labels=False):
 M=p**e;a=b=1;wa=wb=0;ports=[0]*6;extra=[]
 for k in range(p):
  x=(6*k+1)*a%M;y=(8*k+1)*b%M
  wa=(wa+x)%M;wb=(wb+y)%M
  if labels:
   z=(int(4*k>=p)+int(3*k>=p)+int(2*k>=p)
      +int(3*k>=2*p)+int(4*k>=3*p))
   ports[z]=(ports[z]+x-y)%M
   if 3*k>=2*p and 4*k<3*p:
    assert x%p**3==0 and y%p**2==0 and y%p**3!=0
    r=4*k-2*p
    predicted=2*(8*k+1)*factorial(r)*pow(2304,-k,p)*pow(factorial(k),-4,p)%p
    observed=(y//p**2)%p
    assert predicted==observed
    extra.append((k,observed))
  if k+1<p:
   a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M
   b=b*(4*k+1)*(4*k+3)*(2*k+1)*pow(288*(k+1)**3,-1,M)%M
 if labels:
  assert (sum(ports)-wa+wb)%M==0
  return wa,wb,ports,extra
 return wa,wb
def independent(p,e=3):
 M=p**e;aa=bb=0;x=y=1;ix=pow(216,-1,M);iy=pow(2304,-1,M)
 for k in range(p):
  c=comb(2*k,k)
  aa=(aa+(6*k+1)*c*c*comb(3*k,k)*x)%M
  bb=(bb+(8*k+1)*comb(4*k,2*k)*c*c*y)%M
  x=x*ix%M;y=y*iy%M
 return aa,bb
def main():
 pp=primes(2000);classes={1:0,2:0}
 for p in pp:
  a,b=sums(p);chi=1 if p%3==1 else -1
  assert a==b==p*chi%(p**3),(p,a,b)
  classes[p%3]+=1
 assert len(pp)==301 and classes=={1:148,2:153}
 print("301/301 exact finite checks PASS",classes)
 for p in (7,11,13,19,31,37,43,109,373):
  a,b,ports,extra=sums(p,3,True)
  assert (a,b)==independent(p)
  a4,b4=sums(p,4)
  print(p,a,b,"ports",ports,"extra",sum(z for k,z in extra)%p,
        "4th-digit-difference",((a4-b4)%(p**4))//p**3)
 a,b,_,extra=sums(181,3,True)
 assert a==b==181 and len(extra)==15 and all(z!=0 for k,z in extra)
 assert sum(z for k,z in extra)%181==0
 print("p181 labelled high-band alias",extra)
 assert ((sums(7,4)[0]-sums(7,4)[1])%(7**4))//7**3==4
 print("9/9 independent factorial checks PASS")
if __name__=="__main__":main()

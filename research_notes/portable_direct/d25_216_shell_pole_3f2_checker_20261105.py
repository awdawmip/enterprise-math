#!/usr/bin/env python3
"""D25 author-side finite exact two-carrier shell and boundary check; no native H0/B0."""
def primes(N=10000):
 s=bytearray([1])*(N+1);s[:2]=b'\0\0'
 for k in range(2,int(N**.5)+1):
  if s[k]:s[k*k::k]=b'\0'*(((N-k*k)//k)+1)
 return [p for p in range(7,N+1) if s[p] and p%6==1]
def test(p):
 n=(p-1)//6
 fac=[1]*p
 for i in range(1,p):fac[i]=fac[i-1]*i%p
 inv=[1]*p;inv[-1]=pow(fac[-1],-1,p)
 for i in range(p-1,0,-1):inv[i-1]=inv[i]*i%p
 out=0;pow216=pow(216,2*n,p)
 for j in range(2*n+1,3*n+1):
  out=(out+(6*j-1)*pow216*pow(fac[j-1],5,p)*inv[2*j-1]*inv[3*j-p-1])%p
  pow216=pow216*216%p
 C=pow(216,2*n,p)*pow(fac[2*n],5,p)*inv[4*n+1]%p
 a=[1]; v=1;H=0;thetaH=0
 inv3=pow(3,-1,p); inv6=pow(6,-1,p)
 for r in range(n):
  H=(H+v)%p;thetaH=(thetaH+r*v)%p
  if r+1<n:
   denominator=3*(6*r+7)*(3*r+4)*(r+1)%p
   assert denominator
   v=v*4*pow(3*r+2,3,p)*pow(denominator,-1,p)%p
   numer=pow((3*r+2)*inv3%p,3,p)
   denom=(r+1)*((6*r+7)*inv6%p)*((3*r+4)*inv3%p)%p
   assert denom
   a.append(a[-1]*numer*pow(denom,-1,p)%p)
 assert out==3*C*(H+2*thetaH)%p,(p,out,C,H,thetaH)
 assert 6*(n-1)+7==p
 for k in range(n+1):
  lhs=0
  if k<n:lhs+=k*((6*k+1)*inv6%p)*((3*k+1)*inv3%p)*a[k]
  if k:lhs-=pow((3*(k-1)+2)*inv3%p,3,p)*a[k-1]
  expected=(a[-1]*pow(8,-1,p)%p) if k==n else 0
  assert lhs%p==expected,(p,k,lhs,expected)
 assert a[-1]%p!=0
 if p in (13,19,139,373):
  print('anchor',p,'n',n,'T_A',out,'C',C,'H',H,'thetaH',thetaH,'terminal',a[-1]*pow(8,-1,p)%p)
 return out
ps=primes(); zeros=[]
for p in ps:
 if test(p)==0:zeros.append(p)
print('PASS primes',len(ps),'shell_mismatches 0','operator_failures 0','zero_T_A_samples',zeros)

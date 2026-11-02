#!/usr/bin/env python3
"""Exact D25 reflected-Wronskian check; portable author-side, NOT native H0/B0."""
from math import comb,isqrt
import json
def primes(lim):
 s=bytearray(b'\x01')*(lim+1);s[:2]=b'\0\0'
 for k in range(2,isqrt(lim)+1):
  if s[k]: s[k*k::k]=b'\0'*((lim-k*k)//k+1)
 return [p for p in range(7,lim+1) if s[p] and p%6==1]
def invs(p):
 v=[0]*p;v[1]=1
 for k in range(2,p):v[k]=-(p//k)*v[p%k]%p
 return v
def shift(poly,p):
 h=[]
 for s in reversed(poly):
  t=[0]*(len(h)+1)
  for k,a in enumerate(h):t[k]=(t[k]+a)%p;t[k+1]=(t[k+1]-a)%p
  t[0]=(t[0]+s)%p;h=t
 return h
def ev(v,z,p):
 t=0
 for a in reversed(v):t=(t*z+a)%p
 return t
def verify(p,full=False):
 r=(p-1)//6;u=3*r;iv=invs(p)
 a=[1]
 for n in range(2*r):
  a.append(a[-1]*(2*n+1)*(3*n+1)*(3*n+2)*iv[18%p]*pow(iv[n+1],3,p)%p)
 s=[(9*n+4)*a[n]*iv[36%p]%p for n in range(2*r+1)]
 omega=[0]
 for n in range(u):
  omega.append(((s[n] if n<len(s) else 0)-(u-n)*omega[-1])*iv[n+1]%p)
 d=shift(s,p)
 reflect=[d[k]*iv[u-k]%p for k in range(len(d))]
 reflect += [0]*(u-len(reflect));reflect.append(iv[6])
 assert sum(reflect)%p==0
 assert omega[u]==(-1 if r%2 else 1)*iv[6]%p
 ell1=comb(3*r,r)%p
 assert d[0]==ell1*ell1*iv[18%p]%p
 assert ev(omega,1,p)==-ell1*ell1*iv[9%p]%p
 half=iv[2];chi=pow(2,u,p)
 J=sum(d[k]*iv[u-k]*pow(half,k,p) for k in range(2*r+1))%p
 assert ev(omega,half,p)==(chi*iv[6]+J)%p
 for z in [0,1,half,2%p,3%p]:
  assert ev(omega,z,p)==ev(reflect,(1-z)%p,p)
 if full: assert shift(omega,p)==reflect
 row={'p':p,'r':r,'chi2':-1 if chi==p-1 else 1,'J':J,
      'omega_half':ev(omega,half,p),'omega_one':ev(omega,1,p),
      'gap_slots':max(0,r-1),'full':full}
 if p%24 in (13,19):
  m=p*p;ell=[1]
  for k in range(r):
   ell.append(ell[-1]*(r-k)*(2*r-k)*pow((k+1)**2,-1,m)%m)
  h=pow(2,-1,m);power=1;val=0;j=0
  for k,c in enumerate(ell):
   val=(val+c*power)%m;j=(j+k*c*power)%m;power=power*h%m
  assert val%p==0
  g=val//p;j%=p
  row.update({'g':g,'j':j,'reflected_delta':(J-g*j)%p,
              'half_carry':(12*g*j-12*row['omega_half'])%p,
              'one_twelfth':iv[12%p]})
 return row
def main():
 ps=primes(2000)
 full={7,13,19,31,37,43,73,181,373,1171,1999}
 data=[verify(p,p in full) for p in ps]
 tg=[x for x in data if x['p']%24 in (13,19)]
 result={'schema':'D25_REFLECTED_WRONSKIAN_SOURCE_CHECK_V1',
 'all_primes':len(ps),'full_polynomial_primes':[x['p'] for x in data if x['full']],
 'target_primes':len(tg),'target_finite_equalities':sum(x['reflected_delta']==x['one_twelfth'] for x in tg),
 'target_failures':[x for x in tg if x['reflected_delta']!=x['one_twelfth']],
 'samples':[x for x in data if x['p'] in [7,13,19,31,37,43,73,181,373,1171]],
 'scientific_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
 'native_H0_B0':'NOT_EXECUTED','admission':'UNREVIEWED_NOT_ADMITTED'}
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()

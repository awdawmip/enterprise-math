#!/usr/bin/env python3
"""Standalone exact rational Bellman interval certificate, source-sensitive R5 diamond."""
from fractions import Fraction as F
from itertools import product
S=(F(1,2),F(1),F(3,2),F(5,2)); r=S[2]
a=F(1,4)
mu=((F(7,50),F(11,75),F(1,2),F(16,75)),
    (F(17,200),F(23,150),F(3,5),F(97,600)))
nu=(( (F(1,2),F(1,6),F(1,4),F(1,12)),
       (F(17,100),F(23,75),F(1,5),F(97,300)) ),
    ( (F(5,12),F(1,3),F(1,6),F(1,12)),
       (F(31,120),F(5,18),F(1,15),F(143,360)) ))
eta=((F(1,8),F(1,4),F(3,8),F(1,4)),
     (F(5,32),F(3,16),F(13,32),F(1,4)))
x=(F(41,1200),F(59,3600)); I=(F(1,8),F(5,32))
star=F(787,5824); peak=F(2419,6988800)
f=lambda t,s,h: t*h+min(F(0),F(2)-2*s)
for i in range(2):
 for row,parent in [(mu[i],r),(eta[i],r),(nu[i][0],S[1]),(nu[i][1],r)]:
  assert min(row)>0 and sum(row)==1 and sum(q*s for q,s in zip(row,S))==parent
 assert I[i]== f(3,r,F(0))-sum(q*f(4,s,F(0)) for q,s in zip(eta[i],S))

def margins(i,h,g):
 m=f(3,r,h)+g*(h-I[i]); cost=[]; ans=[]
 for k,s in enumerate(S):
  if k in (1,2):
   cont=sum(q*(m if j==2 else f(3,S[j],h)) for j,q in enumerate(nu[i][k-1]))
   ans.append(f(2,s,h)-cont);cost.append(cont)
  else:cost.append(f(2,s,h))
 ans.append(f(1,r,h)-sum(q*v for q,v in zip(mu[i],cost)))
 return tuple(ans)

mins=tuple(tuple(min(margins(i,h,g)[j] for h in I for g in (F(0),F(1)))
                 for j in range(3)) for i in range(2))
assert mins==((F(43,128),F(3,400),F(353,9600)),
              (F(25,96),F(49,480),F(431,14400)))

def full(h):
 z=F(2)+f(1,S[0],h)/2
 for i in range(2):
  stop=f(3,r,h);tail=sum(q*f(4,s,h) for q,s in zip(eta[i],S));vals=[]
  for k,s in enumerate(S):
   if k in (1,2):
    cont=sum(q*(min(stop,tail) if j==2 else f(3,S[j],h))
             for j,q in enumerate(nu[i][k-1]))
    vals.append(min(f(2,s,h),cont))
   else:vals.append(f(2,s,h))
  z+=a*min(f(1,r,h),sum(q*v for q,v in zip(mu[i],vals)))
 return z

def lr(h,root,L,R,g):
 z=F(2)+f(1,S[0],h)/2+(1-root)*f(1,r,h)/2
 for i in range(2):
  for k,s in enumerate(S):
   m=a*root*mu[i][k]
   if k not in (1,2):z+=m*f(2,s,h);continue
   t=L if k==1 else R;z+=m*(1-t)*f(2,s,h)
   m*=t
   for j,ss in enumerate(S):
    w=m*nu[i][k-1][j]
    if j==2:z+=w*((1-g)*f(3,ss,h)+g*sum(q*f(4,v,h) for q,v in zip(eta[i],S)))
    else:z+=w*f(3,ss,h)
 return z

assert star==(x[0]*I[0]+x[1]*I[1])/sum(x)
assert peak==x[0]*(star-I[0])==x[1]*(I[1]-star)
for k in range(251):
 h=I[0]+(I[1]-I[0])*F(k,250)
 v=F(155161,115200)+F(6719,3600)*h
 w=min(F(2429,1800)+F(37,20)*h,F(154669,115200)+F(3421,1800)*h)
 assert full(h)==v
 assert min(lr(h,*d) for d in product((F(0),F(1)),repeat=4))==w
 assert w-v==min(x[0]*(h-I[0]),x[1]*(I[1]-h))
assert peak/(4+star)==F(2419,28899600)
print('UPSTREAM_MARGIN_MINIMA',mins)
print('THETA_INTERVAL',*I,'SWITCH',star,'MAX_GAP',peak)
print('OBSERVER_LINF_CERT',F(2419,28899600))
print('EXACT_RATIONAL_PARAMETER_CASES',251,'LR_VERTEX_CASES_EACH',16)
print('PASS_EXACT_R5_ROBUST_BELLMAN_INTERVAL')

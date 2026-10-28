#!/usr/bin/env python3
"""Exact Fraction N4 BRC one-bit observer asymmetry; external finite model."""
from fractions import Fraction as F
from itertools import product
import json
Z,O=F(0),F(1)
N={1:{'A':(F(1,2),F(1,2)),'B':(F(1,2),F(3,2))},
   2:{'AU':(F(1,6),O),'AV':(F(1,3),F(1,4)),
      'BU':(F(1,4),O),'BV':(F(1,4),F(2))}}
for t in (3,4):
 N[t]={}
 for h,(q,r) in N[t-1].items():
  e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[h] if t==3
     else Z if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
  for j,s in (('0',-1),('1',1)):N[t][h+j]=(q/2,r*(1+s*e))
for t in N:
 assert len(N[t])==2**t and all(q>0 and r>0 for q,r in N[t].values())
 assert sum((q for q,r in N[t].values()),Z)==sum((q*r for q,r in N[t].values()),Z)==O
 if t>1:
  for h,(q,r) in N[t-1].items():
   ch=[(qq,rr) for k,(qq,rr) in N[t].items() if k.startswith(h) and len(k)==len(h)+1]
   assert len(ch)==2 and sum((qq for qq,rr in ch),Z)==q and sum((qq*rr for qq,rr in ch),Z)==q*r
def policy(a,b,ca,cb,repair=False):
 assert Z<a<=O and Z<b<=O and Z<=cb<=ca<=O
 d=ca-cb
 av,bv=(F(2,7)*d,F(2,7)*a*d/b) if repair else (Z,Z)
 assert Z<=av<=O and Z<=bv<=O
 rates={'AU':cb if repair else ca,'BU':cb,'AV':av,'BV':bv}
 g={(1,'A'):(Z,O-a,a),(1,'B'):(Z,O-b,b)}
 for h,c in rates.items():g[2,h]=(Z,O-c,c)
 for h in N[3]:
  p=h.startswith('AU') or (repair and (h.startswith('AV') or h.startswith('BV')))
  g[3,h]=(O,Z,Z) if p else (Z,O,Z)
 for h in N[4]:g[4,h]=(Z,O,Z)
 assert all(min(v)>=Z and sum(v,Z)==O for v in g.values())
 if repair:
  for t in (2,3,4):
   by={}
   for h,(q,r) in N[t].items():
    if r in by:assert g[t,h]==by[r]
    by[r]=g[t,h]
 return g
def law(g,prefix):
 out={'P':{},'Q':{}}
 for leaf,(q,r) in N[4].items():
  live=O
  for t in range(1,5):
   h=leaf[:t];pp,qq,cc=g[t,h]
   tag='REACH3' if t>=3 and h.startswith(prefix) else 'OTHER'
   for name,w in (('Q',q),('P',q*r)):
    for dec,prob in (('P',pp),('Q',qq)):
     key=(t,dec,tag)
     out[name][key]=out[name].get(key,Z)+w*live*prob
   live*=cc
  assert live==Z
 for name in out:assert sum(out[name].values(),Z)==O
 return out
def tv(x,y,name):
 ks=x[name].keys()|y[name].keys()
 return sum((abs(x[name].get(k,Z)-y[name].get(k,Z)) for k in ks),Z)/2
def test(a,b,ca,cb):
 d=ca-cb
 if 2*a*d>7*b:return False
 m=a*d/6;x=4*m/7;y=3*m/7
 assert x+y==m and x/4+2*y==m
 assert a/F(3)*F(2,7)*d==x and b/F(4)*F(2,7)*a*d/b==y
 old=policy(a,b,ca,cb);new=policy(a,b,ca,cb,True)
 assert law(old,'BU')==law(new,'BU')
 return True
def main():
 vals=(F(1,4),F(1,2),F(3,4),O)
 cs=(Z,F(1,4),F(1,2),F(3,4),O)
 n=sum(test(a,b,ca,cb) for a,b,ca,cb in product(vals,vals,cs,cs) if cb<=ca)
 a=b=F(3,4);ca=F(5,12);cb=F(1,3)
 assert test(a,b,ca,cb)
 x=policy(a,b,ca,cb);y=policy(a,b,ca,cb,True)
 A=[str(tv(law(x,'AU'),law(y,'AU'),name)) for name in ('P','Q')]
 B=[str(tv(law(x,'BU'),law(y,'BU'),name)) for name in ('P','Q')]
 assert A==['1/96','1/96'] and B==['0','0'] and n==239
 print(json.dumps({'status':'PASS_EXACT_N4_ONE_BIT_OBSERVER_ASYMMETRY',
 'exact_grid_cases':n,'witness':{'a':str(a),'b':str(b),'cA':str(ca),'cB':str(cb),
 'm':'1/96','x_AV':'1/168','y_BV':'1/224','AV_BV_continue':'1/42',
 'AU_BU_continue':'1/3','BU_bit_TV_P_Q':B,'AU_bit_TV_P_Q_for_this_repair':A},
 'universal_analytic_proof':'PROOF.md','native_X6_bridge':'NOT_ESTABLISHED',
 'admission':'AUTHOR_UNREVIEWED_NOT_ADMITTED'},ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact integer/Fraction certificate for R5 high-degree rare-failure spectrum.
Usage: python VERIFY_N84.py /path/to/EXACT_R5_ALL_101_BUDGETS.json
"""
import sys, hashlib, json
from math import comb, factorial
from fractions import Fraction as Q
from pathlib import Path
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
A=tuple(range(214,219));S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
B=tuple(range(219,315));D=tuple(range(222,315));J=219*220*221
LOG={1:Q(1,2),2:-Q(1,24),4:Q(1,2880),6:-Q(1,181440),8:Q(1,9676800),10:-Q(1,479001600)}
FAC={0:Q(1),1:Q(1,2),2:Q(1,12),4:-Q(1,720),6:Q(1,30240),8:-Q(1,1209600),10:Q(1,47900160)}
def moments(prices,m,R):
 s=[[0]*(R+1) for _ in range(m)];s[0][0]=1
 for p in prices:
  new=[[0]*(R+1) for _ in range(m)]
  for t,row in enumerate(s):
   for n in range(m-t):
    w=p*n
    for r in range(R+1):
     new[t+n][r]+=sum(comb(r,k)*row[k]*w**(r-k) for k in range(r+1))
  s=new
 return [sum(row[r] for row in s) for r in range(R+1)]
def split(m,R):
 out=[]
 for c in range(m):
  v=[sum((z-x)**k for x in range(c+1) for z in range(c-x+1)) for k in range(R+1)]
  assert v[0]==comb(c+2,2)
  out.append(v)
 return out
def overlap(m,R):
 S=split(m,R)
 Qs=[[[sum(comb(r,k)*S[c][k]*S[d][r-k] for k in range(r+1))
       for r in range(R+1)] for d in range(m)] for c in range(m)]
 v=[0]*(R+1)
 for a in range(m):
  for b in range(m):
   for c in range(m):
    for d in range(m):
     h=int(a+b+c<m)+int(a+c+d<m)+int(b+c+d<m)-1
     if h<1:continue
     W=214*a+215*b+217*c+220*d
     for r in range(R+1):
      v[r]+=h*sum(comb(r,k)*W**(r-k)*Qs[c][d][k] for k in range(r+1))
 return v
def brute(m,R):
 out=[0]*(R+1)
 def go(ns):
  if len(ns)==8:
   a,b,x,y,z,u,v,w=ns;c=x+y+z;d=u+v+w
   h=int(a+b+c<m)+int(a+c+d<m)+int(b+c+d<m)-1
   if h>0:
    total=sum((214+i)*n for i,n in enumerate(ns))
    for k in range(R+1):out[k]+=h*total**k
   return
  for n in range(m):go(ns+[n])
 go([])
 return out
def laplace(prices,R):
 log={k:val*sum(p**k for p in prices) for k,val in LOG.items() if k<=R}
 a=[Q(0)]*(R+1);a[0]=1
 for n in range(1,R+1):
  a[n]=sum(k*val*a[n-k] for k,val in log.items() if k<=n)/n
 return a
def laplace_other(prices,R):
 a=[Q(1)]+[Q(0)]*R
 for p in prices:
  a=[sum(a[n-k]*val*p**k for k,val in FAC.items() if k<=n) for n in range(R+1)]
 return a
def compute(m):
 M=moments(A,m,11);H1=moments(S1,m,9);H2=moments(S2,m,9);V=overlap(m,8)
 lB=laplace(B,11);lD=laplace(D,8)
 l1=laplace(D+(215,),9);l2=laplace(D+(214,),9)
 coeff=[]
 for j in range(12):
  ans=sum(Q((-1)**r*M[r],factorial(r))*lB[j-r] for r in range(j+1))
  if j>=2:
   ans+=sum(Q(J,e)*sum(Q((-1)**r*H[r],factorial(r))*ll[j-2-r] for r in range(j-1))
            for e,H,ll in ((215,H1,l1),(214,H2,l2)))
  if j>=3:
   ans-=J*sum(Q((-1)**r*V[r],factorial(r))*lD[j-3-r] for r in range(j-2))
  coeff.append(ans)
 return {"m":m,"V5":str(V[5]),"V8":str(V[8]),
         "B":{str(95-j):str(ans) for j,ans in enumerate(coeff)}}
def main(path):
 digest=hashlib.sha256(Path(path).read_bytes()).hexdigest()
 assert digest==PIN,(digest,PIN)
 for m in (1,2,3):assert overlap(m,8)==brute(m,8),m
 for E in (A,S1,S2,B,D,D+(214,),D+(215,)):
  assert laplace(E,11)==laplace_other(E,11)
 rows=[compute(m) for m in (1,2,3,5,8,17)]
 old={1:"15282978029842507634701865804458/1449315",
      2:"55643159669186529815868389465581/966210",
      3:"12654461370869371404220539364348/69015",
      5:"4178587966230297936349481600780/4601",
      8:"683963433828874003574585270763374/161035",
      17:"945681411601270137810199016293172/23005"}
 for row in rows:assert Q(row["B"]["88"])==Q(old[row["m"]])
 print(json.dumps({"schema":"R5_HIGH_DEGREE_N84_V1","pin":digest,
  "checks":{"brute_m":[1,2,3],"laplace_price_sets":7,"max_degree":11,
            "predecessor_B88_m":[1,2,3,5,8,17],"arithmetic":"int/Fraction"},
  "rows":rows},ensure_ascii=False,indent=2))
if __name__=="__main__":
 main(sys.argv[1])

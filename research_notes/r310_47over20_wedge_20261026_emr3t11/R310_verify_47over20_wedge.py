#!/usr/bin/env python3
"""R310 exact core verifier. Python 3 standard library only, integer/Fraction comparisons."""
import json
from math import comb, factorial
from fractions import Fraction as F
from collections import defaultdict

pascal=[[1]]
for n in range(1,700):
    a=pascal[-1]
    pascal.append([1]+[a[k-1]+a[k] for k in range(1,n)]+[1])

def majorant(d):
    n=(47*d*d+19)//20
    A=comb(n-2*d-4,d-1)
    c=[1]*(d-1)
    for j in range(1,d-1):
        c[j]=c[j-1]*(n-j+1)//j
    U=sum(pascal[d-r][t]*pascal[r-1][t-1]*c[d-r-t]
          for r in range(1,d) for t in range(1,min(r,d-r)+1))
    return n,A,U

checked=0
minimum_gap=None
min_gap_at=None
for d in range(401,700):
    n,A,U=majorant(d)
    assert n>=4*d+4 and A>U,(d,n)
    checked+=1
    if minimum_gap is None or A-U<minimum_gap:
        minimum_gap=A-U
        min_gap_at=(d,n)
assert checked==299 and min_gap_at==(401,377883)

s=F(213,250)
X=s+s*s/(2*(698-s))
assert X==F(74291631,87143500)
T7=sum(((-X)**j/F(factorial(j)) for j in range(8)),F(0))
margin=(F(47,20)-F(1,700))*T7-1/(1-F(3,2800))
assert margin==F(
  2092488275231236871099971363617114085359816057210835071819907,
  10460767115167513586602035754911397412770296875000000000000000000)
assert margin>0 and 11*700**2-4260*700+52780>0

n,A,U=majorant(20)
assert n==940 and A<U
edges={0:[(0,2,-1,-1),(1,2,1,-1)],
       1:[(1,0,1,-1)],
       2:[(0,1,1,1),(1,2,1,-1)]}
state={(0,1,1,0):1}
for _ in range(n):
    nxt=defaultdict(int)
    for (q,last,eps,k),count in state.items():
        for bit,q2,eta,c in edges[q]:
            if bit==0 and last==0: continue
            nxt[q2,bit,eta*eps,eta*k+c]+=count
    state=nxt
target=2-n+2*20
plus=sum(v for (q,last,e,k),v in state.items() if q==0 and e==1 and k==target)
minus=sum(v for (q,last,e,k),v in state.items() if q==0 and e==-1 and k==target)
assert (target,plus-minus)==(-898,823494305027016527734702960836351229563)
print(json.dumps({"status":"PASS","checked_middle_d":checked,
 "min_gap_at":{"d":min_gap_at[0],"n":min_gap_at[1]},
 "tail_margin":str(margin),
 "majorant_failure":{"d":20,"n":n,"A":str(A),"U":str(U)},
 "original_DP":{"plus":str(plus),"minus":str(minus),"difference":str(plus-minus)},
 "inherited_r307":"d=2..400; 80199 Newton coefficients, NOT rerun"}))

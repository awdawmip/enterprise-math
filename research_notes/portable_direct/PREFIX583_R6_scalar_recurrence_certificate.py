#!/usr/bin/env python3
"""Exact 5-step recurrence certificate for stationary paired-axis gate cubic q_n."""
from collections import Counter
from fractions import Fraction as F
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN,ZERO_ROOT,ACTIONS,edge
import json
import time
assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
N=96
CHECKS=768
DEPTH=CHECKS+5
edges=[]
for i in range(N):
    row=[]
    for a in ACTIONS:
        j,w=edge(i,a,ZERO_ROOT)
        h=64*w[6]-3*w[0]-w[1]-3*w[2]-w[3]
        p0=w[0]+w[1]
        p1=w[2]+w[3]
        assert sum(w[:6])==1
        row.append((j,h,p0,p1))
    edges.append(row)
assert Counter(j for row in edges for j,h,a,b in row)==Counter({i:6 for i in range(N)})
assert sum(h for row in edges for j,h,a,b in row)==-N*6
assert sum(a for row in edges for j,h,a,b in row)==N*2
assert sum(b for row in edges for j,h,a,b in row)==N*2
subsets=[[(s,m^s) for s in range(8) if (s&m)==s] for m in range(8)]
def compute_integer_q():
    V=[[0]*N for _ in range(8)]
    V[0]=[1]*N
    vals=[]
    for n in range(DEPTH):
        S=[sum(row) for row in V]
        D=N*6**n
        assert S[0]==D
        Q=9*S[7]-3*n*(S[3]+S[5])+9*n*S[6]-2*n**3*D
        vals.append(Q)
        if n==DEPTH-1:break
        W=[[0]*N for _ in range(8)]
        for i,row in enumerate(edges):
            for j,h,a,b in row:
                p=(1,h,a,h*a,b,h*b,a*b,h*a*b)
                for mask in range(8):
                    for sub,rem in subsets[mask]:
                        v=V[sub][i]
                        if v:W[mask][j]+=p[rem]*v
        V=W
    return vals
if __name__=="__main__":
    start=time.monotonic()
    Qs=compute_integer_q()
    for n in range(CHECKS):
        F_n=(9*Qs[n+5]+18*Qs[n+4]-72*Qs[n+3]-1296*Qs[n+2]
             -3888*Qs[n+1]-7776*Qs[n])
        assert F_n==0,(n,F_n)
    q=[F(Qs[i],576*N*6**i) for i in range(5)]
    expected=[F(0),F(1,576),-F(1,864),F(1,1728),F(1,1944)]
    assert q==expected
    c=[F(1),F(1,3),-F(2,9),-F(2,3),-F(1,3),-F(1,9)]
    numerator=[sum(c[k]*q[i-k] for k in range(i+1)) for i in range(5)]
    assert numerator==[F(0),F(9,5184),-F(3,5184),-F(1,5184),-F(1,5184)]
    print("ALL_CHECKS_PASS")
    print(json.dumps({
      "status":"ALL_CHECKS_PASS",
      "states":96,"labeled_actions":576,
      "science_pin":SCIENCE_PIN,
      "integer_moment_depths":DEPTH,
      "integer_recurrence_checks":CHECKS,
      "first_five":[str(v) for v in q],
      "recurrence":"9q[n+5]+3q[n+4]-2q[n+3]-6q[n+2]-3q[n+1]-q[n]=0",
      "characteristic":"(x-1)(3x^2+2x+1)^2",
      "generating_function":"-z(z^3+z^2+3z-9)/[5184(1-z)(1+2z/3+z^2/3)^2]",
      "limit":"1/5184",
      "error":"O(n*3^(-n/2))",
      "elapsed_seconds":round(time.monotonic()-start,3)
    },indent=2))

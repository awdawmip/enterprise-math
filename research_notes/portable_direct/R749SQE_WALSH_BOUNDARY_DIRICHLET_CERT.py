#!/usr/bin/env python3
"""Exact arithmetic checks for R749SQE: 23-letter slack-simplex limit.

Reconstruct the first-grid Walsh alphabet from R749SPR facets; check exact
limiting moments and finite-r source moment polynomials by two integer routes.
The universal limit law follows from rational-simplex Riemann sums in the note.
"""
from collections import defaultdict, Counter
from fractions import Fraction as F
import json

FACETS = [(-1,-1,-1,-2),(-1,-1,1,-2),(-1,1,-1,-2),(-1,1,1,-2),
          (1,-1,-1,-2),(1,-1,1,-4),(1,1,-1,-4),(1,1,1,-2)]
P = [(h,u,v) for h in range(-2,3) for u in range(-2,3) for v in range(-2,3)
     if all(a*h+b*u+c*v>=t for a,b,c,t in FACETS)]
assert len(P) == 33
by_pair = defaultdict(list)
for i in range(len(P)):
    for j in range(i,len(P)):
        by_pair[tuple(P[i][k]+P[j][k] for k in range(3))].append((i,j))
F25 = sorted({P[i] for opts in by_pair.values() if len(opts)==1 for i in opts[0]})
assert len(F25)==25
B = [(h,2-u,v) for h,u,v in F25 if u<2]
assert len(B)==23 and B.count((0,1,1)) == 1
OTHER = sorted((2*d-1-v, h+d-v, h,d,v) for h,d,v in B if (h,d,v)!=(0,1,1))
assert len(OTHER)==22
# Last entry is optional source; A0/A1 weights are 2/1 respectively.
LETTERS = [(s,t,t,0) for s,t,_,_,_ in OTHER]+[(3,2,1,1)]
assert len(LETTERS)==23
assert Counter(s for s,_,_,_ in LETTERS)=={1:3,2:4,3:6,4:4,5:3,6:2,7:1}
assert all(s>0 and 0<=a<=2*s and 0<=b<=2*s for s,a,b,k in LETTERS)

N=24
A0=[F(a,s) for s,a,b,k in LETTERS]+[F(0)]
A1=[F(b,s) for s,a,b,k in LETTERS]+[F(0)]
K=[F(k,s) for s,a,b,k in LETTERS]+[F(0)]
def mean(v): return sum(v)/N
def variance(v): return (N*sum(x*x for x in v)-sum(v)**2)/(N*N*(N+1))
def covariance(x,y):
    return (N*sum(a*b for a,b in zip(x,y))-sum(x)*sum(y))/(N*N*(N+1))
M={"mean_A0":mean(A0),"mean_A1":mean(A1),"mean_K":mean(K),
   "var_A0":variance(A0),"var_A1":variance(A1),"var_K":variance(K),
   "cov_A0_A1":covariance(A0,A1),"cov_A0_K":covariance(A0,K),
   "cov_A1_K":covariance(A1,K)}
assert M=={
    "mean_A0":F(379,630),"mean_A1":F(1481,2520),"mean_K":F(1,72),
    "var_A0":F(1489163,158760000),"var_A1":F(752929,79380000),
    "var_K":F(23,129600),"cov_A0_A1":F(1483423,158760000),
    "cov_A0_K":F(41,1134000),"cov_A1_K":F(-641,4536000)}
assert mean(A0)-mean(A1)==mean(K)

R=120
# Moments by slack grade: count, A0,A1,K,A0^2,A1^2,K^2,A0K,A1K
Z=9
mom=[[0]*Z for _ in range(R)]
mom[0][0]=1
for s,a,b,k in LETTERS:
    for d in range(s,R):
        n,x,y,z,xx,yy,zz,xz,yz=mom[d-s]
        dst=mom[d]
        dst[0]+=n;dst[1]+=x+n*a;dst[2]+=y+n*b;dst[3]+=z+n*k
        dst[4]+=xx+2*a*x+n*a*a
        dst[5]+=yy+2*b*y+n*b*b
        dst[6]+=zz+2*k*z+n*k*k
        dst[7]+=xz+a*z+k*x+n*a*k
        dst[8]+=yz+b*z+k*y+n*b*k

# Distinct check: full Laurent polynomial by slack, both H shifts, optional k.
R_SMALL=10
poly={(0,0,0,0):1}
for s,a,b,k in LETTERS:
    nxt=dict(poly)
    for (d,ha,hb,kk),cnt in poly.items():
        mul=1
        while d+mul*s<R_SMALL:
            key=(d+mul*s,ha+mul*a,hb+mul*b,kk+mul*k)
            nxt[key]=nxt.get(key,0)+cnt
            mul+=1
    poly=nxt
for d in range(R_SMALL):
    rows=[(ha,hb,k,c) for (q,ha,hb,k),c in poly.items() if q==d]
    got=[sum(c for ha,hb,k,c in rows),
         sum(ha*c for ha,hb,k,c in rows),sum(hb*c for ha,hb,k,c in rows),
         sum(k*c for ha,hb,k,c in rows),sum(ha*ha*c for ha,hb,k,c in rows),
         sum(hb*hb*c for ha,hb,k,c in rows),sum(k*k*c for ha,hb,k,c in rows),
         sum(ha*k*c for ha,hb,k,c in rows),sum(hb*k*c for ha,hb,k,c in rows)]
    assert got==mom[d], (d,got,mom[d])

prefix=[0]*Z
cases=[]
for r in range(1,R+1):
    prefix=[a+b for a,b in zip(prefix,mom[r-1])]
    c,h0,h1,k,_,_,_,_,_=prefix
    if r in (1,2,3,4,5,6,7,8,9,10,20,40,80,120):
        if r<=9:
            assert c==[1,4,14,42,113,279,651,1437,3040][r-1]
            assert k==[0,0,0,1,4,14,43,117,293][r-1]
        cases.append({"r":r,"C_r":str(c),"T_r":str(k),
            "E_A0_over_r":str(F(h0,r*c)),
            "E_A1_over_r":str(F(h1,r*c)),
            "E_K_over_r":str(F(k,r*c))})
assert all(row["C_r"]!="0" for row in cases)
result={"schema":"R749SQE_WALSH_BOUNDARY_DIRICHLET_V1","status":"PASS",
    "scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "predecessor":"R749SQB PR 2487 / R749SQC-SQD PR 2488",
    "model":"frozen 16-atom auxiliary Walsh, t=1/10 s=1/2",
    "arithmetic":"exact Python integers/Fraction, no floating arithmetic",
    "alphabet_counts":{"first_grid":len(P),"forced":len(F25),
                       "positive_slack":len(LETTERS),"simplex_barycentric":N},
    "slack_multiplicities":dict(sorted(Counter(s for s,a,b,k in LETTERS).items())),
    "limiting_moments":{key:str(value) for key,value in M.items()},
    "moment_cases":cases,
    "independent_checks":"two distinct finite graded algorithms agree for slack degrees 0..9 on all nine count/moment statistics",
    "theorem_proof":"Riemann-sum equidistribution on 23-dimensional rational simplex; not inferred from finite checks",
    "review":"AUTHOR_EXACT_NOT_REVIEWED"}
print(json.dumps(result,ensure_ascii=False,indent=2))

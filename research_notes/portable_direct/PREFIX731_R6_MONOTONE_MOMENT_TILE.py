"""PREFIX-731-R6. Exact 144-whole-cell Gamma maximum exclusion certificate.
Science pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run: python PREFIX731_R6_MONOTONE_MOMENT_TILE.py  (Python 3 standard library).
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from hashlib import sha256
from pathlib import Path
import json

N = 189
WD = 1 << 18

@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(WD-x)**(n-k) > WD**n

@lru_cache(None)
def wide(n,k):
    if k > n//2: return wide(n,n-k)
    mid = k*WD//n
    assert inside(n,k,mid)
    if k == 0:
        lo = hi = 0
    else:
        a,b = 0,mid
        while b-a > 1:
            x = (a+b)//2
            if inside(n,k,x): b=x
            else: a=x
        lo,hi=a,b
    a,b=mid,WD
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x): a=x
        else: b=x
    if 4*(a-hi)>WD: return True
    if 4*(b-lo)<WD: return False
    raise ValueError("Frozen width undecided")

rows=[{0:1}]
for n in range(1,N+1):
    count=defaultdict(int)
    for k,v in rows[-1].items():
        count[k]+=v
        count[k+1]+=v
    rows.append({k:v for k,v in count.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529

# Exact normalized Bernstein symmetry and unimodality of survivor tails.
for n,row in enumerate(rows[:N]):
    assert all(0<=v<=comb(n,k) for k,v in row.items())
    assert all(row.get(k,0)==row.get(n-k,0) for k in range(n+1))
    for k in range(n//2):
        assert row.get(k+1,0)*comb(n,k) >= row.get(k,0)*comb(n,k+1)

@lru_cache(None)
def scaled_tails(q):
    a,b=q.numerator,q.denominator-q.numerator
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*a)
        pb.append(pb[-1]*b)
    vals=tuple(sum(v*pa[k]*pb[n-k] for k,v in row.items())*
               q.denominator**(N-1-n)
               for n,row in enumerate(rows[:N]))
    return vals,q.denominator**(N-1)

# Correct two-Gamma kernel: c[n,m] = binom(n+m,n)/2**(n+m+1).
# The scaled integer representation avoids rational accumulation.
C=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)]
   for n in range(N)]
Z=2**(2*N-1)

@lru_cache(None)
def pair(p,z):
    t1,d1=scaled_tails(p);t2,d2=scaled_tails(z)
    a1,a2=sum(t1),sum(t2)
    b1=sum((n+1)*v for n,v in enumerate(t1))
    b2=sum((n+1)*v for n,v in enumerate(t2))
    cross0=cross1=0
    for n,x in enumerate(t1):
        if not x: continue
        for m,y in enumerate(t2):
            if not y: continue
            a=x*y*C[n][m]
            cross0+=a
            cross1+=(n+m+1)*a
    D=d1*d2*Z
    mu=F((a1*d2+a2*d1)*Z-cross0,D)
    M2=F(2*(b1*d2+b2*d1)*Z-cross1,D)
    assert mu>=0 and M2>=mu*mu
    return mu,M2

h=F(1,384); c=F(11,96)
edges=tuple(c-6*h+i*F(1,576) for i in range(19))
assert edges[0]==F(38,384) and edges[-1]==F(50,384)
e_mu,e_m2=pair(F(0),F(73,500))
e_W=e_m2-e_mu*e_mu
# Published PREFIX-726 moment hashes, recomputed here from the same frozen integer data.
center_mu,center_m2=pair(c,c)
center_W=center_m2-center_mu**2
def dig(x): return sha256(str(x).encode("utf-8")).hexdigest()
assert dig(center_mu.numerator)=="b15f79c4b0fc17598c7b19404f7eecdb083334496f81c4e27aaf17de164f2837"
assert dig(center_W.numerator)=="e4bd76b871f468d154f971a4cc69371fa21fad5bee103be950554fe83d7ea03c"
assert dig(e_mu.numerator)=="797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e"
assert dig(e_W.numerator)=="814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae"

floors=[]
worst=(10**9,None,None)
for i in range(18):
    for j in range(i,18):
        lo_mu,_=pair(edges[i],edges[j])
        _,hi_m2=pair(edges[i+1],edges[j+1])
        U=hi_m2-lo_mu**2
        g0=e_W-U
        gh=g0-(e_mu-lo_mu)/2
        assert g0>40 and gh>40
        f0=g0.numerator//g0.denominator
        fh=gh.numerator//gh.denominator
        floors.append([i,j,f0,fh])
        if f0<worst[0]: worst=(f0,[i,j],"t=0")
        if fh<worst[0]: worst=(fh,[i,j],"t=1/2")
assert len(floors)==171 and worst==(46,[0,17],"t=1/2")
cells=[[i,j] for i in range(38,50) for j in range(38,50)]
assert len(cells)==144
result={
    "schema":"PREFIX731_R6_MONOTONE_MOMENT_TILE_V1",
    "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "observer":"189-row BRC stopped-count; independent unit-rate Gamma maximum",
    "domain":"all real q>=2, p,z in [38/384,50/384]",
    "witness":["0","73/500"],"grid_denominator":384,
    "tile_index_range_half_open":[38,50],
    "whole_grid_cells_independently_certified":144,
    "subrectangle_count":324,
    "symmetry_reduced_exact_checks":171,
    "minimum_floor":46,"minimum_at":{"indices":[0,17],"endpoint":"t=1/2"},
    "uniform_strict_gap":"V_q(e)-V_q(p,z)>40*q^2",
    "all_endpoint_floors":floors,
    "union_dedup":"PENDING against exact prior 384-grid certified union",
    "grade":"AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED",
    "verification":"ALL_CHECKS_PASS PREFIX731-R6"
}
if __name__=="__main__":
    Path(__file__).with_name("PREFIX731_R6_RESULTS.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX731-R6")
    print("144 whole cells, 324 subrectangles; minimum endpoint gap floor:",worst)

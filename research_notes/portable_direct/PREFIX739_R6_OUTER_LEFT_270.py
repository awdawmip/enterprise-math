#!/usr/bin/env python3
"""PREFIX-739-R6. Exact frozen BRC-Gamma outer-left 270 new complete-cell exclusions.
Standard library Python 3; execute in research_notes/portable_direct with the four
original PREFIX713/716/718 historical JSON sources. Author-level certificate only.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

N=189
WD=1<<18
PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
ROOT=Path(__file__).resolve().parent
ROW_DATA=[
    (96,58,91559557,-20011808),
    (97,58,96255680,-16968178),
    (98,58,100935263,-13806781),
    (99,58,105590543,-10535419),
    (100,58,110215106,-7161288),
    (101,58,114803847,-3690919),
    (102,58,119352903,-130131),
    (103,55,123859584,-807413),
    (104,52,128322290,-93009),
    (105,46,132740416,-274507)
]

@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(WD-x)**(n-k)>WD**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:
        return wide(n,n-k)
    mid=k*WD//n
    assert inside(n,k,mid)
    if k==0:
        lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
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
    raise ArithmeticError("frozen width undecided")

rows=[{0:1}]
for n in range(1,N+1):
    new=defaultdict(int)
    for k,v in rows[-1].items():
        new[k]+=v
        new[k+1]+=v
    rows.append({k:v for k,v in new.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529
for n,row in enumerate(rows[:N]):
    assert all(0<=v<=comb(n,k) for k,v in row.items())
    assert all(row.get(k,0)==row.get(n-k,0) for k in range(n+1))
    assert all(row.get(k+1,0)*comb(n,k)>=row.get(k,0)*comb(n,k+1)
               for k in range(n//2))
@lru_cache(maxsize=256)
def tails(q):
    a,b=q.numerator,q.denominator-q.numerator
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*a)
        pb.append(pb[-1]*b)
    return (tuple(sum(v*pa[k]*pb[n-k] for k,v in row.items())*
                  q.denominator**(N-1-n) for n,row in enumerate(rows[:N])),
            q.denominator**(N-1))

C=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)] for n in range(N)]
Z=2**(2*N-1)
@lru_cache(maxsize=256)
def pair(p,z):
    t1,d1=tails(p)
    t2,d2=tails(z)
    a1,a2=sum(t1),sum(t2)
    b1=sum((n+1)*v for n,v in enumerate(t1))
    b2=sum((n+1)*v for n,v in enumerate(t2))
    cross0=cross1=0
    for n,x in enumerate(t1):
        if not x: continue
        for m,y in enumerate(t2):
            if not y: continue
            xy=x*y*C[n][m]
            cross0+=xy
            cross1+=(n+m+1)*xy
    denom=d1*d2*Z
    mu=F((a1*d2+a2*d1)*Z-cross0,denom)
    m2=F(2*(b1*d2+b2*d1)*Z-cross1,denom)
    assert mu>=0 and m2>=mu*mu
    return mu,m2

wm,wm2=pair(F(0),F(73,500))
wv=wm2-wm*wm
om,om2=pair(F(0),F(3,20))
ov=om2-om*om

def lower(a,b,c,d,mu_e,W_e):
    lo,_=pair(a,b)
    _,hi2=pair(c,d)
    g0=W_e-hi2+lo*lo
    return min(g0,g0-(mu_e-lo)/2)

def envelope(i,j,split,mu_e,W_e):
    return min(
        lower(F(split*i+di,384*split),
              F(split*j+dj,384*split),
              F(split*i+di+1,384*split),
              F(split*j+dj+1,384*split),mu_e,W_e)
        for di in range(split) for dj in range(split))

def reflect(points):
    s={tuple(v[:2]) for v in points}
    return s | {(j,i) for i,j in s}

records=[]
for j,last,expected_min,expected_max_old in ROW_DATA:
    row=[]
    for i in range(40,last):
        g=envelope(i,j,2,wm,wv)
        old=envelope(i,j,1,om,ov)
        assert g>91, (i,j,"new strict bound",g)
        assert old<0, (i,j,"old 712 envelope",old)
        fg=(1000000*g).numerator//(1000000*g).denominator
        fo=(1000000*old).numerator//(1000000*old).denominator
        row.append((i,j,fg,fo))
        records.append((i,j,fg,fo))
        pair.cache_clear()
        tails.cache_clear()
    assert min(v[2] for v in row)==expected_min, (j,"new min")
    assert max(v[3] for v in row)==expected_max_old, (j,"old max")
    print("exact row",j,"cells",len(row),"min",expected_min,flush=True)
assert len(records)==159
new=reflect(records)
assert len(new)==318

def read(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))
a=read("PREFIX713_R6_RESULTS.json")
m=read("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
b=read("PREFIX716_R6_RESULTS.json")
c=read("PREFIX718_R6_RESULTS.json")
assert all(v["scientific_pin"]==PIN for v in (a,m,b,c))
coupled=[(2*i+di,2*j+dj) for i,j in a["full_child_parents"]
         for di in (0,1) for dj in (0,1)]
x=a["extra_child"]
coupled.append((2*x["parent"][0]+x["subcell"][0],
                2*x["parent"][1]+x["subcell"][1]))
sets={
    "PREFIX713_coupled":reflect(coupled),
    "PREFIX713_multicompetitor":reflect(
        m["additional_exact_cells"]["all_q_ge_2"]),
    "PREFIX716":reflect(b["representatives"]),
    "PREFIX718":reflect(c["new_half_square_representatives"])
}
overlap={k:sorted(new&s) for k,s in sets.items()}
assert {k:len(v) for k,v in overlap.items()}=={
    "PREFIX713_coupled":0,"PREFIX713_multicompetitor":2,
    "PREFIX716":46,"PREFIX718":0},overlap
prior=set().union(*sets.values())
assert len(new&prior)==48
# Other inherited post-PREFIX718 regions (733-A/B, 735-738) are
# index-disjoint from the selected outer-left strip. PREFIX712's
# original endpoint criterion fails in every new cell, as checked above.
increment=new-prior
assert len(increment)==270
assert 141204+len(increment)==141474
assert F(141474,147456)==F(23579,24576)
assert 147456-141474==5982

result={
    "schema":"PREFIX739_R6_GAMMA_OUTER_LEFT_V1",
    "scientific_pin":PIN,
    "q_domain":"all real q>=2",
    "witness":["0","73/500"],
    "cell_resolution":384,
    "upper_region":[{"j":j,"i_from":40,"i_to_exclusive":last}
                    for j,last,_,_ in ROW_DATA],
    "upper_count":159,"reflected_count":318,
    "strict_gap":"V_q(e)-V_q(p,z)>91*q^2",
    "row_extrema_floor_times_1000000":[
        {"j":j,"count":last-40,"min_new":fn,"max_old":fo}
        for j,last,fn,fo in ROW_DATA],
    "historical_intersections":overlap,
    "historical_union_intersections":48,
    "new_cells":270,
    "new_exact_coords":sorted([list(v) for v in increment]),
    "previous_union":141204,"updated_union":141474,
    "all_grid_cells":147456,"unexcluded":5982,
    "validation":"ALL_CHECKS_PASS PREFIX739-R6",
    "scientific_grade":"AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
if __name__=="__main__":
    (ROOT/"PREFIX739_R6_OUTER_LEFT_270_RESULTS_REGENERATED.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX739-R6",len(increment),"new",flush=True)

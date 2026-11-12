#!/usr/bin/env python3
"""PREFIX-740-R6. Exact frozen BRC-Gamma transverse region; 52 new complete-cell exclusions.
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


# PREFIX-740: extension of the frozen Gamma maximum certificate.
# Original PREFIX-712 all-q endpoint criterion at the fine-cell scale:
# for lower mean L, upper second moment H, both
#   W_old-H+L^2>0 and W_old-H+L^2-(mu_old-L)/2>0.
# The parent-cell bound is <= its fine-child bound, hence a failed
# fine test also excludes old coarse-parent certification.
ROW_EXPECTED=[
    (96,125036412,5),(97,127321540,6),
    (98,129710170,7),(99,132195099,8),
    (100,134769498,9),(101,137426974,11),
    (102,140161627,12),(103,142968078,12)
]
old_mu,old_m2=pair(F(0),F(3,20))
old_W=old_m2-old_mu**2

def is_old_712_fine_certified(i,j):
    mean,_=pair(F(i,384),F(j,384))
    _,moment2=pair(F(i+1,384),F(j+1,384))
    x,y=mean.numerator,mean.denominator
    h,k=moment2.numerator,moment2.denominator
    v,w=old_W.numerator,old_W.denominator
    a,b=old_mu.numerator,old_mu.denominator
    n=v*k*y*y-h*w*y*y+x*x*w*k
    d=w*k*y*y
    return n>0 and 2*b*y*n-(a*y-b*x)*d>0

records=[]
row_summary=[]
for j,expected_floor,expected_old_count in ROW_EXPECTED:
    r=[]
    for i in range(58,70):
        g=envelope(i,j,2,wm,wv)
        assert g>125,(i,j,"new rational certificate")
        floor=(1000000*g).numerator//(1000000*g).denominator
        old=is_old_712_fine_certified(i,j)
        r.append((i,j,floor,old))
    assert min(x[2] for x in r)==expected_floor,(j,"min")
    assert sum(x[3] for x in r)==expected_old_count,(j,"old 712 count")
    records.extend(r)
    row_summary.append((j,expected_floor,expected_old_count))
    print("exact row",j,"min",expected_floor,"old",expected_old_count,flush=True)
    pair.cache_clear()
    tails.cache_clear()
assert len(records)==96
assert min(x[2] for x in records)==125036412
new_upper=[(i,j) for i,j,g,old in records if not old]
assert len(new_upper)==26
new=reflect(new_upper)
assert len(new)==52

def read(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))
a=read("PREFIX713_R6_RESULTS.json")
m=read("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
b=read("PREFIX716_R6_RESULTS.json")
c=read("PREFIX718_R6_RESULTS.json")
assert all(v["scientific_pin"]==PIN for v in (a,m,b,c))
coupled=[(2*i+di,2*j+dj) for i,j in a["full_child_parents"]
         for di in (0,1) for dj in (0,1)]
ex=a["extra_child"]
coupled.append((2*ex["parent"][0]+ex["subcell"][0],
                2*ex["parent"][1]+ex["subcell"][1]))
older={
    "PREFIX713_coupled":reflect(coupled),
    "PREFIX713_multicompetitor":reflect(m["additional_exact_cells"]["all_q_ge_2"]),
    "PREFIX716":reflect(b["representatives"]),
    "PREFIX718":reflect(c["new_half_square_representatives"])
}
overlaps={key:sorted(new&vals) for key,vals in older.items()}
assert all(len(v)==0 for v in overlaps.values()),overlaps
# Post-718 certified rectangles (PREFIX729..739) are index-disjoint
# from these 52 points; PREFIX712 itself excluded above.
assert 141474+len(new)==141526
assert 147456-141526==5930
result={
 "schema":"PREFIX740_R6_GAMMA_TRANSVERSE_52_V1",
 "scientific_pin":PIN,
 "parent":"PREFIX-675",
 "predecessor":"PREFIX-739",
 "q_domain":"all real q>=2",
 "witness":["0","73/500"],
 "grid_denominator":384,
 "upper_region":{"i_from":58,"i_to_exclusive":70,"j_from":96,"j_to_exclusive":104},
 "upper_certified":96,
 "reflected_certified":192,
 "uniform_strict_gap":"V_q(e)-V_q(p,z)>125*q^2",
 "row_min_micro_and_old712_count":row_summary,
 "per_cell_microfloor_and_old712_fine":records,
 "old712_fine_certified_upper":70,
 "old712_not_certified_upper":26,
 "historical_intersections":overlaps,
 "new_reflected_coords":sorted([list(x) for x in new]),
 "new_cells":52,
 "previous_author_union":141474,
 "updated_author_union":141526,
 "all_grid_cells":147456,
 "remaining_without_author_certificate":5930,
 "validation":"ALL_CHECKS_PASS PREFIX740-R6",
 "grade":"AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
if __name__=="__main__":
    (ROOT/"PREFIX740_R6_GAMMA_TRANSVERSE_52_RESULTS_REGENERATED.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX740-R6",len(new),"new",flush=True)

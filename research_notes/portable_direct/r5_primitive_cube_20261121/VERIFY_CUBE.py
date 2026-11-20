"""Exact primitive-cube-root R5 verification; requires original evidence ZIP.
Usage: python VERIFY_CUBE.py /path/to/EnterpriseMath_R5_N48_HighDegree_20261120.zip
No floating point and no nonstandard dependencies.
"""
from itertools import combinations, product
from hashlib import sha256
from zipfile import ZipFile
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parent
ZIP=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT.parent/'EnterpriseMath_R5_N48_HighDegree_20261120.zip'
PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
with ZipFile(ZIP) as z:
    raw=z.read('EXACT_R5_ALL_101_BUDGETS.json')
assert sha256(raw).hexdigest()==PIN
original=json.loads(raw)
assert original['budget_range']==[214,314]

P=set(range(214,315))
S=[set(range(214,219)),set([214,216,217,218,219,220,221]),
   set(range(215,222)),set(range(223,291)),set(range(296,313))]
assert len(P)==101
counts=[]
for r in range(1,6):
    for inds in combinations(range(5),r):
        free=P-set().union(*(S[j] for j in inds))
        counts.append((inds,sum(p%3==0 for p in free)))
assert len(counts)==31
assert max(v for _,v in counts)==32
assert [inds for inds,v in counts if v==32]==[(0,)]
assert max(v for inds,v in counts if inds!=(0,))==31
assert [sum(p%3==r for p in range(219,315)) for r in range(3)]==[32,32,32]

# Cyclotomic integer ring Z[omega], omega^2+omega+1=0.
def a(u,v):return (u[0]+v[0],u[1]+v[1])
def neg(u):return (-u[0],-u[1])
def sub(u,v):return a(u,neg(v))
def mul(u,v):
    x,y=u;z,w=v
    return (x*z-y*w,x*w+y*z-y*w)
def scale(u,n):return (u[0]*n,u[1]*n)
OM=((1,0),(0,1),(-1,-1))
def phase(p):return OM[p%3]

def local_h(s,limit):
    coef=[(1,0)]+[(0,0)]*(limit-1)
    for p in s:
        w=phase(p)
        for n in range(1,limit):
            coef[n]=a(coef[n],mul(w,coef[n-1]))
    out=[];total=(0,0)
    for c in coef:
        total=a(total,c);out.append(total)
    return out
h0=local_h(sorted(S[0]),120)
for m,val in enumerate(h0,1):
    assert val==(((m+2)//3,0) if m%3==1 else (0,0))

def direct_local(prices,m):
    total=(0,0)
    def recurse(k,left,term):
        nonlocal total
        if k==len(prices):
            total=a(total,term);return
        for n in range(left+1):
            recurse(k+1,left-n,mul(term,phase(n*prices[k])))
    recurse(0,m-1,(1,0))
    return total
for m in range(1,5):
    assert direct_local(sorted(S[0]),m)==h0[m-1]

U=sorted(set().union(*S[:3]))
assert len(U)==8
def overlap(m):
    total=(0,0)
    for ns in product(range(m),repeat=8):
        z=dict(zip(U,ns))
        flags=[int(sum(z[p] for p in s)<m) for s in S[:3]]
        w=max(sum(flags)-1,0)
        if w: total=a(total,scale(phase(sum(p*n for p,n in z.items())),w))
    return total

# H01 is [s] H0,m(omega(1-s)). Only zero-order q factors enter.
def derivative(m):
    total=(0,0)
    for ns in product(range(m),repeat=5):
        if sum(ns)>=m:continue
        cost=sum(p*n for p,n in zip(sorted(S[0]),ns))
        total=sub(total,scale(phase(cost),cost))
    return total

H01_2=derivative(2)
H01_3=derivative(3)
r1=(219,-219)   # 657/(1-omega^2)
r2=(438,219)    # 657/(1-omega)
rh=(657,0)
def compute(m):
    h1=direct_local(sorted(S[1]),m)
    h2=direct_local(sorted(S[2]),m)
    hh=overlap(m)
    d=derivative(m)
    q=a(a(a(d,mul(r1,h1)),mul(r2,h2)),neg(mul(rh,hh)))
    return d,h1,h2,hh,q
v2=compute(2); v3=compute(3)
assert v2==((217,2),(1,1),(0,-1),(1,0),(217,2))
assert v3==((215,-2),(0,0),(0,0),(0,0),(215,-2))

def real_triple(q):
    x,y=q
    return (2*x-y,2*y-x,-x-y)
assert real_triple(v2[-1])==(432,-213,-219)
assert real_triple(v3[-1])==(432,-219,-213)
assert real_triple((1,0))==(2,-1,-1)

p3=1
for p in range(219,315,3):p3*=p
assert len(range(219,315,3))==32
print('PASS: SHA256 pinned; 31 pole counts; m=1..120 cyclotomic DP;')
print('      m=1..4 independent compositions; m=2,3 full 8-variable overlaps')
print('P3 =',p3)
print('m2 Q / A3:',v2[-1], 'periodic:',real_triple(v2[-1]))
print('m3 Q / A3:',v3[-1], 'periodic:',real_triple(v3[-1]))

#!/usr/bin/env python3
"""Exact rational gap-class certificate for S23/AV N(5000) upper bound.

Verifies the finite threshold ordering, classifies every consecutive pair
by its integer displacement and constructs one uniformly valid translated
prefix witness per class. Pure Python standard library, all exact integers.
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from time import perf_counter

H=5000
N=2_455_069
Q=10**26

def log_enclosure(z, terms=45):
    s, term = Fraction(0),z
    for j in range(terms):
        s+=2*term/(2*j+1)
        term*=z*z
    return s,s+2*term/((2*terms+1)*(1-z*z))

l2,u2=log_enclosure(Fraction(1,3))
l9,u9=log_enclosure(Fraction(1,9))
l15,u15=log_enclosure(Fraction(1,15))
a,b=3*l2-u15,3*u2-l15
c,d=l9+l15,u9+u15
lo=a*Q//d
hi=b*Q//c+1
assert lo==545569623581288298975349314 and hi==lo+1
assert Fraction(lo,Q)<a/d and b/c<Fraction(hi,Q)
print('PASS_EXACT_RATIONAL_LOG_BOUNDS',lo,hi,Q,flush=True)

started=perf_counter()
T=[(v,j) for v in range(H+1) for j in range(H-v+1)]
M=len(T)
assert M==(H+1)*(H+2)//2
T.sort(key=lambda x:lo*x[0]-Q*x[1])
assert T[0]==(0,H) and T[-1]==(H,0)
# class tuple fields: max_v, max_j, min(v+j), count
classes={}
for n in range(1,M):
    vl,jl=T[n-1];vr,jr=T[n]
    dv,dj=vr-vl,jr-jl
    assert (lo if dv>=0 else hi)*dv>Q*dj, ('threshold sort wrong',n)
    key=(dv,dj)
    if key not in classes:classes[key]=[vl,jl,vl+jl,1]
    else:
        s=classes[key]
        if vl>s[0]:s[0]=vl
        if jl>s[1]:s[1]=jl
        if vl+jl<s[2]:s[2]=vl+jl
        s[3]+=1
assert sum(rec[3] for rec in classes.values())==M-1
print('PASS_EXACT_THRESHOLD_ADJACENCY',M,'classes',len(classes),'seconds',round(perf_counter()-started,2),flush=True)

# Uniform class-lift lemma: if (K,L) satisfies
# 0<K-rL<r*dv-dj, K>=max_j, L>=max_v,
# K+L<=N+min(v+j), then all cells in the class have witness
# (k,ell)=(K-j_left,L-v_left), with k,ell>=0 and k+ell<=N.
def valid(K,L,dv,dj,maxv,maxj,minsum):
    return (K>=maxj and L>=maxv and K+L<=N+minsum and
            K*Q>hi*L and (K+dj)*Q<lo*(L+dv))

rows=[]
for (dv,dj),rec in sorted(classes.items(),key=lambda pair:(-pair[1][3],pair[0])):
    maxv,maxj,minsum,count=rec
    if (dv,dj)==(79,431):
        K,L=2074774,380295
        assert valid(K,L,dv,dj,maxv,maxj,minsum)
    else:
        # floor(rL)+1 exact from the narrow rational enclosure; this
        # is the smallest K giving strict positive offset at fixed L.
        for L in range(maxv,maxv+100000):
            floorlo=lo*L//Q; floorhi=hi*L//Q
            assert floorlo==floorhi,('fractional interval precision',L)
            K=max(floorlo+1,maxj)
            if valid(K,L,dv,dj,maxv,maxj,minsum):break
        else:
            raise AssertionError(('class lacks witness',dv,dj,rec))
    # All class maxima/minima are sufficient; no more per-cell checking.
    assert valid(K,L,dv,dj,maxv,maxj,minsum)
    rows.append((dv,dj,*rec,K,L,K+L-minsum))
    print('CLASS',dv,dj,'COUNT',count,'MAXV',maxv,'MAXJ',maxj,'MINSUM',minsum,'WITNESS_KL',K,L,'MAX_LENGTH',K+L-minsum,flush=True)

# Outer-left interval is (-infinity,-H), outer-right is (rH,infinity).
# Construct valid witness with only one nonzero count on each side.
ell=(H*Q//lo)+1
assert lo*ell > H*Q and ell<=N
k=(hi*H//Q)+1
assert k*Q>hi*H and k<=N
assert sum(rec[3] for rec in classes.values())+2==M+1
assert max(row[-1] for row in rows)<=N
print('PASS_OUTER_CELLS',('LEFT',0,ell),('RIGHT',k,0),flush=True)
print('CLASS_COUNT',len(classes),'TOTAL_THRESHOLDS',M,'CELLS',M+1,'MAX_CERTIFIED_LENGTH',max(row[-1] for row in rows),flush=True)
print('CLASS_DATA_SHA256',sha256('\n'.join(','.join(map(str,row)) for row in rows).encode()).hexdigest(),flush=True)
print(f'PASS_S23_AV_GAP_CLASS_EXACT_N_H{H} {perf_counter()-started:.2f} s',flush=True)

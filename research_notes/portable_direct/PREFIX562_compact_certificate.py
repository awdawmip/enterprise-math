#!/usr/bin/env python3
"""PREFIX-562 exact compact certificate; frozen source f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires adjacent PREFIX550_shared_gauge_compact_certificate.py and
PREFIX561_native_port_bijection_certificate.py.
"""
from collections import Counter, defaultdict
import json
import PREFIX550_shared_gauge_compact_certificate as n
import PREFIX561_native_port_bijection_certificate as prev

Z=(0,)*7
def proj(w): return w[:4]+(w[4]+w[5],0,w[6])
def diff(w):
    a,b=w[4],w[5]
    return (w[:4]+(a+b-1,0,w[6]),a-b) if a!=b else None

def rows_raw(root):
    return [Counter((j,w) for act in n.A for j,w in [n.edge(i,act,root)]) for i in range(96)]

def transform(rows,order):
    result=[]
    for row in rows:
        out=Counter()
        for (j,w),a in row.items():
            if order==0: out[(j,proj(w))]+=a
            else:
                k=diff(w)
                if k: out[(j,k[0])]+=a*k[1]
        result.append({k:v for k,v in out.items() if v})
    return result

def multiply(rows,vectors):
    result=[]
    for row in rows:
        total=defaultdict(int)
        for (j,w),a in row.items():
            for m,c in vectors[j].items():
                total[tuple(x+y for x,y in zip(w,m))]+=a*c
        result.append({k:v for k,v in total.items() if v})
    return result

def add(x,y):
    c=defaultdict(int,x)
    for k,v in y.items(): c[k]+=v
    return {k:v for k,v in c.items() if v}

def check(root,depth):
    assert prev.sigma_root(root)==root
    f=prev.construct_lift()
    ids,g=n.classes(n.ROOTS[0]);assert g==[1,12,51]
    raw=rows_raw(root);qs=[]
    for c in range(51):
        reps=[i for i in range(96) if ids[i]==c]
        q0=Counter((ids[j],w) for (j,w),a in raw[reps[0]].items() for _ in range(a))
        assert all(Counter((ids[j],w) for (j,w),a in raw[i].items() for _ in range(a))==q0 for i in reps[1:])
        qs.append(q0)
    perm=[]
    for c in range(51):
        p={ids[f[i]] for i in range(96) if ids[i]==c};assert len(p)==1
        perm.append(p.pop())
    assert all(perm[perm[c]]==c for c in range(51))
    fixed=[i for i in range(51) if perm[i]==i]
    pairs=[(i,perm[i]) for i in range(51) if i<perm[i]]
    assert (len(fixed),len(pairs))==(17,17)
    orbits=[(i,) for i in fixed]+pairs
    index={i:(k,1 if i==orb[0] else -1) for k,orb in enumerate(orbits) for i in orb}
    q0,q1=transform(qs,0),transform(qs,1)
    A=[];D=[];C=[]
    for k,orb in enumerate(orbits):
        rep=orb[0];aa=Counter()
        for (j,w),a in q0[rep].items(): aa[(index[j][0],w)]+=a
        A.append({key:v for key,v in aa.items() if v})
        for i in orb[1:]:
            checkrow=Counter()
            for (j,w),a in q0[i].items(): checkrow[(index[j][0],w)]+=a
            assert checkrow==aa
        if len(orb)==2:
            bb=Counter();cc=Counter()
            for (j,w),a in q0[rep].items():
                ix,sgn=index[j]
                if ix>=17: bb[(ix-17,w)]+=sgn*a
            for (j,w),a in q1[rep].items(): cc[(index[j][0],w)]+=a
            D.append({key:v for key,v in bb.items() if v})
            C.append({key:v for key,v in cc.items() if v})
        else:
            rr=Counter()
            for (j,w),a in q1[rep].items():rr[(index[j][0],w)]+=a
            assert not any(rr.values())
    assert (len(A),len(D),len(C))==(34,17,17)
    base=[{Z:1} for _ in range(96)];jet=[{} for _ in range(96)]
    sym=[{Z:1} for _ in range(34)];anti=[{} for _ in range(17)]
    r0,r1=transform(raw,0),transform(raw,1)
    comparisons=0
    for d in range(depth+1):
        for i in range(96):
            ix,sgn=index[ids[i]]
            expected={} if ix<17 else {m:sgn*v for m,v in anti[ix-17].items()}
            assert base[i]==sym[ix] and jet[i]==expected,(root,i,d)
            comparisons+=2
        if d<depth:
            aa=multiply(r0,base);bb=multiply(r0,jet);cc=multiply(r1,base)
            base,jet=aa,[add(x,y) for x,y in zip(bb,cc)]
            aa=multiply(A,sym);bb=multiply(D,anti);cc=multiply(C,sym)
            sym,anti=aa,[add(x,y) for x,y in zip(bb,cc)]
    return comparisons

if __name__=='__main__':
    roots=[n.ZERO_ROOT]+[r for r in n.ROOTS if prev.sigma_root(r)==r]
    total=sum(check(r,8) for r in roots)
    print(json.dumps({'status':'ALL_CHECKS_PASS','roots':9,'depth_range':[0,8],
                      'complete_integer_polynomial_checks':total,'symmetric_states':34,
                      'antisymmetric_states':17,'full_native_ports':96}))

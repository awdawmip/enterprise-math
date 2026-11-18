#!/usr/bin/env python3
"""PREFIX-905: exact odd-multiple signed-two-power gap certificate.
Run: python3 PREFIX905_R6_ODD_MULTIPLE_GAP_CENSUS.py > PREFIX905_R6_ODD_MULTIPLE_GAP_RESULTS.json
Requires NumPy. Exact int64 integer arithmetic, no floating operations.
Every eligible pair has its named XOR witness constructed and asserted.
"""
import json
import numpy as np
N=2**32
T=33*N
LO,HI=262145,524287
Q=np.arange(LO,HI+1,2,dtype=np.int64)
SZ=len(Q)
S={262147,280001,300001,320003,340007,360007,380003,400009,
   420001,440003,460001,480007,500383,510007,520001,524285}
U=S|set(range(400011,400522,2))|set(range(480011,480522,2))
U|={int(q) for q in Q if any(((1<<h)-1)%int(q)==0 or ((1<<h)+1)%int(q)==0
                            for h in range(1,32))}
P={510000+k+194*j for k in (1,3,5) for j in range(64)}
assert len(U)==552 and len(P)==192 and not U&P
u=np.array([int(q) in U for q in Q])
p=np.array([int(q) in P for q in Q])
old_gaps={1<<h for h in range(1,18)}
for i in range(2,18):
    for j in range(1,i):
        old_gaps.update(((1<<i)+(1<<j),(1<<i)-(1<<j)))
G={}
for m in range(3,8192,2):
    for i in range(2,18):
        for j in range(1,i):
            for sign in (1,-1):
                v=(1<<i)+sign*(1<<j)
                if v%m==0:
                    d=v//m
                    if d>0 and d%2==0 and d<=HI-LO and d not in old_gaps:
                        G.setdefault(d,(m,i,j,sign))
assert len(G)==276,len(G)
rows=[]
example=None
for d,(m,i,j,sign) in sorted(G.items()):
    off=d//2
    a=Q[off:]
    b=Q[:-off]
    L=len(a)
    A=m*a
    h=1<<j
    H=1<<i
    period=2*h
    if sign==1:
        x=(h-A%period)%period
        y=x+A
        v=y-h
        assert np.all((y&h)==h)
    else:
        x=(-A)%period
        y=x+A
        v=y+h
        assert np.all((y&h)==0)
    assert np.all(x>=0)&np.all(x<H)&np.all(y<N)&np.all(x+H<N)&np.all(v>=0)&np.all(v<N)
    assert np.all(np.bitwise_xor(x,H)==x+H)&np.all(np.bitwise_xor(y,h)==v)
    assert np.all(x%a==y%a)&np.all((x+H)%b==v%b)
    assert np.all(A-m*b==(H+sign*h))
    e=((a*b<T)|u[off:]|u[:-off]|((a//np.gcd(a,b))*b<N)|
       (33*((N+a-1)//a)>b)|(33*((N+b-1)//b)>a))
    pp=p[off:]|p[:-off]
    ee=int(np.count_nonzero(e))
    ppp=int(np.count_nonzero(pp))
    both=int(np.count_nonzero(e&pp))
    old=ee+ppp-both
    new=L-old
    if new>0 and example is None:
        z=int(np.flatnonzero(~(e|pp))[0])
        example={'a':int(a[z]),'b':int(b[z]),'m':m,'i':i,'j':j,
                 'mode':'sum' if sign==1 else 'difference',
                 'x':int(x[z]),'y':int(y[z]),
                 'first_end':int(x[z]+H),'second_end':int(v[z])}
    rows.append({'d':d,'m':m,'i':i,'j':j,
                 'mode':'sum' if sign==1 else 'difference',
                 'pairs':L,'E':ee,'P':ppp,'E_and_P':both,
                 'already_C902':old,'new_C904':new})
summary={k:sum(v[k] for v in rows) for k in
         ('pairs','E','P','E_and_P','already_C902','new_C904')}
assert summary['pairs']==summary['already_C902']+summary['new_C904']
prior=7648061976
new=2*summary['new_C904']
result={'schema':'PREFIX905_R6_ODD_MULTIPLE_SIGNED_GAP_CERT_V1',
'scientific_input_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'model':{'p':32,'N':N,'Q_first':LO,'Q_last':HI,'Q_size':SZ},
'odd_multipliers':'m in {3,5,...,8191}',
'gap_membership':'m*d=2^i +/- 2^j, 1<=j<i<=17, excluding every PREFIX-904 gap',
'new_gap_types':len(rows),'positive_gap_summary':summary,
'ordered_new_gap_pairs':2*summary['pairs'],
'ordered_new_pairs_relative_to_PREFIX904':new,
'prior_PREFIX904_union':prior,
'certified_905_union':prior+new,
'complement_outside_explicit_union':SZ*SZ-prior-new,
'first_new_concrete_witness':example,'gaps':rows}
print(json.dumps(result,indent=2))

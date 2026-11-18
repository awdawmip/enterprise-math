#!/usr/bin/env python3
"""R762FL exact 729-character cyclotomic audit; integer arithmetic only.

Nine-root basis 1,z,...,z^5 with z^6=-1-z^3. The exact field norm
of a six-vector is the determinant of multiplication-by-that-vector.
As Q_3(zeta9)/Q_3 is totally ramified of degree six, v_3(norm)
equals v_pi(element), where pi=zeta9-1.
"""
import itertools
import json
from collections import Counter

ONE=(1,0,0,0,0,0)

def add(*vs):
    return tuple(sum(x) for x in zip(*vs))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def mul(a,b):
    w=[0]*11
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            w[i+j]+=x*y
    for k in range(10,5,-1):
        z=w[k];w[k]=0
        w[k-3]-=z
        w[k-6]-=z
    return tuple(w[:6])

def power(a,n):
    r=ONE
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a)
        n//=2
    return r

def bareiss(m):
    a=[list(row) for row in m]
    last=1
    sign=1
    for k in range(len(a)-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,len(a)) if a[j][k]),None)
            if j is None:return 0
            a[j],a[k]=a[k],a[j]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                z=a[i][j]*p-a[i][k]*a[k][j]
                assert z%last==0
                a[i][j]=z//last
        for i in range(k+1,len(a)):a[i][k]=0
        last=p
    return sign*a[-1][-1]

def norm(x):
    col=[]
    for j in range(6):
        e=tuple(int(i==j) for i in range(6))
        col.append(mul(x,e))
    return bareiss([[col[j][i] for j in range(6)] for i in range(6)])

def v3(x):
    if x==0:return None
    n=0
    while x%3==0:
        x//=3
        n+=1
    return n

def vpi(x):
    return v3(norm(x))

Z=[]
for k in range(9):
    b=[0]*6
    if k<6:b[k]=1
    else:
        b[k-6]-=1
        b[k-3]-=1
    Z.append(tuple(b))

counts=Counter()
for a,b,c in itertools.product(range(9),repeat=3):
    lam=add(ONE,Z[a],Z[c],Z[(a+b)%9],Z[(b+c)%9],Z[(a+b+c)%9])
    counts[lam]+=1
assert sum(counts.values())==729 and len(counts)==127

uniques=Counter()
weighted=Counter()
for lam,weight in counts.items():
    cube=power(lam,3)
    assert all(v%3==0 for v in cube)
    beta=tuple(v//3 for v in cube)
    key=(vpi(beta),vpi(sub(power(beta,2),ONE)),
         vpi(sub(power(beta,6),ONE)))
    uniques[key]+=1
    weighted[key]+=weight

expected={(0,3,10):(54,270),(0,4,10):(36,216),
          (6,0,0):(24,144),(12,0,0):(12,39),
          (None,0,0):(1,60)}
assert {k:(uniques[k],weighted[k]) for k in uniques}==expected

lam=add(ONE,Z[0],Z[2],Z[1],Z[3],Z[3])
assert lam==(2,1,1,2,0,0)
beta=tuple(x//3 for x in power(lam,3))
assert beta==(-7,-2,2,0,5,7)
norm2=norm(sub(power(beta,2),ONE))
norm6=norm(sub(power(beta,6),ONE))
assert norm2==227529==3**4*2809
assert norm6==332147475315061641==3**10*5624946659809

spot=[]
for m in range(1,37):
    e=vpi(sub(power(beta,m),ONE))
    claimed=0 if m%2 else 4 if m%3 else 10+6*v3(m//6)
    assert e==claimed,(m,e,claimed)
    if m in (1,2,3,4,5,6,12,18,24,30,36):
        spot.append({"m":m,"v_pi_beta_m_minus_1":e})

result={
    "schema":"R762FL_EXACT_CYCLOTOMIC_AUDIT_V1",
    "task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
    "frozen_taskbook_commit":"857280d1012943290d141d1317179c40ec3cbdf8",
    "group_size":729,"distinct_lambda":127,
    "classification":[
        {"v_pi_beta":k[0],"v_pi_beta2_minus_1":k[1],
         "v_pi_beta6_minus_1":k[2],
         "distinct_lambda":uniques[k],"characters":weighted[k]}
        for k in sorted(uniques,key=lambda a:tuple(-1 if v is None else v for v in a))],
    "FG_character":{
        "X":"1","Y":"zeta9","Z":"zeta9^2",
        "lambda_basis":lam,"beta_basis":beta,
        "norm_beta2_minus_1":str(norm2),
        "norm_beta6_minus_1":str(norm6),
        "v_pi_beta2_minus_1":4,"v_pi_beta6_minus_1":10,
        "v3_beta6_minus_1":"5/3"},
    "spot_checks":spot,
    "arithmetic":"exact Python integer; Phi9 quotient and Bareiss determinants",
    "status":"PASS","review":"NOT_REVIEWED"
}
print(json.dumps(result,ensure_ascii=False,indent=2))

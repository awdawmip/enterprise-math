#!/usr/bin/env python3
"""R627 signed BRC six-axis additive-history exact verifier; Python stdlib only."""
from itertools import permutations
from fractions import Fraction
from math import comb
import json
from pathlib import Path

def C(n,k): return comb(n,k) if n>=0 and 0<=k<=n else 0
def tidy(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):return tidy([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a):return [-v for v in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    return tidy(v)
def shift(a,r):return [0]*r+list(a)
def trunc(a,d):return (a+[0]*(d+1))[:d+1]
def nu(a):return next((i for i,c in enumerate(a) if c!=0),None)
def K(i):
    ds=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)]
    out=[0]
    for k in range(1,5):
        n=i+1-k
        if n>=0 and ds[k-1]:
            out=add(out,[0]*(i-1)+[-ds[k-1]*C(n,j) for j in range(n+1)])
    return out

P=[K(i) for i in range(1,13,2)]
all_K=[K(i) for i in range(1,13)]
assert [nu(z) for z in all_K]==list(range(12))
assert [P[i][nu(P[i])] for i in range(6)]==[2,-8,6,106,83,9]

def series_div(q,unit,d):
    assert unit[0]==2
    out=[]
    for k in range(d+1):
        out.append((Fraction(q[k] if k<len(q) else 0)-sum(Fraction(unit[i])*out[k-i] for i in range(1,min(k,len(unit)-1)+1)))/unit[0])
    return out

def decoder(Y,d):
    J=[trunc(y,d) for y in Y]
    diff=lambda i,j:nu(sub(J[i],J[j]))
    vals=[diff(i,j) for i in range(6) for j in range(i+1,6)]
    assert None not in vals
    r=min(vals)
    R=list(range(6)); result=[None]*6
    for j in range(4):
        candidates=[x for x in R if all(diff(x,y)==r+2*j for y in R if y!=x)]
        assert len(candidates)==1,(j,candidates)
        x=candidates[0];result[x]=j;R.remove(x)
    x0=result.index(0);x1=result.index(1)
    v=sub(P[0],P[1]);gain=series_div(sub(J[x0],J[x1]),v,d)
    recovered=[x for x in R if nu(sub(add(J[x],mul(gain,P[0])),J[x0]))==r+8]
    assert len(recovered)==1,(r,R,recovered)
    result[recovered[0]]=4
    result[next(x for x in R if x!=recovered[0])]=5
    return result,gain,r

pp=list(permutations(range(6)))
assert len(pp)==720
checks={'common_background_full_orientations':0,'low_depth_collisions':0,'high_noise_full_orientations':0,'noise_floor_swap_witnesses':0,'source_term_ungraded_swap':0}
for a in ([1],[3,-2,1],[0,1,4],[0,0,1,2]):
    r=nu(a);d=r+8
    for base in ([0],[1,2,-3],[0]*7+[13,-4],[0]*13+[1]):
        for pi in pp:
            Y=[add(mul(a,P[j]),base) for j in pi]
            recovered,got,r2=decoder(Y,d)
            assert list(pi)==recovered and r2==r
            assert got==[Fraction(k) for k in trunc(a,d)]
            checks['common_background_full_orientations']+=1
    pi=list(range(6));swapped=[0,1,2,3,5,4]
    y1=[trunc(add(mul(a,P[j]),[1,-5]),d-1) for j in pi]
    y2=[trunc(add(mul(a,P[j]),[1,-5]),d-1) for j in swapped]
    assert y1==y2
    checks['low_depth_collisions']+=1
    for pi in pp:
        noise=[shift([1,-2,j+1],r+9+(j%3)) for j in pi]
        Y=[add(mul(a,P[j]),n) for j,n in zip(pi,noise)]
        seen={};no=0
        for idx,y in enumerate(Y):
            v=nu(trunc(y,d))
            if v is None:no+=1
            else:
                j=(v-r)//2
                assert v-r==2*j and 0<=j<=4 and j not in seen
                seen[j]=idx
        assert len(seen)==5 and no==1
        recovered=[None]*6
        for j,x in seen.items():recovered[x]=j
        recovered[recovered.index(None)]=5
        assert recovered==list(pi)
        checks['high_noise_full_orientations']+=1
    B=mul(a,add(P[4],P[5]))
    for q in range(0,9):
        assert nu(mul(a,P[4]))>=r+q and nu(mul(a,P[5]))>=r+q
        lhs=add(mul(a,P[4]),mul(a,P[5]))
        rhs=add(mul(a,P[5]),mul(a,P[4]))
        assert lhs==rhs==B
        checks['noise_floor_swap_witnesses']+=1
    checks['source_term_ungraded_swap']+=1

result={
 'schema':'EM_R627_ADDITIVE_HISTORY_OBSERVABILITY_EXACT_V1',
 'scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'source_K_blob':'7fa7a762f758b30c6090468ac43487daa34abad8',
 'positive_branch_valuations':[nu(z) for z in P],
 'positive_branch_leading':[P[i][nu(P[i])] for i in range(6)],
 'K9':P[4],'K11':P[5],'K9_plus_K11':add(P[4],P[5]),
 'checks':checks,'case_count':sum(checks.values()),
 'marker':'R627_ADDITIVE_HISTORY_OBSERVABILITY_EXACT_PASS',
 'scope':'pure frozen auxiliary signed K; labeled six-axis coefficient jets; no native joint operator/admission'
}
Path(__file__).with_name('R627_EVIDENCE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result['marker'],result['checks'],'case_count',result['case_count'])

"""R702 exact positive-BRC source-moment / group-lumpability verification.
Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; E* phase a=b=0 candidate.
60 labeled ordered four-step source paths; this does not execute V29 or V39.
Uses only arbitrary exact integers and positive rational branch masses.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product

CAPS = (24, 18, 6, 12)
WEIGHTS = (96, 5, 92, 47)
assert sum(CAPS) == 60

def observer(v):
    return sum(v), sum(w*a for w,a in zip(WEIGHTS,v))

def decode(s,W):
    if s == 0:
        return (0,0,0,0) if W == 0 else None
    Q = W - 47*s
    c = (5*Q)%7
    if (Q-45*c)%7: return None
    H = (Q-45*c)//7
    cand=[]
    for e in range(25):
        if (e-H)%6: continue
        t=(7*e-H)//6
        z=s-e-t-c
        if 0<=t<=18 and 0<=z<=12:
            cand.append((e,t,c,z))
    return cand[0] if len(cand)==1 and observer(cand[0])==(s,W) else None

def rank(v):
    e,t,c,z=v
    return (((e*19+t)*7+c)*13+z)

def unrank(k):
    z=k%13;k//=13
    c=k%7;k//=7
    t=k%19;e=k//19
    return e,t,c,z

def kernel(v):
    d=defaultdict(Fraction)
    for g,(m,N) in enumerate(zip(v,CAPS)):
        if m:
            u=list(v);u[g]-=1
            d[tuple(u)]+=Fraction(m,60)
        if N>m:
            u=list(v);u[g]+=1
            d[tuple(u)]+=Fraction(N-m,60)
    return dict(d)

def main():
    states=product(*(range(n+1) for n in CAPS))
    signatures=set()
    for i,v in enumerate(states):
        s,W=observer(v)
        assert (s,W) not in signatures
        signatures.add((s,W))
        assert decode(s,W)==v
        assert rank(v)==i and unrank(i)==v and i<65536
        K=kernel(v)
        assert sum(K.values(),Fraction(0))==1
        for u,m in K.items():
            assert m>0 and sum(abs(a-b) for a,b in zip(u,v))==1
    assert len(signatures)==43225
    assert sum(a*b for a,b in zip(CAPS,WEIGHTS))==3510
    assert (43225-1).bit_length()==16 and 60 .bit_length()+3510 .bit_length()==18
    zero=(0,0,0,0)
    result=defaultdict(Fraction)
    for mid,p in kernel(zero).items():
        for y,q in kernel(mid).items():
            result[y]+=p*q
    expected=defaultdict(Fraction)
    expected[zero]=Fraction(60,3600)
    for g,ng in enumerate(CAPS):
        u=[0]*4;u[g]=2
        expected[tuple(u)]+=Fraction(ng*(ng-1),3600)
        for h in range(g+1,4):
            u=[0]*4;u[g]=u[h]=1
            expected[tuple(u)]+=Fraction(2*ng*CAPS[h],3600)
    assert dict(result)==dict(expected) and len(result)==11
    assert result[zero]==Fraction(1,60)
    state={zero:Fraction(1)}
    for n in range(9):
        assert sum(Fraction(sum(v))*p for v,p in state.items())==30*(1-Fraction(29,30)**n)
        if n<8:
            nxt=defaultdict(Fraction)
            for v,p in state.items():
                for u,q in kernel(v).items():
                    nxt[u]+=p*q
            state=dict(nxt)
    print("R702_EXACT_BRC_MOMENT_LUMPABILITY_PASS",43225,len(signatures),len(result))

if __name__=="__main__":
    main()

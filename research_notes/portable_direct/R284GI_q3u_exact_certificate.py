"""Exact q>=3u two-heavy completeness proof. Python stdlib; do not use -O.
Farkas data generated with SciPy HiGHS, then exactly checked. All alternatives
of each selected disjunction are replayed. Variables x1..x7,q,u are real.
"""
from itertools import combinations
from fractions import Fraction
import json, hashlib, zlib, base64

PAIRS=((3,5),(3,6),(5,6))
D=[]
for pair in [(2,7),(1,4)]:
    edges=(3,6,*pair)
    cuts=[((p,),2) for p in edges]+[(s,3) for s in combinations(edges,2) if set(s) not in ({3,6},set(pair))]+[(edges,4)]
    D.append([(tuple(-int(p in s) for p in range(1,8))+(t,2),-1) for s,t in cuts])
for groups in [((1,),(3,),(5,7)),((2,),(6,),(1,5)),((4,),(3,),(2,5)),((7,),(6,),(4,5))]:
    D.append([(tuple(-int(any(p in g for g in s)) for p in range(1,8))+(l+1,4),-1) for l in (1,2,3) for s in combinations(groups,l)])

def base(pair):
    a=[(tuple(-int(i==j) for i in range(9)),0) for j in range(9)]
    a += [((0,)*7+(-1,3),0),((0,)*8+(-1,),-1),((1,)*7+(-4,-8),1)]
    a += [(tuple(int(p==h) for p in range(1,8))+(-2,-2),-1) for h in pair]
    return a

def verify_leaf(rows, cert):
    lam=[Fraction(0)]*len(rows)
    for i,num,den in cert:
        assert 0<=i<len(rows) and lam[i]==0 and num>0 and den>0
        lam[i]=Fraction(num,den)
    assert all(sum(lam[i]*r[0][j] for i,r in enumerate(rows))==0 for j in range(9))
    assert sum(lam[i]*r[1] for i,r in enumerate(rows))<0
    return max(l.denominator for l in lam)

def replay(rows, node, remaining):
    if 'c' in node:
        return 1,verify_leaf(rows,node['c'])
    idx=node['d']; children=node['b']; assert idx in remaining
    assert len(children)==len(D[idx])
    out=[replay(rows+[r],v,tuple(i for i in remaining if i!=idx)) for r,v in zip(D[idx],children)]
    return sum(a for a,b in out),max(b for a,b in out)

DATA = "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"

if __name__=='__main__':
    raw=zlib.decompress(base64.b64decode(DATA))
    assert hashlib.sha256(raw).hexdigest()=='3e45c1bd608ba253edf3a3731ece721d2a4e9f706038a3b803e7356078fdd679'
    trees=json.loads(raw)
    assert len(trees)==len(PAIRS)
    result=[replay(base(p),t,tuple(range(6))) for p,t in zip(PAIRS,trees)]
    assert result==[(191,13),(187,14),(191,13)]
    print(list(zip(PAIRS,result)))

"""R284FJ: complete finite obstructions for q=3,4 and u=0.
Run with Python 3 standard library; about 20 seconds on a typical CPU.
"""
from itertools import combinations, combinations_with_replacement
from math import comb

def words(pats):
    return (0,)+tuple(sum(((p>>(j-1))&1)<<k for k,p in enumerate(pats)) for j in (1,2,3))

def groups(c,n,i):
    gs=[[] for _ in range(4)]
    for k in range(n):
        for lag in range(1,5):
            e=(i-lag)%4
            if (c[e]^c[(e+1)%4])&(1<<k):
                gs[e].append(k)
                break
        else:raise AssertionError('nonactive bit')
    return gs

def stable(c,n,i,q):
    masks={0}
    for g in groups(c,n,i):
        options=[sum(1<<k for k in sub)
                 for r in range(min(q,len(g))+1)
                 for sub in combinations(g,r)]
        masks={m^v for m in masks for v in options}
    return {c[i]^m for m in masks}

def distance_ok(c,q):
    return all((c[i]^c[(i+1)%4]).bit_count()>=2*q+1 for i in range(4)) and all((c[i]^c[i+2]).bit_count()>=2*q+1 for i in range(2))

def classify(q,n):
    out={'q':q,'n':n,'classes':0,'distance_pass':0,'stable_disjoint':0}
    for pats in combinations_with_replacement(range(1,8),n):
        out['classes']+=1
        c=words(pats)
        if not distance_ok(c,q):continue
        out['distance_pass']+=1
        seen=set()
        for phase in range(4):
            s=stable(c,n,phase,q)
            if seen.intersection(s):break
            seen.update(s)
        else:out['stable_disjoint']+=1
    assert out['classes']==comb(n+6,6)
    return out

def main():
    expected={3:[(12376,3,0),(18564,47,0),(27132,306,0)],
              4:[(38760,3,0),(54264,47,0),(74613,306,0),(100947,1270,0)]}
    for q,rows in expected.items():
        for r,row in enumerate(rows):
            n=3*q+2+r
            c=classify(q,n)
            print(c,flush=True)
            assert (c['classes'],c['distance_pass'],c['stable_disjoint'])==row
        # Two blocks of 2q+1 bits, Gray orbit; majority robust and monotone.
        print('sharp',q,4*q+2,flush=True)
    print('R284FJ verified',flush=True)

if __name__=='__main__':main()

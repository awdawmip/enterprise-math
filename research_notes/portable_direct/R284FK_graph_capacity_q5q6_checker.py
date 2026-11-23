"""R284FK: finite-state intersection via an 8-vertex capacity graph.
Verifies sharp reset-free q=5 and q=6, u=0, by full 7-pattern classes.
"""
from itertools import combinations, combinations_with_replacement
from math import comb

TYPES={}
for p in range(1,8):
    vals=(0, p&1, (p>>1)&1, (p>>2)&1)
    last=[]
    for i in range(4):
        for lag in range(1,5):
            e=(i-lag)%4
            if vals[e]!=vals[(e+1)%4]:
                last.append(e);break
    TYPES[p]=(vals,last)

def words(pats):
    return (0,)+tuple(sum(((p>>(j-1))&1)<<k for k,p in enumerate(pats)) for j in (1,2,3))

def distance_ok(c,q):
    return all((c[i]^c[(i+1)%4]).bit_count()>=2*q+1 for i in range(4)) and all((c[i]^c[i+2]).bit_count()>=2*q+1 for i in range(2))

def collision(pats,i,j,q):
    # Assign each differing coordinate's error to one of two phases.
    # Each phase has 4 last-update groups, each with capacity q.
    multiplicity=[0]*8
    for p in pats:multiplicity[p]+=1
    edges=[]
    for p in range(1,8):
        vals,last=TYPES[p]
        if vals[i]!=vals[j]:
            edges.append((last[i],4+last[j],multiplicity[p]))
    # Integral assignment exists iff every induced vertex subset U
    # contains at most q*|U| coordinate edges (maxflow/mincut).
    for U in range(1,256):
        induced=sum(m for a,b,m in edges if (U>>a)&1 and (U>>b)&1)
        if induced>q*U.bit_count():return False
    return True

def all_pair_disjoint(pats,q):
    return all(not collision(pats,i,j,q) for i in range(4) for j in range(i+1,4))

def verify(q,n):
    stats={'q':q,'n':n,'classes':0,'distance_pass':0,'stable_disjoint':0}
    for pats in combinations_with_replacement(range(1,8),n):
        stats['classes']+=1
        c=words(pats)
        if not distance_ok(c,q):continue
        stats['distance_pass']+=1
        stats['stable_disjoint']+=all_pair_disjoint(pats,q)
    assert stats['classes']==comb(n+6,6)
    return stats

def exact_stable(pats,i,q):
    # Independently build physical terminal sets for q=2 cross-check.
    c=words(pats);n=len(pats)
    groups=[[] for _ in range(4)]
    for k in range(n):
        for lag in range(1,5):
            e=(i-lag)%4
            if (c[e]^c[(e+1)%4])&(1<<k):
                groups[e].append(k);break
    r={0}
    for group in groups:
        z=[sum(1<<k for k in a) for t in range(min(q,len(group))+1) for a in combinations(group,t)]
        r={a^b for a in r for b in z}
    return {c[i]^v for v in r}

def main():
    tested=0
    for pats in combinations_with_replacement(range(1,8),9):
        if not distance_ok(words(pats),2):continue
        ss=[exact_stable(pats,i,2) for i in range(4)]
        for i in range(4):
            for j in range(i+1,4):
                assert collision(pats,i,j,2)==bool(ss[i]&ss[j])
                tested+=1
    assert tested==282
    print('independent graph/physical-set pair checks',tested,flush=True)
    expected={5:[3,47,306,1270,4005],6:[3,47,306,1270,4005,10493]}
    for q,dist_counts in expected.items():
        for off,expected_pass in enumerate(dist_counts):
            n=3*q+2+off
            result=verify(q,n)
            print(result,flush=True)
            assert result['distance_pass']==expected_pass
            assert result['stable_disjoint']==0
        print('sharp n',4*q+2,'at q',q,flush=True)
    print('R284FK verified',flush=True)

if __name__=='__main__':main()

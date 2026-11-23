"""R284FI: exact n_min(u=0,q=2)=10 in the reset-free four-word model."""
from collections import deque
from itertools import combinations, combinations_with_replacement

Q = 2

def words_of(patterns):
    return (0,) + tuple(sum(((p >> (j-1)) & 1) << k
                             for k, p in enumerate(patterns))
                        for j in (1,2,3))

def last_groups(c, n, phase):
    groups = [[] for _ in range(4)]
    for bit in range(n):
        for lag in range(1,5):
            edge = (phase-lag)%4
            if (c[edge]^c[(edge+1)%4]) & (1<<bit):
                groups[edge].append(bit)
                break
        else:
            raise AssertionError('Constant coordinate should be deleted')
    return groups

def stable(c,n,phase):
    residuals={0}
    for group in last_groups(c,n,phase):
        choices=(sum(1<<b for b in sub)
                 for r in range(min(Q,len(group))+1)
                 for sub in combinations(group,r))
        choices=list(choices)
        residuals={a^b for a in residuals for b in choices}
    return {c[phase]^r for r in residuals}

def distances_pass(c):
    edges=[(c[i]^c[(i+1)%4]).bit_count() for i in range(4)]
    diagonals=[(c[i]^c[i+2]).bit_count() for i in range(2)]
    return min(edges)>=2*Q+1 and min(diagonals)>=2*Q+1

def lower(n):
    counts=dict(classes=0,distance_pass=0,stable_disjoint=0)
    for patterns in combinations_with_replacement(range(1,8), n):
        counts['classes']+=1
        c=words_of(patterns)
        if not distances_pass(c):continue
        counts['distance_pass']+=1
        seen=set()
        ok=True
        for phase in range(4):
            s=stable(c,n,phase)
            if seen.intersection(s):
                ok=False
                break
            seen.update(s)
        counts['stable_disjoint']+=ok
    return counts

def upper():
    n=10
    c=(0,31,1023,992)
    orders=[tuple(k for k in range(n) if (c[i]^c[(i+1)%4])&(1<<k))
            for i in range(4)]
    states=[set() for _ in range(4)]
    states[0].add(0)
    queue=deque([(0,0)])
    while queue:
        i,x=queue.popleft()
        j=(i+1)%4
        for count in range(Q+1):
            for missed in combinations(orders[i],count):
                y=x
                for k in orders[i]:
                    if k not in missed:
                        y=(y & ~(1<<k)) | (c[j]&(1<<k))
                if y not in states[j]:
                    states[j].add(y)
                    queue.append((j,y))
    assert all(states[i]==stable(c,n,i) for i in range(4))
    assert [len(s) for s in states]==[256]*4
    assert len(set.union(*states))==2**10
    def decode(x):
        a=(x&31).bit_count()>=3
        b=(x>>5).bit_count()>=3
        return {(False,False):0,(True,False):1,(True,True):2,(False,True):3}[(a,b)]
    cases=0
    for i in range(4):
        j=(i+1)%4
        for source in states[i]:
            for count in range(Q+1):
                for missed in combinations(orders[i],count):
                    x=source
                    new_seen=False
                    for k in [None]+list(orders[i]):
                        if k is not None and k not in missed:
                            x=(x & ~(1<<k)) | (c[j]&(1<<k))
                        d=decode(x)
                        assert d in (i,j), ('third phase',i,source,missed,k,x,d)
                        assert not(new_seen and d==i), ('rollback',i,source,missed,k,x)
                        new_seen |= (d==j)
                        cases+=1
                    assert decode(x)==j
    return dict(codes=c,stable_counts=[len(s) for s in states],
                union_size=len(set.union(*states)),checked_prefixes=cases)

if __name__=='__main__':
    a=lower(8)
    b=lower(9)
    print('n=8',a)
    print('n=9',b)
    print('upper',upper())
    assert a==dict(classes=3003,distance_pass=3,stable_disjoint=0)
    assert b==dict(classes=5005,distance_pass=47,stable_disjoint=0)
    print('R284FI verified')

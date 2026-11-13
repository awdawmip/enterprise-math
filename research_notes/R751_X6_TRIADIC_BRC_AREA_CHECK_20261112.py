#!/usr/bin/env python3
"""R751: exact signed Path-formal X6 BRC exterior observer on triadic 6-step witnesses."""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

D = 6
K = tuple((i,j) for i in range(D) for j in range(i+1,D))

def signed_port(i,s):
    assert i in range(D) and s in (-1,1)
    return tuple(s if j == i else 0 for j in range(D))

def minus(v):
    return tuple(-x for x in v)

def wedge(u,v):
    return tuple(u[i]*v[j]-u[j]*v[i] for i,j in K)

def plus(u,v):
    return tuple(x+y for x,y in zip(u,v))

def area_and_endpoint(word):
    endpoint=(0,)*D
    A=(0,)*len(K)
    for step in word:
        A=plus(A,wedge(endpoint,step))
        endpoint=plus(endpoint,step)
    return endpoint,A

def branch_words(p,q,r):
    return (
        (p,q,r,minus(p),minus(q),minus(r)),
        (q,r,p,minus(q),minus(r),minus(p)),
        (r,p,q,minus(r),minus(p),minus(q)),
    )

def triad_area(ports,orientation):
    p,q,r=ports
    if orientation == -1:
        q,r=r,q
    words=branch_words(p,q,r)
    return tuple(map(sum,zip(*(area_and_endpoint(w)[1] for w in words))))

def area_formula(ports,orientation):
    p,q,r=ports
    a=wedge(p,q)
    b=wedge(q,r)
    c=wedge(r,p)
    return tuple(2*orientation*(x+y+z) for x,y,z in zip(a,b,c))

def relabel(v,perm):
    out=[0]*D
    for i,x in enumerate(v):
        out[perm[i]]=x
    return tuple(out)

def relabel_area(A,perm):
    out={}
    for (i,j),weight in zip(K,A):
        a,b=perm[i],perm[j]
        out[tuple(sorted((a,b)))]=weight if a<b else -weight
    return tuple(out[k] for k in K)

def run():
    signatures=defaultdict(list)
    visited=[]
    counts=Counter()
    for axes in combinations(range(D),3):
        for signs in product((-1,1),repeat=3):
            ports=tuple(signed_port(i,s) for i,s in zip(axes,signs))
            for orientation in (-1,1):
                A=triad_area(ports,orientation)
                assert A==area_formula(ports,orientation)
                assert len([a for a in A if a])==3
                assert set(A).issubset({-2,0,2})
                signatures[A].append((axes,signs,orientation))
                visited.append((ports,orientation,A))
                counts["oriented_states"]+=1
                a,b,c=ports if orientation==1 else (ports[0],ports[2],ports[1])
                for word in branch_words(a,b,c):
                    endpoint,branch_area=area_and_endpoint(word)
                    assert endpoint==(0,)*D
                    assert len(word)==6
                    assert all(word[t+1]!=minus(word[t]) for t in range(5))
                    assert all(any(x for x in step) for step in word)
                    assert len(set(next(i for i,x in enumerate(v) if x) for v in word))==3
                    counts["six_step_closed_branch_witnesses"]+=1
                # product of the 3 nonzero area coordinates decodes orientation
                i,j,k=axes
                prod=A[K.index((i,j))]*A[K.index((i,k))]*A[K.index((j,k))]
                assert prod == -8*orientation
                counts["orientation_decoder_checks"]+=1
    assert counts["oriented_states"]==320
    assert counts["six_step_closed_branch_witnesses"]==960
    assert len(signatures)==160
    assert all(len(fiber)==2 for fiber in signatures.values())
    for A,fiber in signatures.items():
        (ax0,s0,o0),(ax1,s1,o1)=fiber
        assert ax0==ax1 and o0==o1
        assert s1==tuple(-s for s in s0)
    counts["signature_classes"]=len(signatures)
    counts["fiber_two_classes"]=sum(len(x)==2 for x in signatures.values())
    # All S6 permutations, not just generators: exterior tensor covariance
    for ports,orientation,A in visited:
        for perm in permutations(range(D)):
            new_ports=[relabel(v,perm) for v in ports]
            AA=area_formula(new_ports,orientation)
            assert AA==relabel_area(A,perm)
            counts["S6_covariance_checks"]+=1
    assert counts["S6_covariance_checks"]==230400
    assert triad_area(tuple(signed_port(i,1) for i in (0,1,2)),1) == (2,-2,0,0,0,2,0,0,0,0,0,0,0,0,0)
    print("R751_X6_TRIADIC_BRC_AREA_EXACT_PASS",dict(counts))
    return counts

if __name__=="__main__":
    run()

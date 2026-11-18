"""Small fixed domain counts for the literature crosswalk. Python standard library."""
from fractions import Fraction
from itertools import product
from math import gcd
import json


def depth(x):
    return (x & -x).bit_length()-1


def order(x, p):
    v = x % p
    n = 1
    while v != 1:
        v = v*x % p
        n += 1
    return n


def prime_pair(p, q):
    n = p*q
    odd = (n-1) >> depth(n-1)
    units = [a for a in range(1,n) if gcd(a,n)==1]
    equal = sum(depth(order(a,p)) == depth(order(a,q)) for a in units)
    strong = sum(pow(a,odd,n)==1 or
                 any(pow(a,odd << j,n)==n-1 for j in range(depth(n-1))) for a in units)
    A,B=depth(p-1),depth(q-1)
    P,Q=(p-1)>>A,(q-1)>>B
    weight=1+(4**min(A,B)-1)//3
    assert equal==weight*P*Q and strong==weight*gcd(P,Q)**2
    return dict(n=n, units=len(units), equal_depth=equal, strong_liars=strong)


def additive_graph_pair(A,B,k):
    a,b=2**A,2**B
    L=max(a,b)
    power=lambda u,N: frozenset(tuple((z*x)%N for x in u) for z in range(N))
    total_graph=total_common=0
    uu=list(product(range(a),repeat=k))
    vv=list(product(range(b),repeat=k))
    for u in uu:
        ugroup=power(tuple(x*(L//a) for x in u),L)
        for v in vv:
            common=ugroup==power(tuple(x*(L//b) for x in v),L)
            # In the additive group, compute the actual subgroup and both projections.
            H={(0,0)}
            for x,y in zip(u,v):
                H={((i+c*x)%a,(j+c*y)%b) for i,j in H for c in range(L)}
            gph=len(H)==len({i for i,j in H})==len({j for i,j in H})
            assert gph==common
            total_graph+=gph
            total_common+=common
    numerator=1+sum(2**(t-1)*(2**(t*k)-2**((t-1)*k))
                    for t in range(1,min(A,B)+1))
    assert numerator==total_graph==total_common
    return dict(A=A,B=B,k=k,total=len(uu)*len(vv),same_cyclic_pairs=total_common,
                exact_fraction=str(Fraction(numerator,len(uu)*len(vv))))


if __name__=="__main__":
    print(json.dumps({"semiprime_counts":[prime_pair(p,q) for p,q in [(3,5),(3,7),(5,13),(5,17)]],
                      "additive_subgroup_counts":[additive_graph_pair(*item)
                         for item in [(1,1,3),(1,2,2),(2,2,2),(2,3,2)]]},indent=2))

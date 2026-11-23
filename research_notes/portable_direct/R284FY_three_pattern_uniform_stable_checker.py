#!/usr/bin/env python3
"""R284FY: exact support-{3,5,6} stable-observer classification for q>=5, u=1.

Integer-only; the all-q conclusion follows from the written algebra, not
from the finite regression loop. The oracle in `allowed` is the proved
three-edge stable maxflow reduction, not a numerical approximation.
"""

def stable_adj(a, b, q):
    # Two separate source budget-q groups; one shared target budget-q group.
    return max(0, a+b-q-min(q,a)-min(q,b))


def stable_opp(a, c, q):
    # Pattern 3 and pattern 6: disjoint endpoint pairs.
    return max(0,a-2*q)+max(0,c-2*q)


def allowed(a,b,c,q,k):
    n=4*q+k
    return (a+b+c == n and
            a+b >= 2*q+5 and b+c >= 2*q+5 and
            a+c >= 2*q+3 and
            stable_adj(a,b,q) >= 3 and
            stable_adj(b,c,q) >= 3 and
            stable_opp(a,c,q) >= 3)


def classified(q,k):
    # Disjoint cases: a large/c small, c large/a small, and both large.
    n=4*q+k
    r=set()
    for s in range(3,k-4):   # 3..k-5 inclusive
        for t in range(k-s-2):  # 0..k-s-3 inclusive
            r.add((2*q+s,n-(2*q+s)-t,t))
            r.add((t,n-(2*q+s)-t,2*q+s))
    for s in range(3,k-4):
        for t in range(3,k-4):
            if s+t<=k:
                r.add((2*q+s,k-s-t,2*q+t))
    return r


def brute_triples(q,k):
    n=4*q+k
    return {(a,n-a-c,c) for a in range(n+1)
            for c in range(n-a+1)
            if allowed(a,n-a-c,c,q,k)}


def main():
    for q in (5,6,7,8,11,14,21,32,64):
        for k,expected in ((8,7),(9,18)):
            algebra=classified(q,k)
            direct=brute_triples(q,k)
            assert algebra==direct,(q,k,algebra^direct)
            assert len(algebra)==expected,(q,k,len(algebra))
            print('q=%d n=%d exact=%d verified' %(q,4*q+k,len(algebra)))
    print('REGRESSION PASS: analytic classification verified in nine distinct q-values')


if __name__=='__main__':main()

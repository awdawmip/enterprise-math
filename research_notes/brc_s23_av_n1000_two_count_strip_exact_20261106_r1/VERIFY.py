#!/usr/bin/env python3
"""Exact two-count (stop3, stop4) improvement over six-point S23 stop4-only certificate."""
from fractions import Fraction as F
from math import comb
from decimal import Decimal, localcontext

N = 1000
Z = F(1, 4)
Q = (F(1,28), F(3217,50000), F(10091,100000),
     F(14447,100000), F(9727,50000), F(1,4))
EVENTS = ((0,48),(49,81),(82,121),(122,168),(169,221),(222,1000))
# (stop4 count u, initial class i, destination class j, stop3 range lower, upper).
# The chosen intervals are exact certificate data, independent of floating point.
MOVES = (
    (47,0,1,277,953),(48,0,1,262,952),(49,1,0,0,245),(50,1,0,0,230),
    (80,1,2,264,920),(81,1,2,254,919),(82,2,1,0,244),(83,2,1,0,235),
    (120,2,3,261,880),(121,2,3,254,879),(122,3,2,0,247),(123,3,2,0,241),
    (167,3,4,258,833),(168,3,4,253,832),(169,4,3,0,248),(170,4,3,0,243),
    (220,4,5,256,780),(221,4,5,253,779),(222,5,4,0,248),(223,5,4,0,245),
)

def binomial_interval(n, q, lo, hi):
    r, d = q.numerator, q.denominator
    return F(sum(comb(n, k) * r**k * (d-r)**(n-k)
                 for k in range(lo,hi+1)), d**n)

def multinomial_strip(q, u, slo, shi):
    """Exact Pr(T4=u and slo<=T3<=shi), for (stop1, stop3, stop4)=(3/4-q,1/4,q)."""
    r,d=q.numerator,q.denominator
    m=N-u
    a,b=d,3*d-4*r
    assert 0 <= slo <= shi <= m and a>0 and b>0
    term=comb(m,slo)*a**slo*b**(m-slo)
    total=0
    for s in range(slo,shi+1):
        total+=term
        if s<shi:
            num=term*(m-s)*a
            den=(s+1)*b
            assert num%den==0
            term=num//den
    return F(comb(N,u)*(4*r)**u*total,(4*d)**N)

def likelihood(q,u,s):
    """Common multinomial factor cancels, leaving exactly this rational score."""
    return q**u * (F(3,4)-q)**(N-u-s)

def main():
    assert len(Q)==len(EVENTS)==6 and len(MOVES)==20
    for i,q in enumerate(Q):
        a=F(3,4)-q
        c=F(1,4)/(1-a)
        assert F(1,2)<=a<=F(7,8) and F(1,2)<=c<=F(7,8)
        assert (1-a)*c == Z
        if i: assert EVENTS[i][0]==EVENTS[i-1][1]+1
    old=sum((binomial_interval(N,q,*e) for q,e in zip(Q,EVENTS)),F(0))
    gain=F(0)
    seen=set()
    for u,src,dst,lo,hi in MOVES:
        assert src!=dst and 0<=lo<=hi<=N-u
        assert EVENTS[src][0]<=u<=EVENTS[src][1]
        assert u not in seen
        seen.add(u)
        assert abs(src-dst)==1
        # For each fixed u the score ratio varies monotonically in s,
        # because the two a=3/4-q values differ. Endpoints certify the whole strip.
        assert likelihood(Q[dst],u,lo)>likelihood(Q[src],u,lo)
        assert likelihood(Q[dst],u,hi)>likelihood(Q[src],u,hi)
        if lo>0: assert likelihood(Q[dst],u,lo-1)<=likelihood(Q[src],u,lo-1)
        if hi<N-u: assert likelihood(Q[dst],u,hi+1)<=likelihood(Q[src],u,hi+1)
        delta=multinomial_strip(Q[dst],u,lo,hi)-multinomial_strip(Q[src],u,lo,hi)
        assert delta>0
        gain+=delta
    improved=(old+gain-1)/6
    baseline=(old-1)/6
    assert baseline>F(201,250)
    assert improved>F(807,1000) and improved>baseline
    assert improved<1
    with localcontext() as ctx:
        ctx.prec=45
        print('PASS_S23_N1000_FULL_TAGGED_TWO_COUNT_STRIP_20261106')
        print('samples=1000; shared_binary_observer_z=1/4; parameters=6')
        print('disjoint_reassignments=20; endpoint_and_neighbor_likelihood_checks=60')
        print('stop4_only_lower=',Decimal(baseline.numerator)/Decimal(baseline.denominator))
        print('two_count_lower=',Decimal(improved.numerator)/Decimal(improved.denominator))
        print('strict_certified_bound: delta_1000 > 807/1000 = 0.807')
        print('gain_over_previous=',Decimal((improved-baseline).numerator)/Decimal((improved-baseline).denominator))
        print('arithmetic=integer powers + comb + Fraction; no floating point in certificate')
        print('status=author-side exact arithmetic; independent review pending')
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact 60-strip (stop3,stop4) six-hypothesis lower certificate at n=1000.
No floating point is used in evidence or interval selection verification.
"""
from fractions import Fraction as F
from math import comb
from decimal import Decimal, localcontext

N = 1000
Q = (F(1,28), F(3217,50000), F(10091,100000),
     F(14447,100000), F(9727,50000), F(1,4))
EVENTS = ((0,48),(49,81),(82,121),(122,168),(169,221),(222,1000))
OLD_MOVES = (
    (47,0,1,277,953),(48,0,1,262,952),(49,1,0,0,245),(50,1,0,0,230),
    (80,1,2,264,920),(81,1,2,254,919),(82,2,1,0,244),(83,2,1,0,235),
    (120,2,3,261,880),(121,2,3,254,879),(122,3,2,0,247),(123,3,2,0,241),
    (167,3,4,258,833),(168,3,4,253,832),(169,4,3,0,248),(170,4,3,0,243),
    (220,4,5,256,780),(221,4,5,253,779),(222,5,4,0,248),(223,5,4,0,245),
)
NEW_MOVES = (
    (219, 4, 5, 259, 781),
    (224, 5, 4, 4, 241),
    (166, 3, 4, 262, 438),
    (218, 4, 5, 263, 782),
    (171, 4, 3, 0, 239),
    (225, 5, 4, 0, 238),
    (217, 4, 5, 266, 783),
    (226, 5, 4, 0, 235),
    (165, 3, 4, 267, 441),
    (124, 3, 2, 0, 235),
    (119, 2, 3, 267, 470),
    (172, 4, 3, 0, 234),
    (216, 4, 5, 269, 784),
    (227, 5, 4, 0, 231),
    (164, 3, 4, 271, 444),
    (173, 4, 3, 0, 230),
    (215, 4, 5, 273, 785),
    (118, 2, 3, 273, 475),
    (125, 3, 2, 0, 229),
    (79, 1, 2, 273, 512),
    (228, 5, 4, 0, 228),
    (163, 3, 4, 276, 448),
    (214, 4, 5, 276, 786),
    (174, 4, 3, 0, 226),
    (84, 2, 1, 0, 226),
    (229, 5, 4, 0, 224),
    (117, 2, 3, 279, 479),
    (213, 4, 5, 280, 787),
    (126, 3, 2, 0, 223),
    (162, 3, 4, 280, 451),
    (230, 5, 4, 0, 221),
    (175, 4, 3, 0, 221),
    (78, 1, 2, 282, 519),
    (212, 4, 5, 283, 788),
    (161, 3, 4, 284, 455),
    (231, 5, 4, 0, 218),
    (116, 2, 3, 285, 484),
    (176, 4, 3, 0, 217),
    (211, 4, 5, 286, 789),
    (127, 3, 2, 0, 216),
)

def bin_interval(n, q, lo, hi):
    r,d=q.numerator,q.denominator
    return F(sum(comb(n,k)*r**k*(d-r)**(n-k) for k in range(lo,hi+1)),d**n)

def strip(q,u,lo,hi):
    """Exact Pr(T4=u, lo<=T3<=hi) for (p1,p3,p4)=(3/4-q,1/4,q)."""
    r,d=q.numerator,q.denominator
    m=N-u; a,b=d,3*d-4*r
    assert 0<=lo<=hi<=m and b>0
    term=comb(m,lo)*a**lo*b**(m-lo)
    total=0
    for s in range(lo,hi+1):
        total+=term
        if s<hi:
            div=(s+1)*b
            num=term*(m-s)*a
            assert num%div==0
            term=num//div
    return F(comb(N,u)*(4*r)**u*total, (4*d)**N)

def score(q,u,s):
    return q**u * (F(3,4)-q)**(N-u-s)

def main():
    assert len(Q)==len(EVENTS)==6 and len(OLD_MOVES)==20 and len(NEW_MOVES)==40
    for i,q in enumerate(Q):
        a=F(3,4)-q; c=F(1,4)/(1-a)
        assert F(1,2)<=a<=F(7,8) and F(1,2)<=c<=F(7,8)
        assert (1-a)*c==F(1,4)
        if i: assert EVENTS[i][0]==EVENTS[i-1][1]+1
    baseline_sum=sum((bin_interval(N,q,*event) for q,event in zip(Q,EVENTS)),F(0))
    gains=[]; used=set()
    for series in (OLD_MOVES,NEW_MOVES):
        gain=F(0)
        for u,src,dst,lo,hi in series:
            assert u not in used and src!=dst and 0<=lo<=hi<=N-u
            used.add(u)
            assert EVENTS[src][0]<=u<=EVENTS[src][1]
            assert score(Q[dst],u,lo)>score(Q[src],u,lo)
            assert score(Q[dst],u,hi)>score(Q[src],u,hi)
            # Score ratio = constant * (A_dst/A_src)^(N-u-s),
            # hence both exact endpoint comparisons imply positivity throughout.
            inc=strip(Q[dst],u,lo,hi)-strip(Q[src],u,lo,hi)
            assert inc>0
            gain+=inc
        gains.append(gain)
    prev=(baseline_sum+gains[0]-1)/6
    improved=(baseline_sum+sum(gains)-1)/6
    assert prev>F(807,1000)
    assert improved>F(8081,10000)
    assert improved>prev
    assert improved<F(5,6)
    with localcontext() as ctx:
        ctx.prec=45
        print('PASS_S23_N1000_SIX_HYPOTHESES_SIXTY_STRIPS_EXACT_20261106')
        print('observation_n=1000; six_lawful_common_z=1/4_states; disjoint=60')
        print('baseline+previous_twenty=',Decimal(prev.numerator)/Decimal(prev.denominator))
        print('sixty_strip_lower=',Decimal(improved.numerator)/Decimal(improved.denominator))
        print('increment=',Decimal((improved-prev).numerator)/Decimal((improved-prev).denominator))
        print('CERTIFIED: delta_1000 > 8081/10000 = 0.8081')
        print('checks=all 60 strips exact endpoint likelihoods, exact multinomial sums')
        print('all arithmetic=integer powers/binomial coefficients/Fraction; no floating-point certificate')
        print('status=author-side exact arithmetic; independent review pending')
if __name__=='__main__': main()

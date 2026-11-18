#!/usr/bin/env python3
"""Exact three-gap/Farey circle-risk evaluator for the frozen S23/AV observer.

Works for arbitrary irrational 0<theta<1 via certified rational enclosure.
The operations are integer arithmetic; no floating point participates in tests.
"""
from fractions import Fraction

P = 262204504569236716045286
Q = 10**24
M = 128
LOW = Fraction(P, Q)
HIGH = Fraction(P+1, Q)


def certify_theta():
    def log_bounds(z, terms=160):
        acc, term = Fraction(0), z
        for k in range(terms):
            acc += 2*term/Fraction(2*k+1)
            term *= z*z
        return acc, acc + 2*term/((2*terms+1)*(1-z*z))
    a,b = log_bounds(Fraction(3,4))
    c,d = log_bounds(Fraction(3,17))
    rlo,rhi = a/d,b/c
    assert 79*rlo>431
    def theta(r):
        return 79*(2074774-380295*r)/(79*r-431)-46
    assert LOW < theta(rhi) < theta(rlo) < HIGH


def farey_neighbors(x, bound):
    """Lower and upper Farey neighbors around x, with denominators <= bound."""
    a,b,c,d=0,1,1,1
    while b+d<=bound:
        if (a+c)*x.denominator < (b+d)*x.numerator:
            num=b*x.numerator-a*x.denominator
            den=c*x.denominator-d*x.numerator
            t=min((num-1)//den,(bound-b)//d)
            assert t>=1
            a,b=a+t*c,b+t*d
        else:
            num=c*x.denominator-d*x.numerator
            den=b*x.numerator-a*x.denominator
            t=min((num-1)//den,(bound-d)//b)
            assert t>=1
            c,d=c+t*a,d+t*b
    assert a*d+1==b*c and b+d>bound
    return (a,b),(c,d)


def floor_sum(n,m,a,b):
    """Sum of floor((a*i+b)/m) for i=0..n-1, signed a,b."""
    assert n>=0 and m>0
    aq,a=divmod(a,m)
    bq,b=divmod(b,m)
    answer=aq*n*(n-1)//2 + bq*n
    while True:
        if a>=m:
            answer+=n*(n-1)//2*(a//m)
            a%=m
        if b>=m:
            answer+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:
            return answer
        n=y//m
        b=y%m
        m,a=a,m


def floor_index_sum(left,right,offset,x):
    if left>right: return 0
    return floor_sum(right-left+1,x.denominator,x.numerator,
                     (left-offset)*x.numerator)


def phase(i,x):
    a=i*x
    return a-(a.numerator//a.denominator)


def arc_count(p,q,left,right,x,wrap):
    """Number of left<=i<=right with {i*x} on clockwise arc [{p*x},{q*x})."""
    if left>right:return 0
    n=right-left+1
    fp=(p*x).numerator//(p*x).denominator
    fq=(q*x).numerator//(q*x).denominator
    return (floor_index_sum(left,right,p,x)-floor_index_sum(left,right,q,x)
            +n*(fp-fq+int(wrap)))


def risk(m,n,xlo=LOW,xhi=HIGH):
    """Return exact affine pair (A,B) such that R(m,n-m)=A+B*theta.

    Checking the enclosing Farey cell certifies all n phase orders. Gap
    comparisons are independently verified at both endpoints of the interval.
    """
    assert n>=m>=2 and 0<xlo<=xhi<1
    (a,b),(c,d)=farey_neighbors(xlo,n-1)
    assert Fraction(a,b)<xlo<=xhi<Fraction(c,d)
    assert b+d>=n
    # labels: small-positive, small-negative, sum; disjoint starting-index sets
    classes=[((-a,b),(0,n-b-1)),
             ((c,-d),(d,n-1)),
             ((c-a,b-d),(n-b,d-1))]
    indexes=sorted(range(m),key=lambda i:phase(i,xlo))
    assert indexes==sorted(range(m),key=lambda i:phase(i,xhi))
    chosen=[]
    for p,q in zip(indexes,indexes[1:]+indexes[:1]):
        wrap=phase(p,xlo)>phase(q,xlo)
        assert wrap==(phase(p,xhi)>phase(q,xhi))
        hits=[arc_count(p,q,left,right,xlo,wrap)
              for gap,(left,right) in classes]
        assert hits==[arc_count(p,q,left,right,xhi,wrap)
                      for gap,(left,right) in classes]
        assert all(t>=0 for t in hits) and sum(hits)>=1
        possible=[gap for (gap,_),hit in zip(classes,hits) if hit>0]
        best=max(possible,key=lambda g:g[0]+g[1]*xlo)
        assert best==max(possible,key=lambda g:g[0]+g[1]*xhi)
        chosen.append(best)
    out=(1-sum(v[0] for v in chosen),-sum(v[1] for v in chosen))
    assert 0<=out[0]+out[1]*xlo<=1 and 0<=out[0]+out[1]*xhi<=1
    return out,(a,b),(c,d)


def slow_risk(m,n,x):
    points=sorted((phase(i,x),i) for i in range(n))
    anchors=sorted(range(m),key=lambda i:phase(i,x))
    max_by_anchor={i:Fraction(0) for i in anchors}
    owner=None
    for k,(start,i) in enumerate(points):
        if i<m:owner=i
        if owner is None:owner=anchors[-1]
        stop=points[(k+1)%n][0]
        g=stop-start if stop>start else stop+1-start
        max_by_anchor[owner]=max(max_by_anchor[owner],g)
    return 1-sum(max_by_anchor.values())


def verify():
    certify_theta()
    print('CERTIFIED_THETA_160_TERMS',P,P+1,Q)
    # Independent direct partition checks (no floor sums/Farey formulas in slow).
    x=Fraction(4142135623730950488016887242097,10**31)
    checks=0
    for m in (2,3,4,7,13,21,40):
        for n in (m,m+1,m+2,2*m,5*m,10*m,500):
            (A,B),_,_=risk(m,n,x,x)
            assert A+B*x==slow_risk(m,n,x)
            checks+=1
    # Direct cross-check of the actual S23/AV theta with 24-place bracket.
    for horizon in (1,36,37,164,200,1142):
        (A,B),_,_=risk(M,M+horizon)
        approx=Fraction(P*2+1,2*Q)
        assert A+B*approx==slow_risk(M,M+horizon,approx)
        checks+=1
    print('INDEPENDENT_DIRECT_PARTITION_TESTS',checks)
    expect={
        1142:(-18559,70784),
        10000:(-151935,579456),
        100000:(-2769919,10563968),
        200000:(479873,-1830144),
    }
    for horizon,pair in expect.items():
        out,_,_=risk(M,M+horizon)
        assert out==pair,(horizon,out,pair)
    print('MATCH_ALL_FOUR_PRIOR_CERTIFIED_ENDPOINTS')
    for horizon in (10**6,10**8,10**10,10**12):
        (A,B),left,right=risk(M,M+horizon)
        print('CERTIFIED_R',horizon,A,B,
              'FAREY',f'{left[0]}/{left[1]}',f'{right[0]}/{right[1]}')
    assert risk(M,M+10**12)[0]==(-4017401528447,15321634290944)
    print('PASS_FAREY_THREE_GAP_EXACT_RISK_10E12')


if __name__=='__main__':
    verify()

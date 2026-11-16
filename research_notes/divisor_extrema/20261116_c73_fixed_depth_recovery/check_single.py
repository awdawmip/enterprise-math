"""Evaluate determinant numerator, sectional gcd and divisibility exactly."""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import prod,gcd
from check_prefix import rising,raw_column

def center_pair(c, xs):
    r=len(xs)
    edges = []
    for i,(old,v) in enumerate(zip((c,)+xs,xs)):
        k=2*(r-i)+1
        edges.append(((v+k-1)*rising(old+k+1,3*k),
                      28*(4*v+k-1)*rising(v+k,3*k)))
    w=xs[-1]
    W=(w+2)*(w+3)*(w+4)
    a,b=raw_column(edges,W)
    a2,b2=raw_column(edges,10*W)
    den = a2*b if r%2==0 else a*b2
    num=1680*9*W*prod(n*d for n,d in edges)
    return a,b,a2,b2,num,den

def check(c,xs):
    r=len(xs)
    a,b,a2,b2,N,D=center_pair(c,xs)
    R=max(Fraction(a*b2,b*a2),Fraction(a2*b,b2*a))
    assert R-1==Fraction(N,D)
    M=(R-1).numerator
    k1=2*r+1
    c0=rising(c+k1+1,3*k1)
    M0=((R-1)/c0).numerator
    assert N%c0==0 and (N//c0)%M0==0
    # Alternating rational probes, including both endpoints and interior pairs.
    a0,b0,m,n=[(0,1,1,1),(1,4,2,3),(1,3,1,2),(2,3,1,1)][(sum(xs)+r)%4]
    def test_den(A,B,A2,B2):
        left=((b0-a0)*A+a0*B)*((n-m)*A2+m*B2)
        right=((b0-a0)*A2+a0*B2)*((n-m)*A+m*B)
        return left,right
    star=test_den(a,b,a2,b2)
    assert abs(star[0]-star[1])==(b0*m-a0*n)*N
    less=0 if star[0]<star[1] else 1
    probe_den=star[less]
    probe_num=Fraction(N//c0,probe_den).numerator
    for i,x in enumerate(xs):
        k=2*(r-i)+1
        l=x+k-1
        special=xs[:i]+(1-k,)+xs[i+1:]
        columns=center_pair(c,special)
        E=columns[-1]
        pE=test_den(*columns[:4])[less]
        assert pE>0 and gcd(l,pE)==gcd(l,probe_den)
        assert probe_num%(l//gcd(l,probe_den))==0
        assert E>0 and gcd(l,D)==gcd(l,E) and N%l==0
        assert M%(l//gcd(l,D))==0 and M0%(l//gcd(l,D))==0
        
if __name__=='__main__':
    points=rows=0
    for r in range(1,9):
        for c in range(4,8):
            # Arithmetic controls of the raw centers only
            for asc in combinations_with_replacement(range(2,c+1),r):
                check(c,asc[::-1]); points+=1; rows+=r
    print(points,'formal centers;',rows,'positive sectional substitutions and divisibility checks')

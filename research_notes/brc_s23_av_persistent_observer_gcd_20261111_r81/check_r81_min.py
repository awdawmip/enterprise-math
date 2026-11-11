"""R81 exact reproducible checks for observer-independent time-gap GCD."""
from fractions import Fraction as Q
from functools import reduce
from math import gcd
from random import Random

def summary(times):
    s=sorted(set(times))
    return (s[0],reduce(gcd,(v-u for u,v in zip(s,s[1:])),0)) if s else (None,0)
def query(times,j,a,b):
    anchor,d=summary(times)
    return gcd(abs(a),abs(b),d,abs(anchor-j) if anchor is not None else 0)
def direct(times,j,a,b):return reduce(gcd,[abs(a),abs(b)]+[abs(t-j) for t in times],0)
def frac(v):return v-(v.numerator//v.denominator)
def win(times,j,x,a,b,z):
    A,B=frac(a*z),frac(b*z)
    if A==B:return None
    return max((t for t in times if (A<=frac(x+(t-j)*z)<B if A<B else frac(x+(t-j)*z)>=A or frac(x+(t-j)*z)<B)),default=None)
def main():
    R=Random(8120261111)
    n=0;p=0
    for _ in range(400):
        times=[R.randrange(-30,31) for _ in range(R.randrange(0,16))]
        for _ in range(8):
            j,a,b=(R.randrange(-40,41) for k in range(3))
            g=query(times,j,a,b)
            assert g==direct(times,j,a,b)
            n+=1
            if g:
                z=Q(R.randrange(-20,21),R.randrange(1,15))
                x=Q(R.randrange(-5,6),R.randrange(1,10))
                assert win(times,j,x,a,b,z)==win(times,j,x,a,b,z+Q(1,g))
                p+=1
    assert summary([4,8])==(4,4) and summary([4,6,8])==(4,2)
    assert direct([4,6],0,12,24)==direct([4,10],0,12,24)==2
    assert direct([6],0,12,24)==6 and direct([10],0,12,24)==2
    for s in [1,7,31,2**127+1]:
        z=Q(3,10*s)
        assert query([4*s],0,s,2*s)==query([4*s,5*s],0,s,2*s)==s
        assert win([4*s],0,Q(0),s,2*s,z) is None
        assert win([4*s,5*s],0,Q(0),s,2*s,z)==5*s
    print('R81_MIN_PASS',n,p)
if __name__=='__main__':main()

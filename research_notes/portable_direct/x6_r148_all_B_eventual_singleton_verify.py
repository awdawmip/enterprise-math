"""R148 all-positive-B high-D Port-10 BRC strict-near tail.
Reuse the frozen R121/R122 six-gap observer and the R147 direction generator.
"""
from fractions import Fraction as Q
from x6_r147_post_plateau_near_fan_verify import A,G,score

b=(4,-1,0)
c=(6,-4,1)

def H0(B):
    return 1872-min(B,Q(136))

def T(B):
    return 2448+17*B if B<=136 else 2312+18*B

def predicted(B,D):
    return {c}|({b} if D<T(B) else set())

def full_near(B,D):
    optimum=min(score(a,B,D) for a in A)
    return optimum,{a for a in A if score(a,B,D)<Q(3,2)*optimum}

def main():
    assert len(A)==1935
    assert len({a for a in A if G[a][1]==0})==15
    assert len({a for a in A if G[a][1]==0 and G[a][2]>=22})==13
    checks=0
    Bs=[Q(1,1000),Q(1),Q(8),Q(20),Q(21),Q(40),Q(80),
        Q(135),Q(136),Q(137),Q(292),Q(1000),Q(1000000),Q(271,2)]
    for B in Bs:
        h,t=H0(B),T(B)
        assert h<t
        Ds={h,h+Q(1,100),(h+t)/2,t-Q(1,100),t,t+Q(1,100),2*t}
        for D in sorted(Ds):
            exact,actual=full_near(B,D)
            expected=predicted(B,D)
            assert actual==expected,(B,D,exact,sorted(actual),sorted(expected))
            checks+=1
    print('R148 ALL-POSITIVE-B HIGH-D EXACT TWO-TO-ONE TAIL PASS')
    print('full Port-10 unoriented population',len(A),'zero-fixed-gap',15,'dominated-zero',13)
    print('tail start 1872-min(B,136); singleton onset 2448+17B (B<=136) or 2312+18B (B>=136)')
    print('full_fraction_population_crosschecks',checks)

if __name__=='__main__':
    main()

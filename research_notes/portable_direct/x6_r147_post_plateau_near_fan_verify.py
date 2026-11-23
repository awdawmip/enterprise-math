"""R147 exact Port-10 six-pair BRC strict-near certificate.
Frozen R121/R122 geometry; uses R146's proved optimizer formula.
Pure integer/rational arithmetic, no floating-point inference.
"""
from itertools import product
from fractions import Fraction as Q

P = 10
A = [a for a in product(range(-P,P+1), repeat=3)
     if a != (0,0,0)
     and max(sum(max(v,0) for v in a), sum(max(-v,0) for v in a)) <= P
     and next(v for v in a if v) > 0]

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[j]-h[i]) for i in range(4) for j in range(i+1,4))

G={a:gaps(a) for a in A}
OLD={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}
b,c=(4,-1,0),(6,-4,1)
EIGHT=OLD|{b,c,(1,-3,1),(9,-2,0)}

def score(a,B,D):
    capacities=(B+136,312,D+136,B+176,B+D,D+176)
    return max(Q(g,s) for g,s in zip(G[a],capacities))

def eta(B,D):
    return min(Q(1,104),max(Q(1,B+136),Q(11,D+136),Q(12,B+D)),Q(12,D+136))

def proposed(B,D):
    H=max(Q(1580),Q(1872)-B)
    K=18*B+2312
    return {c}|({b} if D<K else set())|(OLD if D<H else set())

def full_near(B,D):
    optimum=min(score(a,B,D) for a in A)
    return optimum,{a for a in A if score(a,B,D)<Q(3,2)*optimum}

def main():
    assert len(A)==1935
    assert G[(1,-3,1)]==(2,3,16,1,18,19)
    assert G[(9,-2,0)]==(3,3,15,0,18,18)
    assert {a for a in A if G[a][1]<=3 and G[a][2]<18}==EIGHT
    high={a for a in A if G[a][1]>=6}
    low={a for a in A if G[a][1]<=3}
    assert len(high)==1890 and len(low)==45 and len(EIGHT)==8
    assert len({a for a in low if G[a][2]>=18})==37
    for a in OLD:
        assert score(a,Q(136),Q(1008))==Q(1,104)
    assert G[b]==(1,0,11,1,12,11)
    assert G[c]==(0,0,12,0,12,12)
    Bs=list(map(Q,[136,137,140,150,175,200,239,240,241,292,293,400,1000,10000]))
    Bs += [Q(273,2),Q(601,2),Q(1000001,7)]
    checks=0
    for B in Bs:
        lo=max(Q(1008),Q(1248)-B)
        H=max(Q(1580),Q(1872)-B)
        switch=12*B+1496
        K=18*B+2312
        assert lo<H<switch<K
        Ds={lo,H-Q(1,100),H,H+Q(1,100),
            switch-Q(1,100),switch,switch+Q(1,100),
            K-Q(1,100),K,K+Q(1,100),Q(100000),
            (lo+H)/2,(H+switch)/2,(switch+K)/2}
        for D in sorted(Ds):
            if D<lo: continue
            exact,near=full_near(B,D)
            assert exact==eta(B,D),(B,D,'optimizer',exact,eta(B,D))
            assert near==proposed(B,D),(B,D,sorted(near),sorted(proposed(B,D)))
            checks+=1
    print('R147 POST-PLATEAU COMPLETE STRICT-NEAR FAN CERTIFICATE PASS')
    print('population',len(A),'g1>=6 excluded',len(high),'g1<=3 candidates',len(low))
    print('g1<=3 and g2>=18 excluded',37,'two_special_excluded',2,'surviving',6)
    print('old four iff D<max(1580,1872-B); b iff D<18B+2312; c always')
    print('all_fraction_population_crosschecks',checks)

if __name__=='__main__':
    main()

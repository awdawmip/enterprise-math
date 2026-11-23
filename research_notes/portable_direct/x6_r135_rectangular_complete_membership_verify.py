"""X6 R135: exact Port-10 membership sample replay for R134 rectangles.

The continuous classification is proved by affine inequalities in the paired
research note. This script independently enumerates all 1935 direction classes
at 33 rational parameter samples, including exact equality boundaries.
"""
from fractions import Fraction as Q
from itertools import combinations, product

PAIRS = list(combinations(range(4), 2))
S1 = {(1,0,0),(1,3,-1),(4,-4,1),(5,-4,1),(5,-1,0),(6,-1,0),(7,-1,0),(9,-5,1)}
S2 = {(1,0,0),(3,-4,1),(3,3,-1),(4,-4,1),(6,-1,0),(7,-8,2),(7,-1,0),(9,-5,1)}


def port(a):
    return max(sum(max(v, 0) for v in a), sum(max(-v, 0) for v in a))


def gaps(a):
    x, y, z = a
    h = (0, x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)


DIRECTIONS = tuple(a for a in product(range(-10,11), repeat=3)
                   if any(a) and port(a)<=10 and next(v for v in a if v)>0)
GAPS = {a:gaps(a) for a in DIRECTIONS}
assert len(DIRECTIONS)==1935


def exhaustive(A,B,C,D):
    weights = (Q(A),Q(B),Q(C),Q(D))
    capacity = tuple(weights[i]+weights[j] for i,j in PAIRS)
    score = {a:max(Q(g)/s for g,s in zip(GAPS[a],capacity)) for a in DIRECTIONS}
    eta = min(score.values())
    near = {a for a,f in score.items() if 2*f < 3*eta}
    return eta,near


def predict_I(B,D):
    P=3*D>B+544
    T=B<20
    V=9*D>22*B+1408
    U=9*D>20*B+1496
    result={(4,-4,1),(6,-1,0)}
    if P: result.update({(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)})
    if P and T and V: result.add((1,3,-1))
    if P and T and U: result.add((7,-1,0))
    return result


def predict_II(B,D):
    P=9*B>3*D+2880
    T=5*D<243
    W=20*D<9*B-2640
    U=11*D<1698
    result={(4,-4,1),(6,-1,0)}
    if P: result.update({(1,0,0),(3,-4,1),(9,-5,1)})
    if T: result.add((3,3,-1))
    if P and U: result.add((7,-1,0))
    if T and W: result.add((7,-8,2))
    return result


I = [(1,150),(1,180),(1,182),(8,184),(8,185),(10,188),(10,192),
     (19,180),(19,190),(19,204),(19,207),(19,211),(20,215),(20,150),
     (19,Q(563,3)),(19,Q(1826,9)),(19,Q(1876,9))]
II = [(350,1),(350,Q(51,2)),(350,26),(350,48),(350,Q(243,5)),
      (350,80),(350,90),(350,100),(380,48),(400,48),(465,48),
      (465,49),(465,160),(600,200),(Q(1204,3),Q(243,5)),
      (Q(4086,11),Q(1698,11))]


def check():
    for tag,samples,(A,C),forecast in (
        ("I",I,(136,176),predict_I),
        ("II",II,(722,240),predict_II),
    ):
        for B,D in samples:
            B,D=Q(B),Q(D)
            eta,actual=exhaustive(A,B,C,D)
            expected_eta = Q(3)/(A+B if tag=="I" else C+D)
            expected_near = forecast(B,D)
            assert actual == expected_near, (tag,B,D,"near",actual^expected_near)
            assert eta == expected_eta, (tag,B,D,"eta",eta,expected_eta)
            if tag=="I": assert 0<B<=20 and 150<=D<=220
            else: assert 350<=B<=600 and 1<=D<=200
        print(tag,"PASS",len(samples),"exact all-direction checks")
    print("R135 EXACT EXHAUSTIVE SAMPLE REPLAY PASS",len(I)+len(II))


if __name__ == "__main__":
    check()

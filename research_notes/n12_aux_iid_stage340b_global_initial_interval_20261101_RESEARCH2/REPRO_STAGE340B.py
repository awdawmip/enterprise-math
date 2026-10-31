#!/usr/bin/env python3
"""Stage340-B exact global short-budget localisation/Pareto certificate.

Only exact Fraction arithmetic is used for numerical bounds; SymPy is used for
exact polynomial identity checks. A complete 4-way dyadic rectangle tree is
materialised and validated (not sampling the continuous parameter square).
"""
from __future__ import annotations

import csv
import hashlib
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "CERTIFICATE_STAGE340B.csv"
W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
KAPPA = Q(5, 16)
THRESHOLD = Q(51, 12500)  # 0.00408
RX = (Q(29, 128), Q(30, 128))
RY = (Q(69, 128), Q(74, 128))


def B(k: int, z: Q) -> Q:
    return z**k * (1-z)**(3-k)


def dB(k: int, z: Q) -> Q:
    return (
        -3*(1-z)**2,
        (1-z)*(1-3*z),
        z*(2-3*z),
        3*z*z,
    )[k]


def r(k: int, x: Q, y: Q) -> Q:
    return (4*B(k,x)+B(k,y))/5 - Q(M[k], 160)


def err_b(x: Q, y: Q) -> Q:
    return Q(5, 32) * sum(W[k] * abs(r(k, x, y)) for k in range(4))


def err_c(x: Q, y: Q) -> Q:
    d = lambda a,z: Q(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
    return (63*d(Q(1,4),x)+d(Q(3,4),x)+9*d(Q(1,4),y)+7*d(Q(3,4),y))/256


def f_subset(mask: int, z: Q) -> Q:
    return sum(W[k]*B(k,z) for k in range(4) if mask & (1 << k))


def df_subset(mask: int, z: Q) -> Q:
    return sum(W[k]*dB(k,z) for k in range(4) if mask & (1 << k))


def bern_lower(mask: int, a: Q, b: Q) -> Q:
    """Exact degree-three Bernstein convex-hull lower bound."""
    h = b-a
    fa, fb = f_subset(mask,a), f_subset(mask,b)
    return min(fa, fa+h*df_subset(mask,a)/3,
               fb-h*df_subset(mask,b)/3, fb)


def rectangle_lower_and_witness(a: Q,b: Q,c: Q,d: Q):
    lower, witness = None, 0
    for mask in range(1,16):
        S = sum(W[k]*M[k] for k in range(4) if mask & (1 << k))
        v = KAPPA * ((4*bern_lower(mask,a,b)+bern_lower(mask,c,d))/5-Q(S,160))
        if lower is None or v > lower:
            lower,witness = v,mask
    return lower,witness


def wholly_inside(a: Q,b: Q,c: Q,d: Q) -> bool:
    return RX[0]<=a<=b<=RX[1] and RY[0]<=c<=d<=RY[1]


def strq(v: Q) -> str:
    return f"{v.numerator}/{v.denominator}"


def readq(s: str) -> Q:
    n,d=s.split('/');return Q(int(n),int(d))


def build_cover():
    leaves=[]
    def visit(a,b,c,d,depth):
        if wholly_inside(a,b,c,d):
            leaves.append(("INNER",depth,a,b,c,d,0,Q(0)));return
        lower,subset=rectangle_lower_and_witness(a,b,c,d)
        if lower>THRESHOLD:
            leaves.append(("HIGH",depth,a,b,c,d,subset,lower));return
        assert depth<30, "cover failed to close"
        xm=(a+b)/2;ym=(c+d)/2
        for xa,xb in ((a,xm),(xm,b)):
            for yc,yd in ((c,ym),(ym,d)):
                visit(xa,xb,yc,yd,depth+1)
    visit(Q(0),Q(1),Q(0),Q(1),0)
    assert sum((b-a)*(d-c) for _,_,a,b,c,d,_,_ in leaves)==1
    return leaves


def write_and_readback_cover(leaves):
    header=("label","depth","xlo","xhi","ylo","yhi","witness_subset_bitmask","exact_bernstein_lower")
    with CERT.open("w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f,lineterminator="\n")
        writer.writerow(header)
        for lab,dep,a,b,c,d,s,lo in leaves:
            writer.writerow((lab,dep,strq(a),strq(b),strq(c),strq(d),s,strq(lo)))
    with CERT.open(newline="",encoding="utf-8") as f:
        rr=list(csv.DictReader(f))
    assert len(rr)==len(leaves)
    area=Q(0)
    for line in rr:
        a,b,c,d=(readq(line[k]) for k in ("xlo","xhi","ylo","yhi"))
        area+=(b-a)*(d-c)
        if line["label"]=="INNER":
            assert wholly_inside(a,b,c,d)
        else:
            actual,subset=rectangle_lower_and_witness(a,b,c,d)
            assert actual>THRESHOLD
            assert actual==readq(line["exact_bernstein_lower"])
            assert subset==int(line["witness_subset_bitmask"])
    assert area==1
    return hashlib.sha256(CERT.read_bytes()).hexdigest()


def b_extrema(k: int,a: Q,b: Q):
    values=[B(k,a),B(k,b)]
    if k==1 and a<Q(1,3)<b: values.append(B(k,Q(1,3)))
    if k==2 and a<Q(2,3)<b: values.append(B(k,Q(2,3)))
    return min(values),max(values)


def verify_root_bracket():
    xl,xh=Q(231083,10**6),Q(231085,10**6)
    ya,yb=Q(5555201,10**7),Q(5555202,10**7)
    yc,yd=Q(5554961,10**7),Q(5554962,10**7)
    assert r(0,xl,ya)>0 and r(0,xl,yb)<0
    assert r(1,xl,ya)<0 and r(1,xl,yb)<0
    assert r(0,xh,yc)>0 and r(0,xh,yd)<0
    assert r(1,xh,yc)>0 and r(1,xh,yd)>0
    assert RX[0]<xl<xh<RX[1] and RY[0]<yc<yb<RY[1]
    # r_0 is decreasing in y and r_1 increasing along the r_0 graph:
    # the opposite signs at xL and xH prove a unique double zero q*.
    lower2=r(2,RX[0],RY[0])
    upper3=r(3,RX[1],RY[1])
    assert lower2==Q(24111,10485760)>0
    assert upper3==Q(-1915,262144)<0
    # At q*: r0=r1=0, r2>0, r3<0 => b*=5(-r3*)/16.
    bstar_upper=KAPPA*(-r(3,xl,yc))
    assert bstar_upper==Q(60478550833982446319,16000000000000000000000)
    assert bstar_upper + Q(3,10000) < THRESHOLD
    return bstar_upper


def verify_tag_gradients_and_slopes():
    # Rigorous extrema signs for all 15 fixed source-labelled comparisons.
    signs={
        ("x",Q(1,4)):(-1,1,1,1),
        ("x",Q(3,4)):(-1,-1,1,1),
        ("y",Q(1,4)):(1,1,-1,-1),
        ("y",Q(3,4)):(-1,-1,0,1),
    }
    for (variable,anchor),expect in signs.items():
        a,b= (RX if variable=="x" else RY)
        for k in range(4):
            if expect[k]==0:continue
            lo,hi=b_extrema(k,a,b)
            d_lo,d_hi=B(k,anchor)-hi,B(k,anchor)-lo
            assert d_lo>0 if expect[k]>0 else d_hi<0
    # Cusp exact factorisation; ydag sits strictly within the y interval.
    y=sp.symbols('y')
    spB=lambda k,z: z**k*(1-z)**(3-k)
    cusp_poly=(4*y-3)*(16*y**2-4*y-3)/64
    assert sp.expand(spB(2,sp.Rational(3,4))-spB(2,y)-cusp_poly)==0
    assert Q(23,40)>RY[0] and Q(23,40)<RY[1]
    assert Q(13)>Q(18,5)**2 and Q(13)<Q(29,8)**2
    # ydag=(1+sqrt(13))/8 belongs (23/40, 37/64=RY[1]).
    x=sp.symbols('x')
    source_signs={
        ('x',sp.Rational(1,4)):(-1,1,1,1),
        ('x',sp.Rational(3,4)):(-1,-1,1,1),
        ('y',sp.Rational(1,4)):(1,1,-1,-1),
    }
    def tagged_poly(t,anchor,sgns):
        return sp.expand(sp.Rational(1,2)*sum(W[k]*sgns[k]*(spB(k,anchor)-spB(k,t)) for k in range(4)))
    cx=sp.expand((63*tagged_poly(x,sp.Rational(1,4),source_signs[('x',sp.Rational(1,4))])+tagged_poly(x,sp.Rational(3,4),source_signs[('x',sp.Rational(3,4))]))/256)
    assert sp.expand(sp.diff(cx,x)+(1-x)*(189-183*x)/256)==0
    for sigma,target in [(1,3*y*(1-y)/64),(-1,3*y*(18-25*y)/256)]:
        cy=sp.expand((9*tagged_poly(y,sp.Rational(1,4),source_signs[('y',sp.Rational(1,4))])+7*tagged_poly(y,sp.Rational(3,4),(-1,-1,sigma,1)))/256)
        assert sp.expand(sp.diff(cy,y)-target)==0
    # Uniform exact bounds on derivatives over R0, split at ydag.
    xh=RX[1]
    p_min=(1-xh)*(189-183*xh)/256
    assert p_min>Q(2,5)
    # Left cy<=3/256; right cy<1/40 by monotonicity above y=23/40.
    cyr=3*Q(23,40)*(18-25*Q(23,40))/256
    assert cyr<Q(1,40)
    # On -+- b_x=(3/4)(1-2x)>0; -b_y=(3/16)(2y-1)>0.
    bx_max=Q(3,4)*(1-2*RX[0]);by_abs_min=Q(3,16)*(2*RY[0]-1)
    assert Q(3,256)*bx_max/by_abs_min==Q(21,64)<Q(2,5)
    by_abs_right=Q(3,16)*(2*Q(23,40)-1)
    assert Q(1,40)*bx_max/by_abs_right==Q(35,96)<Q(2,5)
    # r1=0 graph y'>0 and y'<5. Along it, cx+cy*y'<0 on BOTH tag sides.
    assert 4*Q(79,100)*Q(37,100)*4 < 5
    assert Q(2,5)-Q(1,40)*5>0
    # r0=0 left: r2 decreases with x. f(t) unimodal at 1/2.
    f=lambda t:t*(2-3*t)/(1-t)**2
    assert f(Q(6,25))==Q(192,361)<Q(3,4)==f(Q(3,5))
    # r1=0 right: -(r3+r0)' > 12/5*(1-2*.24)-3/5*(2*(2/3)-1)*5 >0
    assert Q(12,5)*(1-2*Q(6,25))-Q(3,5)*(2*Q(2,3)-1)*5==Q(31,125)>0
    # The entire right r1 arc in R0 is inside Stage329 curvature rectangle.
    assert r(1,RX[1],Q(577,1000))<0
    # Existence through E=3/10000: at x=15/64 the r1 root is in (.565,.566),
    # and the right-arc b formula decreases with y; hence the value at .566
    # is a strict certified lower bound for the arc endpoint.
    assert r(1,RX[1],Q(565,1000))>0
    assert r(1,RX[1],Q(566,1000))<0
    endpoint_b_lower=KAPPA*(-r(3,RX[1],Q(566,1000))-r(0,RX[1],Q(566,1000)))
    bstar_upper=KAPPA*(-r(3,Q(231083,10**6),Q(5554961,10**7)))
    assert endpoint_b_lower > bstar_upper+Q(3,10000)


def main():
    bstar_upper=verify_root_bracket()
    verify_tag_gradients_and_slopes()
    leaves=build_cover()
    sha=write_and_readback_cover(leaves)
    counts=Counter(leaf[0] for leaf in leaves)
    print("GLOBAL_MAIN_SOURCE_PIN=13c1954f3fddaedfe5b4beaae57ce1e5ec2d1784")
    print("ENTERPRISE_MATH_MAIN_SOURCE_PIN=9412897fb2b8e77bb30ee26391fb65edaba2a8fd")
    print("P000_V5_SOURCE_BLOB=bcc2590d3168a28f72e8b9f0f9b1f76faadcd488")
    print(f"BUDGET_THRESHOLD={strq(THRESHOLD)}")
    print(f"INTERNAL_REGION_X=[{strq(RX[0])},{strq(RX[1])}]")
    print(f"INTERNAL_REGION_Y=[{strq(RY[0])},{strq(RY[1])}]")
    print(f"DOUBLE_ZERO_BETA_STRICT_UPPER={strq(bstar_upper)}")
    print(f"CERTIFICATE_LEAVES={len(leaves)} HIGH={counts['HIGH']} INNER={counts['INNER']} MAX_DEPTH={max(t[1] for t in leaves)}")
    print(f"CERTIFICATE_AREA_EXACT=1/1 SHA256={sha}")
    print("TAG_CHECK=15_CONSTANT_SIGNS_PLUS_ONE_EXACT_CUSP; BOTH_PIECEWISE_GRADIENT_IDENTITIES=PASS")
    print("FOUR_CHAMBER_DERIVATIVE_MONOTONICITY_AND_BOTH_ZERO_ARCS=EXACT_ALGEBRAIC_ARGUMENT")
    print("TWO_SOURCE_E_UPPER=3/10000; STAGE329_STRICT_CONCAVITY_IS_EXPLICIT_UPSTREAM_AUTHOR_DEPENDENCY")
    print("STAGE340B_GLOBAL_INITIAL_PARETO_INTERVAL_EXACT_PASS")


if __name__=="__main__":
    main()

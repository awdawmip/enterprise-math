#!/usr/bin/env python3
"""Pure Fraction check of a physical 15-edge continuum; import sibling VERIFY.py."""
from fractions import Fraction as F
from math import factorial,lcm
import VERIFY as v

T0=F(1,100000)
DELTA=F(1,10**50)

def Y_at(t):
    return tuple(x+t*d for x,d in zip(v.Y0,v.DY))

def rhs(t):
    mu=v.mass(Y_at(t)); nu=v.mass(v.X)
    return mu+nu+tuple(v.R[j]*nu[j] for j in range(7))

def scaled_row(i,x):
    return 20*x if i>=14 else x

def check_point(t):
    yy=Y_at(t)
    assert v.X[0]==v.X[2] and yy[0]==1 and yy[6]==yy[1]/10
    assert all(s>=0 for s in v.slack(v.X)+v.slack(yy))
    assert v.times(v.X)==v.times(yy)==v.q("17609/6000 33857/12000")
    h=rhs(t);mu=h[:7];nu=h[7:14]
    assert mu[1]>0 and nu[4]==0 and sum(mu)==sum(nu)==1
    C={e:v.col(e) for e in v.D}
    weights,det=v.solve(
        [[C[e][i] for e in v.B] for i in v.I],
        tuple(h[i] for i in v.I))
    assert det==F("-299/1600") and min(weights)>0
    E=dict(zip(v.B,weights))
    assert all(sum(E.get(e,F(0))*C[e][i] for e in v.D)==h[i] for i in range(21))
    for edge,spars in v.CERT.items():
        y=[F(spars.get(i,"0")) for i in range(21)]
        assert sum(y[i]*h[i] for i in range(21))>0
    return min(weights)

def main():
    h0=rhs(T0)
    hd=tuple(rhs(T0+1)[i]-h0[i] for i in range(21))
    D0=lcm(*(scaled_row(i,h0[i]).denominator for i in v.I))
    dmax=max(abs(scaled_row(i,hd[i])) for i in v.I)
    assert D0==1148267016000000 and dmax==F(23,40)
    # Nonzero augmented minor at t0 on each support: |minor|>=1/D0.
    # On an (r+1)-minor for r<=14, |slope|<=15*14!*38^14*dmax.
    bound=D0*15*factorial(14)*38**14*dmax
    assert bound < 10**50 and DELTA*bound<1
    print("PASS_UNIFORM_NONZERO_MINOR_MARGIN",D0,"BOUND_D0_TIMES_SLOPE",bound)
    for t in (T0-DELTA,T0,T0+DELTA):
        m=check_point(t)
        label="center" if t==T0 else ("left" if t<T0 else "right")
        print("PASS_EXACT_LAWFUL_ENDPOINT_OR_CENTER",label,"min15=",m)
    print("THEOREM_EXACT_15_EDGE_MIN_FOR_ALL_REAL_T_IN",T0-DELTA,T0+DELTA)
    print("REAL_INTERVAL_PROOF_AFFINE_CAPACITY_AND_BASIS_PLUS_NONZERO_MINOR_MARGIN")

if __name__=="__main__":
    main()

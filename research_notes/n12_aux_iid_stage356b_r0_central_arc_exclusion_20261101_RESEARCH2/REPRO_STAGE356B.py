#!/usr/bin/env python3
"""Stage356-B rational checker: an open r0=0 Pareto-exclusion slab.

This checks rational corner inequalities used in a symbolic proof valid for
all real points of a specified algebraic arc. It does not sample the arc or
claim P000/native BRC-Shor computation.
"""
from fractions import Fraction as F

X_LO, X_HI = F(229, 1000), F(233, 1000)
Y_LO, Y_HI = F(533, 1000), F(59, 100)
Y_RIGHT_HI = F(14, 25)
K = F(37)
W = (1,3,3,1)
M = (61,21,9,9)


def B(k,z):
    return z**k*(1-z)**(3-k)


def r(k,x,y):
    return (4*B(k,x)+B(k,y))/5-F(M[k],160)


def b(x,y):
    return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))


def D(a,z):
    return sum(F(W[k],2)*abs(B(k,a)-B(k,z)) for k in range(4))


def c(x,y):
    return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256


def F_arc(x,y):
    return 4*(1-x)**3+(1-y)**3-F(61,32)


def isolator_star():
    # Same independently checkable algebraic isolator as Stage355-B.
    slo,shi=F('0.768916059144'),F('0.768916059145')
    tlo,thi=F('0.444491142719'),F('0.444491142727')
    A=lambda s:F(41,16)-4*s*s
    C=lambda s:F(61,32)-4*s**3
    P=lambda s:A(s)**3-C(s)**2
    assert P(slo)<0<P(shi)
    assert 0<tlo<thi<slo
    assert tlo*tlo < A(shi)
    assert thi*thi > A(slo)
    assert C(slo)>0 and C(shi)>0
    # On this isolator 12*s*(s-t)>0 for f(s)=4s^3+t(s)^3.
    # Squaring is reversible since A, C, t are positive; P has opposite signs.
    xlo,xhi=1-shi,1-slo
    ylo,yhi=1-thi,1-tlo
    assert X_LO<xlo<xhi<X_HI
    assert Y_LO<ylo<yhi<Y_RIGHT_HI
    return (slo,shi,tlo,thi), (xlo,xhi,ylo,yhi)


def branch_check():
    # Arc monotonic: F_arc decreases strictly in both coordinates. A unique
    # y exists for each x of this slab, and rational corners enclose it.
    assert F_arc(X_LO,Y_HI)<0
    assert F_arc(X_HI,Y_LO)>0
    assert F_arc(X_LO,Y_LO)>0 and F_arc(X_HI,Y_HI)<0
    # Selected extrema by monotonicity of z^2*(1-z) for 0<z<2/3.
    r2low=r(2,X_LO,Y_LO)
    r3high=r(3,X_HI,Y_HI)
    assert X_HI<F(2,3) and Y_HI<F(2,3)
    assert r2low>0 and r3high<0
    # s>t and s+t<4st all across the bounding rectangle.
    smin,smax=1-X_HI,1-X_LO
    tmin,tmax=1-Y_HI,1-Y_LO
    assert smin>tmax>0
    margin_deriv=4*smin*tmin-(smax+tmax)
    assert margin_deriv>0
    return r2low,r3high,margin_deriv


def cost_sign_check():
    a,bp=F(1,4),F(3,4)
    # D(1/4,x): {1,2,3} positive; D(3/4,x): {2,3} positive.
    for endpoint in (X_LO,X_HI):
        assert B(0,a)-B(0,endpoint)<0
        for k in (1,2,3): assert B(k,a)-B(k,endpoint)>0
        for k in (0,1): assert B(k,bp)-B(k,endpoint)<0
        for k in (2,3): assert B(k,bp)-B(k,endpoint)>0
    # D(1/4,y): {0,1} positive; D(3/4,y): k3 positive,
    # k0,k1 negative, and k2 may change sign once.
    for endpoint in (Y_LO,Y_HI):
        for k in (0,1): assert B(k,a)-B(k,endpoint)>0
        for k in (2,3): assert B(k,a)-B(k,endpoint)<0
        for k in (0,1): assert B(k,bp)-B(k,endpoint)<0
        assert B(3,bp)-B(3,endpoint)>0
    assert B(2,bp)-B(2,Y_RIGHT_HI)>0
    assert Y_HI<F(18,25) # positivity in the 'k3 only' cost-branch
    # With x,y in right half-slab, x'=1,y'=37,
    # b'_+ = 3/16*[4(1-2x)+37(1-2y)] < 0.
    b_slope_upper=F(3,16)*(4*(1-2*X_LO)+K*(1-2*Y_LO))
    assert b_slope_upper < 0
    # c'_+ = [-189(1-x)^2 -6x(1-x)+12K y(1-y)]/256;
    # drop the strictly negative middle term, use y(1-y)<=1/4.
    c_slope_upper=(-189*(1-X_HI)**2+3*K)/256
    assert c_slope_upper < 0
    # Independent exact raw 16-label semantics on one rational sign chamber.
    q=(F(233,1000),F(535,1000))
    vals=tuple(r(k,*q) for k in range(4))
    assert vals[0]<0 and vals[1]>0 and vals[2]>0 and vals[3]<0
    assert b(*q)==F(15,16)*(r(1,*q)+r(2,*q))
    return b_slope_upper,c_slope_upper,vals


def main():
    iso,star=isolator_star()
    r2low,r3high,deriv=branch_check()
    bs,cs,signs=cost_sign_check()
    # The proof's two algebraic branches and derivative formulas follow by
    # direct expansion of B_k. Finite assertion is NOT substituted for the
    # analytic monotonicity argument recorded in PROOF_STAGE356B.md.
    print('STAGE356B_R0_ARC_OPEN_SLAB_STRICT_PARETO_EXCLUSION_EXACT_PASS')
    print('model: labeled four-coordinate cubic Bernoulli observer; two-source cost is additive')
    print('slab_x:',X_LO,X_HI,'slab_y_enclosure:',Y_LO,Y_HI)
    print('root_s_t_brackets:',*map(str,iso))
    print('root_xy_brackets:',*map(str,star))
    print('r2_corner_lower:',r2low,'r3_corner_upper:',r3high)
    print('s_t_derivative_margin_lower:',deriv)
    print('right_tangent_direction: dx=1,dy=',K)
    print('right_tangent_b_slope_upper:',bs,'right_tangent_c_slope_upper:',cs)
    print('theorem: r0=0 & x in [229/1000,233/1000] & q!=qstar => locally or globally strictly b,c-dominated')
    print('exception: qstar at r0=r1=0; outer r0=0 arcs not excluded')
    print('scope: exact real continuum in external source-labeled auxiliary model; no P000/X6 correspondence')
    print('status: PORTABLE_AUTHOR_THEOREM / FRACTION_RATIONAL_ASSERTIONS_EXECUTED / UNREVIEWED / NOT_ADMITTED')

if __name__=='__main__':
    main()

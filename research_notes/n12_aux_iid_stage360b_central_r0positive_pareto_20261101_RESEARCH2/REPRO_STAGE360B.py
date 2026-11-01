#!/usr/bin/env python3
"""Stage360-B: exact rational checks for a continuous Pareto dominance theorem.

The universal quantifiers are justified by analytic monotonicity/derivative
bounds in PROOF_STAGE360B.md; this script verifies all rational coefficients,
corner bounds, audit signs, and a non-vacuous rational witness exactly.
"""
from fractions import Fraction as F

W=(1,3,3,1)
M=(61,21,9,9)
XL=F(229,1000)
XH=F(233,1000)
XT=F(234,1000)
YL=F(13,25)
YH=F(27,50)
CAP=F(299,50000)
COEFF=((F(1),F(-3),F(3),F(-1)),
       (F(0),F(1),F(-2),F(1)),
       (F(0),F(0),F(1),F(-1)),
       (F(0),F(0),F(0),F(1)))

def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y): return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y): return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def D(a,z): return sum((F(W[k])*abs(B(k,a)-B(k,z)) for k in range(4)),F(0))/2
def c(x,y): return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

def dpoly(coeff): return tuple(F(i)*coeff[i] for i in range(1,len(coeff)))
def linear_combination(polys,factors):
    n=max(map(len,polys))
    return tuple(sum((f*(p[i] if i<len(p) else 0) for f,p in zip(factors,polys)),F(0)) for i in range(n))

def check():
    assert XL<XH<XT<F(1,4)<F(1,3)<YL<YH<F(2,3)
    # r1 increases in x and decreases in y; r2,r3 increase in both variables.
    r1_min=r(1,XL,YH)
    r2_min=r(2,XL,YL)
    r3_max=r(3,XT,YH)
    assert r1_min==F(630489,1250000000)>0
    assert r2_min==F(2567511,1250000000)>0
    assert r3_max==-F(4533399,312500000)<0
    # r0<0 or >0 is allowed for the search rectangle; this theorem selects r0>0.
    # For x in [XL,XT], audit signs of Bk(a)-Bk(x) are fixed.
    audit1=(-1,1,1,1)
    audit2=(-1,-1,1,1)
    for k in range(4):
        for xx in (XL,XT):
            assert (B(k,F(1,4))-B(k,xx))*audit1[k]>0
            assert (B(k,F(3,4))-B(k,xx))*audit2[k]>0
    dp=[dpoly(crow) for crow in COEFF]
    # On r-sign +++-, b_x has coefficient 4/5*5/32 = 1/8.
    bx=linear_combination(dp,tuple(F(W[k]*[1,1,1,-1][k],8) for k in range(4)))
    cx=linear_combination(dp,tuple(-F(W[k]*(63*audit1[k]+audit2[k]),512) for k in range(4)))
    assert bx==(F(0),F(0),-F(3,4))
    # c_x = -3*(1-x)*(63-61*x)/256.
    assert cx==(-F(189,256),F(372,256),-F(183,256))
    assert bx[2] < 0
    min_b_gradient=F(3,4)*XL**2
    min_c_gradient=F(3,256)*(1-XT)*(63-61*XT)
    assert min_b_gradient==F(157323,4000000)>F(39,1000)
    assert min_c_gradient==F(27993087,64000000)>F(2,5)
    # Globally in the y-coordinate, |Bk'|<=3 and sum weights = 8.
    assert sum(W)==8
    Lb=F(5,32)*F(1,5)*sum(W)*3
    Lc=F(9+7,256)*F(1,2)*sum(W)*3
    assert Lb==Lc==F(3,4)
    assert F(39,1000)-F(3,400)==F(63,2000)>F(3,100)
    assert F(2,5)-F(3,400)==F(157,400)>F(39,100)
    # Bound r0 drift when x increases; N>24/(5*r0) ensures strict positivity.
    assert F(12,5)*F(5,24)==F(1,2)
    # Relevant-budget cap holds for every point in the selected positive-r0
    # sign chamber, since r3 increases in both coordinates and b=-5*r3/16.
    chamber_max_b = -F(5,16)*r(3,XL,YL)
    assert chamber_max_b == b(XL,YL) < CAP
    # One rational interior case; its source remains strictly r0 positive.
    p=(F(231,1000),F(53,100))
    q=(F(232,1000),F(53,100))
    assert XL<=p[0]<q[0]<=XH and YL<=p[1]<=YH
    assert r(0,*p)>0 and r(0,*q)>0
    bgain=b(*p)-b(*q)
    cgain=c(*p)-c(*q)
    assert bgain==F(160777,4000000000)>0
    assert cgain==F(112689397,256000000000)>0
    assert b(*p)<CAP and b(*q)<CAP
    print('STAGE360B_CENTRAL_R0_POSITIVE_SIGN_CHAMBER_PARETO_EXACT_PASS')
    print('domain x in [229/1000,233/1000], y in [13/25,27/50], r0(x,y)>0')
    print('r1_min',str(r1_min),'r2_min',str(r2_min),'r3_max',str(r3_max))
    print('audit_x_signs',audit1,audit2)
    print('db_dx', '-3*x*x/4', 'minus_derivative_strict_lower',str(min_b_gradient))
    print('dc_dx','-3*(1-x)*(63-61*x)/256','minus_derivative_strict_lower',str(min_c_gradient))
    print('global_y_lipschitz',str(Lb),str(Lc))
    print('rational_witness N>max(1000,24/(5*r0)); xprime=(floor(N*x)+1)/N; delta=xprime-x; M>100/delta; yprime=floor(M*y)/M')
    print('strict_gains b_gain>3*delta/100, c_gain>39*delta/100')
    print('entire_chamber_b_upper',str(chamber_max_b),'budget_cap',str(CAP))
    print('example_p',str(p),'example_q',str(q))
    print('example_b_gain',str(bgain),'example_c_gain',str(cgain))
    print('example_r0',str(r(0,*p)),str(r(0,*q)))
    print('status PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED')

if __name__=='__main__': check()
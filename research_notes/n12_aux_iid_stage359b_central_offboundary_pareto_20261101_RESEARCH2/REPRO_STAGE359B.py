#!/usr/bin/env python3
"""Stage359-B: exact continuous central off-boundary Pareto direction.

All decisive inequalities and polynomial identities are Fraction-exact. 
The universal statement uses monotonicity, fixed residual/audit signs and 
polynomial derivatives, not a finite-sample inference.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

W = (1,3,3,1)
M = (61,21,9,9)
X0, X1 = F(23,100), F(119,500)
Y0, Y1 = F(29,50), F(3,5)
CAP = F(299,50000)
B_COEFFS = (
    (F(1),F(-3),F(3),F(-1)),
    (F(0),F(1),F(-2),F(1)),
    (F(0),F(0),F(1),F(-1)),
    (F(0),F(0),F(0),F(1)),
)

def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y): return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y): return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def D(a,z): return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
def c(x,y):
    return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

def poly_diff(coeff): return tuple(F(i)*coeff[i] for i in range(1,len(coeff)))
def lincomb(coeffs, factors):
    m=max(map(len,coeffs))
    return tuple(sum((f*(coeff[i] if i<len(coeff) else 0) for coeff,f in zip(coeffs,factors)),F(0)) for i in range(m))

def sign_str(v): return '+' if v>0 else '-' if v<0 else '0'
def check():
    assert X0 < F(231,1000) < F(233,1000) < X1
    # On X, B0 decreases, B1 increases, B2 increases, B3 increases.
    # On Y, B0 decreases, B1 decreases, B2 increases, B3 increases.
    # These signs follow directly from the factored polynomial derivatives.
    assert X1 < F(1,3) < Y0 < Y1 < F(2,3)
    rx = ((r(0,X0,Y0),'<'), (r(1,X1,Y0),'<'),
          (r(2,X0,Y0),'>'), (r(3,X1,Y1),'<'))
    assert rx[0][0] == -F(603,500000)
    assert rx[1][0] == -F(72807,312500000)
    assert rx[2][0] == F(2297,500000)
    assert rx[3][0] == -F(707807,312500000)
    assert all((value<0 if direction=='<' else value>0) for value,direction in rx)
    # For every y in [Y0,Y1], the sign patterns for B(a)-B(y)
    # cannot change: Bk is monotone on this interval.
    aud1 = (1,1,-1,-1)
    aud2 = (-1,-1,-1,1)
    for k in range(4):
        for y in (Y0,Y1):
            assert (B(k,F(1,4))-B(k,y))*aud1[k] > 0
            assert (B(k,F(3,4))-B(k,y))*aud2[k] > 0
    diffs=[poly_diff(row) for row in B_COEFFS]
    residual_sign=(-1,-1,1,-1)
    bdy=lincomb(diffs,tuple(F(W[k]*residual_sign[k],32) for k in range(4)))
    cdy=lincomb(diffs,tuple(-F(W[k]*(9*aud1[k]+7*aud2[k]),512) for k in range(4)))
    assert bdy == (F(0),F(3,8),-F(9,16))
    assert cdy == (F(0),F(27,128),-F(75,256))
    def bdy_value(z): return F(3,16)*z*(2-3*z)
    def cdy_value(z): return F(3,256)*z*(18-25*z)
    # Both derivative functions strictly decrease on Y: 
    # bdy'(z)=3(2-6z)/16 <0; cdy'(z)=3(18-50z)/256<0.
    assert 2-6*Y0 <0 and 18-50*Y0<0
    assert bdy_value(Y1)==F(9,400)
    assert cdy_value(Y1)==F(27,1280)
    # Constructive rational witness: choose integer N>200/(y-Y0),
    # m=floor(N*x), Q=(m/N,Y0). Global x-Lipschitz bounds
    # |b_x|<=3, |c_x|<=3 follow from |Bk'|<=3 and sum W=8.
    # Thus |x-m/N|< (y-Y0)/200, and both objectives decrease.
    assert sum(W)==8
    assert F(5,32)*F(4,5)*8*3 == 3
    assert F(63+1,256)*F(1,2)*8*3 == 3
    assert F(9,400)-F(3,200) == F(3,400) > 0
    assert F(27,1280)-F(3,200) == F(39,6400) > 0
    # Explicit rational interior example within the b budget.
    xp,yp=F(231,1000),F(3,5)
    qy=Y0
    assert X0<xp<X1 and Y0<yp<=Y1
    assert r(0,xp,yp)<0 and b(xp,yp)<CAP
    db=b(xp,yp)-b(xp,qy)
    dc=c(xp,yp)-c(xp,qy)
    assert db>F(9,400)*(yp-qy) and dc>F(27,1280)*(yp-qy)
    assert db>0 and dc>0
    print('STAGE359B_CENTRAL_NONZERO_R0_PARETO_MONOTONE_DIRECTION_EXACT_PASS')
    print('domain x in [23/100,119/500], y in (29/50,3/5]')
    print('residual_signs', ''.join(sign_str(z) for z,_ in rx), 'extreme_bounds',*[str(z) for z,_ in rx])
    print('audit_signs', ''.join('+' if s>0 else '-' for s in aud1), ''.join('+' if s>0 else '-' for s in aud2))
    print('db_dy', '3*y*(2-3*y)/16', 'uniform_lower',F(9,400))
    print('dc_dy', '3*y*(18-25*y)/256', 'uniform_lower',F(27,1280))
    print('rational_witness_rule', 'N>200/(y-29/50), m=floor(N*x), Q=(m/N,29/50)')
    print('guaranteed_strict_gains', 'b_gain>3*(y-29/50)/400', 'c_gain>39*(y-29/50)/6400')
    print('exact_witness_point', 'p', str((xp,yp)), 'q',str((xp,qy)))
    print('p_error',str(b(xp,yp)),'q_error',str(b(xp,qy)),'error_gain',str(db))
    print('p_cost',str(c(xp,yp)),'q_cost',str(c(xp,qy)),'cost_gain',str(dc))
    print('point_b_cap',str(CAP),'point_r0',str(r(0,xp,yp)))
    print('status PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED')

if __name__=='__main__': check()

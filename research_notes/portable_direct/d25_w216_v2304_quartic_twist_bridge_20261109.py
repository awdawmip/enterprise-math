#!/usr/bin/env python3
"""Independent exact 216/2304 CM-parameter twist and p^2 point-count checker.
AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
Pure integer/Fraction arithmetic; does not execute divided-power H0/B0.
"""
import json
from fractions import Fraction as Q
from pathlib import Path

# Coefficient ring K = Q[T] / (T^2-2).
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def mul(x, y): return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def scale(x, r): return (x[0]*r, x[1]*r)
def neg(x): return scale(x, -1)
def sub(x, y): return add(x, neg(y))
def power(x, n):
    z = (Q(1), Q(0))
    for _ in range(n): z = mul(z, x)
    return z
ONE = (Q(1), Q(0))
T = (Q(0), Q(1))

# E3^sigma: y^2 + xy + ((2+T)/108)y = x^3.
cs = (Q(2, 108), Q(1, 108))
c43 = sub(ONE, scale(cs, 24))
c63 = add(sub(scale(cs,36), ONE), scale(power(cs,2),-216))
delta3 = mul(power(cs,3), sub(ONE,scale(cs,27)))
# E4(v): z^2 = u^3+u^2+((1-v)/4)u, v=(3-2T)/6.
v = (Q(1,2), -Q(1,3))
b = scale(sub(ONE,v),Q(1,4))
c44 = sub(scale(ONE,16),scale(b,48))
c64 = add(scale(ONE,-64),scale(b,288))
delta4 = mul(scale(power(b,2),16),v)
d = (Q(0), Q(-3))
assert c44 == mul(power(d,2),c43)
assert c64 == mul(power(d,3),c63)
assert delta4 == mul(power(d,6),delta3)
# In the short Weierstrass variables X3=x+1/12, Y3=y+(x+cs)/2;
# X4=u+1/3, Y4=z, the isomorphism over K(sqrt(d)) is X4=d*X3, Y4=sqrt(d)^3*Y3.
A3, B3 = scale(c43,-Q(1,48)), scale(c63,-Q(1,864))
A4, B4 = sub(b,scale(ONE,Q(1,3))), sub(scale(ONE,Q(2,27)),scale(b,Q(1,3)))
assert A4 == mul(power(d,2), A3)
assert B4 == mul(power(d,3), B3)
# Clausen arguments: 4t(1-t)=1/2 and 4v(1-v)=1/9.
t=(Q(1,2),-Q(1,4))
assert scale(mul(t,sub(ONE,t)),4)==(Q(1,2),Q(0))
assert scale(mul(v,sub(ONE,v)),4)==(Q(1,9),Q(0))

def legendre_table(p):
    vals=[0]*p
    for n in range(1,p): vals[n] = 1 if pow(n,(p-1)//2,p)==1 else -1
    return vals

def count_points(p, family, independent_square_check=True):
    """Count over Fp[T]/(T^2-2) by Norm-Legendre; independently test all squares."""
    assert p % 24 in (13,19)
    leg=legendre_table(p)
    if family=='E4':
        b0, b1 = (3*pow(24,-1,p))%p, (2*pow(24,-1,p))%p
    else:
        b0, b1 = (2*pow(108,-1,p))%p, pow(108,-1,p)
        iv4 = pow(4,-1,p)
    sq = None
    if independent_square_check:
        sq=set()
        for a in range(p):
            for c in range(p): sq.add(((a*a+2*c*c)%p, (2*a*c)%p))
    total = 0
    cc = {-1:0,0:0,1:0}
    for a in range(p):
        for c in range(p):
            xx=(a*a+2*c*c)%p, (2*a*c)%p
            xxx=(xx[0]*a+2*xx[1]*c)%p, (xx[0]*c+xx[1]*a)%p
            bc=(b0*a+2*b1*c)%p, (b0*c+b1*a)%p
            if family=='E4':
                y0=(xxx[0]+xx[0]+bc[0])%p
                y1=(xxx[1]+xx[1]+bc[1])%p
            else:
                u0=(a+b0)%p; u1=(c+b1)%p
                y0=(xxx[0]+(u0*u0+2*u1*u1)*iv4)%p
                y1=(xxx[1]+2*u0*u1*iv4)%p
            chi=leg[(y0*y0-2*y1*y1)%p]
            if sq is not None:
                direct=(0 if (y0,y1)==(0,0) else (1 if (y0,y1) in sq else -1))
                assert direct==chi, (p,family,a,c,y0,y1)
            cc[chi]+=1; total+=chi
    return {'p':p,'family':family,'point_count':p*p+1+total,'character_sum':total,
            'chi_minus_one':cc[-1],'chi_zero':cc[0],'chi_plus_one':cc[1],
            'independent_square_test': independent_square_check}

def main():
    out=[]
    for p in (13,19,37,43,373):
        assert pow(2,(p-1)//2,p)==p-1  # T^p=-T.
        a=count_points(p,'E3sigma')
        b4=count_points(p,'E4')
        chi=legendre_table(p)[(-18)%p]
        a_trace=p*p+1-a['point_count']
        b_trace=p*p+1-b4['point_count']
        assert b_trace==chi*a_trace
        out.append({'p':p,'norm_twist':(-18)%p,'quadratic_twist_character':chi,
                    'E3sigma':a,'E4':b4,'trace_relation_verified':True})
    result={
      'schema':'D25_AUTHOR_SIDE_CM_QUARTIC_TWIST_V1',
      'status':'AUTHOR_SIDE_EXACT_ALGEBRA_AND_EXHAUSTIVE_FINITE_CHECK_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE',
      'task_id':'RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT',
      'publication_id':'TP2-B6F4FC938FF94941C1B7',
      'frozen_science_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
      'algebra':{'c4_ratio':'d^2=18','c6_ratio':'d^3=-54*T',
                 'discriminant_ratio':'d^6=5832','twist_parameter':'d=-3*T',
                 'j_equal':'2417472-1707264*T',
                 'clausen_arguments':['4t(1-t)=1/2','4v(1-v)=1/9']},
      'observations':out,
      'native_H0B0_not_executed':True}
    dest=Path(__file__).with_name('d25_w216_v2304_quartic_twist_results_20261109.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('PASS exact quadratic-twist invariants + complete Fp^2 point counts',len(out))
    for row in out:
        print(row['p'],row['quadratic_twist_character'],row['E3sigma']['point_count'],row['E4']['point_count'])
    print(dest)

if __name__=='__main__':main()

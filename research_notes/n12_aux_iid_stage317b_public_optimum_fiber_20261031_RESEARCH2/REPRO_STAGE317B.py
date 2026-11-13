#!/usr/bin/env python3
"""Stage317-B exact Fraction certificate: full-cube public-optimum fiber and tagged endpoint.
No floating arithmetic is used in assertions. Stage307-B2's continuum minimizer theorem
is a cited mathematical premise; this checker tests its algebraic root brackets and
independently enumerates finite probability atoms for rational witness rates.
"""
from fractions import Fraction as Q
from itertools import product

M = 10**15
a0, a1 = Q(768916059144478, M), Q(768916059144479, M)
y0, y1 = Q(555508857277, 10**12), Q(555508857278, 10**12)
p0, p1 = Q(1, 4), Q(3, 4)
masses = [(63, 1), (21, 3), (21, 3), (7, 9),
          (9, 7), (3, 21), (3, 21), (1, 63)]

def root_poly(a):
    return (Q(41, 16) - 4*a*a)**3 - (Q(61, 32) - 4*a**3)**2

# Stage307's unique a* root is now enclosed to 15 decimal places.
assert root_poly(a0) < 0 < root_poly(a1)
assert Q(41, 16) - 4*a0*a0 < (1-y0)**2
assert Q(41, 16) - 4*a1*a1 > (1-y1)**2
x0, x1 = 1-a1, 1-a0

B = lambda t, k: t**k * (1-t)**(3-k)
A = lambda t: 1 - 3*t*t + 2*t**3
multiplicity = [1, 3, 3, 1]

def D(s, t):
    return sum(Q(m, 2)*abs(B(s,k)-B(t,k)) for k,m in enumerate(multiplicity))

def block_public(u,v):
    return sum(Q(m, 512)*abs(64*B(u,k)+16*B(v,k)
                     -72*B(p0,k)-8*B(p1,k)) for k,m in enumerate(multiplicity))

def block_tagged(u,v):
    return (63*D(p0,u)+D(p1,u)+9*D(p0,v)+7*D(p1,v))/256

def tag_formula(x,y):
    return Q(33,1024)+(63*(1-x)**3 + A(x)-2*A(y)-Q(1295,64))/128

def pub_formula(x,y):
    return Q(9,256) - (4*x**3+y**3)/8

# Monotonic endpoint evaluation in the root rectangle gives rigorous risks.
P_low, P_high = pub_formula(x1,y1), pub_formula(x0,y0)
T_low, T_high = tag_formula(x1,y0), tag_formula(x0,y1)
assert Q(7558267237,10**12) < P_low < P_high < Q(7558267239,10**12)
assert Q(98134635052,10**12) < T_low < T_high < Q(98134635054,10**12)

# Exact finite trace test: every one of 128 source/h/three-bit atoms.
def vec(u,v):
    return [u,p0,p0,1-v, v,p1,p1,1-u]

def risks(t):
    public_true, public_rep = {}, {}
    tagged_true, tagged_rep = {}, {}
    for h,(a,b) in enumerate(masses):
        j,wy = h//4, h%4
        for s,weight in enumerate((a,b)):
            p = (p0,p1)[s]
            for bits in product((0,1), repeat=3):
                k = sum(bits)
                qtrue, qrep = Q(weight,256)*B(p,k),Q(weight,256)*B(t[h],k)
                kp=(wy,bits); kt=(s,j,wy,bits)
                public_true[kp]=public_true.get(kp,Q(0))+qtrue
                public_rep[kp]=public_rep.get(kp,Q(0))+qrep
                tagged_true[kt]=tagged_true.get(kt,Q(0))+qtrue
                tagged_rep[kt]=tagged_rep.get(kt,Q(0))+qrep
    tv=lambda lhs,rhs:sum(abs(lhs[k]-rhs[k]) for k in lhs)/2
    return tv(public_true,public_rep),tv(tagged_true,tagged_rep)

x, y = Q(231084,10**6), Q(555509,10**6)
t = vec(x,y)
p,tg = risks(t)
assert p == 2*block_public(x,y)
assert tg == Q(33,1024)+2*block_tagged(x,y)
assert tg == tag_formula(x,y)

# On each central public group, the two equal-weight port rates
# can be swapped without changing public observations, but tagged TV rises.
for swap01,swap10 in product((False,True),repeat=2):
    rates=t.copy()
    if swap01: rates[1],rates[5]=rates[5],rates[1]
    if swap10: rates[2],rates[6]=rates[6],rates[2]
    p2,t2=risks(rates)
    assert p2 == p
    assert t2 == tg + Q(99,1024)*(int(swap01)+int(swap10))

# Central exact two-moment recovery: roots of z^2-z+3/16 are 1/4,3/4.
assert p0+p1 == 1 and p0*p1 == Q(3,16)
assert (p0*p0+p1*p1)/2 == Q(5,16)
print('STAGE317B_PUBLIC_FLOOR_TAGGED_ENDPOINT_EXACT_PASS')
print('source_stage307b2: global two-rate uniqueness theorem (independent earlier proof)')
print('a_bracket:',a0,a1)
print('x_bracket:',x0,x1)
print('y_bracket:',y0,y1)
print('P_min_bracket:',P_low,P_high)
print('T_at_P_min_bracket:',T_low,T_high)
print('central_public_minimizers=4; unique_tagged_minimizer=central_MAP')
print('tagged_cost_per_swapped_central_group=99/1024')
print('rational_example:',p,tg)

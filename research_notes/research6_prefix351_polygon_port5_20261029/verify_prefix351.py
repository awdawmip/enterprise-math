#!/usr/bin/env python3
"""Exact auxiliary five-Port C^3 polygon obstruction with port-5 equality check.

Only Gaussian integer/rational identities, 45 provenance-preserving ordered BRC
source pairs and exact rational/integer-square-root interval certificates.
This is NOT a native X6, BRC evolution, phase-propagation or physics test.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path
import json

A = [
    [(4,0),(4,0),(0,0)],
    [(0,0),(-4,0),(4,0)],
    [(-5,3),(0,0),(-3,1)],
    [(-2,-2),(4,4),(2,2)],
    [(-2,0),(0,0),(5,2)],
]
S = [(4,0),(5,-2),(7,-4)]
q0=[Q(2125,3721),Q(200,3721),Q(29125,29768),Q(5825,7442),Q(31525,59536)]
qplus=[Q(4),Q(1),Q(1),Q(1),Q(1)]

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def zsum(items):
    ans=(0,0)
    for x in items: ans=add(ans,x)
    return ans

def ratio(x): return f'{x.numerator}/{x.denominator}'
def qr(t): return [(1-t)*u+t*v for u,v in zip(q0,qplus)]

# Full 45 source-labeled ordered pairs, not a positive-weight substitution.
paths=[]
raw=[]
for j in range(5):
    steps=[mul(A[j][k],S[k]) for k in range(3)]
    port_terms=[]
    for k,l in product(range(3),repeat=2):
        x=mul(steps[k],conj(steps[l]))
        port_terms.append(x)
        paths.append({'port':j+1,'source_k':k+1,'source_l':l+1,'real':x[0],'imag':x[1]})
    v=zsum(port_terms)
    assert v[1]==0
    raw.append(v[0])
assert len(paths)==45 and raw==[1360,128,2330,1864,1261]
assert all(q0[j]==Q(10,61)**2*Q(raw[j],64) for j in range(5))

# Exact Gaussian row-kernel identity and port-5 continuation identity.
b=[(-5,-9),(-3,-7),(0,-8),(2,0)]
assert all(zsum(mul(b[j],A[j][k]) for j in range(4))==(0,0) for k in range(3))
beta=[(Q(46,53),Q(61,212)),(Q(19,212),-Q(13,212)),(Q(245,424),-Q(123,424))]
assert all(zsum(mul(beta[j],A[j+1][k]) for j in range(3))==A[4][k] for k in range(3))

# Strict monotonicity g'(t) > 101801/66978 on [2/5,1].
assert q0[0]<4 and q0[1]>0 and q0[2]>Q(9,10) and q0[3]>Q(3,4)
assert 106>10**2 and 58<8**2 and Q(2,5)>Q(3,5)**2
slope_bound=Q(5,2)*(4-q0[0])-Q(20,3)-Q(40,9)*(1-q0[2])-Q(4,3)*(1-q0[3])
assert slope_bound==Q(101801,66978)>0

SCALE=10**18
def sqrt_interval(x):
    assert x>0
    m=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo,hi=Q(m,SCALE),Q(m+1,SCALE)
    assert lo*lo<=x<hi*hi
    return (lo,hi)

def g_interval(t):
    q=qr(t)
    v=[sqrt_interval(coeff*q[j]) for j,coeff in enumerate([106,58,64,4])]
    return v[0][0]-sum(e[1] for e in v[1:]),v[0][1]-sum(e[0] for e in v[1:])

left,right=Q(470271288587,10**12),Q(470271288588,10**12)
assert Q(2,5)<left<right<1
Gleft,Gright=g_interval(left),g_interval(right)
assert Gleft[1]<0 and Gright[0]>0

# At t_triangle, b_j*y_j (j=2,3,4) are aligned. Normalize common phase:
# y2=(-3+7i)*sqrt(q2/58), y3=i*sqrt(q3), y4=sqrt(q4).
# Therefore 424*y5 = (-1958+2210i)*sqrt(q2/58)
#                  + (26+38i)*sqrt(q3) + (245-123i)*sqrt(q4).
# Bracket every positive square-root monotonically across [left,right].
def increasing_bracket(j,coeff=Q(1)):
    low=sqrt_interval(coeff*qr(left)[j])[0]
    high=sqrt_interval(coeff*qr(right)[j])[1]
    return (low,high)
a=increasing_bracket(1,Q(1,58))
c=increasing_bracket(2)
d=increasing_bracket(3)
real_lo=(-1958*a[1]+26*c[0]+245*d[0])/424
real_hi=(-1958*a[0]+26*c[1]+245*d[1])/424
imag_lo=(2210*a[0]+38*c[0]-123*d[1])/424
imag_hi=(2210*a[1]+38*c[1]-123*d[0])/424
assert 0<real_lo<real_hi<Q(1,4)
assert 0<imag_lo<imag_hi<Q(1,2)
assert qr(left)[4]>Q(3,4)
assert Q(1,4)**2+Q(1,2)**2==Q(5,16)<Q(3,4)

result={
  'status':'PASS_AUTHOR_SIDE_EXACT_POLYGON_OBSTRUCTION_AND_PORT5_BOUNDARY_EXCLUSION',
  'scope':'auxiliary static C^3 five-Port measurements; no native X6 time dynamics',
  'read_pin_global':'38898088a2f45ce1a8fdd5be7b115e617b2fe83d',
  'read_pin_enterprise_math':'b7e005a480e17723d1fced8e1886681e78a3e88d',
  'model_A':A,'reference_source':S,'BRC_ordered_paths':paths,'BRC_count':len(paths),'raw_port_intensity':raw,
  'row_relation_1to4':b,
  'port5_coefficients_2to4_gaussian_rational':[[ratio(Q(x)),ratio(Q(y))] for x,y in beta],
  'g_derivative_strict_lower':ratio(slope_bound),
  't_polygon_strict_bracket':[ratio(left),ratio(right)],
  'g_at_left_certified_interval':[ratio(x) for x in Gleft],
  'g_at_right_certified_interval':[ratio(x) for x in Gright],
  'sqrt_interval_denominator':SCALE,
  'port5_forced_real_interval':[ratio(real_lo),ratio(real_hi)],
  'port5_forced_imag_interval':[ratio(imag_lo),ratio(imag_hi)],
  'forced_port5_mass_upper':ratio(Q(5,16)),
  'reported_q5_lower':ratio(Q(3,4)),
  'unconditional_conclusion':'no real source at t=t_polygon or for t>t_polygon through t=1',
  'conditional_consequence':'assuming six simple real sources at t=0 from PREFIX-349/342, a real critical target occurs at 0<t<t_polygon',
  'scientific_status':'AUTHOR_SIDE_EXACT_ARITHMETIC_UNREVIEWED_NOT_ADMITTED',
}
Path(__file__).with_name('RESULTS_PREFIX351.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['status'])
print('45 ordered source-labeled BRC port pairs verified; all row and port-5 identities exact')
print('derivative g prime strictly above',ratio(slope_bound),'on [2/5,1]')
print('unique polygon root bracket:',str(left),'< t_triangle <',str(right))
print('g(left) upper bound',float(Gleft[1]),'g(right) lower bound',float(Gright[0]))
print('at t_triangle forced |y5|^2 < 5/16 < q5(t_triangle) (which is >3/4)')

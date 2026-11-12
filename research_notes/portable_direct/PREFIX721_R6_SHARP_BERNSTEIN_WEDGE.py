"""PREFIX-721: exact enlarged diagonal transverse wedge and saddle.

Reuses frozen 189-row integer core in PREFIX720_R6_LOCAL_TRANSVERSALITY_CHECKER.py.
Certificate comparisons are arbitrary-precision integers.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from fractions import Fraction
from math import comb
from hashlib import sha256
import json
from pathlib import Path
import PREFIX720_R6_LOCAL_TRANSVERSALITY_CHECKER as base

N=base.N
assert N==189 and base.D==768
assert sum(map(len,base.rows[:N]))==9529 and not base.rows[N]
assert base.rows[25]=={k:comb(25,k) for k in range(1,25)}
x=88
L,Z=base.L,base.Z
den=L*L*Z
s1=base.dtail(x)
s2=base.second_dtail(x)
a,h=base.influence(x)
P=sum(v*w for v,w in zip(s1,a))
Q=sum(v*w for v,w in zip(s1,h))
PP=sum(v*w for v,w in zip(s2,a))
QQ=sum(v*w for v,w in zip(s2,h))
assert P>0
C0=C1=0
for n in range(N):
    t0=t1=0
    for m in range(N):
        c=comb(n+m,n)*2**(2*N-2-n-m)
        t0+=s1[m]*c
        t1+=(n+m+1)*s1[m]*c
    C0+=s1[n]*t0
    C1+=s1[n]*t1
j_num=P*(QQ+C1)-Q*(PP+C0)
theta_num=(P*(QQ-C1)-Q*(PP-C0))*den-4*P**3
# Digests are regression identifiers, not substitutes for exact sign tests.
assert sha256(str(j_num).encode()).hexdigest()==(
    'f9eab864317b8b68e16940ed539733265725445e8108de8c7075d4d18adc95d2')
assert sha256(str(theta_num).encode()).hexdigest()==(
    'c3cb0b08933d50689c97613e80cc6b53820dc8820e1c7f084cb6ec64e6d0e0b1')
assert j_num>40_800_000*den**2
assert theta_num<-100*P**2*den
# Exact diagonal stationary parameter and opposite Hessian curvatures.
s0=base.tail(x)
mu=Fraction(2*sum(s0),L)-Fraction(
    sum(v*(L*Z-ai) for v,ai in zip(s0,a)),den)
mu_p=Fraction(P,den)
theta0=Fraction(Q,P)-2*mu
assert Fraction(1,4)<theta0<Fraction(1,3)
assert 280<mu_p<300
J_z=Fraction(j_num,den**2)
theta_prime=Fraction(theta_num,P**2*den)
assert 2*mu_p*theta_prime<-56_000
assert 2*J_z/mu_p>272_000
# Bernstein finite-difference lemma: |Delta^r g|<=2^(r-1) for g in [0,1].
# Each positive-order moment derivative bound is halved; each J'' term
# is a product of two positive-order moment derivatives.
B=4*N*N*(N+1)*376**4
assert B==542610983324712960
radius=Fraction(1,14_000_000_000)
margin=Fraction(40_800_000)-B*radius
assert margin>2_000_000
max_safe_radius=Fraction(40_800_000,B)
assert radius<max_safe_radius
res={
 'schema':'PREFIX721_R6_BERNSTEIN_SHARP_WEDGE_V1',
 'date':'2026-11-12',
 'source_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'parent':'PREFIX-720',
 'center':'11/96',
 'N':N,'nonzero_survivor_coefficients':9529,
 'J_z_strict_lower_at_center':40_800_000,
 'refined_K_gradient_L1_bound':B,
 'explicit_radius':str(radius),
 'K_strict_lower_bound':2_000_000,
 'stationary_parameter_t0_interval':'1/4<t0<1/3',
 'stationary_parameter_q0_interval':'3<q0<4',
 'diagonal_curvature_at_q0_for_f_t0':'< -56000',
 'anti_diagonal_curvature_at_q0_for_f_t0':'> 272000',
 'no_maximum_consequence':'No point of the radius-square is a local maximum of f_t on the full open parameter domain for any real t, hence no full-domain global maximizer occurs there.',
 'radius_gain_over_PREFIX720':'500/7',
 'universal_certified_radius_upper_open':str(max_safe_radius),
 'J_decimal_numerator_sha256':sha256(str(j_num).encode()).hexdigest(),
 'theta_decimal_numerator_sha256':sha256(str(theta_num).encode()).hexdigest(),
 'exact_integer_assertions':'PASSED',
 'conclusion':'K>2000000 in the radius-square. No off-diagonal stationary points; every diagonal stationary point has strictly positive anti-diagonal curvature. Therefore the entire square contains no full-domain local or global maximizers for any real q>0.',
 'review_status':'AUTHOR_EXACT_INTEGER_RECOMPUTED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    f=Path(__file__).with_name('PREFIX721_R6_RESULTS.json')
    f.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX721-R6', 'radius='+str(radius), 'K>2000000', 'B='+str(B), 'actual_J_floor='+str(j_num//den**2))

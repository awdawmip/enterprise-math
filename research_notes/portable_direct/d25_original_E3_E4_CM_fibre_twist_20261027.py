#!/usr/bin/env python3
"""Original E3/E4 CM-fibre quadratic-twist checker; author-side, not native H0/B0."""
from fractions import Fraction as Q
import json
import hashlib

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
S = (Q(0), Q(1))

def aadd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def aneg(x):
    return (-x[0], -x[1])

def amul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def ascale(x, r):
    return (r*x[0], r*x[1])

def scalar(r):
    return (Q(r), Q(0))

# Published original curves: Chisholm et al., 2013, Sec. 2.
# E3(t): y^2+xy+(t/27)y=x^3, t3=(2-s)/4.
# E4(t): y^2=x(x^2+x+t/4), t4=(3-2s)/6.
# lambda3=4*t3*(1-t3)=1/2; lambda4=4*t4*(1-t4)=1/9.
t3 = ascale(aadd(scalar(2), aneg(S)), Q(1, 4))
t4 = ascale(aadd(scalar(3), ascale(S, -2)), Q(1, 6))
c3 = ascale(t3, Q(1, 27))
A3 = aadd(ascale(c3, Q(1, 2)), scalar(-Q(1, 48)))
B3 = aadd(aadd(scalar(Q(1, 864)), ascale(c3, -Q(1, 24))),
          ascale(amul(c3, c3), Q(1, 4)))
A4 = aadd(ascale(t4, Q(1, 4)), scalar(-Q(1, 3)))
B4 = aadd(scalar(Q(2, 27)), ascale(t4, -Q(1, 12)))
d = ascale(S, Q(1, 6))
assert A3 == (Q(-5, 432), Q(-2, 432))
assert B3 == (Q(12, 23328), Q(7, 23328))
assert A4 == (Q(-5, 24), Q(-2, 24))
assert B4 == (Q(7, 216), Q(6, 216))
assert amul(amul(d, d), A4) == A3
assert amul(amul(amul(d, d), d), B4) == B3
norm_d = d[0]*d[0] - 2*d[1]*d[1]
assert norm_d == Q(-1, 18)  # nonsquare in Q(s)

def point_counts(p):
    assert p%24 in (13, 19) and pow(2, (p-1)//2, p) == p-1
    inv = lambda a: pow(a%p, -1, p)
    def m(x, y):
        a,b=x; c,e=y
        return ((a*c+2*b*e)%p, (a*e+b*c)%p)
    def plus(x, y):
        return ((x[0]+y[0])%p, (x[1]+y[1])%p)
    def rational_pair(z):
        return tuple((int(a.numerator)*inv(int(a.denominator)))%p for a in z)
    a3,b3,a4,b4 = map(rational_pair, (A3,B3,A4,B4))
    twist = rational_pair(d)
    assert m(m(twist,twist),a4) == a3
    assert m(m(m(twist,twist),twist),b4) == b3
    char = [-1]*p
    char[0]=0
    for v in range(1,p):
        char[v*v%p]=1
    n3=n4=p*p+1
    for a in range(p):
        for b in range(p):
            x=(a,b)
            x2=m(x,x)
            x3=m(x,x2)
            f3=plus(plus(x3,m(a3,x)),b3)
            f4=plus(plus(x3,m(a4,x)),b4)
            n3+=char[(f3[0]*f3[0]-2*f3[1]*f3[1])%p]
            n4+=char[(f4[0]*f4[0]-2*f4[1]*f4[1])%p]
    norm_mod_p=-inv(18)%p
    chi=char[norm_mod_p]
    assert chi==(-1 if p%24==13 else 1)
    assert n3==(p-1)**2
    assert n4==((p+1)**2 if chi==-1 else (p-1)**2)
    assert n4-(p*p+1)==chi*(n3-(p*p+1))
    return dict(p=p, f_q_size=p*p, norm_d_mod_p=norm_mod_p,
                character_Fq_of_d=chi, points_original_E3=n3,
                points_original_E4=n4, frob_trace_E3=p*p+1-n3,
                frob_trace_E4=p*p+1-n4)

if __name__=='__main__':
    rows=[point_counts(p) for p in (13,19,37,43,61,67,373)]
    assert rows[-1]['points_original_E3']==138384
    assert rows[-1]['points_original_E4']==139876
    canon=json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    print('EXACT_SYMBOLIC_K_TWIST: PASS; Norm(d)=-1/18')
    for row in rows:
        print(json.dumps(row,sort_keys=True))
    print('SHA256_ROWS:',hashlib.sha256(canon.encode()).hexdigest())
    print('FINITE_EXACT_POINT_COUNT_CHECK: PASS')

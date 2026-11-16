"""R592: rational angle-grid certificate for a good circle of the R462 signed-BRC auxiliary scalar F.
All certificate inequalities are in Q, with no floating point in pass/fail decisions.
This script certifies the fixed circle r=5 (in the annulus (4,8)) and F_k vs F for k=64, 128.
It is not a test of the unconditional asymptotic good-circle selection loop.
"""
from fractions import Fraction as Q
from math import comb, factorial

J = 18
radius = Q(5)
M = 256
threshold = Q(1, 5)  # strictly certified lower bound min |F|>1/5

def a(j):
    return Q(24 * 8**j, factorial(2*j + 4))

def tail_a(start, r):
    b = a(start)*r**start
    q = Q(8)*r / ((2*start+6)*(2*start+5))
    assert q < 1
    return b/(1-q)

def deriv_upper(r, trunc=J):
    partial = sum((j*a(j)*r**(j-1) for j in range(1,trunc+1)), Q(0))
    start=trunc+1
    t0=start*a(start)*r**(start-1)
    q=Q(start+1,start)*8*r/((2*start+6)*(2*start+5))
    assert q<1
    return partial+t0/(1-q)

# Gaussian rational complex arithmetic; tuples for (Re,Im)
def c_mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def c_eval(z):
    w=(Q(0),Q(0))
    for j in range(J,-1,-1):
        w=c_mul(w,z)
        w=(w[0]+(-1)**j*a(j), w[1])
    return w

def c_square_mod(z): return z[0]*z[0]+z[1]*z[1]

def circle_unit(t, sign):
    x=(1-t*t)/(1+t*t)
    y=2*t/(1+t*t)
    return sign*x, sign*y

# Rational circle net: u(t) and -u(t), 0<=t<=1 and conjugates.
# |u'(t)| <=2; every circle point is within chord distance <=2/M of some net node.
# Hence on |z|=r point-to-node distance <=2r/M, not 4r/M.
T=tail_a(J+1,radius)
D=deriv_upper(radius)
angular=2*radius*D/M
required = threshold+T+angular
worst=None
min_re=None
for m in range(M+1):
    t=Q(m,M)
    for sign in (-1,1):
        unit=circle_unit(t,sign)
        w=c_eval((radius*unit[0], radius*unit[1]))
        mod2=c_square_mod(w)
        if min_re is None or w[0]<min_re:min_re=w[0]
        if worst is None or mod2<worst: worst=mod2
        assert mod2>required*required, (m,sign)
assert worst is not None
assert min_re > Q(1,10)+T+angular
print('R592_ZERO_FREE_DISK_REAL_PART_CERT_PASS','radius',radius,'real_part_lower',float(min_re-T-angular),'gt',0.1)
print('R592_RATIONAL_CIRCLE_PROOF_PASS','radius',radius,'J',J,'M',M,'nodes',2*(M+1))
print('R592_CERT_BOUND', 'min_mod_sq_gt',str(required**2),'min_actual_node_mod_sq',str(worst))
print('R592_CERT_TERMS','tail_lt',float(T),'deriv_lt',float(D),'arc_error_lt',float(angular),'min_F_gt',float(threshold))

# Independent finite-spectral error: exact Catalan source sums, no eigenvalue approximations.
def catalan(n):return comb(2*n,n)//(n+1)
def H(k,s):
    return comb(2*k+1+s,2*s)*sum(comb(s-1,2*q)*4**q*catalan(k-q)
        for q in range(min(k,(s-1)//2)+1))
def a_k(k,j):return Q(H(k,j+2),H(k,2)*k**(2*j))

for k in (64,128):
    d=2*k-1
    E=sum((abs(a_k(k,j)-a(j))*radius**j for j in range(d+1)),Q(0))+tail_a(d+1,radius)
    print('R592_FINITE_SPECTRAL_ROUCHE','k',k,'error_lt',float(E),'min_F_gt',float(threshold),'pass',E<threshold)
    assert E<threshold
assert J>=16
print('R592_EXACT_CONSTRUCTIVE_CIRCLE_AND_K128_ROUCHE_PASS')

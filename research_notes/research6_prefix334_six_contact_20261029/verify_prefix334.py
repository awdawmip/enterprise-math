#!/usr/bin/env python3
"""PREFIX-334 self-contained exact rational certificate for four BRC phase arcs.
No floating point, randomization, trigonometric approximation, or external network.
Source roots are uniquely located by Banach tests on rational boxes.
"""
from fractions import Fraction as F
from math import isqrt
import json
import sympy as sp

class IV:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(hi) if hi is not None else F(lo)
        assert self.lo<=self.hi
    def __add__(self, other):
        b=iv(other);return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,other):return self+(-iv(other))
    def __rsub__(self,other):return iv(other)+(-self)
    def __mul__(self,other):
        b=iv(other); vals=[a*x for a in (self.lo,self.hi) for x in (b.lo,b.hi)]
        return IV(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,other):
        b=iv(other)
        assert b.lo>0 or b.hi<0
        return self*IV(F(1)/b.hi,F(1)/b.lo)
    def sq(self):
        if self.lo>=0:return IV(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return IV(self.hi*self.hi,self.lo*self.lo)
        return IV(0,max(self.lo*self.lo,self.hi*self.hi))
    def __repr__(self):return f'[{self.lo}, {self.hi}]'

def iv(a):return a if isinstance(a,IV) else IV(a)
def cx(a,b=0):return (iv(a),iv(b))
def cx_add(a,b):return(a[0]+b[0],a[1]+b[1])
def cx_mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cx_conj(a):return(a[0],-a[1])
def cx_scale(a,f):return (a[0]*f,a[1]*f)
def cx_norm2(a):return a[0].sq()+a[1].sq()

def D(t):return F(t)
I=sp.I
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])/8
q=[sp.Rational(1,2),sp.Rational(1,4),sp.Rational(5,32),sp.Rational(13,8),sp.Rational(29,64)]
x=sp.symbols('x0:5',real=True)
a=sp.Matrix([x[0]+I*x[1],x[2]+I*x[3],x[4]])
# Source-preserving nine ordered BRC path-pair expression per port.
paths=[[sp.expand(A[j,k]*a[k]) for k in range(3)] for j in range(5)]
Q=[sp.expand(sum(paths[j][k]*sp.conjugate(paths[j][l]) for k in range(3) for l in range(3))) for j in range(5)]
assert all(sp.simplify(Q[j]-sp.expand((A*a)[j]*sp.conjugate((A*a)[j])))==0 for j in range(5))
FE=sp.Matrix([sp.expand(Q[j]-q[j]) for j in range(5)])
J=FE.jacobian(x)
H=[[[sp.diff(J[j,k],x[l]) for l in range(5)] for k in range(5)] for j in range(5)]
Lips=max(sum(abs(H[j][k][l]) for k in range(5) for l in range(5)) for j in range(5))
assert Lips<=sp.Rational(49,2),(Lips,'Lipschitz')

rootcenters=[
 ['-0.652520278328','0.397968408605','0.888712463176','0.996382068075','0.803725555834'],
 ['-0.765784033337','-0.436053381316','0.918203961961','-0.969922495205','0.674790007357'],
]
rho=sp.Rational(1,10**9)
for cen in rootcenters:
    cv=[sp.Rational(v) for v in cen]
    subs=dict(zip(x,cv))
    f0=FE.subs(subs)
    B=J.subs(subs).inv()
    normB=max(sum(abs(B[j,k]) for k in range(5)) for j in range(5))
    err=max(abs(y) for y in B*f0)
    assert normB<8,(normB,'Bnorm')
    assert err<sp.Rational(1,10**11),(err,'residual')
    assert err+normB*Lips*rho*rho<rho, 'Banach self-map'
    assert normB*Lips*rho<1, 'Banach contraction'

# Interval roots in the rational Banach boxes.
seeds=[
 [cx(0),cx(1,1),cx(1)],
 [cx(0),cx(1,-1),cx(1)],
]
for cc in rootcenters:
    bb=[IV(F(s)-F(1,10**9),F(s)+F(1,10**9)) for s in cc]
    seeds.append([cx(bb[0],bb[1]),cx(bb[2],bb[3]),cx(bb[4])])
# Rational bracket sqrt(5/8), with verified inequality (no floating estimate).
scale=10**13
v=isqrt(5*scale*scale//8)
lo=F(v,scale);hi=F(v+1,scale)
assert lo*lo<=F(5,8)<hi*hi
s=IV(lo,hi)
# Fourth port coefficients A[3,k] as exact complex rationals.
coeffs=[cx(F(-2,8),F(-2,8)),cx(F(4,8),F(4,8)),cx(F(2,8),F(2,8))]
q4=F(13,8)
pts=[];port4_pos=[]
for source in seeds:
    p=cx(0)
    for ak,coeff in zip(source,coeffs):p=cx_add(p,cx_mul(coeff,ak))
    d=[cx_mul(ak,cx_conj(p)) for ak in source]
    for sign in [-1,1]:
        out=[cx_scale(cx_mul(t,cx(s,sign)),F(1)/q4) for t in d]
        pts.append(out)
    port4_pos.append(d)

# z approximate optimal center, rationals with 12 decimal places.
z=[cx('-0.249980106067','0.248179044755'),cx('0.519656671956','-0.525400484253'),cx('0.289640981507','-0.284363215420')]
# max over each complete arc is at an endpoint when Re <z,d_h> > 0.
positive_real_inner=[]
for d in port4_pos:
    inner=IV(0)
    for zj,dj in zip(z,d):inner += cx_mul(cx_conj(zj),dj)[0]
    positive_real_inner.append(inner)
    assert inner.lo>0

def norm2_diff(v,w):
    out=IV(0)
    for a,b in zip(v,w):
        dv=cx_add(a,cx_scale(b,-1))
        out+=cx_norm2(dv)
    return out
r2=[norm2_diff(pt,z) for pt in pts]
max_upper=max(v.hi for v in r2)

# Explicit rational weights, no numerical solver in the checker.
active=[0,3,4,5,6,7]
wt=[F('0.080512845'),F('0.106679297'),F('0.152950171'),F('0.250366200'),F('0.267088084')]
wt.append(F(1)-sum(wt))
assert min(wt)>0 and sum(wt)==1
mean=[cx(0) for _ in range(3)]
for i,w in zip(active,wt):
    mean=[cx_add(m,cx_scale(c,w)) for m,c in zip(mean,pts[i])]
second=IV(0)
for i,w in zip(active,wt):
    second += w*sum((cx_norm2(c) for c in pts[i]),IV(0))
variance=second-sum((cx_norm2(c) for c in mean),IV(0))

# Fully rational enclosures and gaps, with generous slack for 1e-9 root boxes.
assert variance.lo > F('2.17665810'),(variance.lo,'lower')
assert max_upper < F('2.17665818'),(max_upper,'upper')
L=F(1062562,458329)
assert F('2.17665818')<L

# Prove an EXACT algebraic KKT characterization, not just an interval enclosure.
# M lambda=b: equal squared distances for six support points; sum lambda=1.
# The entries of M and b are algebraic, fixed by the two Banach-isolated roots.
def maxabs(v):return max(abs(v.lo),abs(v.hi))
def icoord(pt):return [v[0] for v in pt]+[v[1] for v in pt]
def dot(u,v):return sum((a*b for a,b in zip(u,v)),IV(0))
active_pts=[icoord(pts[i]) for i in active]
base_pt=active_pts[0]
Miv=[];biv=[]
for point in active_pts[1:]:
    dv=[a-b for a,b in zip(point,base_pt)]
    Miv.append([2*dot(dv,pt) for pt in active_pts])
    biv.append(dot(point,point)-dot(base_pt,base_pt))
Miv.append([IV(1) for _ in range(6)]);biv.append(IV(1))
# A rational preconditioner approximating the inverse of the exact 6x6 matrix.
# Its entries are merely decimal rational literals; correctness is checked by
# the interval Neumann bound, not by trusting the approximation.
preconditioner = [
 ['3.47574154639818562','-4.33247149038445375','-0.0575289092170334661','-1.1815071036210971','-3.37998995207000438','0.208246174804266008'],
 ['3.23006703936280514','-2.93157922802542795','-0.433257085809335915','-0.547148532902430582','-2.79382373902379631','0.202136686334772919'],
 ['-2.93157922802542795','3.65181836072159678','0.130232490817548785','0.760563839265519149','2.72143602760521699','0.0499621561287307085'],
 ['-0.433257085809335915','0.130232490817548785','0.332310996435922191','-0.120232586185460374','0.148475093958358779','0.244036041789023437'],
 ['-0.547148532902430582','0.760563839265519149','-0.120232586185460374','0.473005239864063551','0.615319143579405356','0.241791669067003284'],
 ['-2.79382373902379631','2.72143602760521699','0.148475093958358779','0.615319143579405356','2.68858342595081956','0.0538272718762036437'],
]
Bpre=[[F(v) for v in row] for row in preconditioner]
lambda0=wt
E=[[IV(int(i==j))-sum((Bpre[i][h]*Miv[h][j] for h in range(6)),IV(0))
    for j in range(6)] for i in range(6)]
tau=max(sum(maxabs(e) for e in row) for row in E)
assert tau<F(1,1000),(tau,'preconditioned contraction')
res=[biv[i]-sum((Miv[i][j]*lambda0[j] for j in range(6)),IV(0)) for i in range(6)]
e=[sum((Bpre[i][j]*res[j] for j in range(6)),IV(0)) for i in range(6)]
error=max(maxabs(v) for v in e)/(1-tau)
assert error<F(1,100000),(error,'lambda interval too broad')
lam_boxes=[IV(l-error,l+error) for l in lambda0]
assert all(l.lo>0 for l in lam_boxes)
assert all(l.lo<l.hi for l in lam_boxes)
# For actual roots, M,b lie in these intervals, so ||I-BM||<1 and
# the Neumann theorem establishes a unique exact lambda=M^{-1}b.
# The above box encloses each exact lambda with positive weight.
center_kkt=[sum((l*p[k] for l,p in zip(lam_boxes,active_pts)),IV(0)) for k in range(6)]
max_contact=norm2_diff(pts[active[0]], [cx(center_kkt[k],center_kkt[k+3]) for k in range(3)])
# Distance to non-support points must be strictly smaller than to every support.
for idx in [1,2]:
    d=norm2_diff(pts[idx], [cx(center_kkt[k],center_kkt[k+3]) for k in range(3)])
    assert d.hi<max_contact.lo, (idx, d.hi,max_contact.lo)
# Complete continuous arcs: Re <center,d_h> >0 ensures the worst point
# lies at one of the two endpoints (no antipodal interior minimum).
for d in port4_pos:
    ci=[cx(center_kkt[k],center_kkt[k+3]) for k in range(3)]
    reinner=sum((cx_mul(cx_conj(zz),aa)[0] for zz,aa in zip(ci,d)),IV(0))
    assert reinner.lo>0,('KKT center arc extrema',reinner.lo)
# Exact characterization: MEB squared is ||P0-sum lambda P_active||²,
# where lambda is the uniquely determined algebraic solution M lambda=b.
# All six positive weights are contacts. Inactive endpoints are strict interior.

print(json.dumps({
 'status':'PASS',
 'claim':'2.17665810 < MEB^2(S) < 2.17665818, conditional on PREFIX-330 four-orbit exhaustion',
 'scope':'four full continuous BRC phase arcs; all 8 endpoints; independent Banach root isolations',
 'root_boxes':2,'root_box_radius':'1/1000000000',
 'kkt_exact_six_support':'PASS; M lambda=b with strictly positive lambda, unique center',
 'kkt_preconditioned_row_norm_upper':str(tau),
 'kkt_lambda_max_error_exact':str(error),
 'kkt_contact_radius_lower_exact':str(max_contact.lo),
 'kkt_contact_radius_upper_exact':str(max_contact.hi),
 'BRC_path_pairs_per_source':45,'full_q_equations_from_BRC':True,
 'sqrt_5_over_8_bracket':[str(lo),str(hi)],
 'active_endpoint_indices':active,
 'dual_positive_rational_weights':[str(w) for w in wt],
 'variance_lower_bound_exact':str(variance.lo),
 'variance_upper_bound_exact':str(variance.hi),
 'covering_radius_squared_upper_exact':str(max_upper),
 'endpoint_squared_distance_bounds': [[str(d.lo),str(d.hi)] for d in r2],
 'positive_arc_inner_lower_exact':[str(v.lo) for v in positive_real_inner],
 'benchmark_L':str(L),
 'full_native_X6':'NOT_PROVEN',
 'canonical_Source_admission':'NOT_ATTESTED'
},indent=2,ensure_ascii=False))

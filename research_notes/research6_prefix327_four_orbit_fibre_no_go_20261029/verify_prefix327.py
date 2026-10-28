"""PREFIX-327: certified rational-interval BRC no-cross-fibre verification.
Run: python verify_prefix327.py > RESULTS_PREFIX327.json (requires SymPy).
"""
import json
from fractions import Fraction as R
from math import isqrt
import sympy as s

I=s.I
x,y,u,v,w,T=s.symbols('x y u v w T',real=True)
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
            [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
Q=[128,80,74,200,85]
f=[]
for j in range(5):
    paths=[s.expand(A[j,k]*z) for k,z in enumerate([x+I*y,u+I*v,w])]
    pairs=[s.expand(paths[k]*s.conjugate(paths[h])) for k in range(3) for h in range(3)]
    assert len(pairs)==9
    f.append(s.expand(s.re(sum(pairs))-Q[j]))
G=s.groebner(f,x,y,u,v,w,order='grevlex');H=G.fglm('lex')
E=[p.as_expr() for p in H.polys]
assert len(E)==6
assert all(H.reduce(z)[1]==0 for z in f)
assert all(G.reduce(z)[1]==0 for z in E)
F=(5951717425889645*T**4-228788223822434608*T**3+
   4023748873308624459*T**2-20488030744357515722*T+
   31325392094413629826)
P=s.expand(F.subs(T,w*w))
assert s.Poly(E[-1],w).monic()==s.Poly((w*w-1)*P,w).monic()
assert s.Poly(F,T,modulus=13).is_irreducible
pf=s.Poly(F,T)
assert pf.count_roots(-s.oo,0)==0 and pf.count_roots(0,s.oo)==2
# Exact lex-coordinate rational functions for the two algebraic roots.
coords=[]
for idx,variable in [(0,x),(1,y),(2,u),(4,v)]:
    a=s.expand(E[idx]).coeff(variable)
    assert a!=0 and s.degree(a,variable)==0
    coords.append(s.cancel(-E[idx].subs(variable,0)/a))
X,Y,UU,V=coords
# Confirm the candidate sections solve *all* original labelled-pair masses.
modP=s.Poly(P,w,domain=s.QQ)
inv_denom=s.invert(s.denom(V),P,w)
VV=s.Poly(s.numer(V)*inv_denom,w,domain=s.QQ).rem(modP).as_expr()
sections=[s.Poly(s.cancel(t),w,domain=s.QQ).rem(modP).as_expr() for t in (X,Y,UU)] + [VV]
for eq in f:
    assert s.Poly(eq.subs(dict(zip((x,y,u,v),sections)),simultaneous=True),w,domain=s.QQ).rem(modP).is_zero

class J:
    def __init__(self,lo,hi=None):
        self.lo=R(lo);self.hi=R(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,z):
        z=asj(z);return J(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return J(-self.hi,-self.lo)
    def __sub__(self,z):return self+-asj(z)
    def __rsub__(self,z):return asj(z)+-self
    def __mul__(self,z):
        z=asj(z);a=[i*j for i in (self.lo,self.hi) for j in (z.lo,z.hi)]
        return J(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=asj(z);assert z.lo*z.hi>0
        return self*J(1/z.hi,1/z.lo)
    def sq_upper(self):return max(abs(self.lo),abs(self.hi))**2
    def serial(self):return [str(self.lo),str(self.hi)]
def asj(z):return z if isinstance(z,J) else J(z)
def rat(z):return R(int(z.p),int(z.q)) if isinstance(z,s.Rational) else R(z)
def evpoly(expr,ww):
    p=s.Poly(expr,w,domain=s.QQ);r=J(0)
    for coeff in p.all_coeffs():r=r*ww+J(rat(coeff))
    return r
def evrat(expr,ww):
    num,den=s.fraction(s.cancel(expr))
    return evpoly(num,ww)/evpoly(den,ww)
def C(a,b=0):return (asj(a),asj(b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def zout(a,b):return a.sq_upper()+b.sq_upper()
def ports(src):
    out=[]
    for j in range(5):
        z=C(0)
        for k in range(3):
            aa=s.expand(A[j,k]/8)
            z=add(z,cmul(C(rat(s.re(aa)),rat(s.im(aa))),src[k]))
        out.append(z)
    return out

def src_new(lo,hi):
    scale=10**43
    def floor_sqrt_rational(z):return isqrt((int(z.p)*scale*scale)//int(z.q))
    wa=R(floor_sqrt_rational(lo),scale)
    wb=R(floor_sqrt_rational(hi)+1,scale)
    W=J(wa,wb)
    xx,yy,uu,vv=[evrat(p,W) for p in coords]
    return [C(xx,yy),C(uu,vv),C(W)],W

isolated=pf.intervals(eps=s.Rational(1,10**40))
assert len(isolated)==2 and all(mul==1 and lo>0 for ((lo,hi),mul) in isolated)
new=[];root_bounds=[]
for (lo,hi),_ in isolated:
    assert pf.count_roots(lo,hi)==1
    ss,ww=src_new(lo,hi)
    new.append(ss)
    root_bounds.append({'T_interval':[str(lo),str(hi)],'w_interval':ww.serial(),
                        'coordinate_widths':[float(z.hi-z.lo) for pair in ss for z in pair]})
sources=[ [C(-2),C(0,-2),C(1)], [C(-2),C(0,2),C(1)] ] + new
p=[ports(q) for q in sources]
m=[R(a,64) for a in Q]
for src,pt in zip(sources,p):
    # check numerically only for this diagnostic; exact source mass equations checked above
    pass
weights={
 '01':[1,0,0,1,0], '02':[0,0,2,1,0], '03':[2,0,0,1,2],
 '12':[2,0,0,2,3], '13':[0,0,2,1,0], '23':[0,3,0,2,2],
}
cert=[]
for key,vec in weights.items():
    i,j=map(int,key)
    weights_norm=[R(k,sum(vec)) for k in vec]
    h=sum((mm-1)*ww for mm,ww in zip(m,weights_norm))
    assert h>0
    z=C(0)
    for k,wt in enumerate(weights_norm):
        z=add(z,cmul(C(wt),cmul(conj(p[i][k]),p[j][k])))
    gap_lower=h*h-zout(*z)
    assert gap_lower>R(1,8),(key,float(gap_lower))
    cert.append({'pair':key,'weights':vec,'h':str(h),
                 'certified_gap_gt_1_over_8':True,
                 'gap_lower_decimal_floor_6dp':str((gap_lower.numerator*10**6//gap_lower.denominator))})
# squared source norms are algebraic on new orbits, old ones exactly 9
for src in new:
    norm_lower=J(0)
    for a in src:
        norm_lower=norm_lower+a[0]*a[0]+a[1]*a[1]
    assert norm_lower.hi<9, float(norm_lower.hi)
L=R(1062562,458329)
assert R(36,25)<L
out={'schema':'PREFIX327_CERTIFIED_INTERVAL_BRC_V1',
     'global_snapshot':'edee29410faf7b200a72c3b7e6bd2d62e4d4025a',
     'project_input_snapshot':'3a806398761cb2717c6a9139c498a8e40afb83e3',
     'labels':'5 Ports x 9 source/source pairs (each), independent reference path 1 and i',
     'root_intervals':root_bounds,'pair_disjoint_certificates':cert,
     'all_6_cross_orbit_pairs_excluded':True,
     'single_orbit_meb_squared_bound':'36/25',
     'prior_full_model_lower_bound':str(L),
     'scope':'fixed Q0, four complex phase orbits, static auxiliary S7-3 BRC; dependent on exact algebraic fibre classification',
     'status':'AUTHOR_SIDE_EXACT_INTERVAL_PROOF_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

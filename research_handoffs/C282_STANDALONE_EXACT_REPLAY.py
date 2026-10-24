#!/usr/bin/env python3
"""C271 self-contained author exact checker: all 595 C254 two-box hulls.
Only standard-library Fraction. The C195/H168 auxiliary, NOT native GF(2)-BRC.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
BOX_DATA="4/543,43/62,4/5,9/11,9/613,57/79,38/47,121/147;3/407,5/7,60/77,4/5,7/477,18/25,53/67,9/11;3/407,5/7,18/23,4/5,6/409,31/43,87/109,4/5;3/407,5/7,4/5,81/101,7/477,31/43,21/26,76/93;2/271,7/10,60/77,4/5,6/409,42/59,11/14,4/5;2/271,7/10,4/5,13/16,6/409,27/38,4/5,58/71;2/271,12/17,26/33,4/5,3/233,12/17,59/74,4/5;1/135,16/23,18/23,9/11,3/205,5/7,4/5,9/11;1/135,7/10,26/33,4/5,3/283,7/10,27/34,4/5;1/135,7/10,4/5,49/61,2/137,7/10,4/5,31/38;1/135,12/17,4/5,57/71,3/205,12/17,4/5,30/37;1/127,16/23,18/23,4/5,1/106,16/23,4/5,13/16;3/371,7/10,15/19,4/5,2/171,17/24,53/67,4/5;1/123,34/49,15/19,4/5,1/69,7/10,59/74,4/5;1/123,26/37,48/61,4/5,1/78,27/38,15/19,4/5;1/119,19/27,4/5,17/21,3/205,12/17,4/5,69/85;1/119,12/17,18/23,13/16,3/205,12/17,11/14,9/11;1/119,12/17,15/19,13/16,1/74,12/17,15/19,22/27;1/119,5/7,60/77,19/24,1/69,28/39,34/43,41/51;1/119,5/7,18/23,17/21,3/205,5/7,59/74,9/11;1/117,19/27,4/5,21/26,1/85,22/31,4/5,17/21;1/105,7/10,53/68,9/11,3/205,18/25,53/67,23/28;1/105,12/17,4/5,13/16,1/74,42/59,21/26,9/11;1/104,34/49,18/23,4/5,1/69,7/10,34/43,4/5;1/104,34/49,4/5,41/51,1/69,30/43,4/5,22/27;1/103,7/10,27/34,4/5,2/155,22/31,87/109,4/5;1/103,12/17,18/23,21/26,1/86,12/17,18/23,13/16;2/189,7/10,32/41,4/5,3/205,19/27,37/47,4/5;1/93,16/23,18/23,13/16,2/137,7/10,15/19,9/11;1/93,12/17,18/23,19/24,6/409,27/38,15/19,4/5;1/93,12/17,18/23,21/26,1/69,12/17,11/14,17/21;1/93,12/17,19/24,13/16,1/69,12/17,27/34,13/16;1/89,12/17,15/19,21/26,1/69,12/17,15/19,13/16;1/88,12/17,26/33,4/5,3/232,29/41,72/91,4/5;1/77,7/10,26/33,4/5,6/409,12/17,63/79,4/5"
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
Q=2**128; H=2**166; A=F(6912*50000**2,17**2)
Z=F(141421356237309504880,10**20)
I=(5,50,55,56)
J=tuple(k for k in range(79) if k not in I)
assert len(U)==79 and all(U[k]<U[k+1] for k in range(78))
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert U[56]-U[54] == F(2,63) < Z-U[56]
D=[]
for item in BOX_DATA.split(';'):
    z=tuple(map(F,item.split(',')))
    assert len(z)==8
    l,h=z[:4],z[4:]
    assert all(U[p-1]<l[d]<=h[d]<U[p+1] for d,p in enumerate(I))
    assert l[2]<l[3] and h[2]<h[3]
    D.append((l,h))
assert len(D)==35
basic_delta=[h[2]-l[3] for l,h in D]
assert [k for k,g in enumerate(basic_delta) if g>0]==[3]
assert [k for k,g in enumerate(basic_delta) if g==0]==[11]
assert basic_delta[3]==F(15,2626)


# C274 addendum: global collision collar, exact 128-interval proof.
# Author research only; no Source claim and no native BRC/X6 transfer.
from itertools import combinations
import json

A_MIN=min(lo[0] for lo,hi in D)
B_MIN=min(lo[1] for lo,hi in D)
EPS_MAX=F(1,3077)
assert A_MIN==F(4,543) and B_MIN==F(43,62)
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert 54 in J and 55 not in J and 56 not in J
assert Z+U[54]-2*U[56]>0
assert all(A_MIN<=lo[0]<=hi[0]<U[55] and
           B_MIN<=lo[1]<=hi[1]<U[55] for lo,hi in D)



# C275 author-exact extension to the pinned C271/C274 input.
# No native X6/BRC correspondence, task CLAIM, or independent review is claimed.
from fractions import Fraction as F
from itertools import combinations
import json
P = [
    (F(1,93),F(12,17),F(27,34),F(101,125)),
    (F(1,100),F(703,1000),F(27,34),F(101,125)),
]
EPS=F(1,10000)
def admissible(v):
    return all(U[k-1]<v[i]<U[k+1] for i,k in enumerate(I)) and v[0]<v[1]<v[2]<v[3]<Z
def active(k,v):
    x=v[I.index(k)]
    out=F(Q)*A/H/((2-x*x)*(3-x*x))**3
    for j in J:out*=(Z-U[j])/abs(x-U[j])
    for h,y in zip(I,v):
        if h!=k:out*=(Z-y)/abs(x-y)
    return out
def fixed_data():
    exact,unfloored={},{}
    for j in J:
        u=U[j]
        mass=F(Q)*A/H/((2-u*u)*(3-u*u))**3
        for r in range(len(U)):
            if r!=j:mass*=(Z-U[r])/abs(u-U[r])
        assert mass>1
        unfloored[j]=mass
        exact[j]=mass.numerator//mass.denominator
    assert all(exact[j]>0 for j in J)
    return exact,unfloored
def multiplier(j,v):
    f=F(1)
    for k,p in zip(I,v):
        f*=(Z-p)/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-p)
    return f
def direct(v,weights):
    return sum((weights[j]*multiplier(j,v) for j in J),F(0))+sum((active(k,v) for k in I),F(0))
def independent_unfloored(v):
    # Cancel original active-node factors before computing the fixed branches.
    total=F(0)
    for j in J:
        u=U[j]
        term=F(Q)*A/H/((2-u*u)*(3-u*u))**3
        for r in J:
            if r!=j:term*=(Z-U[r])/abs(u-U[r])
        for p in v:term*=(Z-p)/abs(u-p)
        total+=term
    for k in I:total+=active(k,v)
    return total
def classify():
    out={}
    for i,j in combinations(range(35),2):
        lo=tuple(min(D[i][0][k],D[j][0][k]) for k in range(4))
        hi=tuple(max(D[i][1][k],D[j][1][k]) for k in range(4))
        gap=hi[2]-lo[3]
        out[(i,j)]=(lo,hi,'safe' if gap<0 else 'touch' if gap==0 else 'cross')
    return out
def inside(v,lo,hi):
    return all(lo[k]<=v[k]<=hi[k] for k in range(4))
def positive_point(lo,hi):
    a=(lo[0]+hi[0])/2;b=(lo[1]+hi[1])/2;t=(hi[2]+lo[3])/2
    return(a,b,t-EPS/2,t+EPS/2)

# C281: one rational global affine envelope, no branch-and-bound.
# These aliases retain the original C275 formulas verbatim.
floor_fixed_masses=fixed_data
fixed_multiplier=multiplier
moving_mass=active
original_F=direct
hulls=classify
valid=admissible
import hashlib, json
C281_PAIRS=((8,18),(13,18),(18,25),(18,34))
P_LO=(F(1,135),F(34,49),F(60,77),F(19,24))
P_HI=(F(6,409),F(28,39),F(87,109),F(41,51))
ANCHOR=(F(1253,125000),F(70489,100000),F(79171,100000),F(41,51))
CLAIM_MARGIN=F(1,4000)

def rational_sha(x):
    return hashlib.sha256((str(x.numerator)+'/'+str(x.denominator)).encode('ascii')).hexdigest()

def exact_global_affine_certificate():
    assert len(U)==79 and len(D)==35 and len(J)==75 and I==(5,50,55,56)
    assert all(P_LO[r]<=ANCHOR[r]<=P_HI[r] for r in range(4))
    assert valid(ANCHOR)
    for d,k in enumerate(I):
        assert U[k-1]<P_LO[d]<=P_HI[d]<U[k+1]
    allh=hulls()
    for pair in C281_PAIRS:
        lo,hi,kind=allh[pair]
        assert kind=='cross'
        assert all(P_LO[r]<=lo[r]<=hi[r]<=P_HI[r] for r in range(4))
    weights,_=floor_fixed_masses()
    assert len(weights)==75 and all(w>0 for w in weights.values())
    terms=[]; gradients=[]; numerator_sets=[]
    for j in J:
        mass=F(weights[j])*fixed_multiplier(j,ANCHOR)
        grad=tuple(-1/(Z-x)-1/(x-U[j]) for x in ANCHOR)
        terms.append(mass); gradients.append(grad)
        numerator_sets.append((0,1,2,3))
    for k in I:
        d=I.index(k);x=ANCHOR[d]
        mass=moving_mass(k,ANCHOR)
        grad=[F(0)]*4
        grad[d]=(6*x/(2-x*x)+6*x/(3-x*x)
             -sum((1/(x-U[j]) for j in J),F(0))
             -sum((1/(x-y) for r,y in enumerate(ANCHOR) if r!=d),F(0)))
        for r,y in enumerate(ANCHOR):
            if r!=d:grad[r]=-1/(Z-y)+1/(x-y)
        terms.append(mass); gradients.append(tuple(grad))
        numerator_sets.append(tuple(r for r in range(4) if r!=d))
    total=sum(terms,F(0))
    assert total==original_F(ANCHOR,weights)
    derivative=tuple(sum((w*g[r] for w,g in zip(terms,gradients)),F(0)) for r in range(4))
    radius=tuple(max(ANCHOR[r]-P_LO[r],P_HI[r]-ANCHOR[r]) for r in range(4))
    per_axis=tuple(radius[r]**2/(2*(Z-P_HI[r])**2) for r in range(4))
    error=sum((w*sum((per_axis[r] for r in ns),F(0)) for w,ns in zip(terms,numerator_sets)),F(0))
    endpoint=tuple(P_LO[r] if derivative[r]>=0 else P_HI[r] for r in range(4))
    delta=sum((derivative[r]*(endpoint[r]-ANCHOR[r]) for r in range(4)),F(0))
    lower=total+delta-error
    assert len(terms)==79
    assert tuple(x>0 for x in derivative)==(True,True,True,False)
    assert lower > Q*(1+CLAIM_MARGIN)
    return {
       "result":"C281_ONE_TANGENT_GLOBAL_EXACT_PASS",
       "source":"C275 original frozen 79-node rational auxiliary",
       "parent_bounds":{"lower":list(map(str,P_LO)),"upper":list(map(str,P_HI))},
       "anchor":list(map(str,ANCHOR)),
       "parent_hulls":[list(p) for p in C281_PAIRS],
       "fixed_masses":75,"moving_masses":4,"affine_certificates":1,
       "exact_grad_signs":["+" if x>0 else "-" if x<0 else "0" for x in derivative],
       "normalised_F_anchor_display":float(total/Q),
       "normalised_concavity_budget_display":float(error/Q),
       "normalised_linear_change_display":float(delta/Q),
       "normalised_lower_display":float(lower/Q),
       "exact_L_over_Q_sha256":rational_sha(lower/Q),
       "exact_assertion":"4000*L > 4001*Q",
       "formal_Source_claim":False,
       "independent_driver_admission":False,
       "native_X6_or_signed_BRC_promotion":False,
    }


# C282 author research: separable concave-quadratic minorant on the same 4D parent.
# All decisive comparisons below use exact Fraction arithmetic.
T282=(F(1253,125000),F(176223,250000),F(7917,10000),F(41,51))
MARGIN282=F(3,5000)

class Jet282:
    """Independent exact 4D product/quotient automatic derivative."""
    def __init__(self,val,grad=None):
        self.v=F(val)
        self.g=tuple(grad) if grad is not None else (F(0),)*4
    @staticmethod
    def cv(x):return x if isinstance(x,Jet282) else Jet282(x)
    @staticmethod
    def var(x,r):return Jet282(x,tuple(F(int(i==r)) for i in range(4)))
    def __add__(self,y):
        y=self.cv(y)
        return Jet282(self.v+y.v,tuple(a+b for a,b in zip(self.g,y.g)))
    __radd__=__add__
    def __neg__(self):return Jet282(-self.v,tuple(-a for a in self.g))
    def __sub__(self,y):return self+-self.cv(y)
    def __rsub__(self,y):return self.cv(y)+-self
    def __mul__(self,y):
        y=self.cv(y)
        return Jet282(self.v*y.v,tuple(a*y.v+self.v*b for a,b in zip(self.g,y.g)))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=self.cv(y);assert y.v!=0
        return Jet282(self.v/y.v,tuple((a*y.v-self.v*b)/(y.v*y.v) for a,b in zip(self.g,y.g)))
    def __rtruediv__(self,y):return self.cv(y)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        return Jet282(self.v**n,tuple(n*self.v**(n-1)*g for g in self.g) if n else None)
    def __abs__(self):
        assert self.v!=0
        return self if self.v>0 else -self

def direct_jet282(t,weights):
    p=tuple(Jet282.var(x,r) for r,x in enumerate(t))
    total=Jet282(0)
    for j in J:
        term=Jet282(weights[j])
        for r,k in enumerate(I):
            term=term*(Z-p[r])/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-p[r])
        total=total+term
    for r,k in enumerate(I):
        x=p[r];term=Jet282(F(Q)*A/H)/(((2-x*x)*(3-x*x))**3)
        for j in J:term=term*(Z-U[j])/abs(x-U[j])
        for s in range(4):
            if s!=r:term=term*(Z-p[s])/abs(x-p[s])
        total=total+term
    return total

def exact_c282():
    assert len(U)==79 and len(J)==75 and len(D)==35
    assert all(P_LO[r]<=T282[r]<=P_HI[r] for r in range(4))
    assert valid(T282)
    for r,k in enumerate(I):
        assert U[k-1]<P_LO[r]<=P_HI[r]<U[k+1] and Z>P_HI[r]
    for pair in C281_PAIRS:
        lo,hi,kind=hulls()[pair]
        assert kind=="cross" and all(P_LO[r]<=lo[r]<=hi[r]<=P_HI[r] for r in range(4))
    weights,_=floor_fixed_masses()
    vals=[];glog=[];N=[]
    for j in J:
        v=F(weights[j])*fixed_multiplier(j,T282)
        g=tuple(-1/(Z-x)-1/(x-U[j]) for x in T282)
        vals.append(v);glog.append(g);N.append((0,1,2,3))
    for r,k in enumerate(I):
        x=T282[r];v=moving_mass(k,T282)
        g=[F(0)]*4
        g[r]=(6*x/(2-x*x)+6*x/(3-x*x)
            -sum((1/(x-U[j]) for j in J),F(0))
            -sum((1/(x-y) for s,y in enumerate(T282) if s!=r),F(0)))
        for s,y in enumerate(T282):
            if s!=r:g[s]=-1/(Z-y)+1/(x-y)
        vals.append(v);glog.append(tuple(g))
        N.append(tuple(s for s in range(4) if s!=r))
    assert len(vals)==79 and all(v>0 for v in vals)
    F0=sum(vals,F(0))
    D1=tuple(sum((v*g[r] for v,g in zip(vals,glog)),F(0)) for r in range(4))
    C1=tuple(sum((v for v,n in zip(vals,N) if r in n),F(0))
           /(2*(Z-P_HI[r])**2) for r in range(4))
    assert all(v>0 for v in C1)
    z=tuple(tuple(D1[r]*(x-T282[r])-C1[r]*(x-T282[r])**2
                  for x in (P_LO[r],P_HI[r])) for r in range(4))
    idx=tuple(0 if q[0]<=q[1] else 1 for q in z)
    lower=F0+sum((z[r][idx[r]] for r in range(4)),F(0))
    # This quadratic bound dominates the old same-anchor uniform-radius affine bound.
    radius=tuple(max(T282[r]-P_LO[r],P_HI[r]-T282[r]) for r in range(4))
    old=(F0+sum((min(D1[r]*(x-T282[r]) for x in (P_LO[r],P_HI[r]))
             for r in range(4)),F(0))
             -sum((C1[r]*radius[r]**2 for r in range(4)),F(0)))
    assert lower>old
    jet=direct_jet282(T282,weights)
    assert jet.v==F0 and jet.g==D1
    assert 5000*lower>5003*Q
    return {
       "result":"C282_CONCAVE_QUADRATIC_GLOBAL_EXACT_PASS",
       "scope":"C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY_ONLY",
       "parent_hulls":[list(p) for p in C281_PAIRS],
       "anchor":[str(x) for x in T282],
       "corner_indices":list(idx),
       "gradient_signs":["+" if x>0 else "-" if x<0 else "0" for x in D1],
       "bound":"5000*L2 > 5003*2**128",
       "normalized_lower_display_only":float(lower/Q),
       "lower_ratio_sha256":rational_sha(lower/Q),
       "dual_product_gradient_crosscheck":"PASS",
       "source_claim":False,"independent_driver_admission":False,
       "native_brc_or_x6_promotion":False
    }

if __name__=="__main__":
    print(json.dumps(exact_c282(),ensure_ascii=False,indent=2))

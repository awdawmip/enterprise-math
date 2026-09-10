#!/usr/bin/env python3
"""Exact arithmetic checks for a Hodge first-seed research note, 2026-09-10.

No external packages. This checks polynomial, exterior-algebra, graph-intersection
and tangent-matrix identities. It does NOT verify existence on a very-general
sixfold, deformation unobstructedness, or the Hodge conjecture.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
from dataclasses import dataclass
import json
import sys

@dataclass(frozen=True)
class G:
    re: F
    im: F = F(0)
    def __add__(self, b):
        b = b if isinstance(b, G) else G(F(b))
        return G(self.re+b.re, self.im+b.im)
    __radd__ = __add__
    def __neg__(self): return G(-self.re, -self.im)
    def __sub__(self,b): return self + (-b if isinstance(b,G) else -F(b))
    def __rsub__(self,b): return -self+b
    def __mul__(self,b):
        b = b if isinstance(b,G) else G(F(b))
        return G(self.re*b.re-self.im*b.im, self.re*b.im+self.im*b.re)
    __rmul__ = __mul__
    def __truediv__(self,b):
        b = b if isinstance(b,G) else G(F(b))
        return self*b.conj()*(1/(b.re*b.re+b.im*b.im))
    def __pow__(self,n):
        if n < 0: raise ValueError("only nonnegative powers")
        out=G(F(1))
        for _ in range(n): out=out*self
        return out
    def conj(self): return G(self.re,-self.im)

checks=[]
def check(name, condition):
    if not condition: raise AssertionError(name)
    checks.append(name)

def add(*forms):
    result={}
    for a in forms:
        for mask,c in a.items(): result[mask]=result.get(mask,0)+c
    return {m:c for m,c in result.items() if c != 0 and c != G(F(0))}
def scale(a,s): return {m:c*s for m,c in a.items() if c*s != 0 and c*s != G(F(0))}
def wedge(a,b):
    result={}
    for x,c in a.items():
        for y,d in b.items():
            if x & y: continue
            inv=sum((y & ((1<<k)-1)).bit_count() for k in range(12) if x>>k & 1)
            mask=x|y
            result[mask]=result.get(mask,0)+(-1 if inv%2 else 1)*c*d
    return {m:c for m,c in result.items() if c != 0 and c != G(F(0))}
def product(forms):
    out={0:F(1)}
    for a in forms: out=wedge(out,a)
    return out
def pull(a,n,conjugate=False):
    z=G(F(1),F(2))**n
    if conjugate: z=z.conj()
    images={}
    for j in range(6):
        aa,bb=z.re,(z.im if j<3 else -z.im)
        images[2*j]={1<<(2*j):aa,1<<(2*j+1):-bb}
        images[2*j+1]={1<<(2*j):bb,1<<(2*j+1):aa}
    out={}
    for mask,c in a.items():
        out=add(out,scale(product([images[k] for k in range(12) if mask>>k&1]),c))
    return out
def integral(a): return a.get((1<<12)-1,F(0))
def pi(a):
    """Self-adjoint cubic projector, expanded into actual isogeny pullbacks."""
    return scale(add(
        scale(a,3562500),
        scale(add(pull(a,1),pull(a,1,True)),-2375),
        scale(add(pull(a,2),pull(a,2,True)),30),
        scale(add(pull(a,3),pull(a,3,True)),-1),
    ),F(1,1867776))
def rank(rows):
    a=[[F(x) for x in row] for row in rows]
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        z=a[r][c]
        a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i != r:
                z=a[i][c]
                a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def run():
    u=G(F(1),F(2)); one=G(F(1)); zero=G(F(0))
    expected=[(117,-44),(-35,120),(-75,-100),(125,0),
              (-75,100),(-35,-120),(117,44)]
    eigen=[]
    for p in range(7):
        z=u**p*u.conj()**(6-p); eigen.append(z)
        check(f"eigenvalue_{p}",z==G(*map(F,expected[p])))
        check(f"similitude_{p}",z*z.conj()==G(F(15625)))
        s=z+z.conj()
        q=-(s+70)*(s+150)*(s-250)/1867776
        check(f"cubic_selector_{p}",q==(one if p in (0,6) else zero))
        old=-(z-125)*(9881*z-609029)*(z*z+70*z+15625)*(z*z+150*z+15625)/57000000000000000
        check(f"old_projector_agreement_{p}",old==q)
        c=(z**3).re-30*(z**2).re+2375*z.re-1781250
        check(f"moment_selector_{p}",c==(-933888 if p in (0,6) else 0))
    dims=[comb(6,p)*comb(6,6-p) for p in range(7)]
    check("full_middle_dimension",sum(dims)==924)
    check("projector_rank",dims[0]+dims[6]==2)
    check("cubic_normalization",304*384*16==1867776)

    # E_i^6 with physical coordinates (z_1,...,z_6).
    # Gamma is z_4=z_1, z_5=z_2, z_6=z_3.
    gamma=product([
        wedge({1<<(2*(j+3)):F(1),1<<(2*j):F(-1)},
              {1<<(2*(j+3)+1):F(1),1<<(2*j+1):F(-1)})
        for j in range(3)])
    check("graph_class_terms",len(gamma)==64)
    moments=[]
    for n in range(4):
        m=integral(wedge(gamma,pull(gamma,n)))
        moments.append(m)
        point_count=0 if n==0 else 64*(u**n).im**6
        check(f"independent_graph_intersection_{n}",m==point_count)
        check(f"adjoint_graph_moment_{n}",
              m==integral(wedge(gamma,pull(gamma,n,True))))
    check("graph_moments",moments==list(map(F,[0,4096,262144,4096])))
    delta=moments[3]-30*moments[2]+2375*moments[1]-1781250*moments[0]
    check("positive_graph_detector",delta==1867776)

    w=pi(gamma)
    eta=product([{1<<(2*j):G(F(1)),
                  1<<(2*j+1):G(F(0),F(1 if j<3 else -1))}
                 for j in range(6)])
    expected_w={m:c.im/4 for m,c in eta.items() if c.im}
    check("explicit_Weil_projection",w==expected_w)
    check("projection_idempotence",pi(w)==w)
    check("special_seed_square",integral(wedge(w,w))==-2)
    check("orthogonal_projection_pairing",
          integral(wedge(gamma,w))==integral(wedge(w,w)))
    check("detector_norm_identity",
          delta == -933888*integral(wedge(w,w)))

    # Check that the four-moment identity survives rational combinations, keeping
    # the full exterior class (not inventing geometric realizations from moments).
    for a,b,c in [(1,2,3),(-2,3,1),(0,1,-1),(7,0,0),(0,0,0)]:
        v=add(scale(gamma,a),scale(pull(gamma,1),b),scale(pull(gamma,2),c))
        mv=[integral(wedge(v,pull(v,n))) for n in range(4)]
        dv=mv[3]-30*mv[2]+2375*mv[1]-1781250*mv[0]
        pv=pi(v)
        check(f"four_moment_combination_{a}_{b}_{c}",
              dv == -933888*integral(wedge(pv,pv)))
        check(f"nonnegative_combination_{a}_{b}_{c}",dv>=0)

    theta=add(*[{(1<<(2*j))|(1<<(2*j+1)):F(1 if j<5 else 3)} for j in range(6)])
    theta3=product([theta]*3)
    check("Weil_primitivity",not wedge(theta,w))
    check("divisor_control",not pi(theta3))
    check("polarization_volume",integral(product([theta]*6))==2160)
    check("graph_degree",integral(wedge(gamma,theta3))==96)
    naive=F(96**2,2160)
    check("two_number_detector_not_valid_on_special_fiber",naive != 2)

    # B^T = D B for D=diag(1,1,3). This is the fixed rational graph-subtorus
    # preservation condition, NOT the obstruction theory of all cycles.
    rows=[]
    for i,d in enumerate([1,1,3]):
        for j in range(3):
            row=[F(0)]*9
            row[3*j+i]+=1
            row[3*i+j]-=d
            rows.append(row)
    r=rank(rows)
    check("graph_tangent_rank",r==6)
    check("graph_tangent_complex_dimension",9-r==3)
    for vals in [[1,0,0,0,0,0,0,0,0],
                 [0,1,0,1,0,0,0,0,0],
                 [0,0,0,0,1,0,0,0,0]]:
        check("allowed_graph_tangent_"+str(vals),all(sum(x*y for x,y in zip(row,vals))==0 for row in rows))
    for n in range(1,4):
        check(f"transverse_graph_normal_map_{n}",(u**n-u.conj()**n)!=zero)
    # A rational sum of two squares equal to 3 is excluded by infinite descent:
    # mod 3 a zero sum of two squares forces both summands divisible by 3.
    zeros=[(x,y) for x in range(3) for y in range(3) if (x*x+y*y)%3==0]
    check("nonsplit_norm_mod3_base",zeros==[(0,0)])
    return {
        "status":"PASS_EXACT_IDENTITIES_ONLY",
        "checks":len(checks),
        "failures":0,
        "graph_moments":[int(x) for x in moments],
        "graph_detector":int(delta),
        "special_projection_square":-2,
        "ambient_period_complex_dimension":9,
        "fixed_graph_tangent_complex_dimension":3,
        "ext1_between_distinct_transverse_graph_structure_sheaves":0,
        "ext3_dimension_for_Gamma_and_u_pullback":4096,
        "ext_statement_status":"proved_by_Koszul_in_note_not_certified_by_this_script",
        "very_general_target_seed_constructed":False,
        "deformation_unobstructedness_proved":False,
        "independent_review_obtained":False,
        "checks_performed":checks,
    }
if __name__=="__main__":
    try:
        print(json.dumps(run(),indent=2,ensure_ascii=False))
    except (AssertionError,ValueError,TypeError) as exc:
        print(json.dumps({"status":"FAIL","error":str(exc)}),file=sys.stderr)
        raise SystemExit(1)

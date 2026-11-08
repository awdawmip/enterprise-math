#!/usr/bin/env python3
"""Exact X6-BRC stationary two-class characteristic and resonance certificate.
Frozen source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires SymPy; exact integers/rationals only; no floating-point calculation.
"""
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp

w, t = sp.symbols("w t")
STAR = ((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k != abs(c))
phases = tuple((a,p,sign*k)
    for a in range(4) for k in STAR[a] for sign in (-1,1)
    for p in near(a,sign*k))
ix = {p:i for i,p in enumerate(phases)}
def succ(i):
    a,p,c = phases[i]
    b = next(b for b in range(4) if b!=a and abs(c) in STAR[b])
    return tuple(ix[x] for x in
        [(a,c,k) for k in near(a,c) if k!=p]+
        [(b,c,k) for k in near(b,c)])
N = tuple(succ(i) for i in range(48))
g=ix[(0,1,-3)]
axis=tuple(abs(p[2])-1 for p in phases)
assert len(phases)==48 and len(set(phases))==48 and all(len(x)==3 for x in N)
assert g==4 and sum(g in x for x in N)==3
assert sum(a>=4 for a in axis)==16
assert [axis[i] for i in range(48) if g in N[i]] == [0,0,0]
def Q(a,z):
    x=(1,1,1,1,a,a)
    m=sp.zeros(48)
    for i in range(48):
        for j in N[i]:
            m[i,j]=x[axis[i]]*(1 if i==g else (3+z if j==g else 2))
    return m

J=t**4+4*(w+1)*t**2-48*w
C1=t**3-2*t**2-12*w*t-72*w
C2=t**3-2*t**2+4*w*t+24*w
C3=t**3+2*t**2-12*w*t+72*w
C4=t**3+2*t**2+4*w*t-24*w
Cs=(C1,C2,C3,C4)
F=(t**2-4)*(t**2+12*w)**2*(t**2-4*w)**6*J**3
P=(t**2-4)*J*sp.prod(Cs)
H=(t**2-4)*(t**2+12*w)*(t**2-4*w)*J
B=(4*(4*w+1)*t**14
 +16*(16*w**2-11*w-2)*t**12
 +64*(24*w**3+34*w**2-2*w+1)*t**10
 +256*w*(48*w**3-270*w**2-92*w+9)*t**8
 +3072*w**2*(12*w**3-81*w**2+140*w-18)*t**6
 -110592*w**3*(21*w**2+38*w+10)*t**4
 +3981312*w**4*(10*w+7)*t**2
 -143327232*w**5)
assert sp.Poly(F,t).degree()==30 and sp.Poly(P,t).degree()==18
assert sp.Poly(B,t).degree()==14 and sp.Poly(H,t).degree()==10
assert sp.Poly(F,w).degree()==11
assert sp.Poly(P,w).degree()<=5 and sp.Poly(B,w).degree()<=5
# Sixteen w-scaled rows imply deg_w chi<=16.
# All gate contributions occupy one target column, so deg_z chi<=1.
# Thus equality at 17 distinct w values and 2 distinct z values
# proves a polynomial identity for all real w,z (not merely these samples).
for a in range(17):
    for z in (1,2):
        got=sp.Poly(Q(a,z).charpoly(t).as_expr(),t)
        want=sp.Poly((F*(P-(z-1)*B)).subs(w,a),t)
        assert got==want,(a,z)

prime=1000003
def rank_mod(cols):
    a=[[int(v[i])%prime for v in cols] for i in range(48)]
    rank=0
    for j in range(len(cols)):
        pivot=next((i for i in range(rank,48) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,prime)
        for k in range(j,len(cols)): a[rank][k]=a[rank][k]*inv%prime
        for i in range(rank+1,48):
            v=a[i][j]
            if v:
                for k in range(j,len(cols)):
                    a[i][k]=(a[i][k]-v*a[rank][k])%prime
        rank+=1
    return rank

def krylov_rank(a,z,n,seed=1):
    zz=Fraction(z)
    zm=zz.numerator*pow(zz.denominator,-1,prime)%prime
    x=(1,1,1,1,a,a)
    v=[(i+seed)**3+5*i+1 for i in range(48)]
    cols=[]
    for _ in range(n):
        cols.append(v)
        v=[sum(x[axis[i]]*(1 if i==g else
           ((3+zm)%prime if j==g else 2))*v[j]
           for j in N[i])%prime for i in range(48)]
    return rank_mod(cols)

def annihilates(poly,m):
    x=sp.zeros(48)
    eye=sp.eye(48)
    for c in sp.Poly(poly,t).all_coeffs():
        x=x*m+c*eye
    return x.is_zero_matrix

A=Q(2,1)
G22=(H*sp.prod(Cs)).subs(w,2)
assert sp.Poly(G22,t).degree()==22 and annihilates(G22,A)
u=sp.Matrix([int(g in ns) for ns in N])
vs=[]; v=u
for _ in range(18):
    vs.append(v)
    v=A*v
assert sp.Matrix.hstack(*vs).rank()==18
assert krylov_rank(2,1,22,seed=5)==22

res={"frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
     "native_phases":48,"native_ports":96,"native_typed_actions":576,
     "interpolation":{"w_nodes":list(range(17)),"z_nodes":[1,2],
       "deg_w_max":16,"deg_z_max":1,"all_exact_comparisons_pass":True},
     "special_cases":[]}
for z,quad in ((sp.Rational(109,17),t**2-8),
               (sp.Rational(153,13),t**2+24)):
    R=sp.Poly(P.subs(w,2)-(z-1)*B.subs(w,2),t)
    HH=sp.Poly(H.subs(w,2),t)
    common=sp.gcd(HH,R)
    assert common.monic().as_expr()==quad
    L=(HH*R).quo(common)
    assert L.degree()==26
    assert annihilates(L.as_expr(),Q(2,z))
    assert krylov_rank(2,z,26)==26
    res["special_cases"].append({"w":2,"z":str(z),"common_factor":str(quad),
        "sharp_minpoly_degree":26,"exact_rational_annihilation":True,
        "modulus":prime,"explicit_krylov_seed":"(i+1)^3+5i+1",
        "krylov_rank":26})
R=sp.Poly(P.subs(w,2)-B.subs(w,2),t)
HH=sp.Poly(H.subs(w,2),t)
assert sp.gcd(R,HH).degree()==0
assert annihilates((HH*R).as_expr(),Q(2,2))
assert krylov_rank(2,2,28)==28

X=sp.Symbol("X")
def even(f):
    pp=sp.Poly(f,t)
    assert all(ex[0]%2==0 for ex,co in pp.terms())
    return sp.Poly.from_dict({(ex[0]//2,):co for ex,co in pp.terms()},X).as_expr()
Pe=even(P); Be=even(B)
zplus=sp.factor(1+Pe.subs(X,4*w)/Be.subs(X,4*w))
zminus=sp.factor(1+Pe.subs(X,-12*w)/Be.subs(X,-12*w))
assert zplus==(4*w**2-100*w+75)/(4*w-25)
assert zminus==(12*w**3+28*w**2-23*w-9)/(5*w+3)
res["w2_z1"]={"sharp_minpoly_degree":22,"krylov_rank_mod_prime":22}
res["w2_z2"]={"sharp_minpoly_degree":28,"krylov_rank_mod_prime":28}
res["w2_all_real_z"]={"z=1":22,"z=109/17":26,"z=153/13":26,"otherwise":28}
res["resonance_candidates"]={"t^2=4w":str(zplus),"t^2=-12w":str(zminus)}
dest=Path(__file__).with_name("PREFIX598U3_R2_parametric_spectral_resonance_results.json")
dest.write_text(json.dumps(res,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(res,indent=2,ensure_ascii=False))

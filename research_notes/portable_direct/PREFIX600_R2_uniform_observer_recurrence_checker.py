#!/usr/bin/env python3
"""PREFIX-600-R2: exact Z[z] certificate for 48-phase X6-BRC uniform-source recursion.
Frozen native science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
No floating point; rebuilds native STAR phases, successors, gate and tail exactly.
"""
import sympy as sp
from pathlib import Path
import json

z,u=sp.symbols("z u")
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4)
             for k in STAR[a] for sgn in (-1,1)
             for p in near(a,sgn*k))
idx={phase:i for i,phase in enumerate(phases)}
def successor(i):
    a,p,c=phases[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(idx[v] for v in
       ([(a,c,q) for q in near(a,c) if q!=p]+
        [(b,c,q) for q in near(b,c)]))
N=tuple(successor(i) for i in range(48))
axis=tuple(abs(phase[2])-1 for phase in phases)
g=idx[(0,1,-3)]
assert len(phases)==len(idx)==48 and g==4
assert all(len(ns)==3 for ns in N)
assert sum(g in ns for ns in N)==3

Q=sp.zeros(48)
for i,ns in enumerate(N):
    if axis[i]>=4: continue
    for j in ns:
        Q[i,j]=1 if i==g else (3+z if j==g else 2)
s=4*z+12
V=[sp.ones(48,1)]
for k in range(20):
    V.append(Q*V[-1])
# Universal polynomial vector identity P_z(Q)*ones=0.
assert all(sp.expand(x)==0 for x in V[7]-2*V[6]-s*V[3]+2*s*V[2])
# Stronger z=1 identity.
assert all(sp.expand(x.subs(z,1))==0 for x in V[6]-16*V[2])
f=[sp.expand(sum(v)) for v in V]
for n in range(14):
    assert sp.expand(f[n+7]-2*f[n+6]-s*f[n+3]+2*s*f[n+2])==0

H7=sp.Matrix(7,7,lambda i,j:f[i+j])
h7=sp.factor(H7.det(method="domain-ge"))
want=-sp.Integer(260919263232)*(z-1)**2*(z+3)**3*(
    81*z**3-27*z**2+27*z+11)*(
    4*z**4+31*z**3+123*z**2+61*z+613)
assert sp.expand(h7-want)==0
assert sp.discriminant(243*z**2-54*z+27,z)<0
H6=sp.Matrix(6,6,lambda i,j:f[i+j])
h6_1=sp.factor(H6.det(method="domain-ge").subs(z,1))
assert h6_1==-sp.Integer(179821690748928)

denom=(1-2*u)*(1-s*u**4)
D=[1,-2,0,0,-s,2*s]
Ncoef=[sp.factor(sum(D[j]*f[i-j] for j in range(min(i,5)+1)))
       for i in range(7)]
expected=[48,3*(z+32),3*(3*z+61),18*(z-1),
          -8*(20*z+77),-32*(11*z+38),-768*(z+3)]
assert all(sp.expand(a-b)==0 for a,b in zip(Ncoef,expected))

# Distinct exact integer/rational specializations verify full path evolution.
for zz in (sp.Integer(0),sp.Integer(1),sp.Integer(2),
           sp.Rational(3,2),sp.Integer(5)):
    M=Q.subs(z,zz)
    v=sp.ones(48,1)
    vals=[]
    for n in range(21):
        vals.append(sum(v))
        v=M*v
    ss=4*zz+12
    assert all(vals[n+7]==2*vals[n+6]+ss*vals[n+3]-2*ss*vals[n+2]
               for n in range(14))
    if zz==1: assert all(vals[n+6]==16*vals[n+2] for n in range(15))

data={
 "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "model":"48-phase positive tail from original 96 ports, 576 typed actions",
 "axis_weights":[1,1,1,1,0,0],
 "observer":"uniform right vector e=ones(48); all-phase f_n=e^T Q^n e",
 "vector_annihilator":"t^2*(t-2)*(t^4-4z-12)",
 "z=1_vector_annihilator":"t^2*(t^4-16)",
 "minimal_zero_start_uniform_order":{"z=1":6,"z>=0,z!=1":7},
 "hankel7_factorization":str(h7),
 "hankel6_z1":str(h6_1),
 "generating_denominator":"(1-2u)*(1-(4z+12)u^4)",
 "generating_numerator_coefficients":[str(p) for p in Ncoef],
 "exact_parameter_checks":["0","1","2","3/2","5"],
 "verification":"all coefficient identities in Z[z], exact Hankel determinants, 5 x 21-step rational trajectories",
 "status":"AUTHOR_SIDE_EXACT_CHECKS_PASS_INDEPENDENT_REVIEW_PENDING"
}
out=Path(__file__).with_name("PREFIX600_R2_uniform_observer_recurrence_results.json")
out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(data,indent=2,ensure_ascii=False))

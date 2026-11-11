#!/usr/bin/env python3
"""Exact certificate: 1,144 fixed first-zero phases persist for the full
nonnegative initial/terminal r range of the original frozen 15-atom R5 ray.
No native X6 interpretation or Source Result is implied.
"""
from fractions import Fraction as F
from pathlib import Path
from runpy import run_path

parent=(Path(__file__).resolve().parent.parent
        /"brc_r5_sharp_nonlocal_fifteen_ray_20261111"
        /"VERIFY_R5_SHARP_RAY.py")
assert parent.is_file()
z=run_path(str(parent))
X,IX,steps,D,eps_max=(z[key] for key in
                       ("X","IX","steps","D","eps_max"))
assert len(X)==28 and len(steps)==15
k0=IX[(0,3)]
x=X[k0]
assert x==F(155682221,25142124560000000)
assert eps_max==F(9,115400000)

H=[0]*28
for i,a in ((1,-23),(2,28),(6,-5)):
    H[IX[(i,3)]]=a
    H[IX[(i,1)]]=-a
assert not any(z["obs"](H))

atoms=[tuple(int(36*a*v) for v in h) for j,i,a,h in steps]
size=1<<15
P=[(0,)*28]+[None]*(size-1)
for s in range(1,size):
    bit=s&-s
    j=bit.bit_length()-1
    P[s]=tuple(P[s^bit][k]+atoms[j][k] for k in range(28))

# Exact largest closed r interval with all 28 initial masses and the
# complete-15-atom endpoint at eps_max nonnegative.
lower=[]; upper=[]
for name,original in (("initial",X),
                      ("terminal",tuple(X[k]+eps_max*D[k] for k in range(28)))):
    for k in range(28):
        if H[k]:
            root=-original[k]/(x*H[k])
            if H[k]>0: lower.append((root,name,k))
            else: upper.append((root,name,k))
lo=max(v for v,name,k in lower)
hi=min(v for v,name,k in upper)
assert lo==F(-427508577031693280,628800490619),lo
assert hi==F(1,23),hi
assert any(v==lo and name=="terminal" and k==IX[(6,1)]
           for v,name,k in lower)
assert any(v==hi and name=="initial" and k==IX[(1,3)]
           for v,name,k in upper)
for r in (lo,hi):
    assert all(X[k]+x*r*H[k]>=0 for k in range(28))
    assert all(X[k]+x*r*H[k]+eps_max*D[k]>=0 for k in range(28))

weights=[h[k0] for h in atoms]
Hset={0}
for w in weights:
    Hset|={s+w for s in list(Hset)}
needed={-h for h in Hset if h<=-3}
assert len(Hset)==2293 and min(Hset)==-1348 and max(Hset)==1348
assert len(needed)==1144 and min(needed)==3 and max(needed)==1348
assert F(36)*x/3<eps_max

# For every fixed phase t_n=36*x/n, construct one labeled prefix
# S with P_S[k0]=-n, and certify that X(r)+t_n P_S/36 >=0 at
# BOTH parameter endpoints. Every inequality is affine in r,
# hence the same S works for ALL real r in the entire interval.
witness={}
for s in range(1,size):
    n=-P[s][k0]
    if n not in needed or n in witness:
        continue
    t=F(36)*x/n
    if all(X[k]+x*r*H[k]+t*F(P[s][k],36)>=0
           for r in (lo,hi) for k in range(28)):
        witness[n]=s
assert set(witness)==needed,(len(witness),len(needed-set(witness)))
assert sum(witness.values())==9387630
assert witness[3]==1050 and witness[420]==1024 and witness[1348]==31744

print("INT_WEIGHTS",weights)
print("INT_SUPPORT",min(Hset),max(Hset),len(Hset))
print("FIXED_INTERIOR_PHASE_FORMS",len(needed),min(needed),max(needed))
print("COMPLETE_RAY_CLOSED_PARAMETER_DOMAIN",lo,hi)
print("FULL_RANGE_SINGLE_WITNESS_FOR_EACH_FORM",len(witness))
print("WITNESS_EXAMPLES",[(n,witness[n]) for n in
                          (3,4,5,6,7,8,9,10,100,420,910,1348)
                          if n in witness])
print("WITNESS_MASK_MIN_MAX",min(witness.values()),max(witness.values()))
print("WITNESS_MASK_SUM",sum(witness.values()))
print("PASS_R5_GLOBAL_1144_FIXED_FIRST_ZERO_WITNESSES")

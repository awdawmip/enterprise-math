#!/usr/bin/env python3
"""R749SSM exact four-read 7-versus-8 separation certificate. Python standard library only."""
from fractions import Fraction as F
from itertools import permutations
import json

W=(1,1,2,3,6)
N=26
a=[0]*(N+1); a[0]=1
for w in W:
    for n in range(w,N+1):
        a[n]+=a[n-w]
C=[0]*(N+1); T=[0]*(N+1)
for q in range(1,N+1):
    C[q]=C[q-1]+a[q-1]
    T[q]=T[q-1]+C[q-1]
anchors={7:(65,91),8:(98,156),13:(506,1261),14:(662,1767),
         19:(2106,7447),20:(2576,9553),25:(6331,28883),26:(7441,35214)}
assert all((C[q],T[q])==v for q,v in anchors.items())

def S(q): return 18*q**4+54*q**3-345*q**2+2070*q-16315

# Bivariate rational polynomials: (power_e,power_d) -> exact coefficient.
ONE={(0,0):F(1)}
E={(1,0):F(1)}
D={(0,1):F(1)}
def const(v): return {(0,0):F(v)} if v else {}
def add(*polys):
    o={}
    for p in polys:
        for k,v in p.items(): o[k]=o.get(k,F(0))+v
    return {k:v for k,v in o.items() if v}
def scale(p,v): return {k:v*x for k,x in p.items() if v*x}
def mul(p,q):
    o={}
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            key=(i+k,j+l); o[key]=o.get(key,F(0))+v*w
    return {k:v for k,v in o.items() if v}
def det3(rows):
    o={}
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        x=ONE
        for i in range(3): x=mul(x,rows[i][perm[i]])
        o=add(o,scale(x,-1 if inv%2 else 1))
    return o
def row(j):
    q,p=7+6*j,8+6*j
    v=scale(add(const(C[q]),D),p**3)
    u=add(scale(add(const(T[q]),E),q**3),
          scale(add(const(C[q]),D),F(S(p)-S(q),108)))
    return v,scale(u,-1),add(scale(u,C[p]),scale(v,-T[p]))
rows=[row(j) for j in range(4)]
H2=det3([rows[i] for i in (0,1,2)])
H3=scale(det3([rows[i] for i in (0,1,3)]),6)

coef2={
 (2,0):-25999464658656, (2,1):-2170402847280,
 (1,0):25665881152213864, (1,1):3818332725903764, (1,2):8517190893192,
 (0,0):-45032970208568420, (0,1):-49829920474516588,
 (0,2):-4939292865911139, (0,3):923243492481
}
coef3={
 (2,0):-2376041366849184, (2,1):-111784049774064,
 (1,0):2145129655398174560, (1,1):315754546776127640,
 (1,2):531210657740480,
 (0,0):-851458936224224926, (0,1):-4586875289048978667,
 (0,2):-423838272588088662, (0,3):55771703467759
}
assert H2=={k:F(v) for k,v in coef2.items()}
assert H3=={k:F(v) for k,v in coef3.items()}

# Coefficients in Z[d], low degree to high.
def p_add(*polys):
    o=[0]*max(map(len,polys))
    for p in polys:
        for i,v in enumerate(p): o[i]+=v
    while len(o)>1 and o[-1]==0: o.pop()
    return o
def p_scale(p,v): return [v*x for x in p]
def p_mul(p,q):
    o=[0]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q): o[i+j]+=v*w
    while len(o)>1 and o[-1]==0: o.pop()
    return o
def p_sub(p,q): return p_add(p,p_scale(q,-1))
def by_e(coef,k):
    n=max(j for (i,j) in coef if i==k)
    return [coef.get((k,j),0) for j in range(n+1)]
a2,b2,c2=[by_e(coef2,k) for k in (2,1,0)]
a3,b3,c3=[by_e(coef3,k) for k in (2,1,0)]
# Quadratic resultant: (a*C-A*c)^2-(a*B-A*b)*(b*C-B*c).
x=p_sub(p_mul(a2,c3),p_mul(a3,c2))
y=p_sub(p_mul(a2,b3),p_mul(a3,b2))
z=p_sub(p_mul(b2,c3),p_mul(b3,c2))
res=p_sub(p_mul(x,x),p_mul(y,z))

Q=[
 109796349314075020060949372306640574723358682,
 -38045439719073116059985350517020931359464817,
 -2277402286244385991893563886215342942920759,
 923053369069668327403631270396371444479035,
 14501898594290005726122391371730051335594,
 175742992512176288201620423729874424
]
expected=p_scale(p_mul(p_mul(p_mul([65,1],[506,1]),
                             [1569882365,234443938]),Q),-67436544)
assert res==expected, "Exact resultant factorization failed"
margin=Q[0]-sum(2**i*abs(Q[i]) for i in range(1,6))
assert margin==16979397777109496872916184850765128499562660>0
assert 1569882365-2*234443938==1100994489>0

# The earlier R749SSL exact three-read intersection is reproduced as a
# root-isolation check; its full inverse bounds were proved in that source.
def P(t): return 5957265452844*t*t-5464016404300823*t+35816460863863
assert P(F(0))>0 and P(F(1,100))<0
assert 2*5957265452844*F(1,100)-5464016404300823<0

result={
 "schema":"R749SSM_FOUR_READ_7_8_PAIR_SEPARATION_V1",
 "status":"PASS",
 "cutoffs":[7,8], "read_offsets":[0,6,12,18],
 "weights":list(W), "shared_real_calibration_error_bounds":["-2","2"],
 "anchors":{str(q):[str(v) for v in vals] for q,vals in anchors.items()},
 "determinants":{"H2":"det(L0,L1,L2)","H3":"6*det(L0,L1,L3)"},
 "resultant":"-67436544*(d+65)*(d+506)*(234443938*d+1569882365)*Q(d)",
 "Q_coefficients_low_to_high":[str(v) for v in Q],
 "Q_lower_bound_for_abs_d_le_2":str(margin),
 "verification":"Exact source counts, full bivariate determinants, quadratic resultant polynomial identity, exact interval triangle positivity; no floats.",
 "claim":"Four reads distinguish cutoff 7 and 8 uniformly on bounded real common-error model; three reads intersect by R749SSL.",
 "boundary":"Local cutoff-pair theorem, not global four-read injectivity or native X6/BRC."
}
with open("R749SSM_FOUR_READ_PAIR_SEPARATION_RESULTS.json","w",encoding="utf-8") as f:
    json.dump(result,f,indent=2,sort_keys=True,ensure_ascii=False)
    f.write("\n")
print("PASS; strict Q lower bound",margin)

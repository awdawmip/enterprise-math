#!/usr/bin/env python3
"""PREFIX-603-R2: exact native X6-BRC one-step reachability and sharp recurrence.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
This proves exact algebra for typed native path recurrence; no classical phase approximation.
"""
import json
from collections import Counter
from pathlib import Path
import sympy as sp

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
PHASES=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
IX={q:i for i,q in enumerate(PHASES)}
def successors(i):
    a,p,c=PHASES[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(IX[q] for q in ([(a,c,r) for r in near(a,c) if r!=p]
                                 + [(b,c,r) for r in near(b,c)]))
N=tuple(successors(i) for i in range(48))
G=IX[(0,1,-3)]
assert len(PHASES)==48 and G==4 and all(len(ns)==3 for ns in N)
z,t=sp.symbols('z t')
s=4*z+12
# All original typed transitions, with weight vector (1,1,1,1,0,0):
# source bit ports v in 0,1; destination bit ports u in 0,1;
# three native successor phases j; original gated edge (j=G,u=v=1) weighted z.
A=sp.zeros(96,96)
typed_native_edges=0
for i,ns in enumerate(N):
    for j in ns:
        for u in (0,1):
            for v in (0,1):
                typed_native_edges+=1
                if abs(PHASES[i][2])>4:continue
                A[2*i+u,2*j+v]+=z if (j==G and u==v==1) else 1
assert typed_native_edges==576
# 48-phase tail encoder C and its verified raw port-embedding E.
C=sp.zeros(48,96)
E=sp.zeros(96,48)
for j in range(48):
    C[j,2*j]=1
    E[2*j,j]=1
    if j!=G:C[j,2*j+1]=1
    else:E[2*j+1,j]=1
F=C*A
Q=F*E
# Independent row/successor formula of native positive 48 tail.
Qdirect=sp.zeros(48,48)
for i,ns in enumerate(N):
    if abs(PHASES[i][2])>4:continue
    for j in ns:
        Qdirect[i,j]=1 if i==G else (3+z if j==G else 2)
assert Q==Qdirect
assert sum(all(Q[i,j]==0 for j in range(48)) for i in range(48))==16
# Explicit 32x32 symbolic minor found from exact fixed-gate integer pivots.
M=Q.subs(z,2)
rows=tuple(M.T.rref()[1]); cols=tuple(M.rref()[1])
assert len(rows)==len(cols)==32
minor=sp.factor(Q.extract(rows,cols).det(method='domain-ge'))
assert sp.simplify(minor-7044820107264*(z+3))==0
# Hence rank(Q)=32 for every real z>=0; rank F=32 also, since
# Q=FE and 16 rows of F vanish. Therefore image(F)=image(Q).
assert sum(all(F[i,j]==0 for j in range(96)) for i in range(48))==16
# z=1 / z!=1: known exact full matrix annihilator, rechecked symbolically.
p10=t**2*(t**4-16)*(t**4-s)
p6=t**2*(t**4-16)
Qpowers=[sp.eye(48)]
for k in range(10):Qpowers.append(Q*Qpowers[-1])
def apply(poly,vec):
    return sp.Matrix(sum((sp.expand(c)*Qpowers[k]*vec for (k,),c in sp.Poly(poly,t).terms()),sp.zeros(*vec.shape)))
assert all(sp.expand(v)==0 for v in apply(p10,sp.eye(48)))
assert all(sp.expand(v)==0 for v in apply(p6,sp.eye(48)).subs(z,1))
# On image F: one step drops a factor t from matrix-wide annihilator.
p9=t*(t**4-16)*(t**4-s)
p5=t*(t**4-16)
assert all(sp.expand(v)==0 for v in apply(p9,F))
assert all(sp.expand(v)==0 for v in apply(p5,F).subs(z,1))
# A single original nonnegative raw bit port e_16 is sharp across all z>=0.
raw_port=16
v=F[:,raw_port]
assert [(i,str(v[i])) for i in range(48) if v[i]!=0]==[(2,'2'),(14,'2'),(15,'2')]
K=sp.Matrix.hstack(*(Qpowers[k]*v for k in range(9)))
rows9=tuple(K.subs(z,2).T.rref()[1]);assert len(rows9)==9
witness_minor=sp.factor(K.extract(rows9,range(9)).det())
assert sp.simplify(witness_minor+34359738368*(z-1)**4*(z+3))==0
assert K.subs(z,1).rank()==5
# The actual first-step image has 64 nonzero columns, each with 3 positive
# native phase support entries, and 32 zero columns for all z>=0.
support_by_gate={}
for zv in (0,1,2):
    Fv=F.subs(z,zv)
    hist=Counter(sum(Fv[i,j]!=0 for i in range(48)) for j in range(96))
    assert hist=={0:32,3:64}
    support_by_gate[str(zv)]={str(k):hist[k] for k in sorted(hist)}
# At z>=0 every symbolic nonzero F entry is 1/2/3+z, and none vanishes.
assert set(F) <= {sp.Integer(0),sp.Integer(1),sp.Integer(2),z+1,z+2,z+3}
# Check fixed-gate exact ranks on single original raw port inputs.
single_port_counts={}
for zv in (1,2):
    Qv=Q.subs(z,zv);Fv=F.subs(z,zv)
    pows=[sp.eye(48)]
    for k in range(9):pows.append(Qv*pows[-1])
    tally=Counter()
    for j in range(96):
        inp=Fv[:,j]
        if inp==sp.zeros(48,1):tally[0]+=1;continue
        arr=[pows[k]*inp for k in range(6 if zv==1 else 10)]
        tally[sp.Matrix.hstack(*arr).rank()]+=1
    single_port_counts[str(zv)]={str(k):tally[k] for k in sorted(tally)}
assert single_port_counts['1']=={'0':32,'4':32,'5':32}
assert single_port_counts['2']=={'0':32,'4':32,'5':16,'9':16}
# Thus original positive first-step source vectors have either support 0
# or >=3, ruling out exactly-supported formal e_i+e_j mixtures for z>=0.
result={
  'schema':'PREFIX603_R2_NATIVE_REACHABLE_ONE_STEP_SHARP_MINPOLY',
  'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'original_native_ports':96,'original_native_typed_edges':typed_native_edges,
  'tail_dimension':48,'gate_target_phase':G,'axis_weights':[1,1,1,1,0,0],
  'factorization':'F=C*A; Q=F*E',
  'symbolic_32_minor':str(minor),
  'rank_F_and_Q_for_all_z_ge_0':32,
  'sharp_mu_restricted_image_F':{'z=1':str(sp.factor(p5)),
                                 'z>=0,z!=1':str(sp.factor(p9))},
  'native_nonnegative_port_16_reaches_sharp_mu':True,
  'port_16_tail_support':[(i,str(v[i])) for i in range(48) if v[i]!=0],
  'port_16_krylov_9_minor':str(witness_minor),
  'port_16_krylov_9_minor_rows':rows9,
  'port_16_rank_at_z1':5,
  'native_raw_port_first_step_support_counts':support_by_gate,
  'native_raw_port_sharp_degree_census':single_port_counts,
  'observer':'all 48 phase outputs from first original 96-port step onward',
  'future_operation_scope':'arbitrary count of further stationary same-parameter Q steps',
  'proof_status':'AUTHOR_SIDE_EXACT_CHECK; independent driver review pending'
}
path=Path(__file__).with_name('PREFIX603_R2_native_reachable_tail_results.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PREFIX-603 exact proof/checker PASS')
print('rank minor=',minor)
print('port16 lower minor=',witness_minor)
print('native nonzero support counts=',support_by_gate)
print('native raw port minimum-degree counts=',single_port_counts)

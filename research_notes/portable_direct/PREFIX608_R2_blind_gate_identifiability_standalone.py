#!/usr/bin/env python3
"""Frozen X6 native STAR phase-sum checker, PREFIX-608-R2 (exact SymPy)."""
import json
from pathlib import Path
import sympy as s

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
phases=tuple((a,p,sign*c) for a in range(4) for c in STAR[a]
             for sign in (-1,1) for p in near(a,sign*c))
assert len(phases)==48 and len(set(phases))==48
index={p:i for i,p in enumerate(phases)}
def successors(i):
    a,p,c=phases[i]
    b=next(x for x in range(4) if x!=a and abs(c) in STAR[x])
    return tuple(index[x] for x in ([(a,c,v) for v in near(a,c) if v!=p]
                                    +[(b,c,v) for v in near(b,c)]))
N=[successors(i) for i in range(48)]
g=index[(0,1,-3)]
assert g==4 and all(len(x)==3 for x in N)
def Q(q):
    m=s.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js:
            m[i,j]=1 if i==g else (3+q if j==g else 2)
    return m
A=Q(1); G=Q(2)-A; D=Q(0)*Q(1)
cols=list((A*A).rref()[1]); assert len(cols)==16
E=(A*A)[:,cols]
rows=list(E.T.rref()[1]); K=E.extract(rows,range(16)).inv()*s.eye(48).extract(rows,range(48))
assert K*E==s.eye(16) and D.rank()==16 and E*K*D==D
T=K*A*E; H=K*G*E
assert G.rank()==1 and E*T==A*E and E*H==G*E
r,c=next((i,j) for i in range(16) for j in range(16) if H[i,j]!=0)
u=H[:,c]; h=H[r,:]/H[r,c]
W=s.Matrix.hstack(u,T*u,T*T*u,T*T*T*u)
O=s.Matrix.vstack(h,h*T,h*T*T,h*T*T*T)
L=(O*W).inv()*O
P=W*L
z=s.symbols('z')
B=L*(T+(z-1)*H)*W
assert B==s.Matrix([[0,0,0,4*(z+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert L*W==s.eye(4) and (s.eye(16)-P)*H==s.zeros(16)

v=s.ones(48,1); v2=v.copy(); v2[28]=s.Rational(2501,2500);v2[32]=s.Rational(2499,2500)
y0=D*v; ya=D*v2
c0=L*K*y0; ca=L*K*ya
f0=(s.eye(16)-P)*K*y0; fa=(s.eye(16)-P)*K*ya
assert c0==s.Matrix([s.Rational(9,2),4,s.Rational(3,2),s.Rational(3,4)])
assert ca==s.Matrix([s.Rational(9,2),4,s.Rational(3,2),s.Rational(7499,10000)])
assert f0==fa
qfirst=s.Rational(7503,7499)
assert (B.subs(z,1)*c0)==(B.subs(z,qfirst)*ca)
assert {str(i):str((ya-y0)[i]) for i in range(48) if ya[i]!=y0[i]}=={
    '4':'-1/1250','5':'-1/625','29':'-1/625'}
word=[1,0,2,5,s.Rational(3,2),0,7,4,1,0,2,9]
a=y0;b=ya; equal=0
for step,q in enumerate(word):
    a=Q(q)*a;b=Q(qfirst if step==0 else q)*b
    assert a==b
    equal+=48
assert equal==576

# Consecutive full-phase inverse is exact for all excited gates.
y=y0; inverse=0
for q in [0,2,1,3,s.Rational(5,2),0,8,1,4,0]:
    before=L*K*y; nxt=Q(q)*y; after=L*K*nxt
    assert before[3]!=0 and after[0]/(4*before[3])-3==q
    assert all(x>=0 for x in nxt)
    y=nxt;inverse+=1
assert (L*K*(Q(1)*y0))[0]/(4*c0[3])-3==1

# Genuine nonnegative native basis-source: exactly one excited residue class.
src=s.eye(48)[:,4]; y=D*src
c=L*K*y
assert c==s.Matrix([0,2,0,0]) and all(x>=0 for x in y)
wa=[0,2,1,7,4,0,3,5,2,6,1]
wb=[8,2,1,7,9,0,3,5,0,6,1]
b=y; invisible=0
for q,qp in zip(wa,wb):
    y=Q(q)*y;b=Q(qp)*b
    assert y==b
    invisible+=48
assert invisible==528
results={
 'schema':'PREFIX608_R2_UNKNOWN_SOURCE_NATIVE_BRC_EXACT_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'phase_count':48,'native_port_count':96,'native_tagged_action_count':576,
 'weights':[1,1,1,1,0,0],'tail_rank':16,'gate_factor_dimension':4,
 'full_phase_blind_pair_equalities':equal,'excited_gate_inversions':inverse,
 'nonnegative_unexcited_source_equalities':invisible,
 'different_positive_sources':{'default':'all 1','alternate':{'28':'2501/2500','32':'2499/2500'}},
 'different_first_gates':['1','7503/7499'],
 'blind_initial_gate_component':['3/4','7499/10000'],
 'unexcited_source_phase_index':4,'unexcited_c0':['0','2','0','0'],
 'status':'AUTHOR_SIDE_EXACT_VERIFICATION; INDEPENDENT_DRIVER_REVIEW_PENDING'
}
Path(__file__).with_name('PREFIX608_R2_blind_gate_identifiability_results.json').write_text(json.dumps(results,indent=2)+'\n')
print('PREFIX608 EXACT PASSED',equal,inverse,invisible)

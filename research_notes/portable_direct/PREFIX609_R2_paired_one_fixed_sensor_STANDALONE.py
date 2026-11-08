#!/usr/bin/env python3
"""PREFIX-609 exact native X6-BRC phase-sum paired-probe checker.
Frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires SymPy; preserves 48 phase/96 port/576 tagged-action scope.
"""
import json
from pathlib import Path
import sympy as S
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
phases=tuple((a,p,sgn*c) for a in range(4) for c in STAR[a]
             for sgn in (-1,1) for p in near(a,sgn*c))
assert len(phases)==48 and len(set(phases))==48
ix={p:i for i,p in enumerate(phases)}
def successors(i):
    a,p,c=phases[i]
    b=next(x for x in range(4) if x!=a and abs(c) in STAR[x])
    return tuple(ix[x] for x in
                 [(a,c,v) for v in near(a,c) if v!=p]
                 +[(b,c,v) for v in near(b,c)])
N=[successors(i) for i in range(48)]
g=ix[(0,1,-3)]
assert g==4 and all(len(r)==3 for r in N)
def Q(q):
    m=S.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js:
            m[i,j]=1 if i==g else (q+3 if j==g else 2)
    return m
A=Q(1); G=Q(2)-A; D=Q(0)*A
cols=list((A*A).rref()[1]);assert len(cols)==16
E=(A*A)[:,cols]; rows=list(E.T.rref()[1])
K=E.extract(rows,range(16)).inv()*S.eye(48).extract(rows,range(48))
T=K*A*E; H=K*G*E
assert K*E==S.eye(16) and D.rank()==16
assert E*T==A*E and E*H==G*E and T**4==16*S.eye(16)
r,c=next((i,j) for i in range(16) for j in range(16) if H[i,j]!=0)
u=H[:,c];h=H[r,:]/H[r,c]
W=S.Matrix.hstack(u,T*u,T*T*u,T*T*T*u)
O=S.Matrix.vstack(h,h*T,h*T*T,h*T*T*T)
L=(O*W).inv()*O; P=W*L
z=S.symbols('z')
B=L*(T+(z-1)*H)*W
assert B==S.Matrix([[0,0,0,4*(z+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert (E*W)[3,:]==S.Matrix([[2,0,0,0]])
one=S.ones(48,1)
c0=L*K*D*one
assert c0==S.Matrix([S.Rational(9,2),4,S.Rational(3,2),S.Rational(3,4)])
f0=(S.eye(16)-P)*K*D*one
for t in range(8): assert (E*T**t*f0)[3]==12*2**t
words=[
 [0,2,1,5,S.Rational(3,2),0,7,4,1,0,2,9],
 [1,S.Rational(7,3),0,4,S.Rational(1,7),6,0,1,S.Rational(17,5)],
 [S.Rational(3,5)]*17,
]
sources=[one,S.eye(48)[:,4],S.Matrix([S.Rational((7*i+3)%11+1,11) for i in range(48)])]
recoveries=0;nonnegative_checks=0;phase_equalities=0
for src in sources:
    for word in words:
        a=D*src; b=D*(src+one); contrast=D*one
        c=c0.copy()
        for t,q in enumerate(word,1):
            a=Q(q)*a; b=Q(q)*b;contrast=Q(q)*contrast
            assert b-a==contrast
            assert all(x>=0 for x in a) and all(x>=0 for x in b)
            assert c[3]!=0
            sensor=b[3]-a[3]
            recovered=S.cancel((sensor-12*2**t)/(8*c[3])-3)
            assert recovered==q
            c=B.subs(z,recovered)*c
            recoveries+=1;nonnegative_checks+=2;phase_equalities+=48
v=one.copy();vp=one.copy()
vp[28]=S.Rational(2501,2500);vp[32]=S.Rational(2499,2500)
q1=S.Integer(1);qp=S.Rational(7503,7499)
assert Q(q1)*D*v==Q(qp)*D*vp
s1=(Q(q1)*D*(v+one)-Q(q1)*D*v)[3]
s2=(Q(qp)*D*(vp+one)-Q(qp)*D*vp)[3]
assert s2-s1==S.Rational(24,7499)
res={
 'schema':'PREFIX609_R2_PAIRED_NATIVE_BRC_ONE_SENSOR_EXACT_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'axis_weights':[1,1,1,1,0,0], 'phases':48,'bit_ports':96,'tagged_actions':576,
 'transient':'Q(0)Q(1)','paired_inputs':'v and v + ones(48), same unknown gates',
 'zero_based_fixed_phase_sensor':3,'contrast_initial_c':[str(x) for x in c0],
 'sensor_identity':'difference_phase3(t)=12*2**t+8*(q_t+3)*c_(t-1,3)',
 'exact_gate_recoveries':recoveries,'full_phase_difference_equalities':phase_equalities,
 'nonnegative_complete_phase_state_checks':nonnegative_checks,
 'blind_pair_controlled_probe_gap':str(s2-s1),
 'review':'AUTHOR_SIDE_EXACT;INDEPENDENT_REVIEW_PENDING'
}
Path(__file__).with_name('PREFIX609_R2_paired_one_fixed_sensor_results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))

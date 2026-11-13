#!/usr/bin/env python3
"""Exact unknown two-step transient recovery from paired native X6-BRC phase-3 observations.
Uses frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d; SymPy.
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
    a,p,c=phases[i];b=next(x for x in range(4) if x!=a and abs(c) in STAR[x])
    return tuple(ix[x] for x in [(a,c,v) for v in near(a,c) if v!=p]
                              + [(b,c,v) for v in near(b,c)])
N=[successors(i) for i in range(48)];g=ix[(0,1,-3)];assert g==4
def Q(z):
    M=S.zeros(48)
    for i,ns in enumerate(N):
        if abs(phases[i][2]) in (5,6):continue
        for j in ns: M[i,j]=1 if i==g else (z+3 if j==g else 2)
    return M
A=Q(1);G=Q(2)-A
cols=list((A*A).rref()[1]);E=(A*A)[:,cols];assert len(cols)==16
rows=list(E.T.rref()[1]);K=E.extract(rows,range(16)).inv()*S.eye(48).extract(rows,range(48))
T=K*A*E;H=K*G*E
assert K*E==S.eye(16) and T**4==16*S.eye(16) and E*T==A*E and E*H==G*E
k,l=next((i,j) for i in range(16) for j in range(16) if H[i,j]!=0)
u=H[:,l];h=H[k,:]/H[k,l]
W=S.Matrix.hstack(u,T*u,T*T*u,T*T*T*u);O=S.Matrix.vstack(h,h*T,h*T*T,h*T*T*T)
L=(O*W).inv()*O;P=W*L
q=S.symbols('q');B=S.Matrix([[0,0,0,4*(q+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert L*(T+(q-1)*H)*W==B and (E*W)[3,:]==S.Matrix([[2,0,0,0]])
assert (S.eye(16)-P)*H==S.zeros(16)
a,b=S.symbols('a b');one=S.ones(48,1)
fst=Q(b)*one;snd=Q(a)*fst
assert S.factor(fst[3]-(b+7))==0
assert S.factor(snd[3]-3*(a+7))==0
c0=L*K*snd;f0=(S.eye(16)-P)*K*snd
c_expected=S.Matrix([3*(a+3)/2,(b+7)/2,S.Rational(3,2),S.Rational(3,4)])
assert all(S.factor(c0[i]-c_expected[i])==0 for i in range(4))
assert all(S.factor((E*T**t*f0)[3]-12*2**t)==0 for t in range(4))
# T^4=16I implies this relation for all t>=0.
words=[
 [0,2,1,5,S.Rational(3,2),0,7,4,1,0,2,9],
 [1,S.Rational(7,3),0,4,S.Rational(1,7),6,0,1,S.Rational(17,5),2,3,1],
 [S.Rational(3,5)]*16,
]
pairs=[(0,0),(1,2),(S.Rational(7,3),S.Rational(5,4)),(3,0)]
sources=[one,S.eye(48)[:,4],S.Matrix([S.Rational(((7*i+3)%11)+1,11) for i in range(48)])]
recover=0;phase_checks=0;positive_checks=0; runs=0
for aa,bb in pairs:
    known=S.Matrix([v.subs({a:aa,b:bb}) for v in c_expected])
    for v in sources:
        for word in words:
            runs+=1
            x=v;xx=v+one
            for gate in [bb,aa]:
                x=Q(gate)*x;xx=Q(gate)*xx
                assert all(z>=0 for z in x) and all(z>=0 for z in xx)
                positive_checks+=2
            sb= (Q(bb)*(v+one))[3]-(Q(bb)*v)[3]
            sa=xx[3]-x[3]
            recovered_b=S.cancel(sb-7)
            recovered_a=S.cancel(sa/3-7)
            assert recovered_a==aa and recovered_b==bb
            c=S.Matrix([z.subs({a:recovered_a,b:recovered_b}) for z in c_expected]);assert c==known
            for t,gate in enumerate(word,1):
                x=Q(gate)*x;xx=Q(gate)*xx
                assert xx-x==Q(gate)*Q(aa)*Q(bb)*one if t==1 else True
                phase_checks+=48 if t==1 else 0
                assert all(z>=0 for z in x) and all(z>=0 for z in xx)
                positive_checks+=2
                s=xx[3]-x[3]
                assert c[3]>0
                gate_recovered=S.cancel((s-12*2**t)/(8*c[3])-3)
                assert gate_recovered==gate
                c=B.subs(q,gate_recovered)*c
                recover+=1
out={'schema':'PREFIX611_R2_UNKNOWN_TWO_GATE_TRANSIENT_PAIRED_SINGLE_SENSOR_V1',
     'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'original_phases':48,'original_ports':96,'tagged_actions':576,
     'axis_weights':[1,1,1,1,0,0],'sensor_zero_based':3,
     'initial_contrasts':['b+7','3*(a+7)'],
     'initial_four_state':['3*(a+3)/2','(b+7)/2','3/2','3/4'],
     'gate_free_sensor':'12*2**t','unknown_transient_pairs_checked':len(pairs),
     'unknown_source_vectors_checked':len(sources),'gate_words_checked':len(words),
     'full_run_combinations':runs,'exact_gate_recoveries':recover,
     'initial_native_48_phase_contrast_equalities':phase_checks,
     'nonnegative_complete_phase_states':positive_checks,
     'result':'AUTHOR_SIDE_EXACT_PROOF_AND_EXECUTED_CHECKS; DRIVER_REVIEW_PENDING'}
Path(__file__).with_name('PREFIX611_R2_unknown_twostep_single_sensor_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

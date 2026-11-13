#!/usr/bin/env python3
"""Exact native X6-BRC four-step single-phase residual certificate.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires SymPy. All arithmetic exact; zero-based phase indices.
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
    a,p,c=phases[i]; b=next(x for x in range(4) if x!=a and abs(c) in STAR[x])
    return tuple(ix[x] for x in [(a,c,v) for v in near(a,c) if v!=p]
                              +[(b,c,v) for v in near(b,c)])
N=[successors(i) for i in range(48)]
g=ix[(0,1,-3)]; assert g==4 and all(len(r)==3 for r in N)
def Q(q):
    m=S.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js: m[i,j]=1 if i==g else (q+3 if j==g else 2)
    return m
A=Q(1); G=Q(2)-A; D=Q(0)*Q(1)
cols=list((A*A).rref()[1]);assert len(cols)==16
E=(A*A)[:,cols]; rows=list(E.T.rref()[1]); K=E.extract(rows,range(16)).inv()*S.eye(48).extract(rows,range(48))
T=K*A*E;H=K*G*E
assert K*E==S.eye(16) and E*T==A*E and E*H==G*E and T**4==16*S.eye(16)
i,j=next((i,j) for i in range(16) for j in range(16) if H[i,j]!=0)
u=H[:,j];h=H[i,:]/H[i,j];W=S.Matrix.hstack(u,T*u,T*T*u,T*T*T*u)
O=S.Matrix.vstack(h,h*T,h*T*T,h*T*T*T);L=(O*W).inv()*O;P=W*L
q=S.symbols('q');B=S.Matrix([[0,0,0,4*(q+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert L*(T+(q-1)*H)*W==B and (E*W)[3,:]==S.Matrix([[2,0,0,0]])
assert (S.eye(16)-P)*H==S.zeros(16) and (S.eye(16)-P)*T*P==S.zeros(16)
assert T*(S.eye(16)-P)==(S.eye(16)-P)*T
one=S.ones(48,1)
sources=[one,S.eye(48)[:,4],S.Matrix([S.Rational(((7*i+3)%11)+1,11) for i in range(48)])]
words=[
 [0,2,1,5,S.Rational(3,2),0,7,4,1,0,2,9,3,1,0,5],
 [1,S.Rational(7,3),0,4,S.Rational(1,7),6,0,1,S.Rational(17,5),2,3,1,0,2,1,3,4],
 [S.Rational(3,5)]*18,
 [2,3,5,7, 4,2,3,5, 6,4,2,1, 9,6,4,2, 12,8],
]
checks_4=checks_8=checks_annihilate=checks_positive=0; max_horizon=0
example=None;recovery_n=0
for src in sources:
    y0=D*src; c0=L*K*y0; f0=(S.eye(16)-P)*K*y0
    for word in words:
        y=[y0];cs=[c0]; max_horizon=max(max_horizon,len(word))
        for gate in word:
            y.append(Q(gate)*y[-1]); cs.append(B.subs(q,gate)*cs[-1])
        for t in range(len(y)):
            # A complete independent 48-state reconstruction identity.
            assert y[t]==E*(W*cs[t]+T**(t%4)*16**(t//4)*f0)
            checks_annihilate+=48
            checks_positive+=1
            assert all(u>=0 for u in y[t])
        for t in range(len(word)-3):
            r=y[t+4][3]-16*y[t][3]
            assert S.expand(r-8*(word[t+3]-1)*cs[t][0])==0
            checks_4+=1
            if t+8<=len(word):
                rr=y[t+8][3]-16*y[t+4][3]
                a=word[t+3];b=word[t+7]
                assert S.expand(rr*(a-1)-4*(a+3)*(b-1)*r)==0
                checks_8+=1
                if src==one and word is words[3] and r!=0 and cs[t][0]!=0:
                    recovered=S.cancel(1+(a-1)*rr/(4*(a+3)*r))
                    assert recovered==b
                    recovery_n+=1
            if src==one and word is words[0] and t==0:
                example={'y_0_phase3':str(y[0][3]),'y_4_phase3':str(y[4][3]),
                         'q_4':str(word[3]),'c_0_0':str(c0[0]),'residual':str(r)}
# Exact symbolic four-step term is 4(q+3) regardless of the intervening three gates.
qq=S.symbols('q1:5')
product=S.eye(4)
for z in qq: product=B.subs(q,z)*product
assert product==4*S.diag(qq[3]+3,qq[2]+3,qq[1]+3,qq[0]+3)
assert example is not None
results={'schema':'PREFIX610_R2_FOUR_STEP_SINGLE_SENSOR_RESIDUAL_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'axis_weights':[1,1,1,1,0,0],'phase_count':48,'original_ports':96,'tagged_actions':576,
 'observed_phase_zero_based':3,'transient':'Q(0)Q(1)',
 'exact_identity':'y[t+4][3]-16*y[t][3] = 8*(q[t+4]-1)*c[t,0]',
 'eight_step_identity':'r[t+4]*(q[t+4]-1)=4*(q[t+4]+3)*(q[t+8]-1)*r[t]',
 'sources_checked':len(sources),'gate_words_checked':len(words),'max_gate_word_length':max_horizon,
 'four_step_exact_checks':checks_4,'eight_step_exact_checks':checks_8,
 'full_48_phase_reconstruction_exact_entries':checks_annihilate,
 'nonnegative_phase_state_checks':checks_positive,
 'self_calibrated_gate_recoveries':recovery_n,'example':example,
 'claim_status':'AUTHOR_SIDE_DERIVATION_AND_EXECUTED_EXACT_CHECKS; NO_INDEPENDENT_REVIEW'}
Path(__file__).with_name('PREFIX610_R2_four_step_sensor_residual_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(results,indent=2,ensure_ascii=False))

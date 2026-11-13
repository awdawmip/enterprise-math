#!/usr/bin/env python3
"""Exact native X6-BRC 4-sparse universal probe / recoverability certificate.
Science fixed at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Independent derived observer: original 48 phase-sum linear transfer; no path-history quotient claim.
"""
from pathlib import Path
import json
import sympy as S
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
phases=tuple((a,p,sign*c) for a in range(4) for c in STAR[a] for sign in (-1,1) for p in near(a,sign*c))
assert len(phases)==len(set(phases))==48
ix={p:i for i,p in enumerate(phases)}
def successors(i):
    a,p,c=phases[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
    return tuple(ix[x] for x in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)])
N=[successors(i) for i in range(48)]
g=ix[(0,1,-3)]; assert g==4
active={i for i in range(48) if abs(phases[i][2]) in (1,2,3,4)}
def Q(z):
    M=S.zeros(48)
    for i,ns in enumerate(N):
        if i not in active: continue
        for j in ns:
            M[i,j]=1 if i==g else (z+3 if j==g else 2)
    return M
z=S.symbols('z',nonnegative=True)
Qz=Q(z); Q0=Q(0); Q1=Q(1)
assert Qz-Q0 == z*(S.eye(48)[:,3]+S.eye(48)[:,14]+S.eye(48)[:,15])*S.eye(48)[4,:]
assert [j for j in range(48) if Qz[3,j]!=0]==[4,16,20]
assert [Qz[3,j] for j in [4,16,20]]==[z+3,2,2]
assert [j for j in range(48) if Qz[4,j]!=0]==[11,26,35]
assert [Qz[4,j] for j in [11,26,35]]==[1,1,1]
# Support identity: [Q(z_k)...Q(z_1)d]_4 >0 iff support(d) intersects R_k.
R=[{4}]
for k in range(16):
    R.append({j for i in R[-1] if i in active for j in N[i]})
G0={4};G1={11,26,35};G2={32,40,44};G3={14,23,47};G4={4,8,20}
assert R[0]==G0 and R[1]==G1 and R[2]==G2 and R[3]==G3 and R[4]==G4
assert all(R[k+4]==R[k] for k in range(1,13))
assert all(not (x&y) for i,x in enumerate([G0,G1,G2,G3]) for y in [G0,G1,G2,G3][i+1:])
assert N[4] == (11,26,35) and N[26] == (32,40,44) and set(N[40])==G3 and set(N[14])==G4
# Exact minimally supported input; nonzero support in one site of every period class.
d=S.zeros(48,1)
for i in [4,11,32,14]:d[i]=1
assert {i for i in range(48) if d[i]} == {4,11,32,14}
assert sum(d[j] for j in G1)==1
# Exact recovery via only phase 3 at every step and one additional phase 4 at the first step.
words=[
    [S.Integer(v) for v in [0,1,2,3,4,5,0,7,2,0,1,9,0,8,6,4]],
    [S.Rational(v) for v in [S.Rational(1,2),S.Rational(5,3),0,S.Rational(7,4),4,1,S.Rational(3,2),0,5,2,S.Rational(11,7)]],
]
sources=[S.zeros(48,1),S.ones(48,1),S.Matrix([S.Rational(((13*i+1)%17)+1,5) for i in range(48)])]
scales=[S.Rational(1),S.Rational(7,5),S.Rational(2,3)]
state_checks=0;decoded_gates=0; positivity_checks=0;first_excitation=[]
for v in sources:
    for lam in scales:
        for word in words:
            x=v.copy();xp=v+lam*d;observed=[];exact=lam*d;extras=[]
            for gate in word:
                x=Q(gate)*x; xp=Q(gate)*xp
                exact=Q(gate)*exact
                assert xp-x==exact
                observed.append(exact[3]);extras.append(exact[4])
                assert all(u>=0 for u in x) and all(u>=0 for u in xp)
                state_checks+=48
            scale_rec=S.cancel(extras[0]/sum(d[j] for j in G1))
            assert scale_rec==lam
            w=scale_rec*d
            first_excitation.append([str(w[4])])
            for k,(gate,y) in enumerate(zip(word,observed)):
                assert w[4]>0
                recovered=S.cancel((y-2*(w[16]+w[20]))/w[4]-3)
                assert recovered==gate
                w=Q(recovered)*w
                decoded_gates+=1;positivity_checks+=1
            assert w==exact
# sharp lower bound. If any of the 4 support representatives is removed,
# an early gate is invisible in the complete difference trajectory.
invisibility_checks=0
for r,src_idx in enumerate([4,11,32,14]):
    sparse=d-S.eye(48)[:,src_idx]
    assert sum(sparse[j] for j in [G0,G1,G2,G3][r])==0
    word=[S.Integer(1),S.Integer(2),S.Integer(3),S.Integer(4),S.Integer(5),S.Integer(6),S.Integer(7),S.Integer(8)]
    modified=word[:];modified[r]=S.Rational(17,5)
    def orbit(gs):
        w=sparse
        outs=[]
        for gate in gs:
            w=Q(gate)*w
            outs.append(w)
        return outs
    world1=orbit(word);world2=orbit(modified)
    assert all(a==b for a,b in zip(world1,world2))
    invisibility_checks+=len(word)*48
# Verify the recurrence valid after first positive step: w_(t+4)[4] = 4*(gate_(t+1)+3)*w_t[4]
period_checks=0
for word in words:
    w=d;states=[w]
    for gate in word:
        w=Q(gate)*w;states.append(w)
    for t in range(1,len(word)-3):
        assert states[t+4][4]==4*(word[t]+3)*states[t][4]
        period_checks+=1
# First 4 denominator values for d; symbolically first-step gate-free for t=0..3.
for t,val in enumerate([1,1,2,4]):
    s=d
    for _ in range(t):s=Q0*s
    assert s[4]==val
out={
 'schema':'PREFIX613_R2_SPARSE_NONUNIFORM_NATIVE_PROBE_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'carrier':'original X6-STAR 48-phase linear-sum observer; 96 ports and 576 tagged actions retained upstream',
 'axis_weights':[1,1,1,1,0,0],
 'gate_observer':3, 'scale_calibration_observer':4,
 'exact_4_support_groups':[sorted(x) for x in [G0,G1,G2,G3]],
 'support_path_mod4_certificate':[sorted(x) for x in R[:9]],
 'sparse_probe_nonzero_indices':[4,11,14,32],
 'probe_lambda_calibration':'phase4 first contrast = lambda*(d11+d26+d35)',
 'gate_formula':'g_t=(Y_t-2*(w_[t-1,16]+w_[t-1,20]))/w_[t-1,4]-3',
 'global_support_condition':'supp(d) intersects each G0,G1,G2,G3 (nonnegative d); full gate word n>=4',
 'support_lower_bound':4,
 'positive_scales_checked':len(scales),
 'unknown_base_sources_checked':len(sources),
 'gate_words_checked':len(words),
 'decoded_gates':decoded_gates,
 'full48_state_coordinate_equalities':state_checks,
 'all_phase_lower_bound_equalities':invisibility_checks,
 '4_step_excitation_equalities':period_checks,
 'result':'ALL_EXECUTED_ASSERTIONS_PASSED; AUTHOR_SIDE_EXACT_PROOF; INDEPENDENT_REVIEW_PENDING'
}
path=Path(__file__).with_name('PREFIX613_R2_sparse_probe_results.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps(out,indent=2,ensure_ascii=False))

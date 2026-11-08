#!/usr/bin/env python3
"""Author-side exact native X6-BRC phase observer checks for PREFIX-612.
Frozen scientific inputs: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Observer: original 48-phase linear sum, zero-based sensors 3 and 4.
"""
import json
from pathlib import Path
import sympy as S
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
phases=tuple((a,p,sign*c) for a in range(4) for c in STAR[a] for sign in (-1,1) for p in near(a,sign*c))
assert len(phases)==48 and len(set(phases))==48
ix={p:i for i,p in enumerate(phases)}
def successors(i):
    a,p,c=phases[i]; b=next(j for j in range(4) if j!=a and abs(c) in STAR[j]);
    return tuple(ix[x] for x in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)])
N=[successors(i) for i in range(48)]; g=ix[(0,1,-3)]; assert g==4 and len(N[g])==3
def Q(z):
    M=S.zeros(48)
    for i,ns in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in ns: M[i,j]=1 if i==g else (z+3 if j==g else 2)
    return M
u=S.ones(48,1); z=S.symbols('z');
assert S.factor((Q(z)*u)[3]-(z+7))==0
assert S.factor((Q(z)*u)[4]-3)==0
A,B=S.symbols('a b')
assert S.factor((Q(A)*Q(B)*u)[3]-3*(A+7))==0
C=S.symbols('c',positive=True)
assert S.factor((Q(B)*(C*u))[4]-3*C)==0
n=6
base=[S.Integer(2),S.Integer(3)]
word=[1,2,S.Rational(5,2),4,0,3]
sources=[u, S.eye(48)[:,4], S.Matrix([S.Rational(((7*i+3)%11)+1,11) for i in range(48)])]
scales=[S.Rational(1),S.Rational(2,3),S.Rational(7,5)]
sensor4_calibrations=0; decoded_parameters=0; exact_state_differences=0
for v in sources:
  for c in scales:
    x=v; xp=v+c*u
    y=[]; first4=None
    for k,gate in enumerate(base+word):
        x=Q(gate)*x; xp=Q(gate)*xp
        diff=xp-x
        if k==0: first4=diff[4]; sensor4_calibrations+=1
        y.append(diff[3])
        assert all(val>=0 for val in x) and all(val>=0 for val in xp)
        assert diff==c*Q(gate)*u if k==0 else True
        exact_state_differences+=48
    c_recovered=S.cancel(first4/3)
    assert c_recovered==c
    b_recovered=S.cancel(y[0]/c_recovered-7)
    a_recovered=S.cancel(y[1]/(3*c_recovered)-7)
    assert [b_recovered,a_recovered]==base
    decoded_parameters+=2
    four=S.Matrix([3*(a_recovered+3)/2,(b_recovered+7)/2,S.Rational(3,2),S.Rational(3,4)])*c_recovered
    for t,gate in enumerate(word,1):
        q_recovered=S.cancel((y[t+1]-12*2**t*c_recovered)/(8*four[3])-3)
        assert q_recovered==gate
        four=S.Matrix([4*(q_recovered+3)*four[3],four[0],four[1],four[2]])
        decoded_parameters+=1
# A strict-positive pair of unknown sources yields identical phase-3 traces under distinct probe scales and gates.
worlds=[(S.Integer(1),[1,2,1,2]),(S.Rational(101,100),[S.Rational(93,101),S.Rational(193,101),S.Rational(93,101),S.Rational(193,101)])]
traces=[]; first4=[]
for c, gates in worlds:
    x=u; xp=(1+c)*u; trace=[]
    for k,gate in enumerate(gates):
        x=Q(gate)*x; xp=Q(gate)*xp
        trace.append(xp[3]-x[3])
        if k==0: first4.append(xp[4]-x[4])
    traces.append(trace)
assert traces[0]==traces[1]==[8,27,48,108]
assert first4==[3,S.Rational(303,100)]
out={
 'schema':'PREFIX612_R2_UNKNOWN_CONTROLLED_INCREMENT_SCALE_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'original_phases':48,'native_ports':96,'tagged_actions':576,
 'fixed_axis_weights':[1,1,1,1,0,0],
 'sensors_zero_based':[3,4],
 'first_gate_calibration':'delta_phase4=3*lambda',
 'first_gate_phase3':'delta_phase3=lambda*(b+7)',
 'full_trace_phase3_counterexample':list(map(str,traces[0])),
 'two_world_increment_scales':list(map(lambda x:str(x[0]),worlds)),
 'two_world_first_phase4':list(map(str,first4)),
 'source_vectors_checked':len(sources),'positive_scales_checked':len(scales),
 'gate_sequences_checked':1,'sensor4_calibrations':sensor4_calibrations,
 'decoded_gate_parameters':decoded_parameters,
 'native_state_coordinate_checks':exact_state_differences,
 'result':'ALL_EXECUTED_ASSERTIONS_PASSED; AUTHOR_SIDE_EXACT_DERIVATION; DRIVER_REVIEW_PENDING'
}
Path(__file__).with_name('PREFIX612_R2_unknown_probe_scale_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

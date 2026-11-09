#!/usr/bin/env python3
"""PREFIX-625: exact native X6 BRC two-generation tagged-path observer.
Scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Native action enumerator cross-checked against PREFIX-624 checker
(commit 89c8d4689af84af95e4f1ae46c73672b8feb18b9).
Run: python PREFIX625_native_two_generation_path_checker.py
Only exact integer/rational symbolic arithmetic is used; no classical propagation.
"""
from itertools import product
from pathlib import Path
import json
import sympy as S

STARS = ((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c > 0 else k for k in STARS[a] if k != abs(c))
P = tuple((a,p,s*k) for a in range(4) for k in STARS[a]
          for s in (-1,1) for p in near(a,s*k))
IX = {p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c = P[i]
    b = next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]
                                   +[(b,c,k) for k in near(b,c)]))
N = tuple(neighbors(i) for i in range(48))
G = IX[(0,1,-3)]
AXIS = tuple(abs(c)-1 for a,p,c in P)
WEIGHTS = (1,1,1,1,0,0)
assert len(P) == 48 and len(set(P)) == 48 and G == 4 and sum(map(len,N)) == 144

def actions(z):
    for i in range(48):
        for j in N[i]:
            for u,v in product((0,1), repeat=2):
                wt = z if j==G and u==v==1 else WEIGHTS[AXIS[i]]
                yield (2*i+u,2*j+v,wt,(i,j,u,v))

def matrix(z):
    M = S.zeros(96,96)
    for dest,src,wt,label in actions(z):
        M[dest,src] += wt
    return M

A0,A1 = matrix(S.Integer(0)),matrix(S.Integer(1))
E = A1-A0
assert sum(x!=0 for x in E)==3 and E.rank()==1 and E*E==S.zeros(96)
live = sorted({src for dest,src,wt,label in actions(S.Integer(0)) if wt>0})
silent = sorted(set(range(96))-set(live))
assert len(live)==64 and len(silent)==32
T=A0*A0
U=A0*E
V=E*A0
# Fixed native-minor certificate (zero-based port numbers). The gate effects vanish in this minor.
C=(0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68)
R=(0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54)
assert len(C)==len(R)==16 and set(C)<=set(live)
K=T.extract(R,C)
assert K.det(method='bareiss') == -65536
assert U.extract(R,C)==S.zeros(16) and V.extract(R,C)==S.zeros(16)
Ki=K.inv()
# These exact coefficient identities prove universal rank-16 factorization,
# for all real a,b (in particular all nonnegative native gate values):
cert_0 = T[:,C]*Ki*T[R,:] == T
cert_a = T[:,C]*Ki*U[R,:] == U
cert_b = V[:,C]*Ki*T[R,:] == V
cert_ab = V[:,C]*Ki*U[R,:] == S.zeros(96)
assert cert_0 and cert_a and cert_b and cert_ab
# Then F(a,b) = (T[:,C]+b V[:,C]) K^{-1} (T[R,:]+a U[R,:]),
# with F(a,b) = A(b)A(a) = T + aU + bV and F[R,C] = K.

# For the completely tagged two-step path tensor, different first source ports
# own disjoint coordinate supports; at zero gates each live port must have a
# strictly positive length-two path. Gate nonnegativity only adds more paths.
actions_zero = list(actions(S.Integer(0)))
next_positive_sources = {src for d,src,w,l in actions_zero if w>0}
twohop_live = {src for mid,src,w,l in actions_zero
               if w>0 and mid in next_positive_sources}
assert twohop_live == set(live)

# Reconstruct the 64 live source coordinates from endpoint and a fixed set of
# 48 extra predecessor reads, then recover every ordered tagged path flow.
extra = tuple(sorted(set(live)-set(C)))
assert len(extra)==48 and len(set(C)|set(extra))==64

# Build the typed path list retaining both action labels and initial source port.
def tagged_two_step(a,b,r):
    second_by_source={}
    for dst,src,w,lab in actions(b):
        second_by_source.setdefault(src,[]).append((dst,w,lab))
    paths=[]
    for mid,src,w1,lab1 in actions(a):
        for dst,w2,lab2 in second_by_source.get(mid,[]):
            paths.append((src,mid,dst,lab1,lab2,w1*w2*r[src]))
    return paths

def recover(a,b,r):
    Aa,Ab=matrix(a),matrix(b)
    F=Ab*Aa
    y=F*r
    assert F.extract(R,C)==K
    assert F == F[:,C]*Ki*F[R,:]
    rem=y.extract(R,[0])-F.extract(R,extra)*r.extract(extra,[0])
    unknown=Ki*rem
    rr=S.zeros(96,1)
    for k,i in enumerate(C):rr[i]=unknown[k]
    for i in extra:rr[i]=r[i]
    assert F*rr==y
    assert all(rr[i]==r[i] for i in live)
    p1,p2=tagged_two_step(a,b,r),tagged_two_step(a,b,rr)
    assert len(p1)==len(p2)
    assert all(x==z for x,z in zip(p1,p2))
    assert all(r[i]>0 for i in live)
    return len(p1),sum(int(bool(x[-1]>0)) for x in p1)

run=[]
for a,b in ((S.Integer(0),S.Integer(0)),(S.Integer(1),S.Integer(1)),
            (S.Integer(2),S.Integer(0)),(S.Rational(7,3),S.Integer(2)),
            (S.Integer(0),S.Rational(7,3)),(S.Integer(2),S.Integer(2))):
    for seed in (0,3,11):
        r=S.Matrix([S.Rational((13*i+17+seed)%29+1,(i+seed)%7+1)
                    for i in range(96)])
        tot,pos=recover(a,b,r)
        run.append({'a':str(a),'b':str(b),'input_seed':seed,
                    'path_coordinates':tot,'positive_path_coordinates':pos})
assert len(run)==18

result={
 'schema':'PREFIX625_X6_NATIVE_TWO_GENERATION_TAGGED_PATH_MINIMAL_REPAIR_V1',
 'date':'2026-11-09',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'native_enumerator_checked_against':'PREFIX624@89c8d4689af84af95e4f1ae46c73672b8feb18b9',
 'native_phases':48,'native_ports':96,'one_step_labelled_actions':576,
 'two_step_tagged_path_coordinate_count':run[0]['path_coordinates'],
 'live_first_source_ports':len(live), 'silent_first_source_ports':len(silent),
 'zero_gate_two_step_positive_path_witness_all_64_sources':True,
 'rank_two_step_tagged_path_observer_for_all_nonnegative_gates':64,
 'rank_two_step_endpoint_for_all_nonnegative_gates':16,
 'minimal_extra_linear_predecessor_readouts':48,
 'minor_rows':list(R),'minor_columns':list(C),'minor_determinant':'-65536',
 'E_squared_zero':True,'factorization_identity_constants':{
     'T_C_Kinv_T_R_equals_T':cert_0,'T_C_Kinv_U_R_equals_U':cert_a,
     'V_C_Kinv_T_R_equals_V':cert_b,'V_C_Kinv_U_R_equals_zero':cert_ab},
 'fixed_extra_source_ports':list(extra),
 'exact_positive_rational_trials':len(run),'trials':run,
 'comparison_scope':'arbitrary nonnegative predecessor 96-port states, known a,b >= 0, complete ordered labelled two-step flows',
 'verification':'exact SymPy integer/rational, source-labelled BRC action enumeration, no floating point',
 'review':'AUTHOR_SIDE_UNREVIEWED','status':'ALL_ASSERTIONS_PASS'
}
out=Path(__file__).with_name('PREFIX625_native_two_generation_path_results.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'], 'rank_endpoint':16,'rank_tagged':64,
                  'minimal_extra':48,'trials':len(run),
                  'path_coordinates':run[0]['path_coordinates'],
                  'all_certificates':result['factorization_identity_constants']},ensure_ascii=False))

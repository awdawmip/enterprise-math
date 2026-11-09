#!/usr/bin/env python3
"""PREFIX-618: exact four-sensor native 48-phase endpoint reconstruction.
Scientific carrier: typed native X6 STAR positive branch-sum Q(g);
frozen input f42f2906d77f24085c123f3ccfe9667d41caa96d.
Uses exact SymPy integer/rational arithmetic (no classical propagator).
"""
import json
import random
from pathlib import Path
import sympy as S

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
P=tuple((a,p,sgn*c) for a in range(4) for c in STAR[a] for sgn in (-1,1) for p in near(a,sgn*c))
index={v:i for i,v in enumerate(P)}
def next_branch(i):
    a,p,c=P[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
    return [index[k] for k in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
N=[next_branch(i) for i in range(48)]
gate_index=index[(0,1,-3)]
assert len(P)==48 and gate_index==4

def Q(g):
    M=S.zeros(48)
    for i,ns in enumerate(N):
        if abs(P[i][2]) in (5,6): continue
        for j in ns:
            M[i,j]=1 if i==gate_index else (g+3 if j==gate_index else 2)
    return M

HC=S.zeros(48,4)
for j,rows in enumerate(((2,3,15),(5,28,29),(27,38,39),(16,17,41))):
    for i in rows: HC[i,j]=1
HB=S.zeros(48,4)
for j,rows in enumerate(({3:1,14:1,15:1},{17:2,40:2,41:2},{26:4,27:4,39:4},{4:4,5:8,29:8})):
    for i,a in rows.items(): HB[i,j]=a
H=HC.row_join(HB)
C=2*S.Matrix([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
def B(g):
    return S.Matrix([[0,0,0,4*(g+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
def M8(g): return S.diag(C,B(g))

g=S.symbols('g')
assert Q(g)*H==H*M8(g)
assert H.rank()==8
sensor_rows=(14,40,26,4)
sensor_scales=(1,2,4,4)
assert HB[list(sensor_rows),:]==S.diag(*sensor_scales)
assert HC[list(sensor_rows),:]==S.zeros(4,4)

def endpoint_reconstruct(a,b,lam,gate_word):
    t=len(gate_word)
    c0=S.Matrix([0,0,4,4])*lam
    w0=S.Matrix([b+3,a+3,1,S.Rational(1,2)])*lam
    baseline=HC*(C**t*c0)
    products=[S.Integer(1)]*4
    for s,q in enumerate(gate_word, start=1):
        assert q>=0
        products[s%4]*=4*(q+3)
    w=S.Matrix([w0[(j-t)%4]*products[(t-j)%4] for j in range(4)])
    observations=S.Matrix([sensor_scales[j]*w[j] for j in range(4)])
    return baseline+HB*w,observations,tuple(products),baseline

d=S.zeros(48,1)
for i in (4,11,14,32): d[i]=1
rng=random.Random(618)
records=[]
comparisons=0
for t in range(0,21):
    for repeat in range(4):
        a=S.Rational(rng.randint(0,9),rng.randint(1,5))
        b=S.Rational(rng.randint(0,9),rng.randint(1,5))
        lam=S.Rational(rng.randint(1,8),rng.randint(1,5))
        word=tuple(S.Rational(rng.randint(0,12),rng.randint(1,7)) for _ in range(t))
        y,obs,products,_=endpoint_reconstruct(a,b,lam,word)
        x=lam*Q(b)*Q(a)*d
        for q in word:x=Q(q)*x
        assert y==x
        for j in range(4): assert x[sensor_rows[j]]==obs[j]
        comparisons+=52
        if repeat==0 and t in (0,1,2,3,4,8,20):
            records.append({'length':t,'input_gates':[str(a),str(b)],'scale':str(lam),'products':list(map(str,products)),'sensor_values':list(map(str,obs))})

q=S.symbols('q1:5', nonnegative=True)
_,obs,_,_=endpoint_reconstruct(S.Integer(1),S.Integer(2),S.Integer(1),q)
J=obs.jacobian(S.Matrix(q))
det=S.factor(J.det())
assert det==81920 and J.rank()==4

words=[S.Integer(v) for v in (0,2,1,5,3,4,7,6)]
same=words[:];same[0],same[4]=same[4],same[0]
y0,s0,p0,_=endpoint_reconstruct(1,2,1,words)
y1,s1,p1,_=endpoint_reconstruct(1,2,1,same)
assert p0==p1 and s0==s1 and y0==y1
cross=words[:];cross[0],cross[1]=cross[1],cross[0]
y2,s2,p2,_=endpoint_reconstruct(1,2,1,cross)
assert p0!=p2 and s0!=s2 and y0!=y2

# Explicit omitted-sensor witness from Theorem 618.2.
_,sa,_,_=endpoint_reconstruct(1,1,1,[1,1,1,1])
_,sb,_,_=endpoint_reconstruct(1,1,1,[2,1,1,1])
assert list(sa)==[64,128,64,32]
assert list(sb)==[64,128,64,40]

summary={
 'record':'PREFIX-618',
 'scientific_input_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'cases':84,'exact_output_and_sensor_component_assertions':comparisons,
 'native_phase_count':48,'sensor_phase_indices_zero_based':list(sensor_rows),
 'sensor_scaling':list(sensor_scales),'symbolic_intertwiner':'verified',
 'full_rank_H':8,'symbolic_jacobian_rank_n4':4,
 'symbolic_jacobian_determinant_n4':str(det),
 'collision_same_class':'verified','separation_cross_class':'verified',
 'explicit_three_sensor_witness':'(64,128,64,32) versus (64,128,64,40)',
 'sample_records':records,
 'scope':'fixed known a,b,lambda; four-point d; native positive-branch-sum 48-phase; arbitrary nonnegative word and same-length terminal observation',
 'proof_status':'AUTHOR_SIDE_SYMBOLIC_AND_EXACT; INDEPENDENT_DRIVER_REVIEW_PENDING'
}
output=Path(__file__).with_name('PREFIX618_native_BRC_four_sensor_results.json')
output.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='sample_records'},indent=2))

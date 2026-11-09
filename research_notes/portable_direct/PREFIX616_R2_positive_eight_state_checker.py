#!/usr/bin/env python3
"""Exact native STAR/BRC one-sensor 8-state positive realization checker.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
PREFIX-614 and PREFIX-615 are author-side dependencies; this checker reconstructs Q.
"""
import json
from pathlib import Path
import sympy as sp

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
P=tuple((a,p,sgn*c) for a in range(4) for c in STAR[a] for sgn in(-1,1) for p in near(a,sgn*c))
I={p:i for i,p in enumerate(P)}
def nxt(i):
    a,p,c=P[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
    return [I[k] for k in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
N=[nxt(i) for i in range(48)]; gate_index=I[(0,1,-3)]
assert len(P)==48 and gate_index==4

def Q(g):
    M=sp.zeros(48)
    for i, ns in enumerate(N):
        if abs(P[i][2]) in (5,6):continue
        for j in ns:M[i,j]=1 if i==gate_index else (g+3 if j==gate_index else 2)
    return M

A=Q(sp.Integer(0)); D=Q(sp.Integer(1))-A
d=sp.zeros(48,1)
for i in (4,11,14,32): d[i]=1
E=sp.Matrix.hstack(A*A*d,D*A*d,A*D*d,A**3*d,A*A*D*d,A**4*d,A**3*D*d)
rows=[2,3,4,5,16,17,26]
K=E[rows,:].inv()*sp.eye(48)[rows,:]
T0=K*A*E; T1=K*D*E
h=sp.eye(48)[3,:]
observ=sp.Matrix.vstack(*[h*E*M for M in (sp.eye(7),T0,T1,T0*T0,T1*T0,T0**3,T1*T0*T0)])
assert E.rank()==7 and E[rows,:].det()==-16384 and observ.det()==-2097152
assert A*E==E*T0 and D*E==E*T1

S=sp.Matrix([
[sp.Rational(1,2),sp.Rational(1,2),-1,0,0,0,0],
[-3,0,0,1,0,0,0],
[sp.Rational(-9,4),sp.Rational(-3,4),sp.Rational(3,2),0,1,0,0],
[0,0,1,0,0,0,0],
[sp.Rational(-7,8),sp.Rational(-1,8),sp.Rational(-5,4),0,0,1,0],
[sp.Rational(1,8),sp.Rational(-1,8),sp.Rational(-1,4),0,0,0,0],
[sp.Rational(-5,8),sp.Rational(1,8),sp.Rational(1,4),0,0,0,1]
])
g=sp.symbols('g')
B=lambda g:sp.Matrix([[0,0,0,4*(g+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
R=sp.Matrix([[0,-4],[1,0]])
assert sp.simplify(S.inv()*(T0+g*T1)*S-sp.diag(sp.Matrix([[2]]),R,B(g)))==sp.zeros(7)
assert sp.trace((T0+g*T1)**2)==-4
assert sp.trace(A*A)>=0

# The extra nonnegative 4-cycle restores the absent -2 eigenmode.
C=2*sp.Matrix([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
H=sp.Matrix([[1,0,0,0,1,0,0,0]])
base=sp.Matrix([0,0,4,4])
assert C**4==16*sp.eye(4)
assert [int((sp.eye(4)[0,:]*C**t*base)[0]) for t in range(8)]==[0,8,16,0,0,128,256,0]
assert all(C[i,j]>=0 for i in range(4) for j in range(4))
assert all(B(sp.Integer(0))[i,j]>=0 for i in range(4) for j in range(4))

words=[
[0,1,2,3,4,0,1,7,3,2,0,9],
[sp.Rational(1,2),2,sp.Rational(7,3),0,5,sp.Rational(13,7),1,0,3,6],
[1,1,1,1,1,1,1,1,1,1,1,1],
]
initials=[(0,0),(1,2),(sp.Rational(2,3),sp.Rational(9,7)),(5,0)]
scales=[sp.Integer(1),sp.Rational(2,3),sp.Rational(7,5)]
checks=0; phase_checks=0; comparisons=[]
for a,b in initials:
    for word in words:
        for lam in scales:
            x=Q(b)*Q(a)*(lam*d)
            y=lam*sp.Matrix.vstack(base,sp.Matrix([3+b,3+a,1,sp.Rational(1,2)]))
            c=lam*sp.Matrix([1,b,a,0,0,0,0])
            for t,gate in enumerate([None]+word):
                if t:
                    x=Q(sp.sympify(gate))*x
                    y=sp.diag(C,B(sp.sympify(gate)))*y
                    c=(T0+sp.sympify(gate)*T1)*c
                assert (h*x)[0]==(H*y)[0],(a,b,word,t,lam)
                assert E*c==x
                assert all(v>=0 for v in y)
                checks+=1;phase_checks+=48
            comparisons.append((str(a),str(b),len(word),str(lam)))

out={
'schema':'PREFIX616_R2_POSITIVE_REALIZATION_V1',
'freeze_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'observer':'native phase index 3 sum after two gates',
'probe_support':[4,11,14,32],
'exact_minimal_signed_linear_dimension':7,
'positive_linear_dimension_lower_bound':8,
'positive_linear_dimension_constructed':8,
'positive_minimal_dimension':8,
'negative_trace_square_7dim':str(sp.trace(T0*T0)),
'positive_8d_trace_square_at_zero':str(sp.trace(sp.diag(C,B(0))**2)),
'cyclic_baseline_initial':['0','0','4','4'],
'positive_w_initial':['3+b','3+a','1','1/2'],
'original_phase3_scalar_equalities_checked':checks,
'original_48_phase_coordinate_equalities_checked':phase_checks,
'cases':len(comparisons),
'input_gates_per_case':[len(x) for x in words],
'result':'ALL_EXACT_ASSERTIONS_PASSED; AUTHOR_SIDE_PROOF; INDEPENDENT_REVIEW_PENDING'
}
Path(__file__).with_name('PREFIX616_R2_positive_eight_state_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

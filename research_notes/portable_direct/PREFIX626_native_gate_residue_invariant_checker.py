#!/usr/bin/env python3
"""PREFIX-626: gate-residue factorization of original X6-BRC 96-port operators.
Immutable science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
Native STAR 48 phases, 96 ports, 576 tagged actions, weights (1,1,1,1,0,0).
Exact SymPy integer/rational arithmetic. No ordinary propagator used.
"""
import json
from itertools import product
from pathlib import Path
import sympy as S

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a]
        for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c=P[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in
        ([(a,c,k) for k in near(a,c) if k!=p]
        +[(b,c,k) for k in near(b,c)]))
N=tuple(neighbors(i) for i in range(48))
G=IX[(0,1,-3)]
AXIS=tuple(abs(c)-1 for a,p,c in P)
WEIGHTS=(1,1,1,1,0,0)
assert G==4 and len(P)==48 and sum(map(len,N))==144

def actions(z):
    for i in range(48):
        for j in N[i]:
            for p,q in product((0,1),repeat=2):
                yield (2*i+p,2*j+q,
                       z if j==G and p==q==1 else WEIGHTS[AXIS[i]],
                       (i,j,p,q))

def matrix(z):
    a=S.zeros(96)
    for dst,src,wt,_ in actions(z):
        a[dst,src]+=wt
    return a

A0=matrix(S.Integer(0))
E=matrix(S.Integer(1))-A0
nz=[(i,j) for i in range(96) for j in range(96) if E[i,j]!=0]
assert nz==[(7,9),(29,9),(31,9)] and all(E[i,j]==1 for i,j in nz)
u=E[:,9]
v=S.zeros(1,96); v[0,9]=1
assert E==u*v and E*E==S.zeros(96)

# One finite native certificate proves the four-step column and row recurrence.
u_p=[u]
v_p=[v]
for _ in range(18):
    u_p.append(A0*u_p[-1]); v_p.append(v_p[-1]*A0)
assert u_p[5]==12*u_p[1]
assert v_p[5]==12*v_p[1]
assert [(v*u_p[k])[0] for k in range(5)]==[0,0,0,4,0]
assert all((v*u_p[k])[0] == (0 if (k%4)!=3 else 4*12**((k-3)//4))
           for k in range(18))
U_supp={k:{i for i in range(96) if u_p[k][i]!=0} for k in range(1,5)}
V_supp={k:{i for i in range(96) if v_p[k][i]!=0} for k in range(1,5)}
assert all(len(U_supp[k])==len(V_supp[k])==6 for k in range(1,5))
assert all(U_supp[i].isdisjoint(U_supp[j]) and V_supp[i].isdisjoint(V_supp[j])
           for i in range(1,5) for j in range(i+1,5))

def actual_product(gates):
    F=S.eye(96)
    for g in gates:
        F=(A0+g*E)*F
    return F

def closed_form(gates):
    n=len(gates)
    assert 2<=n<=18
    P_r={r:S.Integer(1) for r in range(4)}
    B={r:None for r in range(4)}
    for j in range(2,n):
        r=j%4
        P_r[r]*=(1+S.Rational(1,3)*gates[j-1])
        Bj=u_p[n-j]*v_p[j-1]
        if B[r] is None:B[r]=Bj
        else: assert B[r]==Bj
    F=A0**n
    for r in range(4):
        if B[r] is not None:
            F += 3*(P_r[r]-1)*B[r]
    F += gates[0]*P_r[1]*(u_p[n-1]*v)
    F += gates[-1]*P_r[n%4]*(u*v_p[n-1])
    if n>=5 and n%4==1:
        F += gates[0]*gates[-1]*P_r[1]*(4*12**((n-5)//4))*E
    return F,P_r,B

# Exact full-matrix tests, including both boundary gates and rational values.
checks=[]
for n in (2,3,4,5,6,7,8,9,10,13,17):
    patterns=[
      [S.Rational((i*5+3)%11,3) for i in range(n)],
      [S.Integer(0) if i%3 else S.Rational(7,3) for i in range(n)],
    ]
    for t,g in enumerate(patterns):
        act=actual_product(g)
        pred,pval,b=closed_form(g)
        assert act==pred, (n,t)
        supports=[{k for k in range(96**2) if bb[k]!=0} for bb in b.values() if bb is not None]
        assert all(s.isdisjoint(t) for i,s in enumerate(supports) for t in supports[i+1:])
        checks.append({'n':n,'pattern':t,'exact_96_by_96':True,'present_internal_residues':len(supports),
                       'products':{str(k):str(v) for k,v in pval.items()}})

# Explicit exact fiber collision: swap two gates four steps apart, fixed boundaries.
n=10
A=[S.Integer(0)]*n
B=[S.Integer(0)]*n
A[1]=S.Integer(1);A[5]=S.Integer(2)
B[1]=S.Integer(2);B[5]=S.Integer(1)
Fa=actual_product(A)
Fb=actual_product(B)
assert Fa==Fb
_,pa,bs=closed_form(A)
_,pb,_=closed_form(B)
assert pa==pb and pa[2]==S.Rational(20,9)

# Exact source/ordered-action path witness that distinguishes the same pair.
pre=next((dst,src,wt,label) for dst,src,wt,label in actions(S.Integer(0))
         if dst==9 and src==22 and wt==1)
gate=next((dst,src,wt,label) for dst,src,wt,label in actions(S.Integer(1))
          if src==9 and dst==29 and label[1]==G and label[2]==label[3]==1)
path=[pre,gate]
cur=gate[0]
live={src for dst,src,wt,label in actions(0) if wt>0}
while len(path)<n:
    next_step=next((dst,src,wt,label) for dst,src,wt,label in actions(0)
                   if src==cur and wt==1 and dst in live)
    path.append(next_step)
    cur=next_step[0]
assert len(path)==n and all(path[k][0]==path[k+1][1] for k in range(n-1))
def path_weight(gates):
    out=S.Integer(1)
    for t,(_,_,_,(i,j,p,q)) in enumerate(path):
        wt = gates[t] if j==G and p==q==1 else WEIGHTS[AXIS[i]]
        out*=wt
    return out
assert path_weight(A)==1 and path_weight(B)==2

# Exact, nontrivial four-parameter completeness with boundaries zero.
_,_,b6=closed_form([S.Integer(0)]*6)
assert len([x for x in b6.values() if x is not None])==4
assert all(sum(x!=0 for x in bb)==36 for bb in b6.values())

result={
 'schema':'PREFIX626_ORIGINAL_NATIVE_X6_GATE_RESIDUE_OPERATOR_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'native_actions':576,'native_ports':96,'gate_rank_one_positions':nz,
 'exact_krylov_vector_recurrences':{'A0^5 u = 12 A0 u':True,'v A0^5 = 12 v A0':True},
 'scalar_feedback':'v A0^k u = 4*12^((k-3)/4) if k>=3 and k mod 4=3; otherwise 0',
 'operator_formula':'A0^n + 3 sum_r(P_r-1) B_(n,r) + g1 P_1 A0^(n-1) E + gn P_(n mod4) E A0^(n-1) + indicator(n>=5 and n mod4==1) *g1*gn*P_1*4*12^((n-5)/4)*E',
 'P_r':'product_(2<=j<=n-1, j mod4=r) (1+gj/3)',
 'B_r':'A0^(n-j) E A0^(j-1) for any interior j of residue r',
 'universal_proof':'finite exact native Krylov recurrences plus rank-one expansion',
 'fully_checked_96x96_rational_products':checks,
 'check_count':len(checks),
 'four_disjoint_internal_matrix_supports_at_n6':True,
 'fiber_collision':{'n':n,'gates_A':[str(x) for x in A],
  'gates_B':[str(x) for x in B], 'endpoint_operators_equal':True,
  'residue2_product':str(pa[2]),'path_A_weight':str(path_weight(A)),
  'path_B_weight':str(path_weight(B)),
  'tagged_path': [{'src':src,'dst':dst,'label':list(label)} for dst,src,wt,label in path]},
 'arithmetic':'original source-labelled positive native BRC, exact SymPy integers/rationals',
 'status':'ALL_ASSERTIONS_PASS','review':'AUTHOR_SIDE_UNREVIEWED'
}
pathout=Path(__file__).with_name('PREFIX626_native_gate_residue_invariant_results.json')
pathout.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'full_matrix_trials':len(checks),
 'n_max':max(c['n'] for c in checks), 'collision':result['fiber_collision']['endpoint_operators_equal'],
 'path_weights':[str(path_weight(A)),str(path_weight(B))]},ensure_ascii=False))

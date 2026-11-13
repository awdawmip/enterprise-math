#!/usr/bin/env python3
"""PREFIX-602: typed X6-BRC Q(0,z) mixed right-source certificate.
Frozen science awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scope: post-first-step 48-phase tail, not arbitrary original 96-port initializations.
"""
import json
import math
from collections import Counter
from pathlib import Path
import sympy as sp

STAR = ((1, 3, 6), (1, 4, 5), (2, 3, 5), (2, 4, 6))
def near(a, c):
    return tuple(-k if c > 0 else k for k in STAR[a] if k != abs(c))
PHASES = tuple((a, p, sign*k) for a in range(4)
               for k in STAR[a] for sign in (-1, 1)
               for p in near(a, sign*k))
INDEX = {v:i for i, v in enumerate(PHASES)}
def successors(i):
    a, p, c = PHASES[i]
    b = next(k for k in range(4) if k != a and abs(c) in STAR[k])
    return tuple(INDEX[v] for v in ([(a, c, q) for q in near(a,c) if q != p]
                                     + [(b, c, q) for q in near(b,c)]))
N = tuple(successors(i) for i in range(48))
G = INDEX[(0,1,-3)]
assert len(PHASES) == 48 and G == 4 and all(len(n)==3 for n in N)
z, t = sp.symbols('z t')
s = 4*z + 12
Q = sp.zeros(48)
for i, ns in enumerate(N):
    if abs(PHASES[i][2]) > 4:
        continue
    for j in ns:
        Q[i,j] = 1 if i==G else (3+z if j==G else 2)

def minimal_witness(pair, proposed, degree, at_z1, z1_poly):
    v = sp.zeros(48,1)
    for j in pair:
        v[j] += 1
    vs = [v]
    for k in range(degree):
        vs.append(Q*vs[-1])
    poly = sp.Poly(proposed,t)
    residual = sp.zeros(48,1)
    for (k,), c in poly.terms():
        residual += c*vs[k]
    assert all(sp.expand(x)==0 for x in residual), pair
    K = sp.Matrix.hstack(*vs[:degree])
    rows = list(K.subs(z,2).T.rref()[1])
    assert len(rows)==degree
    minor = sp.factor(K.extract(rows,range(degree)).det())
    assert sp.expand(minor.subs(z,2)) != 0
    rank_z1 = sp.Matrix.hstack(*vs[:degree]).subs(z,1).rank()
    assert rank_z1 == at_z1, (pair,rank_z1,at_z1)
    special = sp.Poly(z1_poly, t)
    res1 = sp.zeros(48,1)
    for (k,),c in special.terms():
        res1 += c*vs[k].subs(z,1)
    assert all(x==0 for x in res1)
    assert special.degree() == rank_z1
    return dict(pair=list(pair), polynomial=str(sp.factor(proposed)),
                degree_nonunit=degree, minor_rows=rows,
                lower_minor=str(minor), degree_at_z1=rank_z1,
                polynomial_at_z1=str(sp.factor(z1_poly)))

WITNESSES = [
    minimal_witness((0,36), t*(t*t-4), 3, 3, t*(t*t-4)),
    minimal_witness((0,18), t*(t-2)*(t*t+4), 4, 4, t*(t-2)*(t*t+4)),
    minimal_witness((0,4), t*(t**4-16)*(t**4-s), 9, 5, t*(t**4-16)),
    minimal_witness((8,11), t*t*(t-2)*(t*t+4)*(t**4-s), 9, 5,
                    t*t*(t-2)*(t*t+4)),
]
assert WITNESSES[2]['lower_minor']=='8388608*(z - 1)**4*(z + 3)**4'
assert WITNESSES[3]['lower_minor']=='-4194304*(z - 1)**4*(z + 3)*(z**2 + 10*z + 37)'
assert WITNESSES[0]['lower_minor']=='-8'
assert WITNESSES[1]['lower_minor']=='64'

# Complete 1128 unordered equal-weight two-phase inputs at each fixed gate.
# Fraction-free integer elimination with exact gcd rescaling computes rank over Q.
def exact_rank_columns(columns):
    basis=[]
    for column in columns:
        v=list(column)
        for pivot,b in basis:
            a=v[pivot]
            if a==0:continue
            d=b[pivot]
            v=[d*x-a*y for x,y in zip(v,b)]
            g=math.gcd(*v)
            if g>1:v=[x//g for x in v]
        pivot=next((i for i,x in enumerate(v) if x),None)
        if pivot is not None:
            basis.append((pivot,v))
            basis.sort(key=lambda a:a[0])
    return len(basis)

def census(zvalue):
    A_sym = Q.subs(z,zvalue)
    if zvalue==1:
        assert A_sym**6 == 16*A_sym**2
    else:
        svalue=4*zvalue+12
        assert A_sym**10 -(svalue+16)*A_sym**6 +16*svalue*A_sym**2 == sp.zeros(48)
    A=[[int(Q[i,j].subs(z,zvalue)) for j in range(48)] for i in range(48)]
    n=6 if zvalue==1 else 10
    roots=[]
    for j in range(48):
        v=[int(i==j) for i in range(48)];powers=[]
        for k in range(n):
            powers.append(v)
            v=[sum(A[i][q]*v[q] for q in N[i] if A[i][q]) for i in range(48)]
        roots.append(powers)
    tally=Counter(); examples={}; total=0
    for i in range(48):
        for j in range(i+1,48):
            K=[[roots[i][k][q]+roots[j][k][q] for q in range(48)]
               for k in range(n)]
            d=exact_rank_columns(K)
            tally[d]+=1; examples.setdefault(d,[i,j]);total+=1
    assert total==1128
    return dict(z=zvalue, total=total,
                degree_counts={str(k):tally[k] for k in sorted(tally)},
                witness_pair_for_degree={str(k):examples[k] for k in sorted(examples)})

CENSUS=[census(1),census(2)]
assert CENSUS[0]['degree_counts']=={'1':120,'3':7,'4':30,'5':387,'6':584}
assert CENSUS[1]['degree_counts']=={'1':120,'3':6,'4':20,'5':326,'6':228,'8':16,'9':80,'10':332}
result={
  'schema':'PREFIX602_R2_EXACT_NATIVE_BRC_MIXED_SOURCE',
  'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'observer_scope':'48-dimensional post-first-step phase right-source; entire 48-phase state',
  'axis_weights':[1,1,1,1,0,0],
  'parameter_domain':'nonnegative real gate z; witness rank at z=1 and all z>=0 except z=1',
  'symbolic_witnesses':WITNESSES,
  'complete_fixed_integer_gate_pair_census':CENSUS,
  'exact_arithmetic':'SymPy Z[z] annihilator and minors; integer fraction-free rational rank',
  'status':'AUTHOR_SIDE_EXACT_CHECK; INDEPENDENT_REVIEW_PENDING',
}
path=Path(__file__).with_name('PREFIX602_R2_mixed_source_exact_results.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PREFIX-602 CHECKS PASS; 4 symbolic witnesses; 1128 pair ranks each at z=1,2')
for w in WITNESSES:print(w['pair'],w['polynomial'],'minor',w['lower_minor'])
for c in CENSUS:print('z=',c['z'],c['degree_counts'])

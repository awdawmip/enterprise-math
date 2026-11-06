#!/usr/bin/env python3
"""PREFIX-532 exact fixed-origin gate-only BRC-path observer certificate (Python 3 / SymPy)."""
import json
from collections import Counter, defaultdict
from sympy import Matrix, Poly, symbols, expand, gcd

STARS = ((1, 3, 6), (1, 4, 5), (2, 3, 5), (2, 4, 6))
def near(j, c):
    return tuple((-1 if c > 0 else 1) * a for a in STARS[j] if a != abs(c))

phases = [(j, p, sign*a) for j in range(4)
          for a in STARS[j] for sign in (-1, 1)
          for p in near(j, sign*a)]
lookup = {ph:i for i,ph in enumerate(phases)}
assert len(phases)==len(lookup)==48
edges = []
for j,p,c in phases:
    other = next(i for i in range(4) if i != j and abs(c) in STARS[i])
    destinations = [(j,c,v) for v in near(j,c) if v != p]
    destinations += [(other,c,v) for v in near(other,c)]
    edges.append(tuple(lookup[v] for v in destinations))
assert all(len(x)==3 for x in edges)
T = lookup[(0,1,-3)]
A = Matrix.zeros(48)
for s, successors in enumerate(edges):
    for r in successors: A[r,s] += 1
assert all(sum(A[:,s])==3 for s in range(48))
assert all(sum(A[r,:])==3 for r in range(48))

rows = []
row = [int(i==T) for i in range(48)]
for d in range(30):
    rows.append(row)
    row = [sum(row[r] for r in edges[s]) for s in range(48)]
rec = (5,26,78,135,-243)
assert rows[10] == [5*rows[8][s]+26*rows[6][s]+78*rows[4][s]+135*rows[2][s]-243*rows[0][s] for s in range(48)]
assert all(rows[d][s] == sum(rec[k]*rows[d-2*(k+1)][s] for k in range(5)) for d in range(10,30) for s in range(48))

minor_columns = (0,1,2,3,4,5,6,7,9,14)
minor = int(Matrix([[rows[d][s] for s in minor_columns] for d in range(10)]).det())
assert minor == -120932352

t,z = symbols('t z')
Q = expand(1-5*(2*t)**2-26*(2*t)**4-78*(2*t)**6-135*(2*t)**8+243*(2*t)**10)
qcoeff=[Poly(Q,t).nth(k) for k in range(11)]
C=[]
for s in range(48):
    c=[sum(qcoeff[j]*2**(k-j)*rows[k-j][s] for j in range(k+1)) for k in range(10)]
    C.append(expand(sum(c[k]*t**k for k in range(10))))
D = expand(((z+3)*Q-(z-1)*C[T])/4)
expected_D = 1-20*t**2-(396+20*z)*t**4-(4944+48*z)*t**6-(32832+1728*z)*t**8+(186624+62208*z)*t**10
assert expand(D-expected_D)==0

num=[]
for s in range(48):
    n0,n1=rows[0][s],rows[1][s]
    raw=expand(4*D+(z-1)*(C[s]-(n0+2*t*n1)*Q))
    quotient,rem=Poly(raw,t,z).div(Poly(4*(1-6*t),t,z))
    assert rem.is_zero
    n=quotient.as_expr()
    assert Poly(n,t).degree() <= 10
    assert gcd(Poly(n.subs(z,0),t),Poly(D.subs(z,0),t)).degree()==0
    num.append(n)

classes=defaultdict(list)
for s in range(48): classes[tuple(rows[k][s] for k in range(2,12))].append(s)
assert len(classes)==18 and len(set(map(str,num)))==18
class_hist=Counter(map(len,classes.values()))
assert class_hist==Counter({1:6,2:5,4:6,8:1})

MAXD=14
six=[6**d for d in range(MAXD+1)]
R=[(2**(d-2)*rows[d][T] if d>=2 else 0) for d in range(MAXD+1)]
assert R[4]==20 and R[6]==448 and R[8]==19008
comparisons=0
sample=[]
for origin in range(48):
    U=[(2**(d-2)*rows[d][origin] if d>=2 else 0) for d in range(MAXD+1)]
    F=[[six[d] for d in range(MAXD+1)]]
    F.append([sum(U[j]*six[d-j] for j in range(d+1)) for d in range(MAXD+1)])
    for k in range(2,5):
        prev=F[-1]
        F.append([sum(R[j]*prev[d-j] for j in range(d+1)) for d in range(MAXD+1)])
    dp={(origin,0,0):1}
    for d in range(MAXD+1):
        hist=defaultdict(int)
        for (_,_,h),v in dp.items():hist[h]+=v
        assert sum(hist.values())==six[d]
        for k in range(5):
            count=sum(v*__import__('math').comb(h,k) for h,v in hist.items() if h>=k)
            assert count==F[k][d], (origin,d,k,count,F[k][d])
            comparisons+=1
        if d in (2,6) and origin in (4,9):sample.append({'origin':list(phases[origin]),'d':d,'hist':dict(sorted(hist.items()))})
        nd=defaultdict(int)
        for (s,last_inner,h),v in dp.items():
            for r in edges[s]:
                for inner in (0,1):
                    hit=int(last_inner==1 and inner==1 and r==T)
                    nd[(r,inner,h+hit)]+=v
        dp=nd

assert sum(rows[2])==9
result={
 'verdict':'ALL_CHECKS_PASS','research_line':'PREFIX-532',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':{'states':48,'star_sets':[list(s) for s in STARS],'gate_target_phase':list(phases[T]),'macro_successors_per_phase':3,'branch_options_per_edge':2},
 'theorems':{'target_backward_Krylov_rank':10,'row_recurrence_coefficients_even_lags':list(rec),'rooted_gate_law_classes':18,'fixed_origin_gate_only_generic_minimum_order':10,'fixed_origin_avoidance_minimum_order':10},
 'exact_linear_algebra':{'minor_columns':list(minor_columns),'minor_determinant':minor,'row10_identity':'PASS','symbolic_D_identity':'PASS','all_48_root_divisions':'PASS','all_48_specialized_rational_gcd':'PASS'},
 'root_class_sizes':dict(sorted((str(k),v) for k,v in class_hist.items())),
 'direct_DP':{'depth_max':MAXD,'origins':48,'moment_coefficients_compared':comparisons,'status':'PASS'},
 'sample':sample,
 'remaining':'Prove smaller fixed-origin joint BRC/H quotient or benchmark bounded polynomial-memory bit costs.'
}
print(json.dumps(result,ensure_ascii=False,indent=2))

#!/usr/bin/env python3
"""Exact physical-branch and corank-one vertex-star certificates for R5."""
from collections import Counter
import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
    from VERIFY_STAR_DEGREES import C,D,x,r,star
from sympy import Matrix,Rational
WITNESS_ARCS='''219346331/10192753200,7664319/135903376,2813871/16987922,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,393042/8493961,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,2500147/33975844,393042/8493961,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,7664319/135903376,451274777/3397584400'''
E0=Matrix([Rational(s) for s in WITNESS_ARCS.split(',')]);q=C*E0
assert C*x==q
assert len(D)==30 and C.rank()==15
assert all(v>0 for v in E0)
print('FIBER_RANK',C.rank(),'DIMENSION',30-C.rank())
for j in (1,3,5):
    delta=q[7+j]-q[j]
    assert delta>0
    lower=[i for i in range(7) if r[i]<r[j]]
    upper=[i for i in range(7) if r[i]>r[j]]
    a_min=min(r[j]-r[i] for i in lower)
    a_max=max(r[j]-r[i] for i in lower)
    b_min=min(r[i]-r[j] for i in upper)
    b_max=max(r[i]-r[j] for i in upper)
    lower_fraction=Rational(b_min)/(a_max+b_min)
    upper_fraction=Rational(a_min)/(a_min+b_max)
    assert lower_fraction>0 and upper_fraction>0
    L=Matrix([[1 if (a[1]==j and r[a[0]]<r[j]) else 0 for a in D]])
    U=Matrix([[1 if (a[1]==j and r[a[0]]>r[j]) else 0 for a in D]])
    O=L+U
    assert sum(E0[k]*(r[D[k][0]]-r[j]) for k in range(30) if D[k][1]==j)==0
    assert sum(E0[k] for k,a in enumerate(D) if a[1]==j)==q[7+j]
    assert sum(E0[k] for k,a in enumerate(D) if a[0]==j)==q[j]
    assert (L*E0)[0]>=lower_fraction*(O*E0)[0]
    assert (U*E0)[0]>=upper_fraction*(O*E0)[0]
    assert (O*E0)[0]>=delta
    print('SOURCE',j,'MASS_EXCESS',delta,'LOWER_FRACTION',lower_fraction,
          'UPPER_FRACTION',upper_fraction,'LOWER_MASS_BOUND',lower_fraction*delta,
          'UPPER_MASS_BOUND',upper_fraction*delta)

s=[k for k,v in enumerate(x) if v>0]
assert len(s)==14 and C[:,s].rank()==14
assert [D[k] for k in s if D[k][1]==2]==[(2,2)]
lambda_by_arc={D[k]:(r[D[k][0]]-r[2] if D[k][1]==2 else Rational(0)) for k in range(30)}
assert all(lambda_by_arc[D[k]]==0 for k in s)
zero_arcs=[D[k] for k,v in enumerate(x) if v==0 and lambda_by_arc[D[k]]==0]
negative_arcs=[D[k] for k,v in enumerate(x) if v==0 and lambda_by_arc[D[k]]<0]
positive_arcs=[D[k] for k,v in enumerate(x) if v==0 and lambda_by_arc[D[k]]>0]
assert len(zero_arcs)==10 and len(negative_arcs)==2 and len(positive_arcs)==4
assert len(zero_arcs)+len(negative_arcs)+len(positive_arcs)==16
sigma,nb=star(x)
assert sigma==(14,2,4,10) and len(nb)==10+2*4==18
count=Counter(len([a for a in y if a>0]) for y in nb)
assert count==Counter({14:10,15:8})
second_star=Counter()
for y in nb:
    signature,degree=star(y,False)
    second_star[(signature[0],degree)]+=1
assert second_star==Counter({(14,18):10,(15,15):8})
print('SOURCE2_LOCKED_SUPPORT14_STAR','ZERO',len(zero_arcs),'NEG',
      len(negative_arcs),'POS',len(positive_arcs),'DEGREE',len(nb))
print('CENTER_NEIGHBOR_SUPPORT',dict(sorted(count.items())))
print('FIRST_STAR_NEIGHBOR_DEGREES',dict(sorted(second_star.items())))
print('PASS_EXACT_BRANCH_AND_LOCKED_STAR')

"""R749SMB: exact delayed-history predictive-rank hierarchy over the R749SF conditional model.
Finite checks d=1..5; universal d theorem is proved separately, not by this loop.
All arithmetic is integer or fractions.Fraction; no numerical tolerances.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb, prod
import json

SIGNS=(-1,1)

def binary_basis(z):
    """In the first two slots match R749SM: W0=Z0 Z1, W1=Z0."""
    if len(z)==1: return z
    return (z[0]*z[1], z[0]) + tuple(z[2:])

def det(matrix):
    a=[[Q(v) for v in row] for row in matrix]
    n=len(a)
    assert all(len(row)==n)
    out=Q(1)
    for i in range(n):
        k=next((j for j in range(i,n) if a[j][i]),None)
        if k is None:return Q(0)
        if k!=i:a[k],a[i]=a[i],a[k];out=-out
        pivot=a[i][i];out*=pivot
        for j in range(i+1,n):
            c=a[j][i]/pivot
            for k in range(i,n):a[j][k]-=c*a[i][k]
    return out

def rank(matrix):
    if not matrix:return 0
    a=[[Q(v) for v in row] for row in matrix]
    n,m=len(a),len(a[0]);r=0
    for j in range(m):
        k=next((i for i in range(r,n) if a[i][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k];v=a[r][j]
        for jj in range(j,m):a[r][jj]/=v
        for i in range(r+1,n):
            c=a[i][j]
            for jj in range(j,m):a[i][jj]-=c*a[r][jj]
        r+=1
        if r==n:break
    return r

cycle=[frozenset((i,(i+1)%6)) for i in range(6)]
for i in range(6):
    a,b,c=[cycle[(i+k)%6] for k in (0,1,2)]
    assert len(a&b)==len(b&c)==1
    assert c!=a^b
    assert len(c-b)==1

all_supp=[frozenset(c) for c in combinations(range(6),2)]
edges=[(a,b) for a in all_supp for b in all_supp if len(a&b)==1]
assert len(edges)==120
assert all(sum(len(b&c)==1 for c in all_supp)==8 for a,b in edges)

for i in range(6):
    before=cycle[i]|cycle[(i+1)%6]
    after=cycle[(i+3)%6]|cycle[(i+4)%6]
    assert len(before)==len(after)==3 and not before&after

summary=[]
for d in range(1,6):
    Z=list(product(SIGNS,repeat=d))
    A=list(product(SIGNS,repeat=d))
    W=[binary_basis(z) for z in Z]
    assert len(set(W))==2**d
    M=[[Q(1,4)**d * prod(2+a[i]*w[i] for i in range(d))
        for w in W] for a in A]
    assert all(sum(row[j] for row in M)==1 for j in range(2**d))
    assert rank(M)==2**d
    dv=det(M)
    assert abs(dv)==Q(1,2**(d*2**(d-1)))
    ranks=[];classes=[]
    for h in range(d+1):
        rows=sorted(set(tuple(a[:h]) for a in A))
        Mh=[[Q(1,4)**h * prod(2+ah[i]*w[i] for i in range(h))
            for w in W] for ah in rows]
        assert rank(Mh)==2**h
        ranks.append(rank(Mh))
        classes.append(len({w[:h] for w in W}))
    walsh=0
    for mask in range(1<<d):
        J=[j for j in range(d) if mask>>j&1]
        for iz,w in enumerate(W):
            lhs=sum(Q(1,1)*M[ia][iz]*prod(a[j] for j in J) for ia,a in enumerate(A))
            rhs=Q(prod(w[j] for j in J),2**len(J))
            assert lhs==rhs
            walsh+=1
    masks=list(range(1,1<<d))
    fisher_diag=[]
    for x in masks:
        jx=[j for j in range(d) if x>>j&1]
        fisher_diag.append(Q(1,4**len(jx)))
        for y in masks:
            jy=[j for j in range(d) if y>>j&1]
            val=sum(Q(prod(a[j] for j in jx+jy),2**(len(jx)+len(jy)))*Q(1,2**d) for a in A)
            assert val==(Q(1,4**len(jx)) if x==y else Q(0))
    map_succ=sum(max(M[i][j] for j in range(2**d)) for i in range(2**d))*Q(1,2**d)
    assert map_succ==Q(3,4)**d
    parity=[prod(w) for w in W]
    plus=[Q(1,2**d)*(1+Q(v,2)) for v in parity]
    minus=[Q(1,2**d)*(1-Q(v,2)) for v in parity]
    assert sum(plus)==sum(minus)==1 and min(plus+minus)>0
    out_plus=[sum(M[i][j]*plus[j] for j in range(2**d)) for i in range(2**d)]
    out_minus=[sum(M[i][j]*minus[j] for j in range(2**d)) for i in range(2**d)]
    delta=Q(1,2**(d+1))
    assert all(out_plus[i]==Q(1,2**d)*(1+delta*prod(A[i])) for i in range(2**d))
    assert all(out_minus[i]==Q(1,2**d)*(1-delta*prod(A[i])) for i in range(2**d))
    tv=sum(abs(out_plus[i]-out_minus[i]) for i in range(2**d))/2
    assert tv==delta
    assert Q(1,delta*delta*4)==4**d
    summary.append({"d":d,"rank_by_horizon":ranks,"classes_by_horizon":classes,
      "affine_coordinates_by_horizon":[k-1 for k in ranks],
      "abs_determinant":str(abs(dv)),"fisher_diag_by_walsh_degree":
          {str(k):str(Q(1,4**k)) for k in range(1,d+1)},
      "fisher_degree_multiplicities":{str(k):comb(d,k) for k in range(1,d+1)},
      "one_word_MAP_success":str(map_succ),"walsh_column_checks":walsh,
      "interior_pair_one_word_TV":str(tv),
      "min_repetitions_for_Bayes_error_strictly_below_quarter":f">{4**d}"})
print(json.dumps({"status":"PASS","model":"R749SF conditional six-axis unsigned support kernel plus finite private sign-history controller",
"nonforced_six_support_cycle_verified":True,"legal_unsigned_directed_edges":120,
"full_stale_source_washout_steps":3,"d_checked":[1,2,3,4,5],
"exact_arithmetic":"fractions.Fraction","cases":summary,"native_event_permission":False},sort_keys=True))

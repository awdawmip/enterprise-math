"""Exact rational R749SK signed-Port forced-observer ratio/rank verifier.
The proof is in the accompanying note; this program checks every 120 ordered
unsigned support, three p values and six nondegenerate eight-lift priors.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json

AXES=range(6)
SIGNS=list(product((-1,1),repeat=3))

def rank(rows):
    a=[list(map(F,row)) for row in rows]
    if not a:return 0
    m,n=len(a),len(a[0]);r=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        t=a[r][col];a[r]=[v/t for v in a[r]]
        for i in range(m):
            if i!=r and a[i][col]:
                t=a[i][col]
                a[i]=[v-t*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def make_prior(kind):
    if kind==0:return [F(1,8)]*8
    if kind==1:return [F(j,36) for j in range(1,9)]
    a,b,c=[(F(1,5),F(-1,7),F(1,9)),(F(1,5),F(0),F(0)),(F(0),F(1,5),F(0)),(F(0),F(0),F(1,4))][kind-2]
    out=[(1+a*x[0]+b*x[1]+c*x[0]*x[1])/8 for x in SIGNS]
    assert sum(out)==1 and min(out)>0
    return out

checked=0
low_rank={}
for A in map(frozenset,combinations(AXES,2)):
  for B in map(frozenset,combinations(AXES,2)):
    if len(A&B)!=1:continue
    i=next(iter(A-B));j=next(iter(A&B));k=next(iter(B-A))
    C=A^B
    assert C==frozenset((i,k)) and len(set((i,j,k)))==3
    for p in (F(0),F(1,2),F(1)):
      theta=8*p/(1+7*p)
      # Coordinates are (m_i,m_j,m_ij), constant offsets irrelevant.
      want=1 if p==0 else 2
      assert rank([(theta,1,2*theta),(theta,1,0)])==want
      low_rank[str(p)]=want
      for typ in range(6):
        mu=make_prior(typ)
        mi=sum(w*x[0] for w,x in zip(mu,SIGNS))
        mj=sum(w*x[1] for w,x in zip(mu,SIGNS))
        mij=sum(w*x[0]*x[1] for w,x in zip(mu,SIGNS))
        d=n=F(0)
        for w,(si,sj,sk) in zip(mu,SIGNS):
          for yi in (-1,1):
            tr=F(1,2)*(1+theta*si*yi)
            yj=sj;yk=sk
            assert tr>=0 and yi in (-1,1) and yk in (-1,1)
            gate=F(2+yi+yj,4)
            d+=w*tr*gate
            n+=w*tr*gate*yi*yj
        d_formula=(2+theta*mi+mj)/4
        n_formula=(2*theta*mij+theta*mi+mj)/4
        assert (d,n)==(d_formula,n_formula)
        if d>0:
          assert n/d==(2*theta*mij+theta*mi+mj)/(2+theta*mi+mj)
        checked+=1
assert checked==120*3*6
# Two different priors can have identical 2-combination carrier.
theta=F(8,9)
def moments(weights):
 return (sum(w*x[0] for w,x in zip(weights,SIGNS)),
         sum(w*x[1] for w,x in zip(weights,SIGNS)),
         sum(w*x[0]*x[1] for w,x in zip(weights,SIGNS)))
prior1,prior2=make_prior(3),[(1+F(8,45)*x[1])/8 for x in SIGNS]
assert prior1!=prior2
m1,m2=moments(prior1),moments(prior2)
assert m1!=m2 and theta*m1[0]+m1[1]==theta*m2[0]+m2[1] and m1[2]==m2[2]
print(json.dumps({"status":"PASS", "unsigned_initial_support_edges":120,
 "parameter_values":["0","1/2","1"],"full_support_prior_families":6,
 "exact_direct_kernel_checks":checked,
 "minimum_affine_walsh_coordinates_by_p":low_rank,
 "three_raw_moment_masks":3,"two_combination_carrier_verified":True,
 "distinct_priors_same_compressed_statistics":True,
 "native_event_permission":False},ensure_ascii=False,sort_keys=True))

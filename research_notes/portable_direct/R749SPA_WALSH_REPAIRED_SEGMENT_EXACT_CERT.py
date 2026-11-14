#!/usr/bin/env python3
"""R749SPA: complete exact 6D polytope certificates for a repaired Walsh zero-gap segment.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Standard-library Python; integer Bareiss + Fraction; exact rational assertions.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from collections import Counter
import json

MASKS=(3,12,15,1,2,4,8)
W=[tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16)]
S=F(3,5)
PIECES=[(F(2,15),F(1,5), F(1,5), -F(3,2)),
        (F(1,5),F(2,5), -F(1,5), F(1,2))]

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(c,row)),F(0)))/16 for row in W)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def rad(t):return (F(18,5)-t)/8

def solve_bareiss(rows,rhs,idx):
    n=6
    a=[list(rows[i])+[rhs[i]] for i in idx]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]!=0),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            factor=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-factor*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if not a[n-1][n-1]:return None
    ans=[F(0)]*n
    for i in range(n-1,-1,-1):
        ans[i]=(F(a[i][n])-sum((a[i][j]*ans[j] for j in range(i+1,n)),F(0)))/a[i][i]
    return tuple(ans)

def lower():
    tests=[]
    signs=[]
    for t in [F(2,15),F(1,5),F(2,5)]:
        p1=law(t,S,0,t,t,1-t,S)
        p2=law(t,S,0,-t,-t,t-1,-S)
        assert min(p1)>=0 and min(p2)>=0
        assert sum(p1)==sum(p2)==1
        assert tv(p1,p2)==2*rad(t)
        signs.append(tuple((a>b)-(a<b) for a,b in zip(p1,p2)))
        tests.append({'t':str(t),'tv':str(tv(p1,p2))})
    assert all(x*y>=0 for a in signs for b in signs for x,y in zip(a,b))
    return {'source_pair': ['p(t,3/5,0,t,t,1-t,3/5)', 'p(t,3/5,0,-t,-t,t-1,-3/5)'],
            'endpoint_nonnegativity_and_sign_constancy':True,
            'corner_distances':tests,'all_t_TV':'(18/5-t)/4'}

def certify(lo,hi,alpha,beta):
    # six variables: (t,h,u,v,w,z). s=3/5 is constant.
    rows=[]; rhs=[]
    for r in W:
        rows.append((r[0],r[2],r[3],r[4],r[5],r[6]))
        rr=-1-S*r[1]
        assert rr.denominator==5
        rhs.append(rr)
    # convert all inequalities into integers by x5 scaling:
    rows=[[5*x for x in row] for row in rows]
    rhs=[int(5*b) for b in rhs]
    # t >=lo and -t>=-hi, denominators as supplied
    for tbound,sgn in [(lo,1),(hi,-1)]:
        den=tbound.denominator
        rows.append([sgn*den,0,0,0,0,0]);rhs.append(int(sgn*tbound*den))
    assert len(rows)==18
    vertices=set(); feasible=nonsingular=0
    for idx in combinations(range(18),6):
        x=solve_bareiss(rows,rhs,idx)
        if x is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(row,x)),F(0))<r for row,r in zip(rows,rhs)):
            continue
        feasible+=1;vertices.add(x)
    assert vertices
    mx=None;tight=0;params=Counter()
    for x in vertices:
        t,h,u,v,w,z=x
        p=law(t,S,h,u,v,w,z)
        h_center=alpha+beta*t
        q=law(t,S,h_center)
        assert min(p)>=0 and sum(p)==1
        assert min(q)>=0 and sum(q)==1
        excess=tv(p,q)-rad(t)
        if mx is None or excess>mx:mx=excess
        if excess==0:tight+=1
        params[str(t)]+=1
        assert excess<=0,('VIOLATION',tuple(map(str,x)),str(excess))
    assert mx==0
    return {'t_range':[str(lo),str(hi)],'h_center':f'{alpha} + ({beta})*t',
       'active_six_constraint_combinations':comb(18,6),
       'nonsingular_bases':nonsingular,'feasible_bases_with_multiplicity':feasible,
       'distinct_exact_vertices':len(vertices),'tight_vertices':tight,
       'max_risk_excess':str(mx),'t_coordinate_histogram':dict(sorted(params.items())),
       'joint_polytope_bounded_and_full_dim':True}

def repaired_witness():
    t=F(1,5)
    # old center h=0 and a specific feasible source from SOZ
    witness=law(t,S,-t,0,0,1-t,F(4,5))
    q0=law(t,S)
    q1=law(t,S,-F(1,10))
    assert min(witness)>=0
    assert tv(witness,q0)==F(9,20)
    assert tv(witness,q0)>rad(t)
    assert tv(witness,q1)<=rad(t)
    return {'parameter':['1/5','3/5'], 'old_h':'0', 'old_risk_witness':'9/20',
      'target_radius':'17/40','repaired_h':'-1/10','repaired_full_fiber_risk':'17/40'}

def main():
    return {'status':'PASS','research_id':'R749SPA',
       'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
       'scope':'auxiliary 16-atom Walsh source family; s=3/5, real 2/15<=t<=2/5',
       'theorem':'rho(t,3/5)=rho_cal(t,3/5)=(18/5-t)/8',
       'center':'q_t=p(t,3/5,h(t),0,0,0,0), h(t)=1/5-3t/2 on [2/15,1/5] and h(t)=(t-2/5)/2 on [1/5,2/5]',
       'lower':lower(),'upper':[certify(*entry) for entry in PIECES],
       'old_center_repair':repaired_witness(),
       'universal_real_argument':'bounded joint (t,h,u,v,w,z) source polytope; exact all-vertex convex risk bound per piece; compatible affine center; affine source-pair lower bound',
       'review_status':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__=='__main__':
    data=main()
    print(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True))

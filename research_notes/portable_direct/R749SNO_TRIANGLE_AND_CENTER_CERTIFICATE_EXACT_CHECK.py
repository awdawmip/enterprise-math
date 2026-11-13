#!/usr/bin/env python3
"""R749SNO: exact joint-polytope proof of a triangular Walsh zero-penalty region,
plus an exact nonconvexity counterexample for the fixed candidate center q0.
Standard-library integer Bareiss elimination + Fraction only.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

B=(3,5,6,7,9,10,11,12,13,14)
MOMENTS=(3,12,15,1,2,4,8)
ROWS=[tuple(1 if (m & x).bit_count()%2==0 else -1 for m in MOMENTS) for x in range(16)]
EVENT=(3,5,7,9,11,13,14,15)
TRIANGLE=((Q(1,2),Q(3,10)),(Q(3,5),Q(2,5)),(Q(1),Q(0)))
PIN='a72226e2430ffa4786321ac86e7f0c599d5f0389'

def law(t,s,h,u,v,w,z):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*x for a,x in zip(row,c)),Q(0)))/16 for row in ROWS)

def q0(t,s):
    return law(t,s,0,0,0,0,0)

def radius(t,s):
    return (3+t-s)/8

def upper(t,s,h,u,v,w,z):
    mu=law(t,s,h,u,v,w,z)
    q=q0(t,s)
    assert min(mu)>=0 and min(q)>=0 and sum(mu)==1 and sum(q)==1
    return sum((abs(x-y) for x,y in zip(mu,q)),Q(0))/2

def solve(rows, rhs, active, n):
    a=[list(rows[i])+[rhs[i]] for i in active]
    last=1
    for j in range(n-1):
        pivot=next((i for i in range(j,n) if a[i][j]!=0),None)
        if pivot is None:
            return None
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                value=a[i][k]*p-v*a[j][k]
                assert value%last==0
                a[i][k]=value//last
            a[i][j]=0
        last=p
    if a[n-1][n-1]==0:
        return None
    v=[Q(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(Q(a[j][n])-sum((a[j][k]*v[k] for k in range(j+1,n)),Q(0)))/a[j][j]
    return tuple(v)

def enumerate_vertices(rows,rhs,n,scale):
    assert all(isinstance(r,int) for r in rhs)
    count={'bases':0,'nonsingular':0,'feasible_bases':0,'distinct_vertices':0}
    seen=set()
    for active in combinations(range(len(rows)),n):
        count['bases']+=1
        z=solve(rows,rhs,active,n)
        if z is None:
            continue
        count['nonsingular']+=1
        if any(sum((a*x for a,x in zip(row,z)),Q(0)) < b for row,b in zip(rows,rhs)):
            continue
        count['feasible_bases']+=1
        seen.add(tuple(x/scale for x in z))
    assert count['bases']==comb(len(rows),n)
    count['distinct_vertices']=len(seen)
    assert seen
    return seen,count

def joint_triangle_check():
    # t-s >= 1/5; t+s <= 1; 3t+5s >= 3.
    # y=10*(t,s,h,u,v,w,z) makes all facets integral.
    L=10
    rows=ROWS+[(1,-1,0,0,0,0,0),(-1,-1,0,0,0,0,0),(3,5,0,0,0,0,0)]
    rhs=[-L]*16+[2,-10,30]
    seen,counts=enumerate_vertices(rows,rhs,7,L)
    assert counts['bases']==50388
    counts['tight_vertices']=0
    counts['violating_vertices']=0
    maximum=Q(-100)
    for t,s,h,u,v,w,z in seen:
        excess=upper(t,s,h,u,v,w,z)-radius(t,s)
        counts['tight_vertices']+=int(excess==0)
        counts['violating_vertices']+=int(excess>0)
        maximum=max(maximum,excess)
    counts['max_excess']=str(maximum)
    assert counts['violating_vertices']==0
    assert set(TRIANGLE)=={(Q(1,2),Q(3,10)),(Q(3,5),Q(2,5)),(Q(1),Q(0))}
    assert all(sum(ROWS[x][j] for x in EVENT)==0 for j in range(3))
    for t,s in TRIANGLE:
        w=law(t,s,0,s-1,-t,-s,-s)
        qc=q0(t,s)
        assert min(w)>=0 and min(qc)>=0
        assert sum(w)==sum(qc)==1
        assert sum((w[x] for x in EVENT),Q(0))-Q(1,2)==radius(t,s)
    return counts

def fixed_fiber_check(t,s):
    # y=100*(h,u,v,w,z); all 16 atom constraints are integer.
    L=100
    rows=[r[2:] for r in ROWS]
    rhs=[-int(L*(1+t*r[0]+s*r[1])) for r in ROWS]
    seen,cnt=enumerate_vertices(rows,rhs,5,L)
    assert cnt['bases']==4368
    maxval=Q(-1)
    argmax=None
    for h,u,v,w,z in seen:
        val=upper(t,s,h,u,v,w,z)
        if val>maxval:
            maxval,argmax=val,(h,u,v,w,z)
    return {'t':str(t),'s':str(s),'counts':cnt,
            'q0_worst_tv':str(maxval),'affine_lower':str(radius(t,s)),
            'excess':str(maxval-radius(t,s)),
            'argmax_free_moments':list(map(str,argmax))}

def main():
    joint=joint_triangle_check()
    fixed=[fixed_fiber_check(Q(7,10),s) for s in (Q(1,10),Q(3,20),Q(1,5))]
    assert [x['excess'] for x in fixed]==['0','3/160','0']
    bad=law(Q(7,10),Q(3,20),-Q(3,20),Q(17,20),Q(17,20),0,0)
    assert min(bad)==0 and sum(bad)==1
    assert upper(Q(7,10),Q(3,20),-Q(3,20),Q(17,20),Q(17,20),0,0)==Q(37,80)
    assert radius(Q(7,10),Q(3,20))==Q(71,160)
    return {
      'unit':'R749SNO','status':'PASS',
      'frozen_scientific_pin':PIN,
      'scope':'auxiliary 16-state Walsh observer, author exact certificate; independent review pending',
      'triangle_vertices':[[str(t),str(s)] for t,s in TRIANGLE],
      'triangle_halfspaces':['t-s >= 1/5','t+s <= 1','3t+5s >= 3'],
      'triangle_area':'1/25','old_polygon_area':'11/800','area_ratio':'32/11',
      'theorem':'rho=rho_cal=(3+t-s)/8 throughout the closed triangle for all real parameters',
      'center':'q0(x)=(1+t*chi_3(x)+s*chi_12(x))/16',
      'lower':'W=(h,u,v,w,z)=(0,s-1,-t,-s,-s), E={3,5,7,9,11,13,14,15}',
      'joint_exact_certificate':joint,
      'separate_q0_certificate_nonconvexity':fixed,
      'counterexample':'at (t,s)=(7/10,3/20), source moments (-3/20,17/20,17/20,0,0) have TV(mu,q0)=37/80>71/160 by 3/160; this refutes only the q0-vs-affine-radius bound, not the exact minimax equality.',
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True,ensure_ascii=False))

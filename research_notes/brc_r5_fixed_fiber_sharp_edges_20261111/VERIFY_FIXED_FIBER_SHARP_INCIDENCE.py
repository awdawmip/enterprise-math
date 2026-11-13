#!/usr/bin/env python3
"""Exact fixed-physical-fiber incidence census for R5 K4+high-pair 14-arc
circuits. Rational arithmetic throughout; SymPy is used for exact ranks.
Frozen witness: enterprise-math PR #2017 WITNESS.txt; graph: PR #2045.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from collections import Counter
from sympy import Matrix, Rational

R=(2,10,15,20,25,30,38)
S=(1,2,3,5)
D=[(i,j) for j in (0,1,2,3,5,6) for i in range(7)
   if j not in (0,6) or i==j]
E0=tuple(map(Q,('219346331/10192753200,7664319/135903376,'
'2813871/16987922,196521/33975844,196521/33975844,'
'196521/33975844,196521/33975844,196521/33975844,'
'196521/33975844,393042/8493961,196521/33975844,'
'196521/33975844,196521/33975844,196521/33975844,'
'196521/33975844,196521/33975844,196521/33975844,'
'5251441/33975844,166713611/1274094150,2500147/33975844,'
'393042/8493961,196521/33975844,196521/33975844,'
'196521/33975844,196521/33975844,196521/33975844,'
'196521/33975844,196521/33975844,7664319/135903376,'
'451274777/3397584400').split(',')))
assert len(E0)==len(D)==30 and min(E0)>0
M=tuple(sum((e for (i,j),e in zip(D,E0) if i==k and j in S),Q(0)) for k in range(7))
Qm={j:sum((e for (i,jj),e in zip(D,E0) if j==jj),Q(0)) for j in S}
Tm={j:sum((R[i]*e for (i,jj),e in zip(D,E0) if j==jj),Q(0)) for j in S}
assert sum(M)==sum(Qm.values())
assert sum(R[i]*M[i] for i in range(7))==sum(Tm.values())

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,v):return (x[0]*v,x[1]*v)
def div(x,v):return (x[0]/v,x[1]/v)
def cn(v):return (v,Q(0))

def split_affine(low,labels):
    p,q=low;h,k=(j for j in S if j not in low)
    A,B,C,Dd,E,F,G=labels
    a,b,c,d,e,f,g=(R[i] for i in labels)
    t=(Q(0),Q(1))
    xA=t
    xB=div(sub(cn(Tm[p]-c*Qm[p]),mul(t,a-c)),b-c)
    xC=sub(sub(cn(Qm[p]),t),xB)
    xD=div(add(cn(Tm[q]-e*Qm[q]+(e-a)*M[A]),mul(t,a-e)),d-e)
    xE=sub(add(cn(Qm[q]-M[A]),t),xD)
    H0=add(cn(Qm[h]-M[B]-M[Dd]),add(xB,xD))
    H1=add(cn(Tm[h]-b*M[B]-d*M[Dd]),add(mul(xB,b),mul(xD,d)))
    xF=div(sub(mul(H0,g),H1),g-f)
    xG=sub(H0,xF)
    return (xA,xB,xC,xD,xE,xF,xG)

def strict_interval(labels,xs):
    lower=upper=None
    for i,(alpha,beta) in zip(labels,xs):
        if not beta:
            if not Q(0)<alpha<M[i]:return None
            continue
        lo=min(-alpha/beta,(M[i]-alpha)/beta)
        hi=max(-alpha/beta,(M[i]-alpha)/beta)
        lower=lo if lower is None else max(lower,lo)
        upper=hi if upper is None else min(upper,hi)
        if lower>=upper:return None
    assert lower is not None and upper is not None
    return lower,upper

def coeffs(labels):
    a,b,c,d,e,f,g=(R[i] for i in labels)
    ua=(b-c)*(d-e);ub=(c-a)*(d-e);uc=(a-b)*(d-e)
    ud=-(b-c)*(e-a);ue=-(b-c)*(a-d)
    vf=(-ub)*(b-g)+(-ud)*(d-g)
    vg=(-ub)*(f-b)+(-ud)*(f-d)
    delta=g-f
    return (ua*delta,ub*delta,uc*delta,ud*delta,ue*delta,vf,vg)

def build_vector(low,labels,t):
    p,q=low;h,k=(j for j in S if j not in low)
    pairs=((p,q),(p,h),(p,k),(q,h),(q,k),(h,k),(h,k))
    xs=split_affine(low,labels)
    E=dict(zip(D,E0))
    for ((s,ss),i),(aa,bb) in zip(zip(pairs,labels),xs):
        v=aa+bb*t
        assert 0<=v<=M[i]
        E[(i,s)]=v;E[(i,ss)]=M[i]-v
    used={(i,j) for (s,ss),i in zip(pairs,labels) for j in (s,ss)}
    for i,j in D:
        if j in S and (i,j) not in used:E[(i,j)]=Q(0)
    return tuple(E[a] for a in D)

def obs(vec):
    return (tuple(sum(e for (i,j),e in zip(D,vec) if i==k) for k in range(7)),
            tuple(sum(e for (i,j),e in zip(D,vec) if j==k) for k in (0,1,2,3,5,6)),
            tuple(sum(R[i]*e for (i,j),e in zip(D,vec) if j==k) for k in (0,1,2,3,5,6)))

def main():
    n_all=n_complete=n_feasible=0
    bylow=Counter();examples=[];support_pairs=Counter();vertices=set();edges=[]
    min_width=None;true_obs=obs(E0)
    C=Matrix.hstack(*(Matrix([int(i==ii) for ii in range(7)]
      +[int(j==jj) for jj in range(7)]
      +[Rational(R[i],20) if j==jj else 0 for jj in range(7)])
      for i,j in D))
    assert C.rank()==15
    for low in combinations(S,2):
        for labels in permutations(range(7)):
            if labels[5]>labels[6]:continue
            n_all+=1
            z=coeffs(labels)
            if not z[5]*z[6]:continue
            n_complete+=1
            xs=split_affine(low,labels)
            factor=xs[0][1]/z[0]
            assert all(bb==factor*zz for (aa,bb),zz in zip(xs,z))
            itv=strict_interval(labels,xs)
            if itv is None:continue
            n_feasible+=1;bylow[low]+=1
            left=build_vector(low,labels,itv[0])
            right=build_vector(low,labels,itv[1])
            assert left!=right and obs(left)==obs(right)==true_obs
            p,q=low;h,k=(j for j in S if j not in low)
            pairs=((p,q),(p,h),(p,k),(q,h),(q,k),(h,k),(h,k))
            used=sorted({D.index((i,j)) for pair,i in zip(pairs,labels)
                         for j in pair}|{D.index((0,0)),D.index((6,6))})
            assert len(used)==16 and C[:,used].rank()==15
            assert min(left)>=0 and min(right)>=0
            assert sum(v>0 for v in build_vector(low,labels,sum(itv,Q(0))/2))==16
            support_pairs[tuple(sorted((sum(v>0 for v in left),
                                        sum(v>0 for v in right))))]+=1
            vertices.add(left);vertices.add(right);edges.append((left,right))
            if len(examples)<4:examples.append((low,labels,itv))
            width=itv[1]-itv[0]
            assert width>0
            if min_width is None or width<min_width:min_width=width
    assert n_all==15120 and n_complete==14832 and n_feasible==49
    assert sum(bylow.values())==n_feasible
    neighbors={v:set() for v in vertices}
    for u,v in edges:neighbors[u].add(v);neighbors[v].add(u)
    assert sum(map(len,neighbors.values()))==2*n_feasible
    seen=set();components=[]
    for root in vertices:
        if root in seen:continue
        stack=[root];seen.add(root);size=0
        while stack:
            node=stack.pop();size+=1
            for nxt in neighbors[node]:
                if nxt not in seen:seen.add(nxt);stack.append(nxt)
        components.append(size)
    assert len(components)==len(vertices)-len(edges)==9
    assert Counter(map(len,neighbors.values()))=={1:38,3:20}
    print('EXACT_CANDIDATES',n_all)
    print('EXACT_FULL_14_ARC_CIRCUITS',n_complete)
    print('EXACT_FIXED_FIBER_SHARP_ADJACENT_EDGES',n_feasible)
    print('BY_LOW_SOURCE_PAIR',sorted(bylow.items()))
    print('MIN_POSITIVE_T_INTERVAL_WIDTH',min_width)
    print('ENDPOINT_SUPPORT_PAIR_COUNTS',sorted(support_pairs.items()))
    print('UNIQUE_ADJACENT_VERTICES',len(vertices))
    print('SHARP_SUBGRAPH_DEGREE_COUNTS',sorted(Counter(map(len,neighbors.values())).items()))
    print('SHARP_SUBGRAPH_COMPONENT_SIZES',sorted(components))
    print('UNIQUE_VERTEX_SUPPORT_COUNTS',
          sorted(Counter(sum(v>0 for v in x) for x in vertices).items()))
    for lo,labels,itv in examples:
        print('WITNESS',lo,labels,'T_INTERVAL',itv,
              'INTERIOR_T',sum(itv,Q(0))/2)
    print('PASS_EXACT_FIXED_FIBER_SHARP_INCIDENCE')

if __name__=='__main__':main()

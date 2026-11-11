#!/usr/bin/env python3
"""Exact count of R5 sharp four-circuit edges in fixed pinned positive fiber.

The 14-arc direction support plus the two fixed positive singletons (0,0),(6,6)
completely determines the relative-interior support of any such edge.
For each target i, split the fixed non-singleton marginal M_i between the two
source ports incident to i. All arithmetic is exact (Fraction).
"""
from fractions import Fraction as Q
from math import lcm
from itertools import permutations,combinations
from pathlib import Path
from collections import Counter
R=(2,10,15,20,25,30,38)
J=(1,2,3,5)
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
data=dict(line.split('=',1) for line in Path(__file__).with_name('WITNESS.txt').read_text().splitlines())
e0=tuple(map(Q,data['ARCS'].split(',')))
assert len(e0)==len(D)==30 and min(e0)>0
L=lcm(*(x.denominator for x in e0))
E={d:int(e0[idx]*L) for idx,d in enumerate(D)}
assert all(Q(v,L)==e0[k] for k,v in enumerate(E.values()))  # D order
M=[sum(E[(i,j)] for j in J) for i in range(7)]
SM=[sum(E[(i,j)] for i in range(7)) for j in J]
SW=[sum(R[i]*E[(i,j)] for i in range(7)) for j in J]
assert min(M)>0 and sum(M)==sum(SM)
assert sum(R[i]*M[i] for i in range(7))==sum(SW)


def solution_for_labels(low,labels):
    p,q=low
    h,k=tuple(j for j in J if j not in low)
    pairs=((p,q),(p,h),(p,k),(q,h),(q,k),(h,k),(h,k))
    target_pair=[None]*7
    for i,(j,l) in zip(labels,pairs): target_pair[i]=(j,l)
    # The 8 source moment equations in seven split variables t_i.
    A=[[0]*8 for _ in range(8)]
    for ri,j in enumerate(J):
        A[2*ri][7]=SM[ri]
        A[2*ri+1][7]=SW[ri]
    for i,(j,l) in enumerate(target_pair):
        u,v=J.index(j),J.index(l)
        A[2*u][i]+=1; A[2*u+1][i]+=R[i]
        A[2*v][i]-=1; A[2*v+1][i]-=R[i]
        A[2*v][7]-=M[i]; A[2*v+1][7]-=R[i]*M[i]
    # Row reduce 8x8 over rational numbers. Only 7 unknowns.
    A=[[Q(z) for z in row] for row in A]
    piv=[];prow=0
    for col in range(7):
        idx=next((j for j in range(prow,8) if A[j][col]),None)
        if idx is None: continue
        A[prow],A[idx]=A[idx],A[prow]
        pp=A[prow][col]
        A[prow]=[v/pp for v in A[prow]]
        for j in range(8):
            if j==prow or not A[j][col]: continue
            mult=A[j][col]
            A[j]=[A[j][u]-mult*A[prow][u] for u in range(8)]
        piv.append(col);prow+=1
    assert all(any(A[j][i] for i in range(7)) or A[j][7]==0 for j in range(8))
    assert len(piv)==6,(low,labels,piv)
    free=next(i for i in range(7) if i not in piv)
    const=[Q() for _ in range(7)]
    slope=[Q() for _ in range(7)]
    slope[free]=Q(1)
    for row,col in enumerate(piv):
        const[col]=A[row][7]
        slope[col]=-A[row][free]
    lo=hi=None
    for i in range(7):
        a,b=const[i],slope[i]
        if b==0:
            if not (0<a<M[i]):return False,None
            continue
        z1=-a/b;z2=(Q(M[i])-a)/b
        lower=min(z1,z2); upper=max(z1,z2)
        lo=lower if lo is None else max(lo,lower)
        hi=upper if hi is None else min(hi,upper)
    if lo is None or hi is None or not lo<hi:return False,None
    mid=(lo+hi)/2
    vals=[const[i]+slope[i]*mid for i in range(7)]
    assert all(0<vals[i]<M[i] for i in range(7))
    return True,(target_pair,const,slope,lo,hi,vals)


def verify_endpoints(w):
    tp,const,slope,lo,hi,_=w
    for t in (lo,hi,(lo+hi)/2):
        masses={(0,0):Q(E[(0,0)]),(6,6):Q(E[(6,6)])}
        for i,(j,k) in enumerate(tp):
            z=const[i]+slope[i]*t
            assert 0<=z<=M[i]
            masses[i,j]=z
            masses[i,k]=M[i]-z
        for i in range(7):
            assert sum(masses.get((i,j),Q()) for j in (0,1,2,3,5,6))==sum(E.get((i,j),0) for j in (0,1,2,3,5,6))
        for j in (0,1,2,3,5,6):
            assert sum(masses.get((i,j),Q()) for i in range(7))==sum(E.get((i,j),0) for i in range(7))
            assert sum(R[i]*masses.get((i,j),Q()) for i in range(7))==sum(R[i]*E.get((i,j),0) for i in range(7))
        assert all(x>=0 for x in masses.values())
        if t==lo or t==hi:
            assert any(const[i]+slope[i]*t==0 or const[i]+slope[i]*t==M[i] for i in range(7))



def main():
    full=degenerate=feasible=perlow=0
    cnt=Counter(); example=None; deg_feasible=0
    for low in combinations(J,2):
        thisfull=thisfeas=0
        for labels in permutations(range(7)):
            if labels[5]>labels[6]: continue
            pairs_ok=True
            # six-arc pair at F/G may zero for degenerate assignments
            a,b,c,d,e,f,g=(R[i] for i in labels)
            ub=(c-a)*(d-e);ud=-(b-c)*(e-a)
            vf=-ub*(b-g)-ud*(d-g)
            vg=-ub*(f-b)-ud*(f-d)
            if vf==0 or vg==0:
                degenerate+=1
                continue
            full+=1;thisfull+=1
            yes,w=solution_for_labels(low,labels)
            if yes:
                verify_endpoints(w)
                feasible+=1;thisfeas+=1
                if example is None: example=(low,labels,w)
        cnt[low]=(thisfull,thisfeas)
    assert (full,degenerate)==(14832,288)
    print('SOURCE_SINGLETON_FIXED',((0,0),Q(E[(0,0)],L)),((6,6),Q(E[(6,6)],L)))
    print('INTEGER_SCALING',L)
    print('MARGINAL_TARGET_VARIABLE',M)
    print('SOURCE_MASS',SM)
    print('SOURCE_WEIGHTED_TARGET',SW)
    print('PER_LOW_PAIR_FULL_FEASIBLE',cnt)
    print('TOTAL_FULL_SHARP_CIRCUITS',full)
    print('ACTUAL_FIXED_FIBER_SHARP_EDGES',feasible)
    if example:
        low,labels, (tp,c,s,lo,hi,vals)=example
        print('FIRST_EDGE_LOW_PAIR',low,'TARGET_LABELS',labels)
        print('FIRST_EDGE_OPEN_INTERVAL',str(lo),str(hi))
        print('FIRST_EDGE_INTERIOR_SPLITS',[str(v) for v in vals])
    assert feasible==49 and cnt=={(1,2):(2472,15),(1,3):(2472,0),(1,5):(2472,15),(2,3):(2472,0),(2,5):(2472,19),(3,5):(2472,0)}
    print('PASS_EXACT_FIXED_FIBER_SHARP_CIRCUIT_EDGE_CENSUS_49_WITH_ENDPOINTS')
if __name__=='__main__':main()

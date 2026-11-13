#!/usr/bin/env python3
"""R749SNV exact s in [0,2/15] minimax ray, pin a72226e2430ffa4786321ac86e7f0c599d5f0389."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

T=F(3,5)
MASKS=(3,12,15,1,2,4,8)
ROWS=tuple(tuple(1 if (x&m).bit_count()%2==0 else -1 for m in MASKS) for x in range(16))
SCALE=15

def law(s,h,u,v,w,z):
    return tuple((1+T*row[0]+sum((a*b for a,b in zip(row[1:],(s,h,u,v,w,z))),F(0)))/16 for row in ROWS)
def center(s): return law(s,3*s-F(2,5),0,0,0,0)
def radius(s): return (1-s)/2

def solve_bareiss(normals,bounds,select,n=6):
    mat=[list(normals[i])+[bounds[i]] for i in select]
    prev=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if mat[k][j]),None)
        if k is None:return None
        if k!=j:mat[j],mat[k]=mat[k],mat[j]
        pivot=mat[j][j]
        for i in range(j+1,n):
            v=mat[i][j]
            for k in range(j+1,n+1):
                d=mat[i][k]*pivot-v*mat[j][k]
                assert d%prev==0
                mat[i][k]=d//prev
            mat[i][j]=0
        prev=pivot
    if not mat[n-1][n-1]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(mat[j][n])-sum((mat[j][k]*x[k] for k in range(j+1,n)),F(0)))/mat[j][j]
    return tuple(x)

def main():
    for s in (F(0),F(2,15)):
        pos=law(s,-s,1-s,T+s,0,0)
        neg=law(s,-s,s-1,-T-s,0,0)
        assert min(pos)>=0 and min(neg)>=0
        assert sum(pos)==sum(neg)==1
        assert sum((abs(a-b) for a,b in zip(pos,neg)),F(0))/2==1-s
        q=center(s)
        assert min(q)>=0 and sum(q)==1
    # variables y=15(s,h,u,v,w,z)
    normals=[row[1:] for row in ROWS]+[(1,0,0,0,0,0),(-1,0,0,0,0,0)]
    bounds=[-15-9*row[0] for row in ROWS]+[0,-2]
    stats={'all_active_bases':0,'nonsingular_bases':0,'feasible_bases':0}
    vertices=set()
    for active in combinations(range(18),6):
        stats['all_active_bases']+=1
        x=solve_bareiss(normals,bounds,active)
        if x is None:continue
        stats['nonsingular_bases']+=1
        if any(sum((a*b for a,b in zip(row,x)),F(0))<rhs
               for row,rhs in zip(normals,bounds)):
            continue
        stats['feasible_bases']+=1
        vertices.add(tuple(y/SCALE for y in x))
    assert stats['all_active_bases']==comb(18,6)==18564
    assert vertices
    excess=F(-1)
    tight=violate=0
    for s,h,u,v,w,z in vertices:
        source=law(s,h,u,v,w,z)
        q=center(s)
        assert min(source)>=0 and min(q)>=0
        assert sum(source)==sum(q)==1
        gap=sum((abs(a-b) for a,b in zip(source,q)),F(0))/2-radius(s)
        excess=max(excess,gap)
        tight+=int(gap==0);violate+=int(gap>0)
    assert excess==0 and violate==0
    stats.update(distinct_vertices=len(vertices),tight_vertices=tight,
                 violating_vertices=violate,max_excess=str(excess))
    return dict(unit='R749SNV',status='PASS',review='NOT_REVIEWED',
        scientific_pin='a72226e2430ffa4786321ac86e7f0c599d5f0389',
        model='16-state auxiliary Walsh source observer, not native X6/V29/V39',
        theorem='forall real 0<=s<=2/15: rho(3/5,s)=rho_cal(3/5,s)=(1-s)/2',
        center_eta='3*s-2/5', source_diameter_pair='h=-s, u=+/- (1-s), v=+/- (3/5+s), w=z=0 with simultaneous signs',
        interval=['0','2/15'], transition_at_2_15={'left_radius':'13/30','right_radius':'(3+3/5-2/15)/8=13/30',
                                                    'left_center_eta':'0','right_center_eta':'0'},
        exact_joint_vertex_certificate=stats,
        next_question='Derive the full two-dimensional boundary across this vertical transition, then distinguish positive calibration penalty from larger common minimax risk')
if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True,ensure_ascii=False))

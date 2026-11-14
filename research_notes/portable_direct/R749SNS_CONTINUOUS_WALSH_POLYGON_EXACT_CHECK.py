#!/usr/bin/env python3
"""R749SNS exact 2D piecewise-Walsh-center polygon certificate.
Source math: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Depends on the existing R749SNO and R749SNR certificates on the old Q.
Integer Bareiss for all 7-facet combinations and Fraction exact arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

SOURCE = 'a72226e2430ffa4786321ac86e7f0c599d5f0389'
MASKS = (3,12,15,1,2,4,8)
ROWS = tuple(tuple(1 if (m & x).bit_count()%2==0 else -1 for m in MASKS)
             for x in range(16))
EVENT = (3,5,7,9,11,13,14,15)
A=(F(7,10),F(1,10))
B=(F(7,10),F(3,20))
C=(F(3,5),F(7,40))
D=(F(3,5),F(1,5))
E=(F(1,2),F(3,10))
FOLD=(F(3,5),F(2,5))
G=(F(1),F(0))
SCALE=40

def center_eta_1(t,s): return F(3,20)-F(3,2)*s
def center_eta_2(t,s): return (t+s-1)/2
def center_eta_3(t,s): return (3*t+5*s-3)/2
def radius(t,s): return (3+t-s)/8

def probability_law(t,s,h,u,v,w,z):
    coeff=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,coeff)),F(0)))/16 for row in ROWS)

def solve_bareiss(normals, bounds, active, n=7):
    mat=[list(normals[i])+[bounds[i]] for i in active]
    prev=1
    for col in range(n-1):
        pivot_row=next((i for i in range(col,n) if mat[i][col]!=0),None)
        if pivot_row is None:
            return None
        if pivot_row!=col:
            mat[col],mat[pivot_row]=mat[pivot_row],mat[col]
        pivot=mat[col][col]
        for i in range(col+1,n):
            entry=mat[i][col]
            for j in range(col+1,n+1):
                a=mat[i][j]*pivot-entry*mat[col][j]
                assert a%prev==0
                mat[i][j]=a//prev
            mat[i][col]=0
        prev=pivot
    if mat[n-1][n-1]==0:
        return None
    solution=[F(0)]*n
    for i in range(n-1,-1,-1):
        solution[i]=(F(mat[i][n])-sum((mat[i][j]*solution[j] for j in range(i+1,n)),F(0)))/mat[i][i]
    return tuple(solution)

def area(vertices):
    return abs(sum((x*v[1]-v[0]*y for (x,y),v in zip(vertices,vertices[1:]+vertices[:1])),F(0)))/2

# All normals in coordinates y=40(t,s,h,u,v,w,z), constants are similarly scaled.
TRIANGLES=(
 dict(name='P1_repaired_outer_triangle',vertices=(A,B,C),eta=center_eta_1,
      normal=((-1,0),(3,4),(-1,-4)),bounds=(-28,100,-52),
      region=('t<=7/10','3t+4s>=5/2','t+4s<=13/10')),
 dict(name='P2_center_transition_triangle',vertices=(B,C,D),eta=center_eta_2,
      normal=((1,0),(1,4),(-1,-2)),bounds=(24,52,-40),
      region=('t>=3/5','t+4s>=13/10','t+2s<=1')),
 dict(name='P3_old_edge_extension_triangle',vertices=(B,D,E),eta=center_eta_3,
      normal=((-3,-4),(1,1),(1,2)),bounds=(-108,32,40),
      region=('3t+4s<=27/10','t+s>=4/5','t+2s>=1')),
)

def verify_triangle(tri):
    normals=list(ROWS)+[tuple(row)+(0,0,0,0,0) for row in tri['normal']]
    bounds=[-SCALE]*16+list(tri['bounds'])
    vertices=set()
    stats=dict(active_bases=0,nonsingular_bases=0,feasible_bases=0,
               distinct_vertices=0,tight_vertices=0,violating_vertices=0,maximum_excess=None)
    for active in combinations(range(len(normals)),7):
        stats['active_bases']+=1
        coords=solve_bareiss(normals,bounds,active)
        if coords is None:
            continue
        stats['nonsingular_bases']+=1
        if any(sum((a*b for a,b in zip(row,coords)),F(0))<bound
               for row,bound in zip(normals,bounds)):
            continue
        stats['feasible_bases']+=1
        vertices.add(tuple(z/SCALE for z in coords))
    assert stats['active_bases']==comb(19,7)==50388
    assert vertices
    excess=F(-100)
    for t,s,h,u,v,w,z in vertices:
        q=probability_law(t,s,tri['eta'](t,s),0,0,0,0)
        mu=probability_law(t,s,h,u,v,w,z)
        assert min(q)>=0 and min(mu)>=0 and sum(q)==sum(mu)==1
        gap=sum((abs(x-y) for x,y in zip(q,mu)),F(0))/2-radius(t,s)
        if gap>excess: excess=gap
        stats['tight_vertices']+=int(gap==0)
        stats['violating_vertices']+=int(gap>0)
    stats['maximum_excess']=str(excess)
    stats['distinct_vertices']=len(vertices)
    assert excess==0 and stats['violating_vertices']==0

    for t,s in tri['vertices']:
        q=probability_law(t,s,tri['eta'](t,s),0,0,0,0)
        w=probability_law(t,s,0,s-1,-t,-s,-s)
        assert min(q)>=0 and min(w)>=0 and sum(w)==sum(q)==1
        assert sum((w[x] for x in EVENT),F(0))-F(1,2)==radius(t,s)
    return {**stats,'name':tri['name'],
            'vertices':[[str(a),str(b)] for a,b in tri['vertices']],
            'area':str(area(list(tri['vertices']))),
            'parameter_halfspaces':list(tri['region'])}

def test_bad_affine_join():
    # Interpolate the three optimal vertex coefficients at B,E,C.
    t,s=F(17,30),F(13,60)
    candidate_eta=F(3,4)*t+F(3,2)*s-F(33,40)
    q=probability_law(t,s,candidate_eta,0,0,0,0)
    source=probability_law(t,s,-F(13,60),-F(47,60),-F(47,60),F(0),F(0))
    assert min(q)>=0 and min(source)>=0 and sum(q)==sum(source)==1
    tv=sum((abs(x-y) for x,y in zip(q,source)),F(0))/2
    assert (candidate_eta,radius(t,s),tv,tv-radius(t,s))==(
        -F(3,40),F(67,160),F(41,96),F(1,120))
    # Proves this specific affine candidate fails, not a positive calibration gap.
    return dict(parameter=['17/30','13/60'],candidate_eta=str(candidate_eta),
                source_free_coefficients=['-13/60','-47/60','-47/60','0','0'],
                target_radius=str(radius(t,s)),loss=str(tv),excess=str(tv-radius(t,s)),
                conclusion='Specific single-affine interpolation is not a uniform minimax center')

def main():
    assert all(sum((ROWS[x][j] for x in EVENT),0)==0 for j in range(3))
    assert center_eta_1(*B)==center_eta_2(*B)==center_eta_3(*B)==-F(3,40)
    assert center_eta_1(*C)==center_eta_2(*C)==-F(9,80)
    assert center_eta_2(*D)==center_eta_3(*D)==-F(1,10)
    assert center_eta_3(*E)==0
    checks=[verify_triangle(tri) for tri in TRIANGLES]
    old_Q_area=F(19,400)
    new_polygon=(A,B,G,FOLD,E,D,C)
    total=area(list(new_polygon))
    new_area=sum((area(list(t['vertices'])) for t in TRIANGLES),F(0))
    assert total==old_Q_area+new_area==F(43,800)
    assert new_area==F(1,160)
    assert [x['distinct_vertices'] for x in checks]==[124,114,116]
    bad=test_bad_affine_join()
    return dict(unit='R749SNS',status='PASS',review='NOT_REVIEWED',
      frozen_scientific_input=SOURCE,
      interpretation='16-state auxiliary Walsh source model, NOT native X6/V29/V39',
      theorem='rho(t,s)=rho_cal(t,s)=(3+t-s)/8 on the displayed triangulated polygon',
      old_domain='R749SNO+R749SNR Q (area 19/400)',
      new_triangles=checks,new_polygon_vertices=[[str(x),str(y)] for x,y in new_polygon],
      new_polygon_area=str(total),new_triangle_area=str(new_area),
      area_gain=str(new_area/old_Q_area),
      probability_source_lower_witness='(h,u,v,w,z)=(0,s-1,-t,-s,-s)',
      lower_event=list(EVENT),
      center_coefficients={t['name']: {'P1_repaired_outer_triangle':'3/20-3*s/2',
        'P2_center_transition_triangle':'(t+s-1)/2',
        'P3_old_edge_extension_triangle':'(3*t+5*s-3)/2'}[t['name']] for t in TRIANGLES},
      invalid_naive_center_interpolation=bad,
      next_question='Find the adjacent real chambers and distinguish optimal-center switching from a true positive calibration gap')

if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False,sort_keys=True))

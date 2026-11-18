"""Exact first and second representatives of the strict hexagonal quotient. Standard library."""
from collections import Counter
from fractions import Fraction
import json


def uv(q,r):
    return 2*q+r,q+2*r


def h_uv(u,v):
    return max(abs(u),abs(v),abs(u-v))


def Q(q,r):
    return q*q+q*r+r*r


def rot(q,r):
    return -r,q+r


def rotate_sector(q,r):
    for i in range(6):
        u,v=uv(q,r)
        if (u,v)==(0,0) or 0<=v<u:
            return i,u,v,q,r
        q,r=rot(q,r)
    raise AssertionError('uncovered sector')


def shell_count(s):
    if s==0:
        return 1
    return 2*s+(-2 if s%3==1 else 2 if s%3==2 else 0)


def audit(m,discrete_check):
    s=m-1
    K=m*m-m+1
    # Entire raw candidate lists large enough to contain first two in both metrics.
    # For an inner z, test z and z-(m,-1) as crude upper bounds.
    groups=[[] for _ in range(K)]
    D=(m,-1)
    units=[D]
    for _ in range(5):
        units.append(rot(*units[-1]))
    for q in range(-4*m,4*m+1):
        for r in range(-4*m,4*m+1):
            h=h_uv(*uv(q,r))
            B=Q(q,r)
            if h<=3*m or B<=3*m*m:
                groups[(q+m*r)%K].append((h,B,q,r))
    shell=Counter()
    second_ties=Counter()
    hbound=Counter()
    qbound=Counter()
    joint=Counter()
    samples={}
    integer_perturbations=[(h_uv(*uv(q,r)),q,r) for q in range(-m,m+1) for r in range(-m,m+1)
                           if (q,r)!=(0,0) and h_uv(*uv(q,r))<=m] if discrete_check else []
    for group in groups:
        byh=sorted(group)
        byq=sorted(group,key=lambda row:row[1])
        h,B,q,r=byh[0]
        assert h<=s and byq[0]==byh[0]
        j,U,V,c,d=rotate_sector(q,r)
        assert h==U
        hd=2*m-1-h
        gap=K-m*h+V
        assert byh[1][0]==hd and byq[1][1]-B==gap
        hwin=set((x,y) for a,b,x,y in group if a==hd)
        qwin=set((x,y) for a,b,x,y in group if b==B+gap)
        assert qwin<=hwin and len(qwin)==(6 if not h else 1)
        assert len(hwin)==(6 if h==0 else 2 if V==0 and h<s else 1)
        assert (K-gap+m-1)//m==h
        # Shared-real-error certificates are checked in the canonical sector.
        # Double support coordinates: move along delta=(d_h-h)/2 in the u-normal.
        U2=2*U+(hd-h)
        V2=2*V
        h2=h_uv(U2,V2)
        assert h2==2*m-1
        assert h2==min(h_uv(U2-2*a,V2-2*b) for a,b in (uv(*w) for w in units))
        # Euclidean tie along the unit lattice period D, using denominator 2K.
        den=2*K
        cq,cr=c*den+gap*D[0],d*den+gap*D[1]
        t=Q(cq,cr)
        others=[Q(cq-den*x,cr-den*y) for x,y in units]
        assert min(others)==t and others[0]==t
        # Direct shortest integer perturbation disallowing the old translation center.
        if discrete_check:
            value=min(cost for cost,a,b in integer_perturbations if h_uv(*uv(q+a,r+b))>s)
            assert value==max(2,m-h)
        shell[h]+=1
        hbound[hd-h]+=1
        qbound[gap]+=1
        second_ties[len(hwin)]+=1
        joint[h,hd,gap]+=1
        if V==0 and h in (0,3,s):
            samples[h]={'canonical_qr':[c,d],'h1':h,'h2':hd,'height_gap':hd-h,
                        'Q1':B,'Q2':B+gap,'Q_gap':gap,'h_runnerup_count':len(hwin)}
    expected=Counter({(0,2*m-1,K):1})
    for h in range(1,s+1):
        for v in range(2*h%3,h,3):
            expected[h,2*m-1-h,K-m*h+v]+=6
        assert shell[h]==shell_count(h)
    assert expected==joint
    assert all(count==(1 if b==K else 6) for b,count in qbound.items())
    assert qbound[1]==6 and hbound[1]==2*s
    return dict(m=m,K=K,raw_grid_box=[-4*m,4*m],raw_grid_points=(8*m+1)**2,
                h_runnerup_multiplicities=dict(sorted(second_ties.items())),
                height_gap_one_count=hbound[1],squared_norm_gap_one_count=qbound[1],
                number_of_Q_gap_values=len(qbound),number_of_joint_monomials=len(joint),
                coordinate_shared_error_boundary_tests=2*K,
                optimal_integer_error_checked=discrete_check,vertex_examples=samples)


def missing(m):
    s=m-1
    K=m*m-m+1
    found={(q+m*r)%K for q in range(-m,m+1) for r in range(-m,m+1) if h_uv(*uv(q,r))<=s}
    return sorted(set(range(K))-found)


def main():
    # The noisy-label tie is genuinely between two different residues.
    assert h_uv(*uv(Fraction(1,2),0))==h_uv(*uv(Fraction(-1,2),0))==1
    assert missing(8)==[19,38]
    print(json.dumps({'frozen_family':[audit(m,m<=16) for m in (4,16,64)],
                      'missed_mod57_labels_outside_frozen_family_m8':missing(8),
                      'uniform_h_radius_for_global_label_noise':'1 (ambient lattice decoding)',
                      'uniform_h_radius_for_period_center_noise':'1/2',
                      'uniform_Q_distance_for_period_center_noise':'1/(2*sqrt(K))'},
                     sort_keys=True,indent=2))
if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Exact positive two-measure branch flow, fourth shared LR key; auxiliary model."""
from fractions import Fraction as F
from itertools import product
Z,U=F(0),F(1)
H=(F(5),Z,F(5),F(-8))
EPS=F(1,2)
def observe(params):
    p1,p2,q1,q2,qb,r,k1,k2,l1,l2=params
    out=[Z,Z,Z,Z]; totals=[Z,Z]
    def leaf(mp,mq,answer,t):
        assert mp>=0 and mq>=0
        totals[0]+=mp;totals[1]+=mq
        if answer=='P':out[0]+=mp
        else:out[1]+=mq
        out[2]+=mp*t;out[3]+=mq*t
    for p,q,k,l in ((p1,q1,k1,l1),(p2,q2,k2,l2)):
        ip=iq=F(1,8)
        leaf(ip*p,iq*p,'P',1)
        cp,cq=ip*(1-p),iq*(1-p)
        leaf(cp*F(1,2),cq*F(3,4),'Q',2)
        jp,jq=cp*F(1,2),cq*F(1,4)
        leaf(jp*q,jq*q,'P',2)
        jp,jq=jp*(1-q),jq*(1-q)
        leaf(jp*F(3,5),jq*F(1,2),'Q',3)
        kp,kq=jp*F(2,5),jq*F(1,2)
        leaf(kp*(1-EPS),kq*(1-EPS),'P',3)
        leaf(kp*EPS*k,kq*EPS*k,'P',3)
        kp,kq=kp*EPS*(1-k),kq*EPS*(1-k)
        leaf(kp*F(1,4),kq*F(1,2),'Q',4)
        lp,lq=kp*F(3,4),kq*F(1,2)
        leaf(lp*l,lq*l,'P',4)
        leaf(lp*(1-l),lq*(1-l),'Q',5)
    leaf(F(1,4)*qb,F(1,8)*qb,'P',2)
    leaf(F(1,4)*(1-qb),F(1,8)*(1-qb),'P',3)
    leaf(F(1,2)*r,F(5,8)*r,'Q',1)
    leaf(F(1,2)*(1-r),F(5,8)*(1-r),'P',3)
    assert totals==[U,U],totals
    return tuple(out)
def lr(p,q,r,k,l):return observe((p,p,q,q,q,r,k,k,l,l))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def det(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**j*v*det([row[:j]+row[j+1:] for row in A[1:]]) for j,v in enumerate(A[0]))
def alpha(l):return EPS*(-F(3,4)+l/F(2))
def full_formula(params):
    p1,p2,q1,q2,qb,r,k1,k2,l1,l2=params
    return -F(33,8)+sum(F(13,16)*p-p*q/F(8)+q/F(8)+alpha(l)*(1-p)*(1-q)*(1-k)/F(8)
        for p,q,k,l in ((p1,q1,k1,l1),(p2,q2,k2,l2)))-qb/F(4)+F(5,2)*r
def lr_formula(p,q,r,k,l):
    return -F(33,8)+F(13,8)*p-p*q/F(4)+F(5,2)*r+2*alpha(l)*(1-p)*(1-q)*(1-k)/F(8)
def main():
    full_h=[];lr_h=[]
    for bits in product((Z,U),repeat=10):
        obs=observe(bits); h=dot(H,obs)
        assert h==full_formula(bits),(bits,h,full_formula(bits))
        full_h.append((h,bits,obs))
    for bits in product((Z,U),repeat=5):
        obs=lr(*bits);h=dot(H,obs)
        assert h==lr_formula(*bits),(bits,h,lr_formula(*bits))
        lr_h.append((h,bits,obs))
    assert min(v[0] for v in full_h)==-F(143,32)
    assert min(v[0] for v in lr_h)==-F(135,32)
    assert min(v[0] for v in lr_h)-min(v[0] for v in full_h)==F(1,4)
    O0=lr(Z,Z,Z,U,U)
    Op=lr(U,Z,Z,U,U)
    Oq=lr(Z,U,Z,U,U)
    Opq=lr(U,U,Z,U,U)
    Or=lr(Z,Z,U,U,U)
    B=sub(Op,O0);C=sub(Oq,O0)
    D=tuple(Opq[i]-Op[i]-Oq[i]+O0[i] for i in range(4))
    E=sub(Or,O0)
    rank_det=det([list(B),list(C),list(D),list(E)])
    assert abs(rank_det)==F(59,20480),rank_det
    w=observe((Z,Z,Z,Z,U,Z,Z,Z,Z,Z))
    assert dot(H,w)==-F(143,32)
    print('K=(3,8/5), L=(4,12/5), epsilon=1/2; true shared behavioral key L')
    print('K high nature probabilities P=3/4,Q=1/2; low P=1/4,Q=1/2')
    print('alpha_i(l_i)= -3/8 + l_i/4; l_i in [0,1]')
    print('full_deterministic_vertices=1024; lr_deterministic_vertices=32')
    print('all exact P/Q masses normalized; full and LR H formulas checked on vertices')
    print(f'min_FULL_H={-F(143,32)}; min_LR_H={-F(135,32)}; signed_gap={F(1,4)}')
    print(f'full_witness={w}; H(witness)={dot(H,w)}; Linf_distance_lower={F(1,72)}')
    print(f'LR_rank4_det={rank_det} ; abs={abs(rank_det)}')
    print('PASS_EXACT_R5_FOURTH_SHARED_BEHAVIOR_ISOLATED_TAIL_NO_GO')
if __name__=='__main__':main()

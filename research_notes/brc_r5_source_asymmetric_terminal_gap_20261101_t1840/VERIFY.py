#!/usr/bin/env python3
"""Exact BRC-style positive two-law flow for source-asymmetric K terminal tails.
This is an auxiliary stopping model, not a native X6 execution.
"""
from fractions import Fraction as F
from itertools import product

Z, U = F(0), F(1)
H = (F(5), Z, F(5), F(-8))
PAIRS = ((F(1,4), F(1,2)), (F(3,4), F(1,4)), (F(1,4), F(3,4)))

def obs(full, eps, tails):
    p1,p2,q1,q2,qb,r,k1,k2 = full
    out, total = [Z,Z,Z,Z], [Z,Z]
    def leaf(mp,mq,answer,t):
        total[0] += mp; total[1] += mq
        if answer == 'P': out[0] += mp
        else: out[1] += mq
        out[2] += mp*t; out[3] += mq*t
    for p,q,k,(a,b,h) in ((p1,q1,k1,tails[0]),(p2,q2,k2,tails[1])):
        ip=iq=F(1,8)
        leaf(ip*p,iq*p,'P',1)
        cp,cq=ip*(1-p),iq*(1-p)
        leaf(cp*F(1,2),cq*F(3,4),'Q',2)
        lp,lq=cp*F(1,2),cq*F(1,4)
        leaf(lp*q,lq*q,'P',2)
        lp,lq=lp*(1-q),lq*(1-q)
        leaf(lp*F(3,5),lq*F(1,2),'Q',3)
        kp,kq=lp*F(2,5),lq*F(1,2)
        leaf(kp*(1-eps),kq*(1-eps),'P',3)
        leaf(kp*eps*k,kq*eps*k,'P',3)
        kp,kq=kp*eps*(1-k),kq*eps*(1-k)
        leaf(kp*a,kq*b,'Q',4)
        leaf(kp*(1-a),kq*(1-b),'P',3+h)
    leaf(F(1,4)*qb,F(1,8)*qb,'P',2)
    leaf(F(1,4)*(1-qb),F(1,8)*(1-qb),'P',3)
    leaf(F(1,2)*r,F(5,8)*r,'Q',1)
    leaf(F(1,2)*(1-r),F(5,8)*(1-r),'P',3)
    assert total==[U,U], total
    return tuple(out)

def lr(p,q,r,k,eps,tails):
    return obs((p,p,q,q,q,r,k,k),eps,tails)

def inner(x,y):return sum(a*b for a,b in zip(x,y))
def minus(x,y):return tuple(a-b for a,b in zip(x,y))

def determinant(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**j*a*determinant([row[:j]+row[j+1:] for row in A[1:]]) for j,a in enumerate(A[0]))

def alpha(eps,tail):
    a,b,h=tail
    return eps*(b*(h-1)-a*h)

def full_H(full,as_):
    p1,p2,q1,q2,qb,r,k1,k2=full
    return -F(33,8)+sum(F(13,16)*p-p*q/F(8)+q/F(8)+a*(1-p)*(1-q)*(1-k)/F(8)
        for p,q,k,a in ((p1,q1,k1,as_[0]),(p2,q2,k2,as_[1]))) - qb/F(4)+F(5,2)*r

def lr_H(p,q,r,k,as_):
    return -F(33,8)+F(13,8)*p-p*q/F(4)+F(5,2)*r+sum(as_)*(1-p)*(1-q)*(1-k)/F(8)

def expected(as_):
    mnfull=-F(35,8)+sum(min(Z,a) for a in as_)/F(8)
    mnlr=-F(33,8)+min(Z,sum(as_))/F(8)
    gap=mnlr-mnfull
    assert gap==F(1,4)+(min(Z,sum(as_))-sum(min(Z,a) for a in as_))/F(8)
    assert gap>=F(1,4)
    return mnfull,mnlr,gap

def check_case(eps,tails):
    as_=tuple(alpha(eps,t) for t in tails)
    fullvals=[];lrvals=[]
    for bits in product((Z,U), repeat=8):
        o=obs(bits,eps,tails)
        score=inner(H,o)
        assert score==full_H(bits,as_), (eps,tails,bits,score,full_H(bits,as_))
        fullvals.append(score)
    for p,q,r,k in product((Z,U), repeat=4):
        o=lr(p,q,r,k,eps,tails)
        score=inner(H,o)
        assert score==lr_H(p,q,r,k,as_), (eps,tails,p,q,r,k)
        lrvals.append(score)
    mf,ml,gap=expected(as_)
    assert min(fullvals)==mf and min(lrvals)==ml
    assert min(lrvals)-min(fullvals)==gap
    O0=lr(Z,Z,Z,U,eps,tails)
    Op=lr(U,Z,Z,U,eps,tails)
    Oq=lr(Z,U,Z,U,eps,tails)
    Opq=lr(U,U,Z,U,eps,tails)
    Or=lr(Z,Z,U,U,eps,tails)
    B,C,D,E=minus(Op,O0),minus(Oq,O0),tuple(Opq[i]-Op[i]-Oq[i]+O0[i] for i in range(4)),minus(Or,O0)
    assert abs(determinant([list(B),list(C),list(D),list(E)]))==F(59,20480)
    return as_,mf,ml,gap

def main():
    count=0;opposite=0
    for eps in (F(1,3),F(1,2)):
        for pair1,pair2,h1,h2 in product(PAIRS,PAIRS,(2,4),(2,4)):
            tails=((pair1[0],pair1[1],h1),(pair2[0],pair2[1],h2))
            as_,mf,ml,gap=check_case(eps,tails)
            opposite+=as_[0]*as_[1]<0
            count+=1
    eps=F(1,2)
    tails=((F(3,4),F(1,4),2),(F(1,4),F(3,4),6))
    as_,mf,ml,gap=check_case(eps,tails)
    witness=obs((Z,Z,Z,Z,U,Z,Z,U),eps,tails)
    assert as_==(-F(5,8),F(9,8))
    assert (mf,ml,gap)==(-F(285,64),-F(33,8),F(21,64))
    assert inner(H,witness)==mf
    assert gap/F(18)==F(7,384)
    print('H=(5,0,5,-8); norm1=18; K=(3,8/5)')
    print('alpha_i=epsilon*(b_i*(h_i-1)-a_i*h_i)')
    print('min_FULL_H=-35/8+(min(0,alpha1)+min(0,alpha2))/8')
    print('min_LR_H=-33/8+min(0,alpha1+alpha2)/8')
    print('signed_gap=1/4+[min(0,alpha1+alpha2)-min(0,alpha1)-min(0,alpha2)]/8 >= 1/4')
    print(f'exact_grid_cases={count}; opposite_sign_cases={opposite}; vertex_observations={count*272+272}')
    print('rank_abs_det_kstop=59/20480')
    print(f'example_alpha={as_}; full_min={mf}; lr_min={ml}; gap={gap}; full_witness={witness}')
    print('example_distance_Linf_lower=7/384; universal_distance_Linf_lower=1/72')
    print('PASS_EXACT_R5_SOURCE_ASYMMETRIC_THIRD_KEY_GAP_MONOTONICITY')

if __name__=='__main__':main()

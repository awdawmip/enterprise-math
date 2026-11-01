#!/usr/bin/env python3
"""Independent positive two-law branch-flow verifier for the R5 third-key terminal change.
No external dependencies. Rational inputs and exact arithmetic throughout.
"""
from fractions import Fraction as F
from itertools import product

Z, U = F(0), F(1)
H = (F(5), Z, F(5), F(-8))

def obs(full, eps, a, b, h):
    p1,p2,q1,q2,qb,r,k1,k2 = full
    o = [Z,Z,Z,Z]
    total=[Z,Z]
    def leaf(mp,mq,answer,t):
        total[0] += mp; total[1] += mq
        if answer == 'P': o[0] += mp
        else: o[1] += mq
        o[2] += mp*t; o[3] += mq*t
    for p,q,k in ((p1,q1,k1),(p2,q2,k2)):
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
    assert total == [U,U], total
    return tuple(o)

def lr(p,q,r,k,eps,a,b,h):
    return obs((p,p,q,q,q,r,k,k),eps,a,b,h)

def inner(x,y):return sum(t*v for t,v in zip(x,y))
def diff(x,y):return tuple(t-v for t,v in zip(x,y))

def determinant(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**j*a*determinant([row[:j]+row[j+1:] for row in A[1:]]) for j,a in enumerate(A[0]))

def full_H(full,alpha):
    p1,p2,q1,q2,qb,r,k1,k2=full
    return (-F(33,8) +sum(F(13,16)*p-F(1,8)*p*q+q/F(8)+alpha/F(8)*(1-p)*(1-q)*(1-k)
            for p,q,k in ((p1,q1,k1),(p2,q2,k2))) -qb/F(4)+F(5,2)*r)

def lr_H(p,q,r,k,alpha):
    return (-F(33,8)+F(13,8)*p-p*q/F(4)+F(5,2)*r+alpha/F(4)*(1-p)*(1-q)*(1-k))

def main():
    count=0; verified_cases=0; signed=0
    vals=(F(1,4),F(1,2),F(3,4))
    for eps in (F(1,3),F(2,3)):
        for a,b,h in product(vals,vals,(2,3,7)):
            alpha=eps*(b*(h-1)-a*h)
            lv=[];fv=[]
            for p,q,r,k in product((Z,U),repeat=4):
                o=lr(p,q,r,k,eps,a,b,h)
                v=inner(H,o)
                assert v==lr_H(p,q,r,k,alpha), (eps,a,b,h,p,q,r,k,v)
                lv.append(v); count+=1
            for bits in product((Z,U),repeat=8):
                o=obs(bits,eps,a,b,h)
                v=inner(H,o)
                assert v==full_H(bits,alpha),(eps,a,b,h,bits,v)
                fv.append(v);count+=1
            delta=min(Z,alpha)/F(4)
            assert min(lv)==-F(33,8)+delta
            assert min(fv)==-F(35,8)+delta
            assert min(lv)-min(fv)==F(1,4)
            witness=(Z,Z,Z,Z,U,Z,Z if alpha<0 else U,Z if alpha<0 else U)
            Wo=obs(witness,eps,a,b,h)
            assert inner(H,Wo)==min(fv)
            O0=lr(Z,Z,Z,U,eps,a,b,h)
            Op=lr(U,Z,Z,U,eps,a,b,h)
            Oq=lr(Z,U,Z,U,eps,a,b,h)
            Opq=lr(U,U,Z,U,eps,a,b,h)
            Or=lr(Z,Z,U,U,eps,a,b,h)
            B,C,D,E=diff(Op,O0),diff(Oq,O0),tuple(Opq[i]-Op[i]-Oq[i]+O0[i] for i in range(4)),diff(Or,O0)
            det=determinant([list(B),list(C),list(D),list(E)])
            assert abs(det)==F(59,20480),det
            verified_cases+=1
            if a!=b:signed+=1
    eps,a,b,h=F(1,2),F(3,4),F(1,4),2
    gamma=b*(h-1)-a*h
    assert gamma==-F(5,4)
    assert (F(8,5)*a/b,F(8,5)*(1-a)/(1-b))==(F(24,5),F(8,15))
    assert -F(33,8)+eps*gamma/F(4)==-F(137,32)
    assert -F(35,8)+eps*gamma/F(4)==-F(145,32)
    print('H=(5,0,5,-8), ||H||_1=18')
    print('gamma=b*(h-1)-a*h; alpha=epsilon*gamma')
    print('all_real_min_LR_H=-33/8+min(0,alpha)/4')
    print('all_real_min_FULL_H=-35/8+min(0,alpha)/4')
    print('all_real_signed_gap=1/4, L_infinity_separation_lower=1/72')
    print('law_sensitive_example=(epsilon=1/2,a=3/4,b=1/4,h=2); min_LR=-137/32; min_FULL=-145/32')
    print(f'cases={verified_cases}; non_law_neutral_cases={signed}; exact_full_and_LR_corner_evaluations={count}')
    print('rank_det_abs_kstop=59/20480')
    print('PASS_EXACT_R5_LAW_SENSITIVE_ANSWER_CHANGING_THIRD_KEY_NO_GO')

if __name__=='__main__': main()

#!/usr/bin/env python3
"""Exact rational constructive decision certificates for the four-source K3 observer.
No floating point, no external packages. See RESEARCH.md for universal-real proof.
"""
from fractions import Fraction as F
from itertools import product

C = (F(1,8), F(1,6), F(1,16), F(3,32))
NAMES = ('C','I','BJ','IJ')
TOT = sum(C)

def q(x):
    return x if isinstance(x,F) else F(str(x))

def cv(xs):
    return tuple(q(x) for x in xs)

def observer(x,y,i,stages,r,v,p,qq):
    w = (C[0], C[1]*(1-x), C[2]*y, C[3]*i)
    d = w[2]+w[3]
    M = [w[s] if stages[s] >= 1 else F(0) for s in range(4)]
    Z = [F(2,3)*w[s] if stages[s] >= 2 else F(0) for s in range(4)]
    U = [Z[s] if stages[s] >= 3 else F(0) for s in range(4)]
    ep = F(107,128)-F(21,128)*x+d/4-sum(Z)/2+sum(p[s]*Z[s] for s in range(4))/8
    eq = F(13,64)+F(3,64)*x-d/2+sum(Z)/8+sum(qq[s]*Z[s] for s in range(4))/32
    tp = 3+sum(M)+F(3,2)*sum(Z)+sum(r[s]*U[s] for s in range(4))
    tq = 3+sum(M)/2+F(3,8)*sum(Z)+sum(v[s]*U[s] for s in range(4))/4
    return (ep,eq,tp,tq)

def vertices(r,v,p,qq):
    full=[]; lr=[]
    for x,i in ((F(0),F(0)),(F(0),F(1)),(F(1),F(0))):
        for y in (F(0), F(1)):
            for stages in product(range(4),repeat=4):
                full.append((observer(x,y,i,stages,r,v,p,qq), (x,y,i,stages)))
    for x,y in product((F(0),F(1)),repeat=2):
        i=(1-x)*y
        for stage in range(4):
            lr.append((observer(x,y,i,(stage,)*4,r,v,p,qq),(x,y,i,stage)))
    assert len(full)==1536 and len(lr)==16
    return full,lr

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def support(norm,vs):
    return max((dot(norm,vec),vec,which) for vec,which in vs)

def avg(weights,vals):
    return sum(w*v for w,v in zip(weights,vals))/sum(weights)

def choice(r,v,p,qq):
    """Return rational normal and structural case. A nonuniform profile has a separator."""
    mu=tuple((9+2*v[s])/(8*(3+r[s])) for s in range(4))
    all_clock=len(set(zip(r,v)))==1
    if not all_clock:
        lo=min(mu); hi=max(mu)
        if lo < F(3,8) and lo < hi:
            upper=min(F(3,8),hi)
            for k in range(2,30):
                t=lo+(upper-lo)/k
                if t not in mu:
                    D=frozenset(s for s in range(4) if t>mu[s])
                    assert D and len(D)<4
                    if D in (frozenset([0]),frozenset([0,1]),frozenset([0,2])):
                        return ('threshold_fiber_'+''.join(NAMES[s] for s in sorted(D)),(F(1,2),F(0),t,-F(1)),True)
                    return ('threshold_mask_'+''.join(NAMES[s] for s in sorted(D)),(F(0),F(0),t,-F(1)),False)
            raise AssertionError('failed rational threshold selection')
        if len(set(mu))==1:
            alpha=tuple(v[s]/(4*r[s]) for s in range(4))
            nu=tuple((3+2*v[s])/(4*(3+2*r[s])) for s in range(4))
            if all(v[s]>=r[s] for s in range(4)):
                assert min(nu)<max(nu)
                t=(min(nu)+max(nu))/2
                return ('equal_mu_nu', (F(0),F(0),-t,F(1)),False)
            if all(v[s]<=r[s] for s in range(4)):
                assert min(alpha)<max(alpha)
                t=(min(alpha)+max(alpha))/2
                return ('equal_mu_alpha',(F(0),F(0),-t,F(1)),False)
            return ('equal_mu_cross',(F(0),F(0),-F(1,4),F(1)),False)
        assert min(mu)>=F(3,8)
        nu=tuple((3+2*v[s])/(4*(3+2*r[s])) for s in range(4))
        alpha=tuple(v[s]/(4*r[s]) for s in range(4))
        if min(nu)<max(nu):
            t=(min(nu)+max(nu))/2
            return ('supercritical_nu',(F(0),F(0),-t,F(1)),False)
        assert min(alpha)<max(alpha)
        t=(min(alpha)+max(alpha))/2
        return ('supercritical_alpha',(F(0),F(0),t,-F(1)),False)
    if len(set(p))==1 and len(set(qq))==1:
        return ('actual_real_image_equal',None,False)
    r0=r[0]; v0=v[0]; pbar=avg(C,p); qbar=avg(C,qq)
    if v0<=r0:
        eps=F(1,100)
        if len(set(p))>1:
            return ('uniform_clock_p_le',(-eps,F(0),-F(1,4)-eps*(4-pbar)/12,F(1)),False)
        return ('uniform_clock_q_le',(F(0),eps,-F(1,4)-eps*(4+qbar)/48,F(1)),False)
    nu=(3+2*v0)/(4*(3+2*r0)); A=1+F(2,3)*r0
    eps=F(1,2)
    if len(set(p))>1:
        return ('uniform_clock_p_gt',(eps,F(0),-nu+eps*(4-pbar)/(12*A),F(1)),True)
    return ('uniform_clock_q_gt',(F(0),eps,-nu-eps*(4+qbar)/(48*A),F(1)),True)

def verify_case(label,r,v,p,qq):
    r,v,p,qq=map(cv,(r,v,p,qq))
    assert all(0<x<1 for k in (r,v,p,qq) for x in k)
    full,lr=vertices(r,v,p,qq)
    kind,n,small_eps=choice(r,v,p,qq)
    if n is None:
        # Direct ALL-REAL theorem: reconstruct every deterministic FULL policy.
        for V, (x,y,i,stages) in full:
            w=(C[0],C[1]*(1-x),C[2]*y,C[3]*i)
            d=w[2]+w[3]; W=sum(w)
            ms=sum(w[s] for s in range(4) if stages[s]>=1)
            zs=F(2,3)*sum(w[s] for s in range(4) if stages[s]>=2)
            us=F(2,3)*sum(w[s] for s in range(4) if stages[s]>=3)
            yp=d/(C[2]+C[3]*(1-x)); ip=(1-x)*yp
            zp=ms/W; tp=F(3,2)*zs/ms if ms else F(0); up=us/zs if zs else F(0)
            # Reconstruct without stage enumeration, preserving nested real weights.
            ww=(C[0],C[1]*(1-x),C[2]*yp,C[3]*ip)
            mm=sum(ww)*zp; zz=F(2,3)*mm*tp; uu=zz*up
            V2=(F(107,128)-F(21,128)*x+d/4-zz/2+p[0]*zz/8,
                F(13,64)+F(3,64)*x-d/2+zz/8+qq[0]*zz/32,
                3+mm+F(3,2)*zz+r[0]*uu,
                3+mm/2+F(3,8)*zz+v[0]*uu/4)
            assert V==V2
        return label,kind,'EQUAL_REAL_IMAGE',len(full),len(lr)
    halves=0
    while True:
        hf,V,wf=support(n,full); hl,_,wl=support(n,lr)
        if hf>hl:
            gap=hf-hl
            bound=gap/sum(abs(t) for t in n)
            assert gap>0 and bound>0
            return label,kind,str(gap),str(bound),halves
        if not small_eps:
            raise AssertionError((label,kind,'no strict separation',n,hf,hl))
        n=(n[0]/2,n[1]/2,n[2],n[3]) if kind.startswith('threshold_fiber') else (n[0]/2,n[1]/2,
              (-((3+2*v[0])/(4*(3+2*r[0]))) + (n[2]+((3+2*v[0])/(4*(3+2*r[0]))))/2),n[3])
        # For superdiagonal normals the clock coefficient tracks the halved epsilon.
        halves += 1

def run():
    ph=('1/4','1/3','2/3','3/4')
    qh=('3/4','1/5','2/5','4/5')
    uniform=('1/2',)*4
    models=[
      ('mask_BJ',('1/5','1/5','4/5','1/5'),('1/10','1/10','3/10','1/10'),ph,uniform),
      ('fiber_CBJ',('4/5','1/5','4/5','1/5'),('2/5','1/8','1/3','1/10'),ph,uniform),
      ('equal_mu_low',('1/2','3/5','3/4','9/10'),('1/6','3/10','1/2','7/10'),ph,qh),
      ('equal_mu_cross',('3/10','1/2','4/5','9/10'),('3/25','2/5','41/50','24/25'),ph,qh),
      ('equal_mu_high',('1/10','1/5','1/4','2/5'),('23/50','31/50','7/10','47/50'),ph,qh),
      ('super_nu',('1/10','1/5','3/10','2/5'),('1/5','2/5','3/5','4/5'),ph,qh),
      ('super_alpha',('1/10','1/5','3/10','2/5'),('21/50','27/50','33/50','39/50'),ph,qh),
      ('critical_mu',('1/5','1/3','1/2','3/5'),('3/10','1/2','3/4','9/10'),ph,qh),
      ('hetero_diagonal',('1/5','2/5','3/5','4/5'),('1/5','2/5','3/5','4/5'),ph,qh),
      ('uniform_p_low',('2/3',)*4,('1/3',)*4,ph,uniform),
      ('uniform_q_equal',('1/3',)*4,('1/3',)*4,uniform,qh),
      ('uniform_p_high',('1/5',)*4,('2/5',)*4,ph,uniform),
      ('uniform_q_high',('2/5',)*4,('4/5',)*4,uniform,qh),
      ('homogeneous_up',('1/5',)*4,('2/5',)*4,uniform,uniform),
      ('homogeneous_down',('4/5',)*4,('1/5',)*4,uniform,uniform),
    ]
    for args in models:
        print(' | '.join(map(str,verify_case(*args))))
    print('PASS_EXACT_R5_K3_GLOBAL_CLASSIFICATION_DECISION_CERTIFICATES')

if __name__=='__main__': run()

#!/usr/bin/env python3
"""K3 source-uniform clock: exact exposed-fiber separation, 2026-11-04.
Finite rational regression only; all-real theorem is given by the analytic proof.
"""
from fractions import Fraction as F
from itertools import product

C=(F(1,8),F(1,6),F(1,16),F(3,32))
CT=sum(C)
NAMES=('C','I','BJ','IJ')

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def observer(x,y,i,st,r,v,p,q):
    w=(C[0],(1-x)*C[1],y*C[2],i*C[3])
    d=w[2]+w[3]
    M=[w[s] if st[s]>=1 else F(0) for s in range(4)]
    Z=[F(2,3)*M[s] if st[s]>=2 else F(0) for s in range(4)]
    U=[Z[s] if st[s]==3 else F(0) for s in range(4)]
    ep=F(107,128)-F(21,128)*x+d/4-sum(Z)/2+sum(p[s]*Z[s] for s in range(4))/8
    eq=F(13,64)+F(3,64)*x-d/2+sum(Z)/8+sum(q[s]*Z[s] for s in range(4))/32
    tp=3+sum(M)+F(3,2)*sum(Z)+r*sum(U)
    tq=3+sum(M)/2+F(3,8)*sum(Z)+v*sum(U)/4
    return (ep,eq,tp,tq)

def experiment(r,v,p,q):
    assert 0<r<v<1
    assert all(F(0)<t<F(1) for t in p+q)
    full=[(observer(x,y,i,st,r,v,p,q),(x,y,i,st)) for x in (F(0),F(1))
          for y in (F(0),F(1)) for i in sorted({F(0),1-x})
          for st in product(range(4),repeat=4)]
    lr=[(observer(x,y,(1-x)*y,(st,)*4,r,v,p,q),(x,y,(1-x)*y,st))
        for x,y in product((F(0),F(1)),repeat=2) for st in range(4)]
    assert len(full)==1536 and len(lr)==16
    nu=(3+2*v)/(4*(3+2*r))
    assert F(1,4)<nu<F(1,2)
    n0=(F(0),F(0),-nu,F(1))
    hF=max(dot(w,n0) for w,_ in full)
    hL=max(dot(w,n0) for w,_ in lr)
    assert hF==hL
    h1=observer(F(0),F(1),F(1),(1,)*4,r,v,p,q)
    h3=observer(F(0),F(1),F(1),(3,)*4,r,v,p,q)
    assert dot(h1,n0)==hL==dot(h3,n0)
    lr_face={pol for w,pol in lr if dot(w,n0)==hL}
    assert lr_face=={(F(0),F(1),F(1),1),(F(0),F(1),F(1),3)},lr_face
    pb=sum(C[j]*p[j] for j in range(4))/CT
    qb=sum(C[j]*q[j] for j in range(4))/CT
    residues=[]
    for j in range(4):
        stage=tuple(3 if t==j else 1 for t in range(4))
        w=observer(F(0),F(1),F(1),stage,r,v,p,q)
        frac=C[j]/CT
        middle=tuple(h1[k]+frac*(h3[k]-h1[k]) for k in range(4))
        residue=tuple(w[k]-middle[k] for k in range(4))
        assert dot(w,n0)==hL
        assert w[2:]==middle[2:]
        assert residue==(C[j]*(p[j]-pb)/12,C[j]*(q[j]-qb)/48,F(0),F(0))
        residues.append(residue)
    assert any(z!=(F(0),)*4 for z in residues)==(len(set(p))>1 or len(set(q))>1)
    print('r=',r,'v=',v,'nu=',nu,'h_clock=',hL,'LR_face_two_endpoints_PASS')
    for j,z in enumerate(residues):print('  exposed_source',NAMES[j],'residual',z)
    for target,label in ((2,'P'),(1,'Q')):
        # eP is index 0, eQ is index 1; perturb the exact common-clock face.
        ix=0 if label=='P' else 1
        vals=p if ix==0 else q
        if len(set(vals))==1:continue
        eps=F(1,1024)
        beta=(4-pb)/12 if ix==0 else -(4+qb)/48
        delta=eps*beta/(1+F(2,3)*r)
        n=[F(0)]*4;n[ix]=eps;n[2]=-nu+delta;n[3]=F(1)
        n=tuple(n)
        maxf=max(dot(w,n) for w,_ in full)
        maxl=max(dot(w,n) for w,_ in lr)
        # The P perturbation favors larger p; Q favors larger q.
        expected=eps*sum(C[j]*max(F(0),(vals[j]-(pb if ix==0 else qb))/(12 if ix==0 else 48)) for j in range(4))
        assert maxf-maxl==expected,(label,maxf-maxl,expected)
        assert maxl==dot(h1,n)==dot(h3,n)
        witness=next((w,pol) for w,pol in full if dot(w,n)==maxf)
        print('  mixed_normal',label,n,'hF=',maxf,'hLR=',maxl,'gap=',maxf-maxl,
              'dist_inf_lower=',(maxf-maxl)/sum(abs(x) for x in n),'witness=',witness)
    return residues

if __name__=='__main__':
    pHet=(F(1,4),F(1,3),F(2,3),F(3,4))
    qHet=(F(3,4),F(2,3),F(1,3),F(1,4))
    uniform=(F(1,2),)*4
    for r,v in ((F(1,5),F(2,5)),(F(2,5),F(4,5))):
        for p,q in ((pHet,uniform),(uniform,qHet),(pHet,qHet),(uniform,uniform)):
            experiment(r,v,p,q)
    print('PASS_EXACT_R5_K3_SUPERDIAGONAL_UNIFORM_CLOCK_HETEROGENEOUS_ERROR_FIBER')

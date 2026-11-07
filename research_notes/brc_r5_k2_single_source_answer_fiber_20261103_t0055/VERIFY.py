#!/usr/bin/env python3
"""Exact rational verification of one source-conditioned K2-success answer coin.

Path probabilities are independently summed under P,Q.  The all-real support
claim is algebraic (RESEARCH.md); deterministic checks are exact regressions.
"""
from fractions import Fraction as F
from itertools import product

G = ('C', 'I', 'BJ', 'IJ', 'D')
MASS = {'C': F(1,4), 'I': F(1,4), 'BJ': F(1,8),
        'IJ': F(1,8), 'D': F(1,4)}
ALPHA = {'C': F(1,2), 'I': F(2,3), 'BJ': F(1,2), 'IJ': F(3,4)}
B = ALPHA['BJ']; I = ALPHA['IJ']; C = F(2,3)
N = 0

def ck(ok, label='check failed'):
    global N
    assert ok, label
    N += 1

def dot(u,v):
    return sum((a*b for a,b in zip(u,v)),F(0))

def flows(x,jb0,jb1,ji0,z,t):
    d=r1=r2=s=F(0)
    for flag,pf in ((0,1-x),(1,x)):
        for g in G[:4]:
            if flag and g in ('I','IJ'): continue
            w=pf*MASS[g]
            if g=='BJ':
                jb=jb1 if flag else jb0
                d+=w*(1-jb)*B
                w*=1-jb
            if g=='IJ':
                d+=w*(1-ji0)*I
                w*=1-ji0
            q=w*ALPHA[g]*z[(g,flag)]
            r1+=q
            r2+=C*q*t[(g,flag)]
            if g=='BJ':s+=C*q*t[(g,flag)]
    return x,d,r1,r2,s

def affine(x,d,r1,r2,s,eta):
    return (F(107,128)-F(21,128)*x+d/4-eta*s/8,
            F(13,64)+F(3,64)*x-d/2+eta*s/4,
            3+r1+r2,3+r1/2+r2/4)

def tree(x,jb0,jb1,ji0,z,t,eta):
    result={}
    for law in ('P','Q'):
        total=yes=time=F(0)
        def exit_at(w,at,q):
            nonlocal total,yes,time
            total+=w;yes+=w*q;time+=at*w
        for flag,pf in ((0,1-x),(1,x)):
            for g in G:
                w=pf*MASS[g]
                if g=='D':
                    exit_at(w,3,F(1,2));continue
                if flag and g in ('I','IJ'):
                    exit_at(w,3,F(1,2) if law=='P' else F(1,4));continue
                if g in ('BJ','IJ'):
                    jb=jb1 if flag else jb0
                    stop=jb if g=='BJ' else ji0
                    bet=B if g=='BJ' else I
                    exit_at(w*stop,3,bet*(F(1,4) if law=='P' else F(1,2)))
                    w*=1-stop
                p1=ALPHA[g] if law=='P' else ALPHA[g]/2
                p2=C if law=='P' else C/2
                w4=w*z[(g,flag)]*p1
                exit_at(w-w4,3,F(0))
                w5=w4*t[(g,flag)]*p2
                exit_at(w4-w5,4,F(0))
                qcoin=(eta/8 if law=='P' else eta) if g=='BJ' else F(0)
                exit_at(w5,5,qcoin)
        ck(total==1,f'probability mass normalization {law} {total}')
        result[law]=(yes,time)
    return (1-result['P'][0],result['Q'][0],result['P'][1],result['Q'][1])

def reduced_full(x,jb,ji,z4,t4,eta):
    z={(g,f):v for g,v in zip(G[:4],z4) for f in (0,1)}
    t={(g,f):v for g,v in zip(G[:4],t4) for f in (0,1)}
    return tree(x,jb,jb,ji,z,t,eta)

def lr(x,y,zv,tv,eta):
    z={(g,f):zv for g in G[:4] for f in (0,1)}
    t={(g,f):tv for g in G[:4] for f in (0,1)}
    return tree(x,1-y,1-y,1-y,z,t,eta)

def recover(obs):
    ep,eq,tp,tq=obs
    vp=ep-F(107,128);vq=eq-F(13,64)
    x=(-vp/2-vq/4)/F(9,128)
    d=(-F(3,64)*vp-F(21,128)*vq)/F(9,128)
    u=tp-3;v=tq-3
    return x,d,4*v-u,2*u-4*v

def normal(eta):
    return (F(134,9),F(85,9),-2-eta/2,8+eta)

def full_vertices(eta):
    for bits in product((F(0),F(1)),repeat=11):
        x,jb,ji=bits[:3];z=bits[3:7];t=bits[7:]
        yield bits,reduced_full(x,jb,ji,z,t,eta)

def lr_vertices(eta):
    for bits in product((F(0),F(1)),repeat=4):
        yield bits,lr(*bits,eta)

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

# The two LR collision keys precede the new terminal answer coin.
for g in G[:4]:
    ck(0<ALPHA[g]<1 and 0<ALPHA[g]/2<1)
ck(0<C<1 and 0<C/2<1)
for eta in (F(1,16),F(1,4),F(1,2),F(3,4),F(7,8)):
    ck(0<eta/8<1 and 0<eta<1)
    n=normal(eta)
    ck(sum(map(abs,n))==(F(206,1)+9*eta)/6)
    # Fixed root/J/K policy is an exact, source-retaining FULL witness.
    w=reduced_full(F(0),F(0),F(0),(F(1),)*4,
                   (F(0),F(0),F(1),F(0)),eta)
    ck(w==(F(7,8)-eta/192,F(1,8)+eta/96,F(335,96),F(207,64)))
    l=lr(F(0),F(1),F(1),F(0),eta)
    ck(l==(F(7,8),F(1,8),F(331,96),F(619,192)))
    full=list(full_vertices(eta)); restricted=list(lr_vertices(eta))
    ck(len(full)==2048 and len(restricted)==16)
    hF=max(dot(n,o) for _,o in full)
    hL=max(dot(n,o) for _,o in restricted)
    ck(hF==dot(n,w) and hL==dot(n,l))
    ck(hF-hL==eta/96)
    ck((hF-hL)/sum(map(abs,n))==eta/(16*(206+9*eta)))
    for bits,ob in full:
        # Each reduced deterministic vertex is the observer of a genuine tree.
        ck(F(0)<=ob[0]<=1 and F(0)<=ob[1]<=1 and 3<=ob[2]<=5 and 3<=ob[3]<=5)
    for bits,ob in restricted:
        ck(F(0)<=ob[0]<=1 and F(0)<=ob[1]<=1)

# Compare derived affine path-flow formula to INDEPENDENT direct terminal-path sum,
# including root-flag-dependent J/K actions and nonbinary source policies.
for k in range(1,151):
    eta=(F(1,16),F(1,2),F(3,4))[k%3]
    x=F(k%7+1,9)
    jb0=F((2*k)%7+1,9);jb1=F((3*k)%8+1,10);ji0=F((5*k)%6+1,8)
    z={(g,f):F(((k+2*j+3*f)%8)+1,10) for j,g in enumerate(G[:4]) for f in (0,1)}
    t={(g,f):F(((3*k+j+2*f)%8)+1,10) for j,g in enumerate(G[:4]) for f in (0,1)}
    params=flows(x,jb0,jb1,ji0,z,t)
    direct=tree(x,jb0,jb1,ji0,z,t,eta)
    ck(direct==affine(*params,eta))
    xx,dd,r1,r2,s=params
    ck(recover(direct)==(x,dd-eta*s/2,r1,r2))
    ck(F(0)<=s<=r2 and 0<=r2<=C*r1)

# Full rank at one seedless interior policy; exact Jacobian of
# (x,d-eta*s/2,r1,r2) followed by invertible physical affine A.
for eta in (F(1,16),F(1,2),F(7,8)):
    H=F(5,24); dy=F(7,64);z=t=F(1,2);A=H+F(7,128)
    # Rows d',r1,r2; columns y,z,t at x=y=z=t=1/2.
    J=((dy-eta/192,-eta/192,-eta/192),
       (z*dy,A,F(0)),
       (C*z*t*dy,C*t*A,C*z*A))
    det=det3(J)
    ck(det==F(71407,28311552)-eta*F(505,5308416))
    ck(det>0)
    ck((-F(9,512))*det!=0)

print('PASS_EXACT_R5_K2_SUCCESS_SINGLE_SOURCE_ANSWER_FIBER')
print('exact_assertions=',N)
print('eta_samples=1/16,1/4,1/2,3/4,7/8')
print('reduced_full_vertices_per_sample=2048')
print('seedless_LR_vertices_per_sample=16')
print('adaptive_nonbinary_tree_samples=150')
print('universal_support_gap=eta/96 for all real 0<eta<1 (proved algebraically)')
print('example_eta=1/2 gap=1/192 distance_inf_lower_bound=1/6736')
print('symbolic_aux_Jdet=71407/28311552 - 505*eta/5308416')

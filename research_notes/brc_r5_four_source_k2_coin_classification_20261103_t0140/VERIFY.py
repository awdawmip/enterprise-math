#!/usr/bin/env python3
"""Finite-tree rational verifier: four-source K2 answer coins.
The all-real support classification is proved algebraically in RESEARCH.md;
this program exhausts deterministic observer vertices for pinned rational kernels
and independently checks adaptive real-behavioural path-flow equations.
"""
from fractions import Fraction as F
from itertools import product

G=('C','I','BJ','IJ','D')
M={'C':F(1,4),'I':F(1,4),'BJ':F(1,8),'IJ':F(1,8),'D':F(1,4)}
A={'C':F(1,2),'I':F(2,3),'BJ':F(1,2),'IJ':F(3,4)}
C=F(2,3)
QSTAR=(F(1,8),F(1,6),F(1,16),F(3,32))
AMAX=sum(QSTAR,F(0));DMAX=F(5,32)
N=0

def check(x,msg='check failed'):
    global N
    assert x,msg
    N+=1

def dot(u,v):return sum((a*b for a,b in zip(u,v)),F(0))

def tree(x,jb0,jb1,ji0,z,t,eta):
    """Independent terminal-path mass sum, both laws; includes adaptive flags."""
    ans={}
    for law in ('P','Q'):
        mass=yes=time=F(0)
        def exit_path(w,st,q):
            nonlocal mass,yes,time
            mass+=w;yes+=w*q;time+=w*st
        for flag,prob in ((0,1-x),(1,x)):
            for g in G:
                w=prob*M[g]
                if g=='D':
                    exit_path(w,3,F(1,2));continue
                if flag and g in ('I','IJ'):
                    exit_path(w,3,F(1,2) if law=='P' else F(1,4));continue
                if g in ('BJ','IJ'):
                    stop=(jb1 if flag else jb0) if g=='BJ' else ji0
                    beta=A[g]
                    exit_path(w*stop,3,beta*(F(1,4) if law=='P' else F(1,2)))
                    w*=1-stop
                p1=A[g]*(F(1) if law=='P' else F(1,2))
                p2=C*(F(1) if law=='P' else F(1,2))
                w4=w*z[g,flag]*p1
                exit_path(w-w4,3,F(0))
                w5=w4*t[g,flag]*p2
                exit_path(w4-w5,4,F(0))
                coin=eta[G.index(g)]*(F(1,8) if law=='P' else F(1))
                exit_path(w5,5,coin)
        check(mass==1,'non-normalized law '+law)
        ans[law]=(yes,time)
    return (1-ans['P'][0],ans['Q'][0],ans['P'][1],ans['Q'][1])

def flow(x,jb0,jb1,ji0,z,t,eta):
    """Independent source-labeled P-law continuation flow algebra."""
    d=r1=r2=s=F(0)
    for flag,prob in ((0,1-x),(1,x)):
        for j,g in enumerate(G[:4]):
            if flag and g in ('I','IJ'):continue
            w=prob*M[g]
            if g in ('BJ','IJ'):
                stop=(jb1 if flag else jb0) if g=='BJ' else ji0
                d+=w*(1-stop)*A[g]
                w*=1-stop
            q=w*A[g]*z[g,flag]
            ss=C*q*t[g,flag]
            r1+=q;r2+=ss;s+=eta[j]*ss
    return (x,d,r1,r2,s)

def model(x,d,r1,r2,s):
    return (F(107,128)-F(21,128)*x+d/4-s/8,
            F(13,64)+F(3,64)*x-d/2+s/4,
            3+r1+r2,3+r1/2+r2/4)

def recover(o):
    ep,eq,tp,tq=o
    vp=ep-F(107,128);vq=eq-F(13,64)
    return ((-vp/2-vq/4)/F(9,128),
            (-F(3,64)*vp-F(21,128)*vq)/F(9,128),
            4*(tq-3)-(tp-3),2*(tp-3)-4*(tq-3))

def full(bits,eta):
    x,jb,ji=bits[:3];zs=bits[3:7];ts=bits[7:11]
    z={(g,f):v for g,v in zip(G[:4],zs) for f in (0,1)}
    t={(g,f):v for g,v in zip(G[:4],ts) for f in (0,1)}
    return tree(x,jb,jb,ji,z,t,eta)

def lr(x,y,zv,tv,eta):
    z={(g,f):zv for g in G[:4] for f in (0,1)}
    t={(g,f):tv for g in G[:4] for f in (0,1)}
    return tree(x,1-y,1-y,1-y,z,t,eta)

def mean(eta):return dot(QSTAR,eta)/AMAX

def normal(eta):
    v=mean(eta)
    return (-F(2,3),-F(7,3),-1+v,4-2*v)

def predicted_gap(eta):
    v=mean(eta)
    return sum((q*max(v-u,F(0)) for q,u in zip(QSTAR,eta)),F(0))/3

check(AMAX==F(43,96) and DMAX==F(5,32))
for g in G[:4]:check(0<A[g]<1 and 0<A[g]/2<1)
check(0<C<1 and 0<C/2<1)
SAMPLES=((F(1,4),F(1,2),F(3,4),F(1,2)),
         (F(1,2),)*4,
         (F(1,8),F(1,3),F(3,5),F(7,8)),
         (F(3,4),F(1,4),F(1,2),F(2,3)),
         (F(1,4),F(3,4),F(3,4),F(3,4)))
for eta in SAMPLES:
    for u in eta:check(0<u<1 and 0<u/8<1)
    mu=mean(eta);n=normal(eta)
    check(sum(map(abs,n))==8-3*mu)
    vertF=[(bits,full(bits,eta)) for bits in product((F(0),F(1)),repeat=11)]
    vertL=[(bits,lr(*bits,eta)) for bits in product((F(0),F(1)),repeat=4)]
    check(len(vertF)==2048 and len(vertL)==16)
    hF=max(dot(n,o) for _,o in vertF)
    hL=max(dot(n,o) for _,o in vertL)
    gap=predicted_gap(eta)
    check(hF-hL==gap)
    check((gap==0)==(len(set(eta))==1))
    # Constructive maximizer: x=0, all J continue, all K1 continue;
    # K2 source controls select eta_j below the face-weighted mean.
    tv=tuple(F(int(u<mu)) for u in eta)
    witness=full((F(0),F(0),F(0))+(F(1),)*4+tv,eta)
    check(dot(n,witness)==hF)
    check(dot(n,lr(F(0),F(1),F(1),F(0),eta))==hL)
    if eta==SAMPLES[0]:
        print('example_eta=',tuple(map(str,eta)))
        print('weighted_mean=',mu,'gap=',gap,'witness=',tuple(map(str,witness)))
        print('normal=',tuple(map(str,n)),'hFULL=',hF,'hLR=',hL)
        print('distance_inf_lower_bound=',gap/sum(map(abs,n)))
    for _,o in vertF:
        check(0<=o[0]<=1 and 0<=o[1]<=1 and 3<=o[2]<=5 and 3<=o[3]<=5)
    for _,o in vertL:
        check(0<=o[0]<=1 and 0<=o[1]<=1)

for k in range(1,121):
    eta=SAMPLES[k%len(SAMPLES)]
    x=F(k%7+1,9)
    jb0=F((2*k)%7+1,9);jb1=F((3*k)%8+1,10);ji0=F((5*k)%6+1,8)
    z={(g,f):F(((k+2*j+3*f)%8)+1,10) for j,g in enumerate(G[:4]) for f in (0,1)}
    t={(g,f):F(((3*k+j+2*f)%8)+1,10) for j,g in enumerate(G[:4]) for f in (0,1)}
    x0,d,r1,r2,s=flow(x,jb0,jb1,ji0,z,t,eta)
    obs=tree(x,jb0,jb1,ji0,z,t,eta)
    check(obs==model(x0,d,r1,r2,s))
    check(recover(obs)==(x0,d-s/2,r1,r2))
    check(0<=r2<=C*r1)
    if len(set(eta))==1:
        y=32*d/(5-3*x)
        h=F(1,8)+(1-x)/6
        zz=r1/(h+d)
        tt=r2/(C*r1) if r1 else F(0)
        check(all(0<=v<=1 for v in (y,zz,tt)))
        check(lr(x,y,zz,tt,eta)==obs)

# Uniform-coins LR Jacobian factorization, including the physical determinant.
x=y=z=t=F(1,2)
h=F(1,8)+(1-x)/6
D=(5-3*x)*y/32
jdet=(5-3*x)/32*(h+D)*(C*z*(h+D))
check(jdet>0 and (-F(9,512))*jdet!=0)
print('PASS_EXACT_R5_FOUR_SOURCE_K2_COIN_CLASSIFICATION')
print('exact_assertions=',N)
print('rational_kernel_vectors=',len(SAMPLES))
print('FULL_deterministic_vertices_per_vector=2048')
print('LR_deterministic_vertices_per_vector=16')
print('adaptive_nonbinary_independent_path_checks=120')
print('all_real_support_gap= (1/6)*sum_s(qstar_s*abs(eta_s-mean))')
print('equal_hulls_iff_all_four_eta_equal; in_that_case_actual_images_equal')
print('uniform_LR_auxiliary_Jacobian=',jdet)

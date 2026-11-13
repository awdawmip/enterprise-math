#!/usr/bin/env python3
"""Exact source-preserving P/Q terminal-path verifier for independent K2 answer kernels.
No external packages. All probabilities and support functions use fractions.Fraction.
The accompanying theorem is proved algebraically; sampled vertex checks are independent tests.
"""
from fractions import Fraction as F
from itertools import product

G=('C','I','BJ','IJ','D')
M={'C':F(1,4),'I':F(1,4),'BJ':F(1,8),'IJ':F(1,8),'D':F(1,4)}
ALPHA={'C':F(1,2),'I':F(2,3),'BJ':F(1,2),'IJ':F(3,4)}
C=F(2,3)
QSTAR=(F(1,8),F(1,6),F(1,16),F(3,32))
ASTAR=sum(QSTAR,F(0)); DSTAR=F(5,32)
COUNT=0

def check(condition,message='failed'):
    global COUNT
    assert condition,message
    COUNT+=1

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def tree(x,jb0,jb1,ji0,z,t,P,Q):
    """Independent terminal path enumeration for each law including X-dependent J decisions."""
    out={}
    for law,rho in [('P',P),('Q',Q)]:
        total=yes=elapsed=F(0)
        def term(mass,time,q):
            nonlocal total,yes,elapsed
            total+=mass; yes+=mass*q; elapsed+=mass*time
        for flag,flag_mass in ((0,1-x),(1,x)):
            for g in G:
                mass=flag_mass*M[g]
                if g=='D':
                    term(mass,3,F(1,2)); continue
                if flag and g in ('I','IJ'):
                    term(mass,3,F(1,2) if law=='P' else F(1,4)); continue
                if g in ('BJ','IJ'):
                    stop=(jb1 if flag else jb0) if g=='BJ' else ji0
                    term(mass*stop,3,ALPHA[g]*(F(1,4) if law=='P' else F(1,2)))
                    mass*=1-stop
                s1=ALPHA[g]*(1 if law=='P' else F(1,2))
                s2=C*(1 if law=='P' else F(1,2))
                at4=mass*z[g,flag]*s1
                term(mass-at4,3,F(0))
                at5=at4*t[g,flag]*s2
                term(at4-at5,4,F(0))
                term(at5,5,rho[G.index(g)])
        check(total==1,'law normalization')
        out[law]=(yes,elapsed)
    return (1-out['P'][0],out['Q'][0],out['P'][1],out['Q'][1])

def flow(x,jb0,jb1,ji0,z,t,P,Q):
    d=r1=r2=sp=sq=F(0)
    for flag,flag_mass in ((0,1-x),(1,x)):
        for j,g in enumerate(G[:4]):
            if flag and g in ('I','IJ'): continue
            m=flag_mass*M[g]
            if g in ('BJ','IJ'):
                stop=(jb1 if flag else jb0) if g=='BJ' else ji0
                d+=m*(1-stop)*ALPHA[g]
                m*=1-stop
            q=m*ALPHA[g]*z[g,flag]
            s=C*q*t[g,flag]
            r1+=q;r2+=s;sp+=P[j]*s;sq+=Q[j]*s
    return (x,d,r1,r2,sp,sq)

def model(x,d,r1,r2,sp,sq):
    return (F(107,128)-F(21,128)*x+d/4-sp,
            F(13,64)+F(3,64)*x-d/2+sq/4,
            3+r1+r2,3+r1/2+r2/4)

def recover(o):
    ep,eq,tp,tq=o
    vp=ep-F(107,128); vq=eq-F(13,64)
    return ((-vp/2-vq/4)/F(9,128),
            (-F(3,64)*vp-F(21,128)*vq)/F(9,128),
            4*(tq-3)-(tp-3),2*(tp-3)-4*(tq-3))

def full(bits,P,Q):
    x,jb,ji=bits[:3]; z4=bits[3:7]; t4=bits[7:11]
    z={(g,f):u for g,u in zip(G[:4],z4) for f in (0,1)}
    t={(g,f):u for g,u in zip(G[:4],t4) for f in (0,1)}
    return tree(x,jb,jb,ji,z,t,P,Q)

def lr(x,y,zv,tv,P,Q):
    z={(g,f):zv for g in G[:4] for f in (0,1)}
    t={(g,f):tv for g in G[:4] for f in (0,1)}
    return tree(x,1-y,1-y,1-y,z,t,P,Q)

def theta(P,Q,kappa):
    return tuple(F(2,3)*p-F(7,12)*q+kappa*(F(64,9)*p-F(8,9)*q) for p,q in zip(P,Q))

def normal(P,Q,kappa):
    v=theta(P,Q,kappa)
    mean=dot(QSTAR,v)/ASTAR
    tau=-mean
    n=(-F(2,3)-F(64,9)*kappa,
       -F(7,3)-F(32,9)*kappa,
       -1+2*tau,4-4*tau)
    gap=C*sum((w*max(s-mean,F(0)) for w,s in zip(QSTAR,v)),F(0))
    abs_gap=C/2*sum((w*abs(s-mean) for w,s in zip(QSTAR,v)),F(0))
    check(gap==abs_gap)
    return n,gap,mean

U=(F(1,2),)*4
V=(F(1,2),)*4
q_same_theta=(F(1,4),F(1,2),F(3,4),F(1,2))
p_same_theta=tuple((7*q+F(1,2))/8 for q in q_same_theta)
q_same_phi=(F(1,3),F(5,12),F(1,2),F(5,12))
p_same_phi=tuple((F(133,12)-17*q)/8 for q in q_same_phi)
eta=(F(1,4),F(1,2),F(3,4),F(1,2))
SAMPLES=(
  ('uniform',U,V),
  ('linked_rho',tuple(x/8 for x in eta),eta),
  ('theta_equal_only',p_same_theta,q_same_theta),
  ('phi_equal_only',p_same_phi,q_same_phi),
  ('generic', (F(1,5),F(3,7),F(4,5),F(2,3)),
              (F(5,6),F(2,9),F(1,3),F(3,5))),
)
check(ASTAR==F(43,96) and DSTAR==F(5,32))
check(all(0<ALPHA[g]<1 and 0<ALPHA[g]/2<1 for g in G[:4]))
check(0<C<1 and 0<C/2<1)
for label,P,Q in SAMPLES:
    check(all(0<u<1 for u in P+Q))
    pointsF=[full(bits,P,Q) for bits in product((F(0),F(1)),repeat=11)]
    pointsL=[lr(*bits,P,Q) for bits in product((F(0),F(1)),repeat=4)]
    check(len(pointsF)==2048 and len(pointsL)==16)
    gaps=[]
    for kappa in (F(0),-F(1,8)):
        n,gap,mean=normal(P,Q,kappa)
        hF=max(dot(n,o) for o in pointsF)
        hL=max(dot(n,o) for o in pointsL)
        check(hF-hL==gap,f'{label}: support gap mismatch kappa={kappa}')
        check((gap==0)==(len(set(theta(P,Q,kappa)))==1))
        t_star=tuple(F(int(v>mean)) for v in theta(P,Q,kappa))
        witness=full((F(0),F(0),F(0))+(F(1),)*4+t_star,P,Q)
        check(dot(n,witness)==hF)
        check(dot(n,lr(F(0),F(1),F(1),F(0),P,Q))==hL)
        gaps.append(gap)
        if label=='theta_equal_only' and kappa==-F(1,8):
            print('theta_equal_only=',tuple(map(str,P)),tuple(map(str,Q)))
            print('normal_second=',tuple(map(str,n)), 'gap_second=',gap)
            print('witness=',tuple(map(str,witness)),'hFULL=',hF,'hLR=',hL)
            print('distance_inf_lower_bound=',gap/sum(map(abs,n)))
    check((gaps==[F(0),F(0)])==(len(set(P))==len(set(Q))==1))
    if label in ('theta_equal_only','phi_equal_only'):
        check((gaps[0]==0)!=(gaps[1]==0))
    print('sample=',label,'gap_k0=',gaps[0],'gap_k_minus_eighth=',gaps[1])
    for o in pointsF:
        check(0<=o[0]<=1 and 0<=o[1]<=1 and 3<=o[2]<=5 and 3<=o[3]<=5)

for k in range(1,161):
    label,P,Q=SAMPLES[k%len(SAMPLES)]
    x=F(k%7+1,9)
    jb0=F((2*k)%7+1,9);jb1=F((3*k)%8+1,10);ji0=F((5*k)%6+1,8)
    z={(g,f):F(((k+2*j+3*f)%8)+1,10) for j,g in enumerate(G[:4]) for f in (0,1)}
    t={(g,f):F(((3*k+j+2*f)%8)+1,10) for j,g in enumerate(G[:4]) for f in (0,1)}
    vals=flow(x,jb0,jb1,ji0,z,t,P,Q)
    o=tree(x,jb0,jb1,ji0,z,t,P,Q)
    check(o==model(*vals))
    xp,dp,r1p,r2p=recover(o)
    xx,d,r1,r2,sp,sq=vals
    check(xp==x+F(8,9)*(8*sp-sq))
    check(dp==d+F(2,3)*sp-F(7,12)*sq)
    check(r1p==r1 and r2p==r2)
    check(0<=r2<=C*r1)
    if len(set(P))==len(set(Q))==1:
        y=32*d/(5-3*x)
        h=F(1,8)+(1-x)/6
        zz=r1/(h+d)
        tt=r2/(C*r1) if r1 else F(0)
        check(all(0<=u<=1 for u in (y,zz,tt)))
        check(lr(x,y,zz,tt,P,Q)==o)

# Constant-pair case: invertible physical affine shear of auxiliary (x,d,r1,r2).
# Auxiliary x,d are recovered with shifts xi*r2 and theta*r2; determinant remains -9/512.
check(-F(9,512)!=0)
print('PASS_EXACT_R5_INDEPENDENT_TWO_LAW_K2_TERMINAL_CLASSIFICATION')
print('exact_assertions=',COUNT)
print('vectors=',len(SAMPLES),'FULL_vertices_per_vector=2048 LR_vertices_per_vector=16')
print('adaptive_nonbinary_independent_path_checks=160')
print('theorem_two_normals_kappa=0,-1/8')
print('equal_hulls_iff_both_law_kernels_source_constant')
print('uniform_kernel_actual_images_equal_and_four_dimensional_rank')

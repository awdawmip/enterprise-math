#!/usr/bin/env python3
"""Exact four-observer post-K2 time-fork verifier (author-side, finite coverage).

Uses Python Fraction for deterministic extreme points and full terminal-path sums.
The all-real theorems are analytic results in the companion RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product

SOURCES = ('C', 'I', 'BJ', 'IJ')
MASS = dict(zip(SOURCES + ('D',), (F(1,4), F(1,4), F(1,8), F(1,8), F(1,4))))
ALPHA = (F(1,2), F(2,3), F(1,2), F(3,4))
C = F(2,3)
WSTAR = (F(1,8), F(1,6), F(1,16), F(3,32))
ASTAR = F(43,96)
DSTAR = F(5,32)
CHECKS = 0

def ck(condition, detail):
    global CHECKS
    assert condition, detail
    CHECKS += 1

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def physical(x,b,i,z,t,p,q,r):
    w = (F(1,4), (1-x)/4, b/8, i/8)
    q1 = tuple(w[k]*ALPHA[k]*z[k] for k in range(4))
    success = tuple(C*q1[k]*t[k] for k in range(4))
    d=b/16+3*i/32
    r1=sum(q1,F(0));r2=sum(success,F(0));delay=dot(success,r)
    return (F(107,128)-F(21,128)*x+d/4-dot(p,success),
            F(13,64)+F(3,64)*x-d/2+dot(q,success)/4,
            3+r1+r2+delay,3+r1/2+r2/4+delay/2)

def terminal_tree(x,jb0,jb1,ji0,z,t,p,q,r):
    """Independent path enumeration with history-dependent control and all terminal branches."""
    result={}
    for law in ('P','Q'):
        norm=yes=stop_time=F(0)
        def term(weight,time,answer_q):
            nonlocal norm,yes,stop_time
            norm+=weight;yes+=weight*answer_q;stop_time+=weight*time
        for flag,flag_mass in ((0,1-x),(1,x)):
            for g in SOURCES + ('D',):
                mass=flag_mass*MASS[g]
                if g=='D':
                    term(mass,3,F(1,2));continue
                k=SOURCES.index(g)
                if flag and g in ('I','IJ'):
                    term(mass,3,F(1,2) if law=='P' else F(1,4));continue
                if g in ('BJ','IJ'):
                    stop=(jb1 if flag else jb0) if g=='BJ' else ji0
                    term(mass*stop,3,ALPHA[k]*(F(1,4) if law=='P' else F(1,2)))
                    mass*=1-stop
                prob1=ALPHA[k]*(1 if law=='P' else F(1,2))
                prob2=C*(1 if law=='P' else F(1,2))
                at4=mass*z[g,flag]*prob1
                term(mass-at4,3,F(0))
                at5=at4*t[g,flag]*prob2
                term(at4-at5,4,F(0))
                delay=r[k]*(1 if law=='P' else 2)
                answer=(p if law=='P' else q)[k]
                term(at5*(1-delay),5,answer)
                term(at5*delay,6,answer)
        ck(norm==1,'total probability failure '+law)
        result[law]=(yes,stop_time)
    return (1-result['P'][0],result['Q'][0],result['P'][1],result['Q'][1])

def full(bits,p,q,r):
    x,jb,ji=map(F,bits[:3]);b=1-jb;i=(1-x)*(1-ji)
    z=tuple(map(F,bits[3:7])); t=tuple(map(F,bits[7:11]))
    return physical(x,b,i,z,t,p,q,r)

def lr(bits,p,q,r):
    x,y,z,t=map(F,bits)
    return physical(x,y,(1-x)*y,(z,)*4,(t,)*4,p,q,r)

def physical_to_XDUV(o):
    ep,eq,tp,tq=o
    vp=ep-F(107,128);vq=eq-F(13,64)
    X=(-vp/2-vq/4)/F(9,128)
    D=(-F(3,64)*vp-F(21,128)*vq)/F(9,128)
    U=4*(tq-3)-(tp-3)
    V=2*(tp-3)-4*(tq-3)
    return X,D,U,V

def expose(p,q,r,kappa):
    xi=tuple((64*ps-8*qs)/9 for ps,qs in zip(p,q))
    theta=tuple((8*ps-7*qs)/12 for ps,qs in zip(p,q))
    f=tuple(theta[k]+kappa*xi[k]+r[k] for k in range(4))
    mean=dot(WSTAR,f)/ASTAR
    n=(-F(2,3)-F(64,9)*kappa,-F(7,3)-F(32,9)*kappa,
       -1-2*mean,4+4*mean)
    gap=C/2*sum((w*abs(value-mean) for w,value in zip(WSTAR,f)),F(0))
    ck(gap==C*sum((w*max(value-mean,F(0)) for w,value in zip(WSTAR,f)),F(0)), 'gap center')
    return n,gap,f

ck(sum(WSTAR,F(0))==ASTAR,'source weights')
SAMPLES=[
    ('constant',(F(1,2),)*4,(F(1,2),)*4,(F(1,16),)*4),
    ('compensated',None,None,None),
    ('generic',(F(1,4),F(2,5),F(3,4),F(1,2)),
               (F(2,3),F(1,3),F(3,5),F(4,7)),
               (F(1,32),F(1,16),F(1,24),F(3,32))),
    ('vary_r',(F(1,2),)*4,(F(1,2),)*4,
              (F(1,64),F(3,64),F(1,16),F(5,64))),
]
DELTA=(F(0),F(1,256),-F(1,256),F(1,128))
P=tuple(F(1,2)+e for e in DELTA)
Q=tuple(F(1,2)+8*e for e in DELTA)
R=tuple(F(1,16)+4*e for e in DELTA)
SAMPLES[1]=('compensated',P,Q,R)
for label,p,q,r in SAMPLES:
    ck(all(F(0)<v<F(1) for v in p+q),'answer probability '+label)
    ck(all(F(0)<v<F(1,8) and F(0)<2*v<1 for v in r),'split probability '+label)
    VFULL=[full(bits,p,q,r) for bits in product((0,1),repeat=11)]
    VLR=[lr(bits,p,q,r) for bits in product((0,1),repeat=4)]
    ck(len(VFULL)==2048 and len(VLR)==16,'vertex count')
    for kappa in (F(0),-F(1,8)):
        n,gap,f=expose(p,q,r,kappa)
        ck(max(dot(n,o) for o in VFULL)-max(dot(n,o) for o in VLR)==gap,
           'signed exposing gap '+label+str(kappa))
        ck((gap==0)==(len(set(f))==1),'centered rigidity '+label+str(kappa))
        print('normal_gap',label,'kappa',kappa,'gap',gap)
    for o in VFULL:
        ck(F(0)<=o[0]<=1 and F(0)<=o[1]<=1 and 3<=o[2]<=6 and 3<=o[3]<=6,
           'physical range '+label)
    if label=='constant':
        for bits in product((0,1),repeat=11):
            x,jb,ji=map(F,bits[:3]);b=1-jb;i=(1-x)*(1-ji)
            z=tuple(map(F,bits[3:7]));t=tuple(map(F,bits[7:11]))
            w=(F(1,4),(1-x)/4,b/8,i/8)
            q1=[w[k]*ALPHA[k]*z[k] for k in range(4)]
            r1=sum(q1);r2=C*sum(q1[k]*t[k] for k in range(4));d=b/16+3*i/32
            y=32*d/(5-3*x)
            zz=r1/(F(1,8)+(1-x)/6+d)
            tt=r2/(C*r1) if r1 else F(0)
            ck(all(0<=e<=1 for e in (y,zz,tt)),'aggregation domain')
            ck(lr((x,y,zz,tt),p,q,r)==full(bits,p,q,r),'actual-image aggregation')
    print('sample',label,'FULL_deterministic',len(VFULL),'LR_deterministic',len(VLR))

# Exact new separating physical normal, where both earlier signed normals have zero gap.
N=(F(82,9),F(95,9),F(3),F(0))
allF=[full(bits,P,Q,R) for bits in product((0,1),repeat=11)]
allL=[lr(bits,P,Q,R) for bits in product((0,1),repeat=4)]
hf=max(dot(N,o) for o in allF)
hl=max(dot(N,o) for o in allL)
ck(hf-hl==F(23,2304),'new mixed normal gap')
witness=full((0,1,0,1,1,1,1,0,1,0,1),P,Q,R)
ck(dot(N,witness)==hf,'mixed normal witness')
ck(hf>hl,'actual separating witness')
print('compensation_delta',tuple(map(str,DELTA)))
print('p',tuple(map(str,P)),'q',tuple(map(str,Q)),'rP',tuple(map(str,R)),'rQ',tuple(str(2*x) for x in R))
print('new_normal',tuple(map(str,N)),'hFULL',hf,'hLR',hl,'exact_gap',hf-hl)
print('FULL_witness',tuple(map(str,witness)))
print('distance_Linf_lower', (hf-hl)/sum(map(abs,N)))

# Independent original-flag terminal enumeration, with nonbinary controls.
for k in range(1,161):
    _,p,q,r=SAMPLES[k%len(SAMPLES)]
    x=F((k%7)+1,9)
    jb0=F((2*k)%7+1,9);jb1=F((3*k)%8+1,10);ji0=F((5*k)%6+1,8)
    z={(g,f):F(((k+2*j+3*f)%8)+1,10) for j,g in enumerate(SOURCES) for f in (0,1)}
    t={(g,f):F(((3*k+j+2*f)%8)+1,10) for j,g in enumerate(SOURCES) for f in (0,1)}
    q1=[F(0)]*4;s=[F(0)]*4;b=F(0);i=F(0)
    for flag,flag_mass in ((0,1-x),(1,x)):
        for j,g in enumerate(SOURCES):
            if flag and g in ('I','IJ'):continue
            m=flag_mass*MASS[g]
            if g in ('BJ','IJ'):
                stop=(jb1 if flag else jb0) if g=='BJ' else ji0
                m*=1-stop
                if g=='BJ':b+=flag_mass*(1-stop)
                else:i+=flag_mass*(1-stop)
            mass=m*ALPHA[j]*z[g,flag]
            q1[j]+=mass;s[j]+=C*mass*t[g,flag]
    d=b/16+3*i/32
    obs=physical(x,b,i,tuple(F(1) for _ in SOURCES),tuple(F(0) for _ in SOURCES),p,q,r)
    r1=sum(q1);r2=sum(s);delay=dot(r,s)
    expected=(F(107,128)-F(21,128)*x+d/4-dot(p,s),
              F(13,64)+F(3,64)*x-d/2+dot(q,s)/4,
              3+r1+r2+delay,3+r1/2+r2/4+delay/2)
    actual=terminal_tree(x,jb0,jb1,ji0,z,t,p,q,r)
    ck(expected==actual,'independent full tree '+str(k))
    X,D,U,V=physical_to_XDUV(actual)
    xi=tuple((64*pp-8*qq)/9 for pp,qq in zip(p,q))
    theta=tuple((8*pp-7*qq)/12 for pp,qq in zip(p,q))
    ck(X==x+dot(xi,s) and D==d+dot(theta,s),'recovered answer coordinates')
    ck(U==r1+delay and V==r2,'recovered time coordinates')

print('PASS_EXACT_R5_POSTK2_LAW_COUPLED_SPLIT_RIGIDITY')
print('exact_assertions',CHECKS)
print('deterministic_FULL_per_kernel',2048,'LR',16,'kernel_sets',len(SAMPLES))
print('independent_nonbinary_terminal_path_checks',160)
print('full_real_scope', 'analytic proof in RESEARCH.md; program checks finite rational instances')

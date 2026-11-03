#!/usr/bin/env python3
"""Exact independent all-signed K3 support and fiber checks, standard-library Fraction."""
from fractions import Fraction as F
from itertools import product
Z=F(0); ONE=F(1); c=F(2,3)
alpha=(F(1,2),F(2,3),F(1,2),F(3,4))
VF=tuple((F(x),F(y),F(i)) for x,y,i in ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0)))
VL=tuple((F(x),F(y),F((1-x)*y)) for x,y in product(range(2),repeat=2))
B=(Z,ONE)
def weights(x,y,i):
    return (F(1,4),(1-x)/4,y/8,i/8)
def baseline(x,y,i):
    d=y/16+3*i/32
    return (F(107,128)-21*x/128+d/4,F(13,64)+3*x/64-d/2,F(3),F(3))
def observe(q,z,t,u,r,v):
    x,y,i=q
    w=weights(x,y,i)
    m=[w[s]*alpha[s]*z[s] for s in range(4)]
    S=[c*m[s]*t[s] for s in range(4)]
    U=[S[s]*u[s] for s in range(4)]
    eb=baseline(x,y,i)
    return (eb[0]-sum(S,Z)/2,eb[1]+sum(S,Z)/8,
            eb[2]+sum(m,Z)+F(3,2)*sum(S,Z)+sum((r[s]*U[s] for s in range(4)),Z),
            eb[3]+sum(m,Z)/2+F(3,8)*sum(S,Z)+sum((v[s]*U[s]/4 for s in range(4)),Z))
def dot(n,O):return sum((n[j]*O[j] for j in range(4)),Z)
def support(n,r,v):
    A,B,C,D=n;K=C+D/2
    H=-A/2+B/8+F(3,2)*C+F(3,8)*D
    J=[C*r[s]+D*v[s]/4 for s in range(4)]
    full=[]
    for q in VF:
        x,y,i=q;w=weights(x,y,i);base=dot(n,baseline(x,y,i))
        f=[max(Z,K,K+c*H,K+c*(H+J[s])) for s in range(4)]
        full.append(base+sum((w[s]*alpha[s]*f[s] for s in range(4)),Z))
    lr=[]
    for q in VL:
        x,y,i=q;w=weights(x,y,i);base=dot(n,baseline(x,y,i))
        T=sum((w[s]*alpha[s] for s in range(4)),Z)
        Jtot=sum((w[s]*alpha[s]*J[s] for s in range(4)),Z)
        lr.append(base+max(Z,K*T,(K+c*H)*T,(K+c*H)*T+c*Jtot))
    return max(full),max(lr)
def enumerate_vertices(r,v):
    op=[];ol=[]
    for q in VF:
        for settings in product(range(8),repeat=4):
            bits=[tuple(F((mask>>p)&1) for p in range(3)) for mask in settings]
            z=tuple(a[0] for a in bits);t=tuple(a[1] for a in bits);u=tuple(a[2] for a in bits)
            op.append(observe(q,z,t,u,r,v))
    for q in VL:
        for z,t,u in product(B,repeat=3):
            ol.append(observe(q,(z,)*4,(t,)*4,(u,)*4,r,v))
    return op,ol
def check(b,m):
    global assertions
    assertions+=1
    if not b:raise AssertionError(m)
def main():
    global assertions
    assertions=0
    r=(F(1,2),)*4;v=(F(1,4),F(1,2),F(3,4),F(1,2))
    norms=((Z,Z,-F(1,2),F(4)),(Z,Z,-ONE,F(4)),(ONE,Z,Z,Z),(Z,ONE,Z,Z),
           (ONE,ONE,F(3),-F(2)),(-ONE,F(2),F(1,3),F(3,2)),
           (F(3),-ONE,-F(3),ONE),(F(1,4),-F(2,3),F(4),-F(5,2)),
           (Z,Z,ONE,-F(4)),(F(9),F(11),F(5,7),-F(3)))
    fverts,lverts=enumerate_vertices(r,v)
    check(len(fverts)==24576,'FULL count');check(len(lverts)==32,'LR count')
    for n in norms:
        hf,hl=support(n,r,v)
        check(hf==max(dot(n,p) for p in fverts),f'FULL {n}')
        check(hl==max(dot(n,p) for p in lverts),f'LR {n}')
        check(hf>=hl,f'contain {n}')
    old=(Z,Z,-F(1,2),F(4));other=(Z,Z,-ONE,F(4))
    check(support(old,r,v)[0]-support(old,r,v)[1]==Z,'old zero')
    hf,hl=support(other,r,v);check(hf-hl==F(1,96),'new gap')
    q=(Z,ONE,ONE);z=t=(ONE,)*4
    W=observe(q,z,t,(Z,Z,ONE,Z),r,v);V=observe(q,z,t,(Z,)*4,r,v)
    check(dot(other,W)==hf,'FULL witness')
    check(dot(other,V)==hl,'LR witness')
    check(dot(other,W)-dot(other,V)==F(1,96),'witness gap')
    check(F(1,96)/sum(map(abs,other),Z)==F(1,480),'distance bound')
    S=[c*w*alpha[s] for s,w in enumerate(weights(*q))]
    vC=(S[0]*r[0],S[0]*v[0]/4);vBJ=(S[2]*r[2],S[2]*v[2]/4)
    det=vC[0]*vBJ[1]-vC[1]*vBJ[0]
    check(det==F(1,4608),'fiber determinant')
    rr=(F(1,4),F(1,3),F(3,5),F(2,3))
    vv=(F(2,5),F(3,4),F(1,3),F(1,4))
    F2,L2=enumerate_vertices(rr,vv)
    for n in norms:
        aa,bb=support(n,rr,vv)
        check(aa==max(dot(n,p) for p in F2),f'FULL second {n}')
        check(bb==max(dot(n,p) for p in L2),f'LR second {n}')
    print('PASS_EXACT_R5_K3_ALL_SIGNED_SUPPORT_AND_FIBER')
    print('FULL_DETERMINISTIC_PER_KERNEL',len(fverts))
    print('LR_DETERMINISTIC_PER_KERNEL',len(lverts))
    print('EXACT_ASSERTIONS',assertions)
    print('PREVIOUS_DIRECTION_GAP',support(old,r,v)[0]-support(old,r,v)[1])
    print('NEW_DIRECTION_FULL',hf,'LR',hl,'GAP',hf-hl)
    print('FULL_EXPOSED_W',*[str(x) for x in W])
    print('LR_EXPOSED_V',*[str(x) for x in V])
    print('DISTANCE_LINF_LOWER_BOUND',F(1,480))
    print('K3_C_GATE_INCREMENT',vC)
    print('K3_BJ_GATE_INCREMENT',vBJ)
    print('GATE_FIBER_DETERMINANT',det)
    print('NORMALS_PER_KERNEL',len(norms),'KERNELS',2)
if __name__=='__main__':main()

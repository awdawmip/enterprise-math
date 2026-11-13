#!/usr/bin/env python3
"""Exact finite observers and 2-class Markovization regression. Stdlib only."""
from fractions import Fraction as F
from itertools import product, permutations
from random import Random

Q_XU=((F(3,8),F(1,8)),(F(1,8),F(3,8)))
R_U=(F(3,4),F(5,4))
R_V3=(F(1,2),F(1),F(3,2))
T_X=(F(1,16),F(1,8))
EARLY=(F(1,2),)*2
MIDDLE=(F(1,2),)*2
LATE=(F(1,4),F(1,2),F(3,4))
TERMINAL=(F(1,2),)*3

def leaf_weights_three():
    q,p={},{}
    for x,u,v in product(range(2),range(2),range(3)):
        t=T_X[x]
        cond=((F(1,2)+t,F(1,2)-2*t,t) if u==0
              else (t,F(1,2)-2*t,F(1,2)+t))
        q[x,u,v]=Q_XU[x][u]*cond[v]
        p[x,u,v]=q[x,u,v]*R_V3[v]
    assert sum(q.values())==sum(p.values())==1
    assert min(q.values())>0 and min(p.values())>0
    for x,u in product(range(2),repeat=2):
        qm=sum(q[x,u,v] for v in range(3))
        pm=sum(p[x,u,v] for v in range(3))
        assert qm==Q_XU[x][u] and pm/qm==R_U[u]
    for x in range(2):
        ratio=sum(p[x,u,v] for u in range(2) for v in range(3))/F(1,2)
        assert ratio==(F(7,8),F(9,8))[x]
    return q,p
Q3,P3=leaf_weights_three()

def observe(weights,s,h,z,ax=EARLY,bu=MIDDLE,cv=LATE,dv=TERMINAL):
    ep=eq=tp=tq=F(0)
    for (x,u,v),q in weights[0].items():
        p=weights[1][x,u,v]
        ss=s[x]
        hh=h[x,u] if isinstance(h,dict) else h[u]
        zz=z[x,u,v] if isinstance(z,dict) else z[v]
        err=(1-ss)*ax[x]+ss*((1-hh)*bu[u]+hh*(zz*cv[v]+(1-zz)*dv[v]))
        time=2+ss*(1+hh*(2-zz))
        ep+=p*err; eq+=q*err; tp+=p*time; tq+=q*time
    return (ep,eq,tp,tq)

def determinant4(rows):
    total=F(0)
    for perm in permutations(range(4)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(4)
                         for j in range(i+1,4))
        a=F(sign)
        for i in range(4):a*=rows[i][perm[i]]
        total+=a
    return total

def check_three_class():
    bits_list=list(product((0,1),repeat=7))
    lr={b:observe((Q3,P3),b[:2],b[2:4],b[4:]) for b in bits_list}
    H=lambda o:o[0]-o[2]+o[3]
    lrmax=max(H(o) for o in lr.values())
    assert len(lr)==128 and lrmax==F(205,256)
    cells=tuple(product(range(2),range(2),range(3)))
    score=[]
    for x,u,v in cells:
        p,q=P3[x,u,v],Q3[x,u,v]
        options=[]
        for err,time in ((F(1,2),2),(F(1,2),3),(LATE[v],4),
                         (TERMINAL[v],5)):
            vec=(p*err,q*err,p*time,q*time)
            scaled=tuple(int(1024*y) for y in vec)
            assert all(F(z,1024)==a for z,a in zip(scaled,vec))
            options.append(scaled)
        score.append(options)
    maximum=-10**18
    for mask in range(1<<18):
        total=0
        for j,(x,u,v) in enumerate(cells):
            if ((mask>>x)&1)==0:choice=0
            elif ((mask>>(2+2*x+u))&1)==0:choice=1
            else:choice=2 if ((mask>>(6+j))&1) else 3
            ep,eq,tp,tq=score[j][choice]
            total+=ep-tp+tq
        maximum=max(maximum,total)
    assert maximum==821
    s=(F(1),F(1))
    h={(0,0):F(1),(0,1):F(0),(1,0):F(1),(1,1):F(1)}
    z={(x,u,v):F(int(v==2)) for x,u,v in cells}
    star=observe((Q3,P3),s,h,z)
    assert star==(F(617,1024),F(291,512),F(1095,256),F(573,128))
    assert H(star)==F(821,1024) and H(star)-lrmax==F(1,1024)
    obs=[lr[bits_list[i]] for i in (0,32,40,41,44)]
    mat=[[obs[j][i]-obs[0][i] for j in range(1,5)] for i in range(4)]
    det=determinant4(mat)
    assert det==F(135,4194304)
    print("THREE_CLASS_PATHS=12 LR_DETERMINISTIC=128 FULL_DETERMINISTIC=262144")
    print("THREE_CLASS_LR_RANK4_DET="+str(det))
    print("THREE_CLASS_LR_H_MAX="+str(lrmax))
    print("THREE_CLASS_FULL_H_MAX="+str(F(maximum,1024)))
    print("THREE_CLASS_EXPLICIT_FULL_O="+",".join(map(str,star)))
    print("THREE_CLASS_STRICT_GAP="+str(H(star)-lrmax))
    print("THREE_CLASS_LINF_DISTANCE_LOWER="+str((H(star)-lrmax)/3))

def check_binary_markovization():
    R_V2=(F(1,2),F(3,2))
    Q2={};P2={}
    for x,u,v in product(range(2),range(2),range(2)):
        prob=((F(3,4),F(1,4))[u] if v==0
              else (F(1,4),F(3,4))[u])
        Q2[x,u,v]=Q_XU[x][u]*prob
        P2[x,u,v]=Q2[x,u,v]*R_V2[v]
    assert sum(Q2.values())==sum(P2.values())==1
    ax=(F(1,5),F(4,5)); bu=(F(1,6),F(5,6))
    cv=(F(3,7),F(4,7)); dv=(F(2,9),F(7,9))
    rng=Random(26030)
    for _ in range(256):
        s=tuple(F(rng.randint(0,6),6) for x in range(2))
        h={(x,u):F(rng.randint(0,6),6)
           for x,u in product(range(2),repeat=2)}
        z={(x,u,v):F(rng.randint(0,6),6) for x,u,v in Q2}
        hm=[]
        for u in range(2):
            den=sum(Q_XU[x][u]*s[x] for x in range(2))
            num=sum(Q_XU[x][u]*s[x]*h[x,u] for x in range(2))
            hm.append(num/den if den else F(0))
        zm=[]
        for v in range(2):
            den=sum(Q2[x,u,v]*s[x]*h[x,u]
                    for x,u in product(range(2),repeat=2))
            num=sum(Q2[x,u,v]*s[x]*h[x,u]*z[x,u,v]
                    for x,u in product(range(2),repeat=2))
            zm.append(num/den if den else F(0))
        full=observe((Q2,P2),s,h,z,ax,bu,cv,dv)
        lr=observe((Q2,P2),s,tuple(hm),tuple(zm),ax,bu,cv,dv)
        assert full==lr,(full,lr)
    print("BINARY_LR_MARKOVIZATION_RATIONAL_TESTS=256")
    print("PASS_EXACT_R5_BINARY_LR_MARKOVIZATION_THREECLASS_THRESHOLD")

if __name__=="__main__":
    check_three_class()
    check_binary_markovization()

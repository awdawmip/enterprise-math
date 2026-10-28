#!/usr/bin/env python3
"""Exact rational test for finite two-law LR-fiber Markovization.
All states are external passive P/Q observation histories, not X6 dynamics.
"""
from fractions import Fraction as F
from collections import defaultdict

ZERO=F(0)
ONE=F(1)
Q_BASE=(F(1,4),F(1,2),F(1,4))
Q_B_PERT=(F(1,8),F(3,4),F(1,8))
R2=(F(1,2),F(1),F(3,2))
M3=(F(3,4),F(5,4))

# Each node maps to (t, likelihood ratio, Q mass conditional only on observation tree),
# with optional children. Raw tag is a distinct observed first-stage source.
def build(perturbed=False):
    nodes={}
    for tag in ('A','B'):
        h=(tag,)
        nodes[h]=(1,ONE,F(1,2),[])
        qrow=Q_B_PERT if perturbed and tag=='B' else Q_BASE
        assert sum(qrow)==1 and sum(q*r for q,r in zip(qrow,R2))==1
        children=[]
        for i,(q,r) in enumerate(zip(qrow,R2)):
            k=(tag,i)
            children.append(k)
            grandchildren=[]
            for j,m in enumerate(M3):
                c=(tag,i,j)
                grandchildren.append(c)
                nodes[c]=(3,r*m,F(1,2)*q*F(1,2),[])
            nodes[k]=(2,r,F(1,2)*q,grandchildren)
        nodes[h]=(1,ONE,F(1,2),children)
    assert sum(n[2] for h,n in nodes.items() if len(h)==1)==1
    for h,(t,r,q,children) in nodes.items():
        assert q>0 and r>0
        if children:
            assert sum(nodes[c][2] for c in children)==q
            assert sum(nodes[c][2]*nodes[c][1] for c in children)==q*r
    leaves=[(h,v) for h,v in nodes.items() if v[0]==3]
    assert len(leaves)==12
    assert sum(q for h,(t,r,q,chs) in leaves)==1
    assert sum(r*q for h,(t,r,q,chs) in leaves)==1
    return nodes

def full_actions():
    a={}
    a[('A',)]=(F(1,8),F(1,4),F(5,8))
    a[('B',)]=(F(1,3),F(1,6),F(1,2))
    t2=[((F(1,3),F(1,6),F(1,2)),(F(1,4),F(1,2),F(1,4))),
        ((F(1,5),F(2,5),F(2,5)),(F(1,3),F(1,3),F(1,3))),
        ((F(1,4),F(1,4),F(1,2)),(F(1,5),F(1,5),F(3,5)))]
    for i,(A,B) in enumerate(t2):
        a[('A',i)]=A
        a[('B',i)]=B
    zs={'A':((F(1,6),F(2,3)),(F(1,2),F(1,4)),(F(3,5),F(5,6))),
        'B':((F(3,4),F(1,3)),(F(2,5),F(4,5)),(F(1,7),F(2,7)))}
    for tag in ('A','B'):
        for i in range(3):
            for j in range(2):
                z=zs[tag][i][j]
                a[(tag,i,j)]=(z,1-z,ZERO)
    assert all(sum(row)==ONE and all(v>=0 for v in row) for row in a.values())
    return a

def enact(nodes,actions,by_fiber=False):
    """Compute Q and P joint stop-time/label and active LR-fiber masses."""
    mass={h:nodes[h][2] for h in nodes if len(h)==1}
    stopped={'P':defaultdict(lambda:ZERO),'Q':defaultdict(lambda:ZERO)}
    occupation={'P':defaultdict(lambda:ZERO),'Q':defaultdict(lambda:ZERO)}
    for t in (1,2,3):
        updated=defaultdict(lambda:ZERO)
        for h,w in mass.items():
            _,r,_,ch=nodes[h]
            sig=(t,r)
            for mu,massval in (('P',w*r),('Q',w)):
                occupation[mu][sig]+=massval
            a=actions[sig] if by_fiber else actions[h]
            assert sum(a)==1
            for mu,massval in (('P',w*r),('Q',w)):
                stopped[mu][(t,'P')]+=massval*a[0]
                stopped[mu][(t,'Q')]+=massval*a[1]
            if ch:
                for c in ch:
                    updated[c]+=w*a[2]*nodes[c][2]/nodes[h][2]
            else:
                assert a[2]==0
        mass=updated
    assert not mass
    assert all(sum(stopped[mu].values())==ONE for mu in ('P','Q'))
    obs=(sum(v for (t,lab),v in stopped['P'].items() if lab=='Q'),
         sum(v for (t,lab),v in stopped['Q'].items() if lab=='P'),
         sum(t*v for (t,lab),v in stopped['P'].items()),
         sum(t*v for (t,lab),v in stopped['Q'].items()))
    return obs,stopped,occupation

def markovize(nodes,actions):
    """Exact Q-reach weighted action average in each (time,LR) fiber."""
    weights={h:nodes[h][2] for h in nodes if len(h)==1}
    grouped=defaultdict(lambda:[ZERO,ZERO,ZERO,ZERO])
    for t in (1,2,3):
        nxt=defaultdict(lambda:ZERO)
        for h,w in weights.items():
            r=nodes[h][1]; a=actions[h]; row=grouped[(t,r)]
            row[0]+=w
            for k in range(3): row[k+1]+=w*a[k]
            for c in nodes[h][3]:
                nxt[c]+=w*a[2]*nodes[c][2]/nodes[h][2]
        weights=nxt
    return {s:tuple(v/W for v in row[1:])
            for s,row in grouped.items() if (W:=row[0])>0}

def tv(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))/2

def diameter(nodes,mu,t):
    by=defaultdict(list)
    for h,(stage,r,q,chs) in nodes.items():
        if stage!=t or not chs:continue
        dist=defaultdict(lambda:ZERO)
        for c in chs:
            _,rr,qq,_=nodes[c]
            val=qq/q
            if mu=='P': val*=rr/r
            dist[rr]+=val
        assert sum(dist.values())==1
        by[r].append(dist)
    max_tv=ZERO
    for r, rows in by.items():
        for d1 in rows:
            for d2 in rows:
                keys=set(d1)|set(d2)
                max_tv=max(max_tv,tv([d1[k] for k in keys],[d2[k] for k in keys]))
    return max_tv

def check(perturbed):
    nodes=build(perturbed)
    full=full_actions()
    lr=markovize(nodes,full)
    a,sa,oa=enact(nodes,full)
    b,sb,ob=enact(nodes,lr,True)
    dP=sum(diameter(nodes,'P',t) for t in (1,2))
    dQ=sum(diameter(nodes,'Q',t) for t in (1,2))
    assert dP==dQ==(F(1,4) if perturbed else ZERO)
    assert abs(a[0]-b[0])<=dP and abs(a[1]-b[1])<=dQ
    assert abs(a[2]-b[2])<=2*dP and abs(a[3]-b[3])<=2*dQ
    if not perturbed:
        assert a==b
        assert sa==sb
        assert oa==ob
    return len(nodes),len(lr),a,b,dP,dQ,lr

def generated_policy(nodes,seed):
    a={}
    for h,(t,r,q,children) in nodes.items():
        code=(1 if h[0]=='A' else 7)+11*(h[1] if len(h)>=2 else 0)+17*(h[2] if len(h)>=3 else 0)
        u=1+(seed+3*code)%13
        v=1+(2*seed+5*code)%11
        if t==3:
            a[h]=(F(u,u+v),F(v,u+v),ZERO)
        else:
            w=1+(3*seed+7*code)%17
            a[h]=(F(u,u+v+w),F(v,u+v+w),F(w,u+v+w))
    return a

def regression():
    count=0
    for perturbed in (False,True):
        nodes=build(perturbed)
        DP=sum(diameter(nodes,'P',t) for t in (1,2))
        DQ=sum(diameter(nodes,'Q',t) for t in (1,2))
        for seed in range(64):
            policy=generated_policy(nodes,seed)
            full,stopped,occ=enact(nodes,policy)
            obs,stop2,occ2=enact(nodes,markovize(nodes,policy),True)
            assert abs(full[0]-obs[0])<=DP and abs(full[1]-obs[1])<=DQ
            assert abs(full[2]-obs[2])<=2*DP and abs(full[3]-obs[3])<=2*DQ
            if not perturbed:
                assert full==obs and stopped==stop2 and occ==occ2
            count+=1
    return count

n,k,a,b,dP,dQ,lr=check(False)
print('STRONGLY LUMPABLE 3-stage model: nodes=',n,' LR fibers=',k)
print('all Q/P masses strictly positive, both laws normalized')
print('two-source collision at t=1 and three two-source nonterminal collisions at t=2')
print('exact fiber-weighted full observer:',a)
print('exact LR Markovized observer:',b)
print('per-time, per-fiber occupation and terminal (time,label) laws equal')
print('kernel diameters P/Q:',dP,dQ)
np,kp,ap,bp,pP,pQ,_=check(True)
print('PERTURBED model: nodes=',np,' LR fibers=',kp)
print('kernel diameters P/Q:',pP,pQ)
print('full observer:',ap)
print('LR Markovized observer:',bp)
print('coordinate absolute errors:',tuple(abs(x-y) for x,y in zip(ap,bp)))
print('certified signed support-error envelope for N=3: |lambda1|/4+|lambda2|/4+|lambda3|/2+|lambda4|/2')
print('deterministic exact regression full-policy inputs:',regression())
print('ALL EXACT TWO-LAW FIBER MARKOVIZATION CHECKS PASSED')

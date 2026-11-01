#!/usr/bin/env python3
"""Exact Fraction checks for the local-ray / global-hull R5 example."""
from fractions import Fraction as F
from itertools import product
S=('A','B')
PLOW={'A':F(1,8),'B':F(1,4)}
QLOW={'A':F(1,4),'B':F(1,2)}
W={
('A',True,'P'):(F(1,2),F(1,3),F(1,6)),
('A',True,'Q'):(F(1,2),F(1,3),F(1,6)),
('B',True,'P'):(F(1,2),F(1,6),F(1,3)),
('B',True,'Q'):(F(1,2),F(1,6),F(1,3)),
('A',False,'P'):(F(1,4),F(3,8),F(3,8)),
('A',False,'Q'):(F(3,4),F(1,8),F(1,8)),
('B',False,'P'):(F(3,4),F(1,8),F(1,8)),
('B',False,'Q'):(F(1,4),F(3,8),F(3,8))}
LK=('c','l','hA','hB')
FK=('cA','cB','lA','hA','lB','hB')
def succ(s,low,law):
    return sum(W[s,low,law][1:],F(0))
def obs(policy,lr=False):
    ep,eq,tp,tq=F(0),F(1),F(1),F(1)
    for s in S:
        c=policy['c'] if lr else policy['c'+s]
        if not c: continue
        tp+=c;tq+=c
        for low in (True,False):
            pm=F(1,2)*(PLOW[s] if low else 1-PLOW[s])
            qm=F(1,2)*(QLOW[s] if low else 1-QLOW[s])
            key=('l' if low else 'h'+s) if lr else (('l' if low else 'h')+s)
            a=policy[key]
            ep+=c*a*pm*succ(s,low,'P')
            eq-=c*a*qm*succ(s,low,'Q')
            tp+=c*a*pm;tq+=c*a*qm
    return ep,eq,tp,tq
def det4(rows):
    m=[list(map(F,r)) for r in rows]
    out=F(1)
    for j in range(4):
        p=next((i for i in range(j,4) if m[i][j]),None)
        if p is None: return F(0)
        if p!=j: m[j],m[p]=m[p],m[j];out=-out
        x=m[j][j];out*=x
        for i in range(j+1,4):
            c=m[i][j]/x
            for k in range(j+1,4):m[i][k]-=c*m[j][k]
            m[i][j]=F(0)
    return out
def run():
    for s in S:
        for v in (PLOW[s],QLOW[s]):assert 0<v<1
        for low,law in product((True,False),('P','Q')):
            p=W[s,low,law]
            assert all(0<x<1 for x in p) and sum(p,F(0))==1
    assert PLOW['A']/QLOW['A']==PLOW['B']/QLOW['B']==F(1,2)
    assert (1-PLOW['A'])/(1-QLOW['A'])==F(7,6)
    assert (1-PLOW['B'])/(1-QLOW['B'])==F(3,2)
    assert W['A',True,'P']!=W['B',True,'P']
    assert W['A',True,'Q']!=W['B',True,'Q']
    D={}
    for s in S:
        pm=F(1,2)*PLOW[s];qm=F(1,2)*QLOW[s]
        D[s]=(pm*succ(s,True,'P'),-qm*succ(s,True,'Q'),pm,qm)
    assert D['A']==(F(1,32),-F(1,16),F(1,16),F(1,8))
    assert D['B']==tuple(2*x for x in D['A'])
    n=0
    for bits in product((0,1),repeat=6):
        f=dict(zip(FK,bits));ca,cb=f['cA'],f['cB']
        den=ca+2*cb
        l=F(ca*f['lA']+2*cb*f['lB'],den) if den else F(0)
        q=dict(f);q['lA']=q['lB']=l
        assert obs(f)==obs(q)
        n+=1
    lr=[(v,obs(dict(zip(LK,v)),True)) for v in product((0,1),repeat=4)]
    full=[(v,obs(dict(zip(FK,v))) for v in product((0,1),repeat=6)]
    def j(o):return 5*o[0]-o[2]
    hiL=max(j(o) for v,o in lr);hiF=max(j(o) for v,o in full)
    assert hiL==-1 and hiF==-F(45,64) and hiF-hiL==F(19,64)
    witness=obs(dict(zip(FK,(1,0,1,1,0,0))))
    assert witness==(F(23,64),F(27,32),F(5,2),F(5,2))
    assert j(witness)==hiF
    keys=((0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0))
    vs=[obs(dict(zip(LK,v)),True) for v in keys]
    det=det4([[x-y for x,y in zip(v,vs[0])] for v in vs[1:]])
    assert det==F(135,4096)
    print('TRUE_LR_KEYS_t1=1_t3low=1/2_t3highA=7/6_t3highB=3/2')
    print('POSITIVE_FINE_PORTS=8; LOW_PORT_NONLUMPABILITY=YES')
    print('LOW_COLLISION_D_A=(1/32,-1/16,1/16,1/8)')
    print('LOW_COLLISION_D_B=2*D_A')
    print('FULL_DETERMINISTIC_LOW_REPAIRS=',n,sep='')
    print('FULL_VERTICES=64 LR_VERTICES=16')
    print('LR_AFFINE_RANK4_MINOR=',det,sep='')
    print('SUPPORT_DIRECTION=(5,0,-1,0)')
    print('MAX_FULL=',hiF,' MAX_LR=',hiL,' GAP=',hiF-hiL,sep='')
    print('FULL_WITNESS=(23/64,27/32,5/2,5/2)')
    print('LINF_DISTANCE_LOWER_BOUND=19/384')
    print('PASS_EXACT_R5_LAST_COLLISION_RAY_NOT_GLOBAL_HULL')
if __name__=='__main__':run()

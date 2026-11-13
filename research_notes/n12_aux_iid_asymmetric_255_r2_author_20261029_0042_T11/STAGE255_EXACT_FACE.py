#!/usr/bin/env python3
"""Stage255: exact exterior optimum and entire coupling contact polygon.
External IID author evidence; no native P000/working-truth admission.
"""
from fractions import Fraction as F
from functools import lru_cache

P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
N=12;R=P[2];K=F(24);THETA=F(1,2)
A=F(15492478957579,55725627801600)
B=F(580533802651,1160950579200)
W254=(F(969734737,2902376448),F(1932641711,4353564672))
V254=(-F(244140625,2176782336),F(244140625,2176782336))
K254=F(1310563224,20009183)
H254=F(204301839860512073,3629636342682624)

def nxt(s,z):
    t=list(s);t[z]+=1;return tuple(t)

def likelihood(s):
    return F(2,3)**s[0]*F(2)**s[1]

def h(s):
    return K*min(F(1),likelihood(s))

@lru_cache(None)
def bellman(s):
    l=likelihood(s)
    costs={'P':K*l,'Q':K}
    if sum(s)<N:
        costs['C']=THETA+(1-THETA)*l+sum(P[z]*bellman(nxt(s,z))[0] for z in range(3))
    m=min(costs.values())
    return m,tuple(a for a,v in costs.items() if v==m),costs

def ordered_dfs(root_p,root_q,root_c,terminal_p):
    assert all(F(0)<=z<=F(1) for z in (root_p,root_q,root_c,terminal_p))
    assert root_p+root_q+root_c==1
    ep=eq=tp=tq=mp=mq=F(0)
    nodes=leaves=0
    def rec(hist,pw,qw):
        nonlocal ep,eq,tp,tq,mp,mq,nodes,leaves
        nodes+=1;d=len(hist)
        if d==0:
            decisions=(('P',root_p),('Q',root_q),('C',root_c))
        elif all(z==2 for z in hist):
            decisions=(('P',terminal_p),('Q',1-terminal_p)) if d==N else (('C',F(1)),)
        else:
            first=next(z for z in hist if z!=2)
            decisions=((('P' if first==0 else 'Q'),F(1)),)
        for act,coin in decisions:
            if not coin:continue
            pp,qq=pw*coin,qw*coin
            if act=='C':
                assert d<N
                for z in range(3):rec(hist+(z,),pp*P[z],qq*Q[z])
            else:
                leaves+=1;mp+=pp;mq+=qq
                tp+=pp*d;tq+=qq*d
                if act=='P':eq+=qq
                elif act=='Q':ep+=pp
                else:raise AssertionError(act)
    rec((),F(1),F(1))
    assert (mp,mq)==(1,1)
    return (ep,eq,tp,tq),nodes,leaves

def main():
    states=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
    assert len(states)==455
    ties=[];gaps=0;actions=0
    for s in states:
        val,acts,costs=bellman(s)
        assert val==h(s)
        actions+=len(costs)
        gaps+=sum(v>val for v in costs.values())
        if len(acts)>1:ties.append((s,acts))
        if likelihood(s)!=1:
            assert acts==(('P',) if likelihood(s)<1 else ('Q',))
    expected=[((0,0,k),('P','Q','C')) for k in range(N)]+[((0,0,N),('P','Q'))]
    assert ties==expected and gaps==794 and actions==1274
    assert bellman((0,0,0))[0]==24

    rn=R**N;sn=(3+rn)/4
    fp=((1-rn)/4,(1+rn)/2)
    fq=((1+3*rn)/4,(1-rn)/2)
    assert W254==fq and V254==(-rn,rn)
    assert tuple(W254[i]+V254[i] for i in range(2))==fp
    assert H254-K254*sn==24*(1-sn) and K254>24
    S=A+B;T=24*(1-S)
    assert sn<S<1 and 2*A+B>1 and 2*A+3*B>2
    w=T/(6*(1-rn));g=F(1,2)
    v=A-w*((1-rn)/4+rn*(1-g))
    u=B-w*((1-rn)/2+rn*g)
    assert u+v+w==1 and all(0<q<1 for q in (u,v,w))
    expected_ob=(v+w*((1-rn)/4+rn*(1-g)),
                 u+w*((1-rn)/2+rn*g),
                 6*w*(1-rn),6*w*(1-rn))
    assert expected_ob==(A,B,T,T)
    got,nodes,leaves=ordered_dfs(u,v,w,g)
    assert got==expected_ob and nodes==37 and leaves==28
    extremals={
        'root-P':(F(1),F(0),F(0),F(0)),
        'root-Q':(F(0),F(1),F(0),F(0)),
        'horizon-P':(F(0),F(0),F(1),F(1)),
        'horizon-Q':(F(0),F(0),F(1),F(0))}
    for name,pars in extremals.items():
        ob,nd,lf=ordered_dfs(*pars)
        assert ob[2]==ob[3]==24*(1-ob[0]-ob[1])
        assert (ob[0],ob[1])=={'root-P':(0,1),'root-Q':(1,0),
                              'horizon-P':fp,'horizon-Q':fq}[name]
        print('EXTREMAL',name,ob,'ordered_nodes',nd,'terminal_branches',lf)
    assert THETA*T+(1-THETA)*T+24*(A+B)==24
    assert H254-K254*S<24*(1-S)
    print('SUPPORT lambdaP=lambdaQ=24 thetaP=thetaQ=1/2 Hroot=24')
    print('STATES',len(states),'ACTION_COSTS',actions,'STRICT_POSITIVE_GAPS',gaps)
    print('TIES',ties)
    print('R12',rn,'CONTACT_MIN_SUM',sn,'TARGET_SUM',S,'MARGIN',S-sn)
    print('TARGET_CAPS',A,B)
    print('ROOT_P',u,'ROOT_Q',v,'ROOT_CONTINUE',w,'TERMINAL_P',g)
    print('TARGET_OBSERVERS',got)
    print('V12',T,'float',float(T),'ORDERED_DFS_NODES',nodes,'TERMINAL_BRANCHES',leaves)
    print('ADJACENCY w254=fQ and w254+v254=fP confirmed')
    print('STAGE255_EXACT_AUTHOR_PASS')

if __name__=='__main__':main()

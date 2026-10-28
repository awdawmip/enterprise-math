#!/usr/bin/env python3
"""Stage254: exact adjacent rational Bellman face for ternary IID N=12.

Author-level external auxiliary-model evidence; no native X6 or accepted theorem claims.
Computes candidate multiplier from a genuine local Bellman equality; checks all
455 states exactly; constructs two-coin policies and independent source-mass DFS.
"""
from functools import lru_cache
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=12
O=(0,0,0)
A=(1,0,0)
B=(0,0,12)
A_STAR=F(195427979423,696570347520)
B_STAR=F(43104161797,87071293440)
K_OLD=F(7416207288,112220771)
H_OLD=F(710830290256337191,12527189335646208)
W_OLD=(F(62539020775,185752092672),F(15285594535,34828517376),F(127456938773,23219011584),F(15831662545,2902376448))
V_OLD=(-F(244140625,2176782336),F(244140625,2176782336),F(0),F(0))

def succ(s,z):
    return tuple(s[i]+int(i==z) for i in range(3))

def L(s):
    return F(2,3)**s[0]*F(2)**s[1]

# At K=131/2 identify which affine child piece is locally active. Affine
# pairs (constant, K coefficient) implement exact symbolic evaluation.
@lru_cache(None)
def piece(s):
    d={'P':(F(0),L(s)),'Q':(F(0),F(1))}
    if sum(s)<N:
        children=[piece(succ(s,z)) for z in range(3)]
        d['C']=(F(1)+sum(P[z]*children[z][0] for z in range(3)),
                sum(P[z]*children[z][1] for z in range(3)))
    k0=F(131,2)
    act=min(d,key=lambda a:d[a][0]+k0*d[a][1])
    return d[act]


def compute_k():
    ca=F(1)+sum(P[z]*piece(succ(A,z))[0] for z in range(3))
    cb=sum(P[z]*piece(succ(A,z))[1] for z in range(3))
    assert L(A)!=cb
    k=ca/(L(A)-cb)
    assert F(65)<k<F(66)
    return k

K=compute_k()

@lru_cache(None)
def bell(s):
    costs={'P':K*L(s),'Q':K}
    if sum(s)<N:
        costs['C']=F(1)+sum(P[z]*bell(succ(s,z))[0] for z in range(3))
    m=min(costs.values())
    return m,tuple(a for a,v in costs.items() if v==m),costs


def policy(s,x,y):
    if s==A:
        return (('P',1-x),('C',x))
    if s==B:
        return (('P',y),('Q',1-y))
    return ((bell(s)[1][0],F(1)),)


def observe(x,y):
    @lru_cache(None)
    def tail(s):
        ep=eq=tp=tq=F(0)
        for action,coin in policy(s,x,y):
            if not coin:continue
            if action=='P':eq+=coin
            elif action=='Q':ep+=coin
            else:
                child=[tail(succ(s,z)) for z in range(3)]
                ep+=coin*sum(P[z]*child[z][0] for z in range(3))
                eq+=coin*sum(Q[z]*child[z][1] for z in range(3))
                tp+=coin*(1+sum(P[z]*child[z][2] for z in range(3)))
                tq+=coin*(1+sum(Q[z]*child[z][3] for z in range(3)))
        return ep,eq,tp,tq
    return tail(O)


def ordered_dfs(x,y,root_stop_p=F(0)):
    '''Independent nonmerged ordered histories, separate P/Q positive masses.'''
    mp=mq=ep=eq=tp=tq=F(0)
    nodes=leaves=0
    def rec(s,depth,pw,qw):
        nonlocal mp,mq,ep,eq,tp,tq,nodes,leaves
        nodes+=1
        for action,coin in ((('P',root_stop_p),('C',1-root_stop_p)) if (s==O and root_stop_p) else policy(s,x,y)):
            if not coin:continue
            pc,qc=coin*pw,coin*qw
            if action=='C':
                assert depth<N
                for z in range(3):rec(succ(s,z),depth+1,pc*P[z],qc*Q[z])
            else:
                leaves+=1
                mp+=pc;mq+=qc
                tp+=depth*pc;tq+=depth*qc
                if action=='P':eq+=qc
                else:ep+=pc
    rec(O,0,F(1),F(1))
    assert (mp,mq)==(1,1)
    return (ep,eq,tp,tq),nodes,leaves


def inverse(a,b,w,u,v):
    d=u[0]*v[1]-u[1]*v[0]
    assert d!=0
    da,db=a-w[0],b-w[1]
    return ( (da*v[1]-db*v[0])/d, (db*u[0]-da*u[1])/d)


def main():
    print('K=',K,'float=',float(K))
    states=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
    assert len(states)==455
    ties=[];gaps=0
    for s in states:
        value,actions,costs=bell(s)
        if len(actions)>1:ties.append((s,actions))
        gaps+=sum(cost>value for cost in costs.values())
    print('ties=',ties,'gaps=',gaps)
    assert ties==[(A,('P','C')),(B,('P','Q'))],ties
    H=bell(O)[0]
    w=observe(F(0),F(0));w10=observe(F(1),F(0));w01=observe(F(0),F(1));w11=observe(F(1),F(1))
    u=tuple(w10[i]-w[i] for i in range(4))
    v=tuple(w01[i]-w[i] for i in range(4))
    assert w11==tuple(w[i]+u[i]+v[i] for i in range(4))
    assert tuple(w[i]+u[i] for i in range(4))==W_OLD
    assert v==V_OLD
    D=u[0]*v[1]-u[1]*v[0]
    assert D!=0
    x,y=inverse(A_STAR,B_STAR,w,u,v)
    assert 0<x<1 and 0<y<1,(x,y)
    print('H=',H,'W=',w,'U=',u,'V=',v,'D=',D)
    print('a*,b*=',A_STAR,B_STAR)
    print('target coins x,y=',x,y,'float=',float(x),float(y))
    print('target V affine=',H-K*(A_STAR+B_STAR),'float=',float(H-K*(A_STAR+B_STAR)))
    pstar=tuple(w[i]+x*u[i]+y*v[i] for i in range(4))
    assert pstar[:2]==(A_STAR,B_STAR)
    assert pstar[2]>pstar[3]
    assert pstar[2]==H-K*(A_STAR+B_STAR)
    assert pstar==observe(x,y)
    # Nonnegative time dominance across all real (x,y) in the square.
    assert v[2]==v[3]==0
    assert w[2]-w[3]>=0 and w[2]-w[3]+u[2]-u[3]>0
    # Shared x=1 edge with Stage253 x_old=0: Bellman planes agree on the edge.
    assert (H-K*(W_OLD[0]+W_OLD[1])==H_OLD-K_OLD*(W_OLD[0]+W_OLD[1]))
    tot_nodes=tot_leaves=0
    for X,Y in [(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1)),(x,y)]:
        vec=tuple(w[i]+X*u[i]+Y*v[i] for i in range(4))
        assert 0<vec[0]<1 and 0<vec[1]<1
        assert vec[2]>=vec[3]
        assert vec[2]==H-K*(vec[0]+vec[1])
        assert observe(X,Y)==vec
        d,nodes,leaves=ordered_dfs(X,Y)
        assert d==vec
        tot_nodes+=nodes;tot_leaves+=leaves
        print('verified corner_or_target x=',X,'y=',Y,'vectors=',vec,'DFS=',nodes,leaves)
    assert all((w[i]+u[i])==W_OLD[i] for i in range(4))
    print('TARGET_OBSERVERS=',pstar)
    # Explicit strictly feasible point just beyond x=0, using a genuine
    # source-positive root mixture rather than invalid negative Bellman coin.
    ep0,eq0,tp0,tq0=(w[i]+v[i]/2 for i in range(4))
    aext=ep0-u[0]/100; bext=eq0-u[1]/100
    assert inverse(aext,bext,w,u,v)==(-F(1,100),F(1,2))
    eta=(ep0-aext)/ep0
    assert 0<eta<1
    actual=(aext,(1-eta)*eq0+eta,(1-eta)*tp0,(1-eta)*tq0)
    assert 0<actual[1]<bext and actual[2]==actual[3]
    exact,nodes,leaves=ordered_dfs(F(0),F(1,2),root_stop_p=eta)
    assert exact==actual
    print('EXTERIOR_CAPS=',aext,bext,'ROOT_STOP_P_COIN=',eta,
          'ACTUAL_OBSERVERS=',actual,'Q_SLACK=',bext-actual[1],
          'ORDERED_DFS_NODES=',nodes,'TERMINAL_BRANCHES=',leaves)
    tot_nodes+=nodes;tot_leaves+=leaves
    print('EDGE_ERROR_SUM=',W_OLD[0]+W_OLD[1])
    print('STAGE254_ADJACENT_EXACT_AUTHOR_PASS states=455 ties=2 gaps=',gaps,'DFS_nodes=',tot_nodes,'terminal_branches=',tot_leaves)

if __name__=='__main__':main()

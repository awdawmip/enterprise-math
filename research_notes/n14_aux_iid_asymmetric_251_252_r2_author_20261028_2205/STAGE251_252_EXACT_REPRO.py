#!/usr/bin/env python3
"""Stage251/252 exact Bellman + primal + independent ordered-history audit.
External IID P=(3,1,20)/24, Q=(2,2,20)/24, caps=(3/10,19/40).
No native P000/X6 interpretation is claimed. Requires Python 3 stdlib only.
"""
from fractions import Fraction as F
from functools import lru_cache

P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
CAP=(F(3,10),F(19,40))
EXPECTED={
  11:(F(3667352,54359),F(1571672,3218625),F(50828734113,111757812500),
      F(9981178986983,1729937295360),F(3252255862529,576645765120),637,429,648),
  12:(F(7416207288,112220771),F(1564797113,11222077100),F(1121360544147507,3372018359375000),
      F(4500007219693683431,814267306817003520),F(4465227036670939309,814267306817003520),472,318,817),
}

def solve(N,A,B,probe):
    origin=(0,0,0)
    def succ(s,k):return tuple(v+(i==k) for i,v in enumerate(s))
    def L(s):return F(2,3)**s[0]*F(2)**s[1]

    @lru_cache(None)
    def affine(s):
        acts={'P':(F(0),L(s)),'Q':(F(0),F(1))}
        if sum(s)<N:
            child=[affine(succ(s,k)) for k in range(3)]
            acts['C']=(1+sum(P[k]*child[k][0] for k in range(3)),
                       sum(P[k]*child[k][1] for k in range(3)))
        key=min(acts,key=lambda a:acts[a][0]+probe*acts[a][1])
        return acts[key]

    child=[affine(succ(A,k)) for k in range(3)]
    a=1+sum(P[k]*child[k][0] for k in range(3))
    b=sum(P[k]*child[k][1] for k in range(3))
    K=a/(L(A)-b)

    @lru_cache(None)
    def bell(s):
        act={'P':K*L(s),'Q':K}
        if sum(s)<N:act['C']=1+sum(P[k]*bell(succ(s,k))[0] for k in range(3))
        h=min(act.values())
        return h,tuple(x for x,v in act.items() if v==h),act

    def policy(s,x,y):
        if s==A:return (('P',1-x),('C',x))
        if s==B:return (('P',y),('Q',1-y))
        return ((bell(s)[1][0],F(1)),)

    def observers(x,y):
        @lru_cache(None)
        def obs(s):
            ep=eq=tp=tq=F(0)
            for a,w in policy(s,x,y):
                if a=='P':eq+=w
                elif a=='Q':ep+=w
                else:
                    child=[obs(succ(s,k)) for k in range(3)]
                    ep+=w*sum(P[k]*child[k][0] for k in range(3))
                    eq+=w*sum(Q[k]*child[k][1] for k in range(3))
                    tp+=w*(1+sum(P[k]*child[k][2] for k in range(3)))
                    tq+=w*(1+sum(Q[k]*child[k][3] for k in range(3)))
            return ep,eq,tp,tq
        return obs(origin)

    base=observers(F(0),F(0))
    u=tuple(z-x for x,z in zip(base,observers(F(1),F(0))))
    v=tuple(z-x for x,z in zip(base,observers(F(0),F(1))))
    assert observers(F(1),F(1))==tuple(base[k]+u[k]+v[k] for k in range(4))
    c,d=CAP[0]-base[0],CAP[1]-base[1]
    det=u[0]*v[1]-u[1]*v[0]
    assert det!=0
    x=(c*v[1]-d*v[0])/det
    y=(d*u[0]-c*u[1])/det
    assert 0<x<1 and 0<y<1
    witness=observers(x,y)

    states=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1)
            for j in range(n-i+1)]
    ties=[];gaps=0
    for s in states:
        h,ms,acts=bell(s)
        if len(ms)>1:ties.append((s,ms))
        gaps+=sum(cost>h for cost in acts.values())
        assert all(cost>=h for cost in acts.values())
        assert all(a in ms for a,w in policy(s,x,y) if w>0)
    assert ties==[(A,('P','C')),(B,('P','Q'))]
    assert witness[:2]==CAP and witness[2]>witness[3]
    root=bell(origin)[0]
    V=root-K*sum(CAP)
    assert witness[2]==V

    massp=massq=ep=eq=tp=tq=F(0)
    nodes=leaves=0
    def walk(s,pw,qw,n):
        nonlocal massp,massq,ep,eq,tp,tq,nodes,leaves
        nodes+=1
        for a,w in policy(s,x,y):
            if w==0:continue
            pp,qq=pw*w,qw*w
            if a=='C':
                assert n<N
                for k in range(3):walk(succ(s,k),pp*P[k],qq*Q[k],n+1)
            else:
                leaves+=1;massp+=pp;massq+=qq;tp+=n*pp;tq+=n*qq
                if a=='P':eq+=qq
                else:ep+=pp
    walk(origin,F(1),F(1),0)
    assert (massp,massq)==(1,1)
    assert (ep,eq,tp,tq)==witness
    assert (K,x,y,witness[2],witness[3],nodes,leaves,gaps)==EXPECTED[N]
    print(f'STAGE{N+240}_EXACT_AUTHOR_PASS states={len(states)} ties={len(ties)} '
          f'gaps={gaps} DFS_nodes={nodes} terminal_branches={leaves}')
    print('K=',K,'root=',root,'coin_continue_A=',x,'coin_decide_P_B=',y)
    print('eP,eQ,tP,tQ=',*witness,'V=',V,'tP_minus_tQ=',witness[2]-witness[3])

if __name__=='__main__':
    solve(11,(1,0,2),(0,0,11),F(67465406,1000000))
    solve(12,(1,0,1),(0,0,12),F(6608587,100000))

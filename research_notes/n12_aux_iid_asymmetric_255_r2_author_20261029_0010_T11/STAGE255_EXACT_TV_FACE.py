#!/usr/bin/env python3
"""Stage255 external ternary IID N=12: exact source-preserving TV contact face.
All arithmetic is Python Fraction; author research, not native X6/Driver admission.
"""
from functools import lru_cache
from fractions import Fraction as F

P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12),F(1,12), F(5,6))
N=12
R=F(5,6)**N
S_MAX=1-R
CAP_A=F(15492478957579,55725627801600)
CAP_B=F(580533802651,1160950579200)
K_P=K_Q=F(24)
THETA=F(1,2)
H=F(24)
O=(0,0,0)


def L(s):return F(2,3)**s[0]*2**s[1]
def nxt(s,z):return tuple(s[i]+int(i==z) for i in range(3))

@lru_cache(None)
def bell(s):
    cost={'P':K_Q*L(s), 'Q':K_P}
    if sum(s)<N:
        cost['C']=THETA+(1-THETA)*L(s)+sum(P[z]*bell(nxt(s,z))[0] for z in range(3))
    m=min(cost.values())
    return m, tuple(k for k,v in cost.items() if v==m), cost


def fractions_for(a,b):
    # Positive-time sharpness region parameterization from Stage247.
    s=4*(1-a-b)
    z=2*a+b-1
    w=s/S_MAX
    q=z/(1-s)
    return s,z,w,q


def analytic_observers(w,q):
    # Root activation with probability w; otherwise guess Q with prob q.
    # On active branch stop at first 0 -> P, first 1 -> Q,
    # or at 12 all-2 draws with Q guess probability q.
    s=w*S_MAX
    z=(1-s)*q
    return s/4+z, 1-s/2-z, 6*s, 6*s


def ordered_dfs(w,q):
    totalp=totalq=ep=eq=tp=tq=F(0)
    nodes=leaves=0
    def walk(history, pw, qw):
        nonlocal totalp,totalq,ep,eq,tp,tq,nodes,leaves
        nodes+=1
        depth=len(history)
        if depth==0:
            actions=(('C',w),('Q',(1-w)*q),('P',(1-w)*(1-q)))
        elif history[-1]==0:
            actions=(('P',F(1)),)
        elif history[-1]==1:
            actions=(('Q',F(1)),)
        elif depth==N:
            actions=(('P',1-q),('Q',q))
        else:
            actions=(('C',F(1)),)
        for act,prob in actions:
            if not prob: continue
            a,b=prob*pw,prob*qw
            if act=='C':
                assert depth<N
                for z in range(3):walk(history+(z,),a*P[z],b*Q[z])
            else:
                leaves+=1;totalp+=a;totalq+=b
                tp+=depth*a;tq+=depth*b
                if act=='Q':ep+=a
                else:eq+=b
    walk((),F(1),F(1))
    assert (totalp,totalq)==(1,1)
    return (ep,eq,tp,tq),nodes,leaves


def main():
    states=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
    assert len(states)==455
    ties=[];positive_gaps=0
    for state in states:
        v,acts,costs=bell(state)
        # All 455 values have a simple exact closed form.
        assert v==24*min(F(1),L(state)), (state,v)
        positive_gaps+=sum(cost>v for cost in costs.values())
        if len(acts)>1:ties.append((state,acts))
    assert bell(O)[0]==H
    assert all(s[0]==s[1]==0 for s,acts in ties)
    assert len(ties)==13, ties
    assert all(acts==('P','Q','C') for s,acts in ties if sum(s)<N)
    assert ties[-1]==((0,0,12),('P','Q'))
    assert positive_gaps==794,positive_gaps

    a,b=CAP_A,CAP_B
    threshold=(3+R)/4
    assert a+b<1 and a+b>threshold
    assert 2*a+b>1 and 2*a+3*b>2
    s,z,w,q=fractions_for(a,b)
    assert all(0<=v<=1 for v in (s,z,w,q)) and z<=1-s
    obs=analytic_observers(w,q)
    assert obs[:2]==(a,b)
    assert obs[2]==obs[3]==24*(1-a-b)
    assert THETA*obs[2]+(1-THETA)*obs[3]+24*(obs[0]+obs[1])==H
    dfs,nodes,leaves=ordered_dfs(w,q)
    assert dfs==obs
    print('TARGET',a,b)
    print('S_MAX',S_MAX,'SUM_THRESHOLD',threshold)
    print('PARAMETERS s z w q',s,z,w,q)
    print('OBSERVERS',*obs)
    print('TARGET_REGION_SLACK',a+b-threshold, 2*a+b-1, 2*a+3*b-2)
    print('PRIMAL_DUAL',H,'-',24,'*',a+b,'=',H-24*(a+b))
    print('BELL_STATE_COUNT',len(states),'TIES',len(ties),'POSITIVE_GAPS',positive_gaps)
    print('ORDERED_DFS',nodes,'NODES',leaves,'LEAVES')
    print('TIE_STATES',ties)
    # Exact entire positive-time face; its four vertices are (s,z) box corners
    # s=0 (z=0/1), s=S_MAX (z=0/1-s). These cover a trapezoid.
    vertices=((F(0),F(1)),(F(1),F(0)),
              (S_MAX/4,1-S_MAX/2),
              (S_MAX/4+R,S_MAX/2))
    for va,vb in vertices:
        sv,zv,wv,qv=fractions_for(va,vb)
        assert 0<=sv<=S_MAX and 0<=zv<=1-sv and 0<=wv<=1 and 0<=qv<=1
        observer=analytic_observers(wv,qv)
        truth,nn,ll=ordered_dfs(wv,qv)
        assert observer==truth and observer[:2]==(va,vb)
        assert observer[2]==observer[3]==24*(1-va-vb)
        print('VERTEX',va,vb,'wq',wv,qv,'DFS',nn,ll)
    # Stage254 x=0 edge is identical to this trapezoid's s=S_MAX edge.
    W_E=(F(969734737,2902376448),F(1932641711,4353564672))
    V_E=(-F(244140625,2176782336),F(244140625,2176782336))
    assert W_E==vertices[3] and tuple(W_E[i]+V_E[i] for i in (0,1))==vertices[2]
    K_OLD=F(1310563224,20009183)
    H_OLD=F(204301839860512073,3629636342682624)
    assert H_OLD-K_OLD*threshold==H-24*threshold
    assert K_OLD>24
    assert H_OLD-K_OLD*(a+b)<H-24*(a+b)
    print('ADJACENCY_PASS stage254_x0_edge_equals_tv_smax_edge')
    print('STAGE255_EXACT_TV_FACE_PASS')

if __name__=='__main__': main()

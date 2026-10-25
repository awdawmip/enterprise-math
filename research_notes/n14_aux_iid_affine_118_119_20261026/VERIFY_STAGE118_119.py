"""Exact auxiliary iid Stage118/119 Bellman and ordered-history certificate.
No third-party dependencies; model is NOT Enterprise Math native X6.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json

N=14
P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12), F(1,12), F(5,6))
PN=(3,1,20); QN=(1,1,10)
D=(9,1,2)
A117=F(900390161470101555373,2592933255351443128320)
V117=F(132635001628579939136609,10371733021405772513280)


def children(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))


def add(*terms):
    return tuple(sum(row[j] for row in terms) for j in range(4))


def delta(lhs,rhs):
    return tuple(a-b for a,b in zip(lhs,rhs))


def one(stage,K,L,second,second_stop,alpha_before,value_before,prior_w):
    V={};A={};gaps=[];ties={}
    for n in range(N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                s=(n,a,b)
                R=F(2**(a+b),3**a)
                costs=[K*R,L]
                if n<N:
                    costs.append(F(1)+sum(P[j]*V[ch] for j,ch in enumerate(children(s))))
                v=min(costs);V[s]=v
                acts=[('P','Q','C')[j] for j,x in enumerate(costs) if x==v]
                if len(acts)>1: ties[s]=acts
                A[s]=acts[0]
                gaps.extend(x-v for x in costs if x>v)
    assert set(ties)=={D,second},ties
    assert ties[D]==['Q','C'] and ties[second]==[second_stop,'C']
    assert len(V)==680 and len(gaps)==1238
    @lru_cache(None)
    def moment(s,w,u):
        if s==D: return blend(w,(F(1),F(0),F(0),F(0)),cont(s,w,u))
        if s==second:
            terminal=(F(1),F(0),F(0),F(0)) if second_stop=='Q' else (F(0),F(1),F(0),F(0))
            return blend(u,terminal,cont(s,w,u))
        if A[s]=='P':return (F(0),F(1),F(0),F(0))
        if A[s]=='Q':return (F(1),F(0),F(0),F(0))
        return cont(s,w,u)
    def cont(s,w,u):
        kids=[moment(ch,w,u) for ch in children(s)]
        return (sum(P[j]*kids[j][0] for j in range(3)),
                sum(Q[j]*kids[j][1] for j in range(3)),
                F(1)+sum(P[j]*kids[j][2] for j in range(3)),
                F(1)+sum(Q[j]*kids[j][3] for j in range(3)))
    def blend(t,term,c):return tuple(t*x+(1-t)*y for x,y in zip(term,c))
    root=(0,0,0)
    m00=moment(root,F(0),F(0));m10=moment(root,F(1),F(0))
    m01=moment(root,F(0),F(1));m11=moment(root,F(1),F(1))
    dw=delta(m10,m00);du=delta(m01,m00)
    assert m11==add(m00,dw,du),'nonzero cone cross term'
    err=lambda m:m[0]-m[1]
    w_base=-err(m00)/err(dw); dwd_u=-err(du)/err(dw)
    def evaluate(u):
        w=w_base+dwd_u*u
        m=tuple(m00[j]+w*dw[j]+u*du[j] for j in range(4))
        return w,m
    u_start,u_end=(F(1),F(0)) if stage==118 else (F(0),F(1))
    w0,m0=evaluate(u_start); w1,m1=evaluate(u_end)
    eta=m1[0]-m0[0]
    assert (m0[0],m0[2],w0)==(alpha_before,value_before,prior_w)
    assert eta>0 and 0<=w0<=1 and 0<=w1<=1
    for m in (m0,m1):
        assert m[0]==m[1] and m[2]>m[3]
        assert m[2]+(K+L)*m[0]==V[root]
    def ordered(w,u):
        ep=eq=tp=tq=visits=0
        arrivals=defaultdict(lambda:[0,0,0])
        def walk(s,pw,qw):
            nonlocal ep,eq,tp,tq,visits
            visits+=1
            n,a,b=s
            if s in ties:
                x=arrivals[s];x[0]+=1;x[1]+=pw*24**(N-n);x[2]+=qw*12**(N-n)
            act=('Q' if w else 'C') if s==D else (second_stop if u else 'C') if s==second else A[s]
            if act!='C':
                p=pw*24**(N-n);q=qw*12**(N-n)
                if act=='Q':ep+=p
                else:eq+=q
                tp+=n*p;tq+=n*q
                return
            for j,ch in enumerate(children(s)):
                walk(ch,pw*PN[j],qw*QN[j])
        walk(root,1,1)
        m=(F(ep,24**N),F(eq,12**N),F(tp,24**N),F(tq,12**N))
        hits={str(k):{'count':v[0],'P_mass':str(F(v[1],24**N)),'Q_mass':str(F(v[2],12**N))} for k,v in arrivals.items()}
        return m,visits,hits
    corners={};counts={}; first_hits={}
    for w in (0,1):
        for u in (0,1):
            v,n,h=ordered(w,u);corners[(w,u)]=v;counts[f'{w}{u}']=n
            assert v==tuple(m00[j]+F(w)*dw[j]+F(u)*du[j] for j in range(4))
            if w==0 and u==0:first_hits=h
    assert first_hits[str(D)]['count']==172
    assert first_hits[str(second)]['count']==(15234 if stage==118 else 4)
    return {
        'stage':stage,'dual':{'K':str(K),'L':str(L),'slope':str(K+L),'root':str(V[root])},
        'bellman':{'states':len(V),'strict_gaps':len(gaps),'negative_gaps':0,'minimum_strict_gap':str(min(gaps)),'ties':{str(k):v for k,v in ties.items()}},
        'first_hits':first_hits,'base_moments':list(map(str,m00)),'dw':list(map(str,dw)),'du':list(map(str,du)),
        'w_base':str(w_base),'w_vs_u_slope':str(dwd_u),'u_start':str(u_start),'u_end':str(u_end),
        'w_start':str(w0),'w_end':str(w1),'eta':str(eta),
        'alpha_start':str(m0[0]),'V_start':str(m0[2]),'alpha_end':str(m1[0]),'V_end':str(m1[2]),
        'tP_minus_tQ_start':str(m0[2]-m0[3]),'tP_minus_tQ_end':str(m1[2]-m1[3]),
        'ordered_DFS_visits':counts,'primary_exact_DP':'PASS','independent_integer_DFS':'PASS',
        'full_real_interval':'PROVED_BY_AFFINITY_AND_ENDPOINTS','right_sharpness':'PROVED_BY_ONLY_TWO_TIES_AND_FEASIBLE_RANDOMIZATION_BOX',
        'research_status':'AUTHOR_COMPUTATION_ASSISTED_PROOF; INDEPENDENT_DRIVER_UNREVIEWED'
    }


def main():
    a=one(118,F(254421,296),F(90232,111),(13,6,4),'Q',A117,V117,F(376073711298041,1042086080000000))
    b=one(119,F(14079159385935,17413198588),F(272890577165656,352617271407),(6,5,1),'P',F(a['alpha_end']),F(a['V_end']),F(a['w_end']))
    assert a['alpha_end']=='900390164666042415373/2592933255351443128320'
    assert b['alpha_end']=='900390183707375071351/2592933255351443128320'
    print(json.dumps({'Stage118':a,'Stage119':b},indent=2))

if __name__=='__main__':main()

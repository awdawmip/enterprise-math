#!/usr/bin/env python3
"""Stage184 independent exact Bellman/primal finite full-history check.
Dual input from Stage183's previously validated Stage184 candidate.
P/Q branch weights are kept separate; no signed cancellation occurs.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json

N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(321331011187179,1679273916694)
L=F(480139895871848,2518910875041)
H_EXPECTED=F(1816035087448322622333240298837,12544295497767083269983043584)
S=(9,0,1)     # Q/continue; coin s = P(select Q)
T=(6,2,0)     # P/continue; coin t = P(select P)
EXPECTED={S:('Q','C'),T:('P','C')}
A=('P','Q','C')
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(st): return F(2)**(st[1]+st[2])/F(3)**st[1]
def child(st,i): return (st[0]+1,st[1]+int(i==0),st[2]+int(i==1))
@lru_cache(None)
def bell(st):
    values=[K*ell(st),L]
    if st[0]<N: values.append(1+sum((P[i]*bell(child(st,i))[0] for i in range(3)),F(0)))
    m=min(values)
    return m,tuple(a for a,v in zip(A,values) if v==m),tuple(values)
strict={}; ties={}; gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            st=(n,a,b);v,acts,values=bell(st)
            if len(acts)>1: ties[st]=acts
            else: strict[st]=acts[0]
            gaps.extend(x-v for x in values if x>v)
assert len(strict)+len(ties)==680
assert ties==EXPECTED,(ties,EXPECTED)
assert len(gaps)==1238 and min(gaps)==F(7747768995607,181361583002952)
H=bell((0,0,0))[0]
assert H==H_EXPECTED,(H,H_EXPECTED)
def is_ancestor(a,b):
    return a[0]<b[0] and a[1]<=b[1] and a[2]<=b[2] and (b[1]-a[1])+(b[2]-a[2])<=b[0]-a[0]
assert not is_ancestor(S,T) and not is_ancestor(T,S)

def action(st,s,t):
    if st==S:return 'Q' if s else 'C'
    if st==T:return 'P' if t else 'C'
    return strict[st]

def suffix(s,t):
    @lru_cache(None)
    def rec(st):
        act=action(st,s,t)
        if act=='P':return F(0),F(1),F(0),F(0)
        if act=='Q':return F(1),F(0),F(0),F(0)
        z=[rec(child(st,i)) for i in range(3)]
        return (
            sum((P[i]*z[i][0] for i in range(3)),F(0)),
            sum((Q[i]*z[i][1] for i in range(3)),F(0)),
            1+sum((P[i]*z[i][2] for i in range(3)),F(0)),
            1+sum((Q[i]*z[i][3] for i in range(3)),F(0))
        )
    return rec((0,0,0))

def ordered_dfs(s,t):
    pn=(3,1,20);qn=(1,1,10)
    counts=defaultdict(int)
    hits={S:[0,F(0),F(0)],T:[0,F(0),F(0)]}
    nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1
        st=(n,a,b)
        if st in hits:
            h=hits[st]
            h[0]+=1
            h[1]+=F(p,24**n)
            h[2]+=F(q,12**n)
        act=action(st,s,t)
        if act=='C':
            assert n<N
            for i in range(3):walk(n+1,a+int(i==0),b+int(i==1),p*pn[i],q*qn[i])
        else:
            for tag,val in (('ap',p),('aq',q),('tp',n*p),('tq',n*q)):counts[n,tag]+=val
            if act=='P': counts[n,'eq']+=q
            else: counts[n,'ep']+=p
    walk(0,0,0,1,1)
    mass=lambda tag,den:sum((F(counts[n,tag],den**n) for n in range(N+1)),F(0))
    assert mass('ap',24)==mass('aq',12)==1
    return (mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes

corners={}; nodes={}; hits=None
for s in (0,1):
    for t in (0,1):
        x=suffix(s,t)
        y,h,num=ordered_dfs(s,t)
        print('corner',s,t,'nodes',num,'agrees',x==y,flush=True)
        assert x==y,(s,t,x,y)
        corners[s,t]=x
        nodes[f'{s}{t}']=num
        if hits is None:hits=h
        else: assert h==hits,(h,hits)
assert hits[S][0] and hits[T][0]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0]
dS=sub(corners[1,0],base)
dT=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dT)
assert mixed==(F(0),)*4
D=lambda a:a[0]-a[1]
D0,Ds,Dt=map(D,(base,dS,dT))
assert Ds!=0
s0=-D0/Ds;st=-Dt/Ds
legal=(F(0),F(1))
if st>0: legal=(max(legal[0],-s0/st),min(legal[1],(1-s0)/st))
elif st<0: legal=(max(legal[0],(1-s0)/st),min(legal[1],-s0/st))
lo,hi=legal
print('BALANCE s(t)=',fmt(s0),fmt(st),'LEGAL t=',fmt(lo),fmt(hi),flush=True)
assert lo<=hi
vec=lambda t:tuple(base[i]+(s0+st*t)*dS[i]+t*dT[i] for i in range(4))
prior_alpha=F(6293786652175669191787,17990936586642819907584)
prior_V=F(50134108209086100977021,4497734146660704976896)
prior_s=F(21925676597479349,37833811200000000)
u0,u1=vec(lo),vec(hi)
left,right=(u0,u1) if u0[0]<u1[0] else (u1,u0)
checks={
 'stage183_prior_at_t0':vec(F(0))[0]==vec(F(0))[1]==prior_alpha and vec(F(0))[2]==prior_V,
 'stage183_S_coin_at_t0':s0==prior_s,
 'stage183_exact_left_endpoint':left[0]==prior_alpha and left[2]==prior_V,
 'balanced_both':left[0]==left[1] and right[0]==right[1],
 'timeP_dominates':left[2]>=left[3] and right[2]>=right[3],
 'dual_equality':all(x[2]+K*x[1]+L*x[0]==H for x in (left,right)),
 'alpha_strictly_increasing':right[0]>left[0],
 'cost_strictly_decreasing':right[2]<left[2],
 'slope':right[2]-left[2]==-(K+L)*(right[0]-left[0]),
 'nonancestor':mixed==(F(0),)*4,
 'positive_other_gaps':len(gaps)==1238 and min(gaps)>0,
 'legal_coins':0<=lo<=hi<=1 and 0<=s0+st*lo<=1 and 0<=s0+st*hi<=1
}
print('CHECKS',checks,flush=True)
print('BOUNDARY_LEFT',list(map(fmt,left)),'BOUNDARY_RIGHT',list(map(fmt,right)),flush=True)
print('WIDTH',fmt(right[0]-left[0]),'SLOPE',fmt(K+L),'H',fmt(H),'MIN_GAP',fmt(min(gaps)),flush=True)
print('HITS',{str(k):list(map(fmt,v)) for k,v in hits.items()},'NODES',nodes,flush=True)
print('BASE',list(map(fmt,base)),'dS',list(map(fmt,dS)),'dT',list(map(fmt,dT)),flush=True)
print('TIME_MARGINS',fmt(left[2]-left[3]),fmt(right[2]-right[3]),flush=True)
cert={'schema':'EM_N14_STAGE184_AUTHOR_EXACT_V1','status':'AUTHOR_EXACT_FULL_REAL_VERIFIED' if all(checks.values()) else 'AUTHOR_CANDIDATE_OBSTRUCTED',
      'sources':{'global_snapshot':'28f64a904bd2a8c659ab65dc4eccb0de5b49edff','em_initial_snapshot':'ad62145d6843aa8ac9c57629878b72e904aa0e5b',
      'stage183_commit':'8a985dc98c9762403b37ca51a38ccfabaded4187','dual184_source':'EM_STAGE183_AUTHOR_EXACT_PORTABLE_20261027.zip/dual184.json'},
      'model':{'N':14,'P':list(map(fmt,P)),'Q':list(map(fmt,Q)),'scope':'EXTERNAL_TERNARY_IID_FULL_ORDERED_HISTORIES'},
      'dual':{'K':fmt(K),'L':fmt(L),'sum':fmt(K+L),'H':fmt(H),'states':680,'ties':{str(k):list(v) for k,v in ties.items()},'positive_gaps':len(gaps),'min_gap':fmt(min(gaps))},
      'corners':{f'{s}{t}':list(map(fmt,v)) for (s,t),v in corners.items()},'base':list(map(fmt,base)),'dS':list(map(fmt,dS)),'dT':list(map(fmt,dT)),
      'mixed':list(map(fmt,mixed)), 'first_hit':{str(k):{'ordered_paths':v[0],'P':fmt(v[1]),'Q':fmt(v[2])}for k,v in hits.items()},
      'ordered_dfs_nodes':nodes,'balance':{'D0':fmt(D0),'Ds':fmt(Ds),'Dt':fmt(Dt),'s0':fmt(s0),'st':fmt(st),'t_min':fmt(lo),'t_max':fmt(hi),'s_min':fmt(min(s0+st*lo,s0+st*hi)),'s_max':fmt(max(s0+st*lo,s0+st*hi))},
      'left':{'alpha':fmt(left[0]),'V':fmt(left[2]),'tQ':fmt(left[3]),'tP_minus_tQ':fmt(left[2]-left[3])},
      'right':{'alpha':fmt(right[0]),'V':fmt(right[2]),'tQ':fmt(right[3]),'tP_minus_tQ':fmt(right[2]-right[3])},
      'width':fmt(right[0]-left[0]),'slope':fmt(K+L),'checks':checks}
Path(__file__).with_name('certificate184.json').write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n')
assert all(checks.values()),checks
print('STAGE184_AUTHOR_EXACT_FULL_REAL_PASS')

#!/usr/bin/env python3
"""Exact Stage270 first-switch dual-only scan; import Stage269 exact certificate."""
from fractions import Fraction as F
from REPRO_STAGE269 import S, P, Q, LP, LQ, H, T, U, cert, policy, mass, step, counts, orient

oldp=F(203678720,1502937);oldq=F(12317244,166993)
dp=LP-oldp;dq=LQ-oldq
value,options=cert()
a=policy(value,options,0,1)

def fixed_costs(lp,lq):
    v={};g={}
    for s in S[::-1]:
        p,q=mass(s);cs={'P':lq*q,'Q':lp*p}
        if sum(s)<12:cs['C']=q+sum(v[step(s,k)] for k in range(3))
        v[s]=cs[a[s]]
        for action,cost in cs.items():
            if action!=a[s]:g[s,action]=cost-v[s]
    return v,g

v0,g0=fixed_costs(LP,LQ);v1,g1=fixed_costs(LP+dp,LQ+dq)
assert v0[0,0,0]==H and len(g0)==819 and g0.keys()==g1.keys()
switches=[(gap/(gap-g1[key]),key) for key,gap in g0.items() if gap>0 and g1[key]<gap]
t,key=min(switches)
assert key==((1,2,2),'C')
lp=LQ*0+LP+t*dp;lq=LQ+t*dq
v,g=fixed_costs(lp,lq)
assert all(x>=0 for x in g.values())
assert set(k for k,x in g.items() if x==0)=={(T,'C'),key}
assert (lp,lq,v[0,0,0])==(F(134304895492096,947487230457),F(48948392988,643236409),F(34613913912513106850567,458327437076524179456))
C=counts(a);D=counts(policy(value,options,1,1))
assert a[key[0]]=='Q'
b=a.copy();b[key[0]]='C';new=counts(b)
w=tuple(F(49,100)*C[i]+F(49,100)*D[i]+F(1,50)*new[i] for i in range(4))
assert w[:2]==(F(402360299687,5283615080448),F(431878115465,557256278016))
assert w[3]==F(267107458235,46438023168)>w[2]
assert orient(C,D,w)==F(-4934829325296875,138015359728109104398336)<0
print('STAGE270_DUAL_ONLY_SCAN_PASS')
print('scanned_states',len(S),'alternative_action_gaps',len(g))
print('first_switch_t',t,'state',key)
print('dual_lambdaP',lp,'dual_lambdaQ',lq,'root_H',v[0,0,0])
print('feasible_exterior_caps',w[:2],'upper_bound',w[3])

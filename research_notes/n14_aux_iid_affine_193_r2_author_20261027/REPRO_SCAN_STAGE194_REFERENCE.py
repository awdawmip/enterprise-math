# Reference Stage194 dual-only scan derived from Stage193 published reference.
# Executed original source/log are in the portable archive.
#!/usr/bin/env python3
"""Stage194 exact dual first-gap closure following Stage193 primal endpoint."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
P=(F(1,8),F(1,24),F(5,6));N=14
K=F(4745649819640336341093,29760137871028647236)
L=F(1185007572839608806536,7440034467757161809)
X=(8,0,1);Z=(2,2,0) # Z represents W in Stage193 proof
dK=F(-1080671,869760);dL=F(-1)
@lru_cache(None)
def h(s):
 n,a,b=s;ell=F(2**(a+b),3**a)
 opts={'P':(K*ell,dK*ell),'Q':(L,dL)}
 if n<N:
  children=[h((n+1,a+(i==0),b+(i==1))) for i in range(3)]
  opts['C']=(1+sum(P[i]*children[i][0] for i in range(3)),sum(P[i]*children[i][1] for i in range(3)))
 best=min(v[0] for v in opts.values()); tie=tuple(a for a,v in opts.items() if v[0]==best)
 if s==Z: selected='P'
 elif s==X: selected='Q'
 else:
  assert len(tie)==1,(s,tie)
  selected=tie[0]
 assert selected in tie
 return opts[selected][0],opts[selected][1],opts,tie,selected
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
positive=[];candidates=[]; tied_extra=[]
for s in states:
 val,drv,opts,tie,selected=h(s)
 for act,(cost,cost_drv) in opts.items():
  if act==selected:continue
  g=cost-val;dg=cost_drv-drv
  if g==0:
   tied_extra.append((s,act,dg))
   if s==X:assert dg==0,(s,act,dg)
   if s==Z:assert act=='C' and dg>0,(s,act,dg)
  else:
   assert g>0
   positive.append(g)
   if dg<0:candidates.append((g/(-dg),s,act,g,dg))
assert len(states)==680 and len(positive)==1238
first=min(candidates,key=lambda it:it[0]);step=first[0];K2=K+dK*step;L2=L+dL*step
assert K2>0 and L2>0
@lru_cache(None)
def terminal(s):
 n,a,b=s;ell=F(2**(a+b),3**a)
 opts={'P':K2*ell,'Q':L2}
 if n<N:opts['C']=1+sum(P[i]*terminal((n+1,a+(i==0),b+(i==1)))[0] for i in range(3))
 v=min(opts.values());return v,tuple(q for q,w in opts.items() if w==v),{q:w-v for q,w in opts.items() if w>v}
ties={s:terminal(s)[1] for s in states if len(terminal(s)[1])>1}
gaps=[v for s in states for v in terminal(s)[2].values()]
assert len(ties)==2 and X in ties, ties
assert len(gaps)==1238
cert={'stage':194,'status':'DUAL_ONLY_NOT_PRIMAL','direction':{'dK':str(dK),'dL':str(dL)},'parent':{'K193':str(K),'L193':str(L)},'first_closure':{'step':str(step),'state':list(first[1]),'new_action':first[2],'previous_gap':str(first[3]),'gap_derivative':str(first[4])},'dual':{'K194':str(K2),'L194':str(L2),'H194':str(terminal((0,0,0))[0])},'states':len(states),'strict_gaps':len(gaps),'min_positive_gap':str(min(gaps)),'ties':[{ 'state':list(s),'actions':list(v)} for s,v in ties.items()],'preexisting_ties_direction':[{ 'state':list(s),'alternative_action':act,'derivative':str(dg)} for s,act,dg in tied_extra]}
Path(__file__).with_name('certificate194_dual_reference.json').write_text(json.dumps(cert,indent=2)+'\n')
print('DERIVATIVE_TIES',tied_extra)
print('FIRST_CLOSURE',first,'K193',K2,'L193',L2,'H193',terminal((0,0,0))[0])
print('STATES',len(states),'POSITIVE_GAPS',len(gaps),'MIN_GAP',min(gaps),'TIES',ties)
print('STAGE194_REFERENCE_DUAL_SCAN_PASS')

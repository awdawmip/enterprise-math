#!/usr/bin/env python3
"""Stage190 exact dual-only candidate from Stage189 saturated-T continue policy."""
import contextlib,io,json
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
with contextlib.redirect_stdout(io.StringIO()):
 import VERIFY_STAGE189_EXECUTED as base
P,N,K,L,H=base.P,base.N,base.K,base.L,base.H
X,T=base.X,base.T
states=base.states
@lru_cache(None)
def act(s):return ('Q' if s==X else 'C' if s==T else base.default_action(s))
@lru_cache(None)
def lin(s):
 n,a,b=s;ell=F(2**(a+b),3**a); ac=act(s)
 if ac=='P':return (F(0),ell,F(0))
 if ac=='Q':return (F(0),F(0),F(1))
 vals=[lin((n+1,a+(i==0),b+(i==1))) for i in range(3)]
 return tuple((1 if j==0 else 0)+sum(P[i]*v[j] for i,v in enumerate(vals)) for j in range(3))
def la(s,ac):
 n,a,b=s;ell=F(2**(a+b),3**a)
 if ac=='P':return (F(0),ell,F(0))
 if ac=='Q':return (F(0),F(0),F(1))
 vals=[lin((n+1,a+(i==0),b+(i==1))) for i in range(3)]
 return tuple((1 if j==0 else 0)+sum(P[i]*v[j] for i,v in enumerate(vals)) for j in range(3))
def diff(a,b):return tuple(x-y for x,y in zip(a,b))
def v(x):return x[0]+x[1]*K+x[2]*L
D=diff(la(X,'Q'),la(X,'C'))
assert v(D)==0 and D[1]!=0
raw=[]
for slopeL in (F(-1),F(1)):
 slopeK=-D[2]*slopeL/D[1]
 if slopeK+slopeL>=0:continue
 Tdiff=diff(la(T,'Q'),la(T,'C'))
 T_rate=Tdiff[1]*slopeK+Tdiff[2]*slopeL
 if T_rate<=0:continue
 raw.append((slopeK,slopeL,T_rate))
assert len(raw)==1,raw
slopeK,slopeL,topen=raw[0]
cl=[];flat=[]
for s in states:
 n,a,b=s; chosen=act(s)
 actions=['P','Q']+(['C'] if n<N else [])
 for alt in actions:
  if alt==chosen:continue
  D=diff(la(s,alt),la(s,chosen));g=v(D);r=D[1]*slopeK+D[2]*slopeL
  assert g>=0,(s,chosen,alt,g)
  if g==0:
   flat.append((s,chosen,alt,r));assert (s==X and r==0) or (s==T and alt=='Q' and r>0)
  elif r<0:cl.append((-g/r,s,chosen,alt,g,r))
assert len(flat)==2 and cl
cl.sort();step,first,chosen,other,gap,rate=cl[0]
k2=K+slopeK*step;l2=L+slopeL*step
assert k2>0 and l2>0
h2=lin((0,0,0))[0]+lin((0,0,0))[1]*k2+lin((0,0,0))[2]*l2
@lru_cache(None)
def bell2(s):
 n,a,b=s;ell=F(2**(a+b),3**a);opts={'P':k2*ell,'Q':l2}
 if n<N:opts['C']=1+sum(P[i]*bell2((n+1,a+(i==0),b+(i==1)))[0] for i in range(3))
 val=min(opts.values());return val,tuple(a for a,v in opts.items() if v==val),tuple(v-val for a,v in opts.items() if v>val)
ties=[(s,bell2(s)[1]) for s in states if len(bell2(s)[1])>1]
gaps=[v for s in states for v in bell2(s)[2]]
assert bell2((0,0,0))[0]==h2
print('DIRECTION',slopeK,slopeL,'T_RISE',topen,'SUM',slopeK+slopeL)
print('FIRST 5 CLOSURES',[(str(e[0]),e[1],e[2],e[3]) for e in cl[:5]])
print('ST190_DUAL','step',step,'K',k2,'L',l2,'H',h2,'firstnew',first,'ties',ties,'gaps',len(gaps),'min_gap',min(gaps))
if set(s for s,_ in ties)!={X,first}:raise ValueError('Unexpected tie set')
CERT={'stage':190,'status':'dual_candidate_only','parent_stage':189,'slopeK':str(slopeK),'slopeL':str(slopeL),'previous_T_strict_open_rate':str(topen),'first_closure_step':str(step),'first_new_tie_state':list(first),'new_tie_action':f'{chosen}/{other}','K190':str(k2),'L190':str(l2),'H190':str(h2),'tie_states':{str(s):a for s,a in ties},'strict_gaps':len(gaps),'min_positive_gap':str(min(gaps)),'test_status':'DUAL_SCAN_PASS'}
Path(__file__).with_name('certificate190_dual.json').write_text(json.dumps(CERT,ensure_ascii=False,indent=2)+'\n')
print('STAGE190_DUAL_SCAN_PASS')

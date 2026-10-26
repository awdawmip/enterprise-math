#!/usr/bin/env python3
"""Exact Stage153 dual-ray candidate scanner; not a primal theorem.
Run in same directory as VERIFY_STAGE152.py. Python 3 standard library.
"""
from fractions import Fraction as F
from functools import lru_cache
from importlib.machinery import SourceFileLoader
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json

# Import the exact Stage152 evaluator; capture its certificate/stdout side effects.
with redirect_stdout(StringIO()):
 m=SourceFileLoader('m',str(Path(__file__).with_name('VERIFY_STAGE152.py'))).load_module()

K,L=m.K,m.L
stepK,stepL=F(-1),-F(112,129)

@lru_cache(None)
def slopes(s):
 acts={'P':stepK*m.ratio(s),'Q':stepL}
 if s[0]<m.N:
  acts['C']=sum(m.P[i]*slopes(m.child(s,i))[0] for i in range(3))
 act='Q' if s in (m.B,m.W) else m.dual(s)[1][0]
 return acts[act],acts

candidate=[]
for s,(value,dec,opts) in m.infos.items():
 slope,ds=slopes(s)
 for action,other_value in opts.items():
  gap=other_value-value
  dg=ds[action]-slope
  if gap==0:
   if s==m.B:assert dg==0
   if s==m.W and action=='C':assert dg>0
  elif dg<0:
   candidate.append((-gap/dg,s,action))
assert candidate
t,s,action=min(candidate)
K2=K+stepK*t;L2=L+stepL*t

@lru_cache(None)
def h(state):
 n,a,b=state
 opts={'P':K2*m.ratio(state),'Q':L2}
 if n<m.N:
  opts['C']=1+sum(m.P[i]*h(m.child(state,i))[0] for i in range(3))
 v=min(opts.values())
 return v,tuple(name for name,c in opts.items() if c==v),opts

all_states={st:h(st) for st in m.states()}
ties={str(st):list(item[1]) for st,item in all_states.items() if len(item[1])>1}
gaps=[cost-v for _,(v,_,opts) in all_states.items() for cost in opts.values() if cost>v]
assert len(all_states)==680 and len(gaps)==1238
assert t==F(500973822,617885689) and s==(12,2,2) and action=='Q'
assert K2==F(5994,17) and L2==F(5960,17)
assert h((0,0,0))[0]==F(79691642847444362851,310422953206480896)
assert set(ties)=={str(m.B),str((12,2,2))}
assert min(gaps)==F(71917,33841152)
report={'status':'AUTHOR_DUAL_CANDIDATE_ONLY','dK':'-1','dL':'-112/129',
        't_star':str(t),'closing_state':str(s),'closing_action':action,
        'K153':str(K2),'L153':str(L2),'H153':str(h((0,0,0))[0]),
        'ties':ties,'strict_gap_count':len(gaps),'min_strict_gap':str(min(gaps))}
print(json.dumps(report,indent=2))

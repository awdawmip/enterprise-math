#!/usr/bin/env python3
"""Stage240 exact-dual candidate scan, NOT a primal proof. Standard Python only."""
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path
P=(F(3,24),F(1,24),F(20,24))
LP=F(75778104,1321555)
LQ=F(80621568,1321555)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
@lru_cache(None)
def V(s):
 n,a,b=s
 options={'P':LQ*F(2**(a+b),3**a),'Q':LP}
 if n<14:
  options['C']=1+sum(P[j]*V((n+1,a+(j==0),b+(j==1)))[0] for j in range(3))
 low=min(options.values())
 return low,tuple(k for k,x in options.items() if x==low),options
assert len(S)==680
H=V((0,0,0))[0]
assert H==F(835979987271629,16283420264448)
ties=[(s,V(s)[1]) for s in S if len(V(s)[1])>1]
expect=[((n,1,0),('P','C')) for n in (5,6)]+[((6,1,1),('Q','C'))]+[((n,1,0),('P','C')) for n in range(7,14)]
assert ties==expect,(ties,expect)
assert all(len(V(s)[1])<=2 for s in S)
gaps=[x-V(s)[0] for s in S for x in V(s)[2].values() if x>V(s)[0]]
assert len(gaps)==1230 and min(gaps)==F(15625,9515196)
result={'stage':240,'status':'DUAL_ONLY','lambdaP':str(LP),'lambdaQ':str(LQ),'H':str(H),
        'ties':[{'state':list(s),'actions':list(a)} for s,a in ties],
        'state_count':len(S),'positive_gaps':len(gaps),'minimum_gap':str(min(gaps)),
        'primal_feasibility':'NOT_EVALUATED'}
Path(__file__).with_name('certificate240_dual.json').write_text(json.dumps(result,indent=2)+'\n')
print('STAGE240_DUAL_ONLY_PASS',len(S),len(ties),len(gaps))

"""Stage132 independent-in-implementation ordered-word integer numerator DFS.
Author-side, no Monte Carlo sampling or aggregate-count-path replacement.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import product
import json
from pathlib import Path
N=14;WP=(3,1,20);WQ=(1,1,10);DP=24**N;DQ=12**N
K=F(4830610068,7563701);L=F(4530338888,7563701)
B=(11,0,1);E=(8,3,0)
@lru_cache(None)
def optimum(n,a,b):
 v={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:v['C']=1+sum(F(WP[j],24)*optimum(n+1,a+int(j==0),b+int(j==1))[0] for j in range(3))
 m=min(v.values())
 return m,tuple(k for k,x in v.items() if x==m)
assert optimum(0,0,0)[0]==F(244470485409835455673973219,552457976844897119895552)
assert optimum(*B)[1]==('Q','C') and optimum(*E)[1]==('P','C')
def enumerate_corner(w,u):
 totals=[0,0,0,0]; hits=defaultdict(lambda:[0,0,0]);num=[0,0]
 def visit(n,a,b,p,q):
  num[0]+=1;s=(n,a,b)
  if s in (B,E):
   r=hits[s];r[0]+=1;r[1]+=p*24**(N-n);r[2]+=q*12**(N-n)
  action=('Q' if w else 'C') if s==B else ('P' if u else 'C') if s==E else optimum(n,a,b)[1][0]
  assert action in optimum(n,a,b)[1]
  if action=='C':
   for j in range(3):visit(n+1,a+int(j==0),b+int(j==1),p*WP[j],q*WQ[j])
  else:
   num[1]+=1;pn=p*24**(N-n);qn=q*12**(N-n)
   if action=='Q':totals[0]+=pn
   else:totals[1]+=qn
   totals[2]+=n*pn;totals[3]+=n*qn
 visit(0,0,0,1,1)
 return {'moments':[str(F(totals[0],DP)),str(F(totals[1],DQ)),str(F(totals[2],DP)),str(F(totals[3],DQ))],
  'prefix_visits':num[0],'terminal_words':num[1],
  'first_hits':{str(s):{'word_count':x[0],'P':str(F(x[1],DP)),'Q':str(F(x[2],DQ))} for s,x in hits.items()}}
C={f'{w}{u}':enumerate_corner(w,u) for w,u in product((0,1),repeat=2)}
v={k:tuple(map(F,d['moments'])) for k,d in C.items()}
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,k:tuple(x*k for x in a)
M=v['00'];dB=sub(v['10'],M);dE=sub(v['01'],M)
assert v['11']==add(add(M,dB),dE)
err=lambda a:a[0]-a[1]
w0=-err(M)/err(dB);slope=-err(dE)/err(dB)
assert w0==F(23520944430861437,81438720000000000)
assert slope==F(20223469,159060000)
pt=lambda u:add(add(M,mul(dB,w0+slope*u)),mul(dE,u))
start,end=pt(F(0)),pt(F(1))
assert start[0]==F(36696744092375906695,105616844785075617792)
assert end[0]==F(12234055251084235565,35205614928358539264)
assert end[2]==F(72989119067006060803,5867602488059756544)
for p in (start,end):
 assert p[0]==p[1] and p[2]>p[3]
 assert p[2]+L*p[0]+K*p[1]==optimum(0,0,0)[0]
assert C['00']['first_hits'][str(B)]['word_count']==11
assert C['00']['first_hits'][str(E)]['word_count']==56
assert [(C[k]['prefix_visits'],C[k]['terminal_words']) for k in ('00','01','10','11')]==[(756514,504343),(747778,498519),(756382,504255),(747646,498431)]
Path(__file__).with_name('ordered_evidence132_portable.json').write_text(json.dumps({'status':'AUTHOR_INDEPENDENT_LOCAL_ALGORITHM','corners':C},indent=2),encoding='utf8')
print('PASS STAGE132 PORTABLE LITERAL INTEGER WORD DFS')
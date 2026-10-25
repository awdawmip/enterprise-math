"""Stage132 exact rational Bellman and unrestricted-history four-observer certificate.
Portable author source; Python stdlib Fraction only. Source storage is not remote execution.
"""
from fractions import Fraction as F
from functools import cache
from itertools import product
import json
from pathlib import Path
N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(4830610068,7563701); L=F(4530338888,7563701)
B=(11,0,1); E=(8,3,0); ROOT=(0,0,0)
def kids(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 n,a,b=s
 return F(2**(a+b),3**a)
H={};O={};POS=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);offers={'P':K*ratio(s),'Q':L}
   if n<N:offers['C']=1+sum(P[j]*H[v] for j,v in enumerate(kids(s)))
   best=min(offers.values());H[s]=best
   O[s]=tuple(action for action,val in offers.items() if val==best)
   POS.extend(val-best for val in offers.values() if val>best)
assert len(H)==680 and len(POS)==1238
assert {s:O[s] for s in H if len(O[s])>1}=={B:('Q','C'),E:('P','C')}
assert min(POS)==F(27060626,5513938029)
assert H[ROOT]==F(244470485409835455673973219,552457976844897119895552)
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
scale=lambda x,k:tuple(a*k for a in x)
PD=(F(0),F(1),F(0),F(0));QD=(F(1),F(0),F(0),F(0))
@cache
def obs(s,w,u):
 def cont():
  ch=[obs(z,w,u) for z in kids(s)]
  return (sum(P[j]*v[0] for j,v in enumerate(ch)),
   sum(Q[j]*v[1] for j,v in enumerate(ch)),
   1+sum(P[j]*v[2] for j,v in enumerate(ch)),
   1+sum(Q[j]*v[3] for j,v in enumerate(ch)))
 if s==B:return add(scale(QD,w),scale(cont(),1-w))
 if s==E:return add(scale(PD,u),scale(cont(),1-u))
 op=O[s][0]
 return PD if op=='P' else QD if op=='Q' else cont()
corners={(w,u):obs(ROOT,F(w),F(u)) for w,u in product((0,1),repeat=2)}
base=corners[0,0];dB=sub(corners[1,0],base);dE=sub(corners[0,1],base)
assert corners[1,1]==add(add(base,dB),dE)
err=lambda v:v[0]-v[1]
w0=-err(base)/err(dB);slope=-err(dE)/err(dB)
assert w0==F(23520944430861437,81438720000000000)
assert slope==F(20223469,159060000)
pt=lambda u:add(add(base,scale(dB,w0+slope*u)),scale(dE,u))
start=pt(F(0));end=pt(F(1))
assert start[0]==F(36696744092375906695,105616844785075617792)
assert start[2]==F(660257035708884947227,52808422392537808896)
assert end[0]==F(12234055251084235565,35205614928358539264)
assert end[2]==F(72989119067006060803,5867602488059756544)
assert 0<w0<w0+slope<1
for v in (start,end):
 assert v[0]==v[1] and v[2]>v[3]
 assert v[2]+L*v[0]+K*v[1]==H[ROOT]
assert end[0]-start[0]==F(165455959375,3223170312044544)
assert (start[2]-end[2])/(end[0]-start[0])==K+L==F(9360948956,7563701)
out={'status':'AUTHOR_EXACT_PASS','states':len(H),'strict_gap_count':len(POS),
 'min_positive_gap':str(min(POS)),'K':str(K),'L':str(L),'root':str(H[ROOT]),
 'ties':{str(s):list(O[s]) for s in H if len(O[s])>1},
 'corners':{str(k):list(map(str,v)) for k,v in corners.items()},
 'M00':list(map(str,base)),'dB':list(map(str,dB)),'dE':list(map(str,dE)),
 'w0':str(w0),'w_slope':str(slope),'w_end':str(w0+slope),
 'alpha_start':str(start[0]),'V_start':str(start[2]),
 'alpha_end':str(end[0]),'V_end':str(end[2]),
 'eta':str(end[0]-start[0]),'support_slope':str(K+L),
 'time_margins':[str(start[2]-start[3]),str(end[2]-end[3])]}
Path(__file__).with_name('certificate132_portable.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('PASS STAGE132 PORTABLE AUTHOR BELLMAN')
print('END',out['alpha_end'],out['V_end'])
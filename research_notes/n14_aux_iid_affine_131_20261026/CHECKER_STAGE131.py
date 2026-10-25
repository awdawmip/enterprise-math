"""Exact Stage131 external iid Bellman/ordered-history four-moment certificate.
Author implementation; all arithmetic fractions, no probabilistic sampling.
"""
from fractions import Fraction as F
from functools import cache
from itertools import product
from pathlib import Path
import json

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(3787884,5905);L=F(3551272,5905)
B=(11,0,1);A=(12,7,3);ROOT=(0,0,0)

def kids(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 n,a,b=s
 return F(2**(a+b),3**a)
H={};O={};positive=[]
for n in range(14,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b); offers={'P':K*ratio(s),'Q':L}
   if n<14:offers['C']=1+sum(P[j]*H[k] for j,k in enumerate(kids(s)))
   best=min(offers.values())
   H[s]=best;O[s]=tuple(z for z,v in offers.items() if v==best)
   positive.extend(v-best for v in offers.values() if v>best)
assert len(H)==680 and len(positive)==1238
assert {s:O[s] for s in H if len(O[s])>1}=={A:('P','C'),B:('Q','C')}
assert min(positive)==F(13530313,2204029440)
assert H[ROOT]==F(38329289789453267095823,86261060643965632512)
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
scale=lambda x,k:tuple(a*k for a in x)
PD=(F(0),F(1),F(0),F(0));QD=(F(1),F(0),F(0),F(0))
@cache
def moment(s,w,u):
 def cont():
  cs=[moment(t,w,u) for t in kids(s)]
  return (sum(P[j]*x[0] for j,x in enumerate(cs)),
    sum(Q[j]*x[1] for j,x in enumerate(cs)),
    1+sum(P[j]*x[2] for j,x in enumerate(cs)),
    1+sum(Q[j]*x[3] for j,x in enumerate(cs)))
 if s==B:return add(scale(QD,w),scale(cont(),1-w))
 if s==A:return add(scale(PD,u),scale(cont(),1-u))
 action=O[s][0]
 return PD if action=='P' else QD if action=='Q' else cont()
corners={(w,u):moment(ROOT,F(w),F(u)) for w,u in product((0,1),repeat=2)}
m=corners[0,0];db=sub(corners[1,0],m);da=sub(corners[0,1],m)
assert sub(sub(corners[1,1],corners[1,0]),sub(corners[0,1],corners[0,0]))==(F(0),)*4
d=lambda x:x[0]-x[1]
w0=-d(m)/d(db);wr=-d(da)/d(db)
assert w0==F(23520936469043837,81438720000000000)
assert wr==F(18849,192800000000)
pt=lambda u:add(add(m,scale(db,w0+wr*u)),scale(da,u))
first=pt(F(0));last=pt(F(1))
assert first[0]==F(36696744084893090695,105616844785075617792)
assert first[2]==F(660257040358974188827,52808422392537808896)
assert last[0]==F(36696744092375906695,105616844785075617792)
assert last[2]==F(660257035708884947227,52808422392537808896)
assert 0<w0<w0+wr<1
for v in (first,last):
 assert v[0]==v[1] and v[2]>v[3]
 assert v[2]+K*v[1]+L*v[0]==H[ROOT]
assert last[0]-first[0]==F(1623875,22920322218983424)
assert (first[2]-last[2])/(last[0]-first[0])==K+L==F(7339156,5905)
data={'grade':'AUTHOR_EXACT_LOCAL_PASS','states':len(H),'strict_gaps':len(positive),
 'min_gap':str(min(positive)),'K':str(K),'L':str(L),'Hroot':str(H[ROOT]),
 'ties':{str(s):list(O[s]) for s in H if len(O[s])>1},
 'corners':{str(k):list(map(str,v)) for k,v in corners.items()},
 'base':list(map(str,m)),'dB':list(map(str,db)),'dA':list(map(str,da)),
 'w0':str(w0),'w_slope':str(wr),'w_end':str(w0+wr),
 'alpha_start':str(first[0]),'V_start':str(first[2]),
 'alpha_end':str(last[0]),'V_end':str(last[2]),
 'delta':str(last[0]-first[0]),'support':str(K+L),
 'margins':[str(first[2]-first[3]),str(last[2]-last[3])]}
Path(__file__).with_name('certificate131_portable.json').write_text(json.dumps(data,indent=2),encoding='utf8')
print('PASS STAGE131 exact rational Bellman / full real interpolation')
print('END',data['alpha_end'],data['V_end'])
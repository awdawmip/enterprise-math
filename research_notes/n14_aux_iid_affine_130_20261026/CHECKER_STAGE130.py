"""Exact auxiliary iid Stage130 dual/primal, authorside. All arithmetic Fraction."""
from fractions import Fraction as F
from functools import cache
from itertools import product
import json
from pathlib import Path
N=14; P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(522693,802); L=F(244736,401)
B=(11,0,1); T=(14,7,4); ROOT=(0,0,0)

def kids(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

def r(s):
 n,a,b=s;return F(2**(a+b),3**a)

H={};O={};POS=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);o={'P':K*r(s),'Q':L}
   if n<N:o['C']=1+sum(P[i]*H[ch] for i,ch in enumerate(kids(s)))
   best=min(o.values());H[s]=best;O[s]=tuple(op for op,v in o.items() if v==best)
   POS.extend(v-best for v in o.values() if v>best)
assert len(H)==680 and len(POS)==1238
assert {str(s):O[s] for s in H if len(O[s])>1}=={str(T):('P','Q'),str(B):('Q','C')}
assert H[ROOT]==F(52838467869186182216021,117157274574869495808)
assert min(POS)==F(517,28872)
ADD=lambda a,b:tuple(x+y for x,y in zip(a,b))
SUB=lambda a,b:tuple(x-y for x,y in zip(a,b))
MUL=lambda a,k:tuple(x*k for x in a)
PD=(F(0),F(1),F(0),F(0)); QD=(F(1),F(0),F(0),F(0))
@cache
def OBS(s,w,v):
 def cont():
  ch=[OBS(k,w,v) for k in kids(s)]
  return (sum(P[i]*x[0] for i,x in enumerate(ch)),sum(Q[i]*x[1] for i,x in enumerate(ch)),
          1+sum(P[i]*x[2] for i,x in enumerate(ch)),1+sum(Q[i]*x[3] for i,x in enumerate(ch)))
 if s==B:return ADD(MUL(QD,w),MUL(cont(),1-w))
 if s==T:return ADD(MUL(PD,v),MUL(QD,1-v))
 return PD if O[s][0]=='P' else QD if O[s][0]=='Q' else cont()

C={str(w)+str(v):OBS(ROOT,F(w),F(v)) for w,v in product((0,1),repeat=2)}
M=C['00'];dB=SUB(C['10'],M);dT=SUB(C['01'],M)
assert C['11']==ADD(ADD(M,dB),dT)
err=lambda o:o[0]-o[1]
w0=-err(M)/err(dB)
slope=-err(dT)/err(dB)
startalpha=F(36696744060534746695,105616844785075617792)
startV=F(660257055729711878827,52808422392537808896)
point=lambda v:ADD(ADD(M,MUL(dB,w0+slope*v)),MUL(dT,v))
o0=point(F(0));assert o0[0]==startalpha and o0[2]==startV,(o0,startalpha,startV)
print('corners', {k:list(map(str,a)) for k,a in C.items()})
print('M',list(map(str,M)),'dB',list(map(str,dB)),'dT',list(map(str,dT)))
print('w0',w0,'slope',slope,'w(1)',w0+slope)
if slope>0:vmax=min(F(1),(1-w0)/slope)
else:vmax=min(F(1),-w0/slope)
assert 0<=vmax<=1
end=point(vmax)
assert end[0]>=o0[0] and end[2]<=o0[2]
for a in (o0,end):assert a[0]==a[1] and a[2]>=a[3] and a[2]+K*a[1]+L*a[0]==H[ROOT]
print('vmax',vmax,'w_end',w0+slope*vmax)
print('delta',end[0]-o0[0],'alpha130',end[0],'V130',end[2], 'slope',K+L)
print('margins',o0[2]-o0[3],end[2]-end[3], 'derivative d_alpha_dv',dT[0]+slope*dB[0])
res={'status':'AUTHOR_EXACT_PASS', 'states':len(H),'strict_positive':len(POS),'min_positive':str(min(POS)), 'ties':{str(s):list(O[s]) for s in H if len(O[s])>1},
     'K':str(K),'L':str(L),'Hroot':str(H[ROOT]),'four_corners':{k:list(map(str,a)) for k,a in C.items()},
     'M00':list(map(str,M)),'dB':list(map(str,dB)),'dT':list(map(str,dT)),
     'w0':str(w0),'w_slope':str(slope),'vmax':str(vmax),'w_end':str(w0+slope*vmax),
     'alpha_start':str(o0[0]),'V_start':str(o0[2]),'delta_alpha':str(end[0]-o0[0]),'alpha_end':str(end[0]),'V_end':str(end[2]),
     'S':str(K+L),'margins':[str(o0[2]-o0[3]),str(end[2]-end[3])],'dalpha_dv':str(dT[0]+slope*dB[0])}
with (Path(__file__).resolve().parent/'certificate130.json').open('w') as fp:json.dump(res,fp,indent=2)
print('PASS STAGE130 PRIMARY')

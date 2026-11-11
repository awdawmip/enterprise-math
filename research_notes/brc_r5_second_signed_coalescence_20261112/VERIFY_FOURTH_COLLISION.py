from fractions import Fraction as F
from pathlib import Path
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(Path(__file__).with_name('VERIFY_SECOND_COLLISION.py')))
x=z['x'];spectrum=z['spectrum'];count=z['count'];T0=z['T0'];eps=z['max_eps']
for sign,k in [(1,434),(-1,430)]:
 q=12;eta=x*F(k-12*36,23*k)
 assert (eta>0)==(sign>0)
 t=(x-23*eta)/q
 assert t==36*x/k
 vals,th=spectrum(eta)
 inner=(999*eta + x*F(sign)/(6233 if sign>0 else 6187))/1000
 phase=sorted(vals);i=phase.index(t)
 before=(phase[i-1]+t)/2;after=(t+phase[i+1])/2
 a=count(eta,before);b=count(eta,after)
 assert a>b
 print('FOURTH',sign,'ETA',eta,'EPS',t,'INTERIOR',sum(v<eps for v in vals),'MASKS',sum(v==t for v,c in th.values()),'BEFORE',a,'AFTER',b,'DROP',a-b,flush=True)
 v2,th2=spectrum(inner)
 p2=sorted(v2)
 move=(x-23*inner)/q;fixed=t
 lo=min(move,fixed);idx=p2.index(lo)
 assert p2[idx+1]==max(move,fixed)
 ways=[count(inner,(p2[idx-1]+p2[idx])/2),count(inner,(p2[idx]+p2[idx+1])/2),count(inner,(p2[idx+1]+p2[idx+2])/2)]
 masks=[sum(v==t2 for v,cc in th2.values()) for t2 in (p2[idx],p2[idx+1])]
 print('FOURTH_INSIDE',sign,'ETA',inner,'ORDER',[('MOVING' if v==move else 'FIXED') for v in (p2[idx],p2[idx+1])],'MASKS',masks,'WAYS',ways,'DROPS',[ways[0]-ways[1],ways[1]-ways[2]],flush=True)
 assert ways[0]-ways[2]==a-b
 assert set(v for v in vals if v<eps)==T0|{(x-23*eta)/j for j in (15,12,3)}
print('PASS_R5_FOURTH_SIGNED_COALESCENCE')

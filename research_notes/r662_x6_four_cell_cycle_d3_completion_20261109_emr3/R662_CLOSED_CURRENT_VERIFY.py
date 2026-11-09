#!/usr/bin/env python3
"""R662 six-event stationary signed cycle-current extension; exact four-port enumeration."""
import json
from itertools import product
from pathlib import Path
import R662_VERIFY as r

h=(2,0,3,0)
k=(3,0,0,0)
A=(r.e,r.f,r.g,h,k)
B=(r.f,r.e,r.g,h,k)
CYCLE=(1,1,1,1)
identity=(0,1,2)
rotation=(1,2,0)
def compose(p,q):return tuple(p[q[i]] for i in range(3))
def inverse(p):return tuple(p.index(i) for i in range(3))
def relative(x,y):return tuple(compose(y['slots'][i],inverse(x['slots'][i])) for i in range(4))
def net_chain(word):
  e={(0,1):0,(1,2):1,(2,3):2,(3,0):3}
  out=[0]*4
  for s,_,t,_ in word:
    if (s,t) in e:out[e[s,t]]+=1
    elif (t,s) in e:out[e[t,s]]-=1
    else:raise AssertionError((s,t))
  return tuple(out)
def incidence(v):return (-v[0]+v[3],v[0]-v[1],v[1]-v[2],v[2]-v[3])
assert incidence(CYCLE)==(0,0,0,0)
result=[]
for a,b in product(range(4),repeat=2):
  reverse=(2,a,1,b)
  wa=A+(reverse,)
  wb=B+(reverse,)
  x=r.run(r.S,wa,True)
  y=r.run(r.S,wb,True)
  if x is None or y is None:continue
  assert net_chain(wa)==net_chain(wb)==CYCLE
  assert incidence(net_chain(wa))==(0,0,0,0)
  assert x['triads']==y['triads']
  assert all(x[z]==y[z] for z in ('rin','rout','pairs'))
  assert relative(x,y)==(identity,rotation,identity,identity)
  assert all(sum(map(sum,state))==6 for state in (x['rin'],x['rout'],y['rin'],y['rout']))
  result.append([a,b])
assert result==[[a,b] for a in range(4) for b in range(3)],result
x=r.run(r.S,A+((2,0,1,0),),True)
y=r.run(r.S,B+((2,0,1,0),),True)
assert x['triads']==y['triads']==((1,2,4),(1,3,4),(0,2,4),(1,2,4))
assert x['slots']==((0,2,1),(0,2,1),(1,2,0),(0,2,1))
assert y['slots']==((0,2,1),(1,0,2),(1,2,0),(0,2,1))
marker='R662_CLOSED_SIGNED_CYCLE_CURRENT_D3_PERSISTENCE_EXACT_PASS'
evidence={'marker':marker,'conditional_H':True,'all_16_reverse_port_choices':16,'both_strict':12,
 'valid_reverse_port_pairs':result,'forward_before_reverse':(1,2,1,1),
 'net_current_after_reverse':CYCLE,'incidence_after_reverse':incidence(CYCLE),
 'relative_D3_per_cell':(identity,rotation,identity,identity),
 'example_reverse_event':(2,0,1,0),'example_triads':x['triads'],
 'example_A_slots':x['slots'],'example_B_slots':y['slots'],
 'source_reuse':'R662_VERIFY.py; same exact endpoint-local V29/V27/V17 implementation',
 'status':'AUTHOR_EXACT_COMPUTATION; based-loop V39 frame return not asserted; DRIVER_UNREVIEWED'}
Path(__file__).with_name('R662_CLOSED_CURRENT_EVIDENCE_RECOMPUTED.json').write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(marker,'strict',len(result),'/',16,'net',CYCLE,'delta',relative(x,y))

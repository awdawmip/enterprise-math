#!/usr/bin/env python3
"""PREFIX-605: exact symbolic proof of every native 3-slot binary provenance tag.
Requires the frozen PREFIX565 and PREFIX600/601/602 certificates in this folder.
Original BRC phase graph is used, without any replacement science model.
"""
import hashlib, io, json
from contextlib import redirect_stdout
from pathlib import Path
from fractions import Fraction as F
with redirect_stdout(io.StringIO()):
 from PREFIX565_positive_marginal_certificate import PHASES,NEXT,SCIENCE_PIN
 from PREFIX600_R6_compact_native_certificate import plus,minus,V,Wi
 from PREFIX601_R6_weighted_short_certificate import pairs
 from PREFIX602_R6_native_phase_repair_certificate import rank
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
f=Path(__file__).with_name('PREFIX565_positive_marginal_certificate.py').read_bytes()
assert hashlib.sha1(('blob %d\0'%len(f)).encode()+f).hexdigest()=='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'
order=plus+minus; pos={p:i for i,p in enumerate(order)}
E=sorted({(PHASES[p][0],abs(PHASES[p][2])) for p in order}); ei={e:i for i,e in enumerate(E)}
assert len(order)==48 and len(E)==12 and len(pairs)==6
VW=[[sum(V[e][j]*Wi[j][i] for j in range(24)) for i in range(24)] for e in range(12)]
# Laurent polynomials over Q, represented as exponent->exact rational.
def A(a,b):
 c=a.copy()
 for k,v in b.items():c[k]=c.get(k,F(0))+v
 return {k:v for k,v in c.items() if v}
def M(a,b):
 c={}
 for k,v in a.items():
  for l,w in b.items():c[k+l]=c.get(k+l,F(0))+v*w
 return {k:v for k,v in c.items() if v}
X={1:F(1)}; NX={1:F(-1)}; H={0:F(1,2)}; NH={0:F(-1,2)}
sel={j:[] for j in range(3)}; support={j:set() for j in range(3)}; table=[]
for e,f in pairs:
 w=[A(M(NX,{0:F(VW[e][i])}),M(H,{0:F(VW[f][i])})) for i in range(24)]
 assert sum(bool(y) for y in w)==4
 for offset in (0,24):
  row={'pair':[e,f],'block':offset//24,'tagged':{}}
  for slot in range(3):
   hist={}
   for i,c in enumerate(w):
    if not c:continue
    p=order[offset+i]; h=ei[(PHASES[p][0],abs(PHASES[p][2]))]
    assert h in (e,f)
    factor=({0:F(1)} if slot==0 else (X if h==e else {-1:F(1,4)}))
    q=pos[NEXT[p][slot]]
    hist[q]=A(hist.get(q,{}),M(c,factor))
   hist={q:v for q,v in hist.items() if v}
   values=[tuple(v.items()) for v in hist.values()]
   if slot==0:
    assert sorted(values)==sorted([tuple(H.items())]*2+[tuple(NX.items())]*2)
    target=H
   else:
    assert sorted(values)==sorted([tuple(NH.items()),tuple(X.items())])
    target=NH
   assert not (support[slot]&set(hist))
   support[slot].update(hist)
   q=next(q for q,v in hist.items() if v==target)
   sel[slot].append({'pair':[e,f],'block':offset//24,'endpoint':q})
   row['tagged'][str(slot)]={str(q):{str(k):str(c) for k,c in v.items()} for q,v in hist.items()}
  table.append(row)
assert [len(support[j]) for j in range(3)]==[48,24,24]
assert all(len(sel[j])==12 for j in range(3))
# Independent exact rational ranks for all selected tagged endpoint columns.
def testcase(t):
 P=[[F(0)]*48 for _ in range(48)]
 C=[[[F(0)]*48 for _ in range(48)] for _ in range(3)]
 for i,p in enumerate(order):
  h=ei[(PHASES[p][0],abs(PHASES[p][2]))];s=1+2*t[h]
  for j in range(3):
   q=pos[NEXT[p][j]];a=(F(1) if j==0 else t[h])/s
   C[j][i][q]+=a;P[i][q]+=a
 k=sum(4*t[e]*t[f]==1 for e,f in pairs)
 assert rank(P)==48-2*k
 for j in range(3):
  q=[a['endpoint'] for a in sel[j] if 4*t[a['pair'][0]]*t[a['pair'][1]]==1]
  assert len(q)==2*k
  assert rank([P[i]+[C[j][i][h] for h in q] for i in range(48)])==48
 return {'k':k,'original_rank':48-2*k,'repaired_rank':[48,48,48],'additional_scalar_probabilities':2*k}
cases={'original_all_one':[F(1)]*12,'all_zero':[F(0)]*12}
for k in (1,2,6):
 t=[F(1)]*12
 for e,f in pairs[:k]:t[e]=F(1,4);t[f]=F(1)
 cases['critical_'+str(k)]=t
ranks={name:testcase(t) for name,t in cases.items()}
result={'status':'ALL_CHECKS_PASS','frozen_pin':SCIENCE_PIN,'native_git_blob':'7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41','scope':'all nonnegative finite 12-incidence weights, arbitrary initial 48-phase probability laws, nine original roots','theorem':'all three nonconstant Boolean partitions of native slots 0,1,2 are sufficient, and each admits exactly 2k individually observable tagged endpoint probabilities as sharp scalar repair','symbolic_checks':36,'symbolic_support_cardinalities':[48,24,24],'endpoint_selectors':sel,'full_symbolic_table':table,'rational_rank_cases':ranks,'acceptance':'AUTHOR_PROVED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX605_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':result['status'],'symbolic_checks':36,'supports':[48,24,24],'ranks':ranks},indent=2))

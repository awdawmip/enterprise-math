#!/usr/bin/env python3
"""Exact first boundaries of the signed R5 phase-order chambers.
Run after decoding VERIFY_BIDIRECTIONAL_R5.py in the same folder.
"""
from fractions import Fraction as F
from contextlib import redirect_stdout
from io import StringIO
from runpy import run_path
from pathlib import Path
with redirect_stdout(StringIO()):
 s=run_path(str(Path(__file__).with_name('VERIFY_BIDIRECTIONAL_R5.py')))
x=s['x']; T0=s['T0']; EPS=s['EPS']; X=s['X']; H=s['H']; D=s['D']
V=s['V'];IX=s['IX']; P=s['prefix'];M=s['M']
info=s['limit_info'];zero=s['zero'];orders=s['orders']
fixed=sorted(T0)
qvals=(15,12,3)

def bound(q,sign):
 t=x/q; i=fixed.index(t)
 neighbor=fixed[i-1] if sign>0 else fixed[i+1]
 return (x-q*neighbor)/F(23*sign)
BP=bound(15,+1);BN=bound(15,-1)
assert BP>0 and BN>0
assert BP==F(155682221,312843455900080000000)
assert BN==F(155682221,311686918170320000000)
assert all(BP<bound(q,+1) and BN<bound(q,-1) for q in (12,3))

for sign,B in ((+1,BP),(-1,BN)):
 e=sign*B
 z=tuple(X[k]+e*H[k] for k in range(28))
 assert min(z)>0 and min(z[k]+EPS*D[k] for k in range(28))>=0
 assert z[IX[(0,2)]]+EPS*D[IX[(0,2)]]==0
 boundary=[info(mask,z) for mask in range(M)]
 for mask in range(1,M):
  t0,old=zero[mask];t,now=boundary[mask]
  if t0 is None:assert t is None
  else:assert now and now.issubset(old)
 assert all(any(t==phase and IX[(0,3)] in ks for t,ks in boundary) for phase in T0)
 phases={t for t,k in boundary if t is not None and 0<t<EPS}
 t15=(x-23*e)/15
 assert t15 in T0
 assert phases==T0|{(x-23*e)/q for q in (12,3)}
 assert len(phases)==1146
 # The exact boundary is the first collision: at any smaller signed eta
 # all three t_q remain in their original neighboring open intervals.
 half=e/2
 a=tuple(X[k]+half*H[k] for k in range(28))
 ts=[info(mask,a)[0] for mask in range(M)]
 interior={t for t in ts if t is not None and 0<t<EPS}
 assert interior==T0|{(x-23*half)/q for q in qvals}
 assert len(interior)==1147
 values=sorted(interior|{EPS})
 for q in qvals:
  t=(x-23*half)/q;i=values.index(t)
  if sign>0:assert values[i+1]==x/q
  else:assert values[i-1]==x/q
  lost=orders(ts,(values[i-1]+t)/2)-orders(ts,(values[i+1]+t)/2)
  assert lost==s['EXPECTED'][sign][q][2]
 print('SIGN',sign,'OPEN_ORDER_CHAMBER_BOUND',B,'ETA_OVER_X',B/x,
       'BOUNDARY_INTERIOR_PHASES',len(phases),
       'INSIDE_INTERIOR_PHASES',len(interior),
       'ALL_32768_MINIMIZER_INDICES_STABLE',True)
print('PASS_R5_EXACT_MAXIMAL_SIGNED_PHASE_ORDER_CHAMBERS')

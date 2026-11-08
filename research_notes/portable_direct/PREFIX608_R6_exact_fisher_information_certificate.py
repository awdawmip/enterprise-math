#!/usr/bin/env python3
"""PREFIX608-R6: exact symbolic Fisher information on native critical BRC fibers."""
import hashlib, io, json
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import sympy as S
src=Path(__file__).with_name('PREFIX565_positive_marginal_certificate.py').read_bytes()
blob=hashlib.sha1(('blob %d\0'%len(src)).encode()+src).hexdigest()
assert blob=='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'
with redirect_stdout(io.StringIO()):
 from PREFIX565_positive_marginal_certificate import PHASES,NEXT,SCIENCE_PIN,ROOTS
 import PREFIX605_R6_binary_tag_certificate as prev
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
order,pos,ei,pairs=prev.order,prev.pos,prev.ei,prev.pairs
assert len(order)==48 and len(pairs)==6 and len(ROOTS)==9
x=S.symbols('x',positive=True)
rows=[]
for pair_idx,(e,f) in enumerate(pairs):
 t=[S.Integer(1)]*12;t[e]=x;t[f]=1/(4*x)
 P=[S.Integer(0)]*48
 C=[[S.Integer(0)]*48 for _ in range(3)]
 for i,p in enumerate(order):
  inc=ei[(PHASES[p][0],abs(PHASES[p][2]))]
  den=1+2*t[inc]
  for j in range(3):
   q=pos[NEXT[p][j]]
   C[j][q]+=(S.Integer(1) if j==0 else t[inc])/den
   P[q]+=(S.Integer(1) if j==0 else t[inc])/den
 w=[prev.A(prev.M(prev.NX,{0:F(prev.VW[e][i])}),prev.M(prev.H,{0:F(prev.VW[f][i])})) for i in range(24)]
 for block in (0,24):
  h=[0]*48
  for i,v in enumerate(w):
   if v:
    p=order[block+i];h[block+i]=1 if ei[(PHASES[p][0],abs(PHASES[p][2]))]==e else -1
  assert h.count(1)==h.count(-1)==2
  # Native left-null check, at every output phase, symbolic in positive x.
  for q in range(48):
   z=0
   for i,p in enumerate(order):
    if not h[i]:continue
    inc=ei[(PHASES[p][0],abs(PHASES[p][2]))]
    for j in range(3):
     if pos[NEXT[p][j]]==q:
      z+=h[i]*(S.Integer(1) if j==0 else t[inc])/(1+2*t[inc])
   assert S.cancel(z)==0
  info=[]
  for j in range(3):
   z=[S.Integer(0)]*48
   for i,p in enumerate(order):
    if not h[i]:continue
    inc=ei[(PHASES[p][0],abs(PHASES[p][2]))]
    q=pos[NEXT[p][j]]
    z[q]+=h[i]*(S.Integer(1) if j==0 else t[inc])/(1+2*t[inc])
   total=S.Integer(0)
   for q,zq in enumerate(z):
    zq=S.cancel(zq)
    if zq==0:continue
    a=S.cancel(C[j][q]);b=S.cancel(P[q]-C[j][q])
    assert a!=0 and b!=0
    total+=zq*zq*(1/a+1/b)
   info_j=S.cancel(48*total)
   assert info_j==[192,96,96][j],(pair_idx,block,j,info_j)
   info.append(str(info_j))
  rows.append({'pair':pair_idx,'signed_block':block//24,'fisher_information':info})
result={'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,'native_blob':blob,
 'sympy_version':S.__version__,'scope':'one critical pair t_e=x>0,t_f=1/(4x), other 10 t=1, uniform 48-phase baseline, signed +/- normalized null contrast',
 'symbolic_fisher':{'slot0':'192','slot1':'96','slot2':'96'},
 'cases_checked':36,'null_equations_checked':576,'case_details':rows,
 'sampling':'N independent one-step binary-slot-plus-terminal-phase observations',
 'consequence':'For theta in (-1/48,1/48), local unbiased variance lower bounds at theta=0 are 1/(192N),1/(96N),1/(96N); score estimator attains each at theta=0',
 'stage':'AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX608_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'cases':len(rows),'fisher':result['symbolic_fisher'],'sympy_version':S.__version__},indent=2))

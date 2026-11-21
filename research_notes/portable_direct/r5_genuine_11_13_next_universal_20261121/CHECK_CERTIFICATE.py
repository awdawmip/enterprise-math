#!/usr/bin/env python3
"""R5 primitive-11/13 rigorous finite base and root multiplicity checks.
Run:
 python VERIFY_KERNELS.py 11 44 > KERNEL_11.json
 python VERIFY_KERNELS.py 13 52 > KERNEL_13.json
 python VERIFY_DIRECT.py 11 1 7 8 9 10 11 18 19 20 21 22 > DIRECT_11.json
 python VERIFY_DIRECT.py 13 1 9 10 11 12 13 22 23 24 25 26 > DIRECT_13.json
 python CHECK_CERTIFICATE.py
The global recurrence must also be checked by the mathematical derivation in RESEARCH.md.
"""
import json
from pathlib import Path
BASE=Path(__file__).parent

def pole_multiplicity_test(d):
 x=214%d;y=215%d
 uvals=[p%d for p in (216,217,218)]
 vvals=[p%d for p in (219,220,221)]
 assert (x+y)%d==0
 kinds={k:0 for k in ('P1','P2','P01','P02','P12','P012')}
 for u in uvals:
  for v in vvals:
   specs={
    'P1':([0,x,u,v],[],[]),
    'P2':([0,y,u,v],[],[]),
    'P01':([0,x,u,y,v,(y+v)%d],[],[('quad',(y+v)%d)]),
    'P02':([0,y,u,x,v,(x+v)%d],[],[('quad',(x+v)%d)]),
    'P12':([0,u,v,x,y,(x+y)%d],[],[('quad',(x+y)%d)]),
    'P012':([0,u,x,y,v],[('quad',(x+y+v)%d)],[('cubic',(x+y+v)%d)])
   }
   for kind,(linear,quad,numerator) in specs.items():
    for k in range(2*d):
     den=sum((2*s+k)%(2*d)==0 for s in linear)
     den+=sum((2*s+2*k)%(2*d)==0 for typ,s in quad)
     zero=sum((2*s+(2 if typ=='quad' else 3)*k)%(2*d)==0 for typ,s in numerator)
     rem=den-zero
     assert rem<=2,(d,kind,u,v,k,den,zero)
     kinds[kind]=max(kinds[kind],max(0,rem))
 return kinds

def run():
 data={}
 for d in (11,13):
  j=json.loads((BASE/f'KERNEL_{d}.json').read_text())
  rows={x['m']:x for x in j['rows']}
  directly=json.loads((BASE/f'DIRECT_{d}.json').read_text())
  assert len(directly)==11
  assert all((x['R0'],x['DR'])==(rows[x['m']]['R0'],rows[x['m']]['DR']) for x in directly)
  vanish=list(range(7,12)) if d==11 else list(range(9,14))
  assert j['R0_nonzero_residues_first_cycle']==list(range(1,7 if d==11 else 9))
  assert all(not any(rows[r+k*d]['R0']) for r in vanish for k in range(4))
  pole=pole_multiplicity_test(d)
  assert max(pole.values())<=2
  cert=[]
  for r in vanish:
   a=rows[r]['DR'];b=rows[r+d]['DR'];c=rows[r+2*d]['DR'];e=rows[r+3*d]['DR']
   assert c==[a[i]+b[i] for i in range(d-1)]
   assert e==[2*b[i] for i in range(d-1)]
   assert a[0] and b[0]
   if a[0]*b[0]<0:assert abs(b[0])>abs(a[0])
   cert.append({'r':r,'A':a,'B':b,'first_coordinate_sign_certificate':[a[0],b[0]]})
  data[str(d)]={'R0_nonzero_residues':j['R0_nonzero_residues_first_cycle'],
       'R0_zero_residues':[r%d for r in vanish],
       'R0_first_cycle':[rows[m]['R0'] for m in range(1,d+1)],
       'kernel_pole_order_bounds':pole,
       'independent_direct_comparison_thresholds':[row['m'] for row in directly],
       'all_first_4d_recurrence_base_verified':True,
       'recurrence':'DR[m+4*d]-2*DR[m+2*d]+DR[m]=0 (m>=1)',
       'base_certificates':cert}
 out={'schema':'R5_TRUE_PRIMITIVE11_13_EXACT_CERT_V1',
  'input_model':'frozen scalar R5 / prices 214..314 / S0-S4 @75d986aa',
  'm_range_kernel':{'11':[1,44],'13':[1,52]},
  'm_range_direct':{'11':[1,22],'13':[1,26]},
  'numerical_status':'PASS','independent_review':'NOT_REVIEWED','by_prime':data}
 expected=json.loads((BASE/'RESULT.json').read_text())
 for d in (11,13):
  ref=expected['by_prime'][str(d)];actual=data[str(d)]
  assert ref['R0_nonzero_residues']==actual['R0_nonzero_residues']
  assert ref['R0_first_cycle']==actual['R0_first_cycle']
  assert ref['kernel_max_root_pole_multiplicity']==actual['kernel_pole_order_bounds']
  for cert in actual['base_certificates']:
   original=ref['base_certificates'][str(cert['r'])]
   assert original['A']==cert['A'] and original['B']==cert['B']
 (BASE/'RESULT_RECOMPUTED.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('PASS: 22 direct crosschecks, 10 full-vector 4-block certificates and all 2d-root multiplicities')
 for d in (11,13):
  print('d',d,'max root multiplicities',data[str(d)]['kernel_pole_order_bounds'],
        'signs',[(c['r'],c['first_coordinate_sign_certificate']) for c in data[str(d)]['base_certificates']])
if __name__=='__main__':run()

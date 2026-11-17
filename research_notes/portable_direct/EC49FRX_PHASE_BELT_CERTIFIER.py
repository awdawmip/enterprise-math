#!/usr/bin/env python3
"""EC49FRX exact 2D four-tree price-belt certificate.

Usage:
  python EC49FRX_PHASE_BELT_CERTIFIER.py <extracted-EC49FRW-evidence-root> [output-folder]
Expects the frozen original EC49FRW evidence root containing:
  code/EC49FRW_TWO_PRICE_SOLVER.py, code/EC49FQI_NATIVE_DATA.py,
  code/EC49FRQ_INDEPENDENT_ALL228.py,
  source/frozen_original_master.txt, source/EC49FPG_PROFILE.csv,
  evidence/EC49FRW_T32_FULL_TREE.json, evidence/EC49FRW_T34_FULL_TREE.json.
No network, approximation, modified physical observations, or extra input.
"""
import hashlib
import json
import sys
from pathlib import Path
from collections import Counter
from fractions import Fraction as F

ROOT=Path(sys.argv[1]).resolve()
OUT=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else ROOT/'evidence'
sys.path.insert(0,str(ROOT/'code'))
from EC49FRW_TWO_PRICE_SOLVER import solve,V,PIN
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(V)==228 and all(len(row)==141 for row in V)

SOURCE={
 'frozen_original_master.txt':'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e',
 'EC49FPG_PROFILE.csv':'a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'}
for f,expected in SOURCE.items():
 assert hashlib.sha256((ROOT/'source'/f).read_bytes()).hexdigest()==expected

vertices=[('0','0'),('1/2','0'),('0','1/2'),('1/4','1/4'),
          ('1/2','1/4'),('1/4','1/2'),('1/3','1/3'),
          ('1/2','1/3'),('1/3','1/2')]
anchors=[]
witness_new={}
for sa,sb in vertices:
 a,b=F(sa),F(sb)
 info,tree=solve(a,b,True)
 M,m=max(a,b),min(a,b)
 target=F(296)-141*M-11*m if m<=F(1,4) else F(297)-141*M-15*m
 computed=F(info['Bellman_integer_value'],info['denominator'])
 assert computed==target,(str(a),str(b),computed,target)
 anchors.append({'a':str(a),'b':str(b),'optimum':str(computed),
                 'states_evaluated':info['states'],'root':info['root_observer'],
                 'optimal_tree_type':[info['U'],info['N32'],info['N34']]})
 if (a,b)==(F(1,2),F(1,3)):witness_new['high32']=tree
 if (a,b)==(F(1,3),F(1,2)):witness_new['high34']=tree
 print('ANCHOR_PASS',str(a),str(b),str(computed),flush=True)

types={'low32':(296,141,11),'low34':(296,11,141),
       'high32':(297,141,15),'high34':(297,15,141)}
checked={}
OUT.mkdir(parents=True,exist_ok=True)
for name,trip in types.items():
 if name.startswith('low'):
  q=32 if name=='low32' else 34
  tree=json.loads((ROOT/'evidence'/f'EC49FRW_T{q}_FULL_TREE.json').read_text())['tree']
 else:
  tree=witness_new[name]
  (OUT/f'EC49FRX_{name.upper()}_FULL_TREE.json').write_text(
    json.dumps(tree,ensure_ascii=False,separators=(',',':'))+'\n')
 counts=Counter()
 maxdepth=0
 for state in range(141):
  node=tree
  depth=0
  seen=set()
  while 'named_observer' in node:
   q=node['named_observer']
   assert 0<=q<228 and q not in seen
   seen.add(q)
   counts[q]+=1
   depth+=1
   node=node['children'][str(V[q][state])]
  assert node['leaf']==state
  maxdepth=max(maxdepth,depth)
 assert (sum(counts.values()),counts[32],counts[34])==trip
 assert maxdepth==3
 checked[name]={'U':trip[0],'N32':trip[1],'N34':trip[2],
                'all_states_replayed':141,'max_depth':maxdepth}
 print('TREE_PASS',name,trip,'141/141',flush=True)

certificate={
 'schema':'EC49FRX_EXACT_NATIVE_BRC_PHASE_BELT_V1',
 'frozen_science_pin':PIN,
 'model':'original native BRC class16943; 141 original named states, 228 physical named observers, uniformly weighted',
 'domain':'0<=a,b<=1/2 and min(a,b)<=1/3; t>0; p32=(1-a)*t,p34=(1-b)*t,other 226 queries t',
 'theorem':'F=141*V/t=296-141M-11m if 0<=m<=1/4; =297-141M-15m if 1/4<=m<=1/3; M=max(a,b),m=min(a,b)',
 'four_affine_types':checked,'nine_all228_Bellman_anchors':anchors,
 'source_sha256':SOURCE,
 'continuous_proof':'four convex trapezoids; concavity of all-tree affine infimum, exact vertex Bellman lower bounds, matching full-tree upper bounds',
 'review_status':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'}
dest=OUT/'EC49FRX_PHASE_BELT_EXACT_CERT.json'
dest.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
print('ALL_PASS nine Bellman anchors; four full trees; SHA256',
      hashlib.sha256(dest.read_bytes()).hexdigest())

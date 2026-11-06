"""EC49FCE: reproducible exact fixed-schedule quartets, 370 verified groups.
Run from this folder on the PR branch. Requires Python 3.10+, no third-party dependencies.
Imports the frozen EC49FBY signed-X6 candidate generator from its sibling directory.
"""
from pathlib import Path
from itertools import combinations
import json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import build
HERE=Path(__file__).resolve().parent
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
EXPECTED={
 'H7_H7_H7':(40,188116992000,88324,256804,131592),
 'H7_H7_H9':(120,1525837824000,202052,572020,538800),
 'H7_H7_H8_FIRST_210':(210,3666321792000,352384,1093949,1909746),
}

def test(slots,pools,single):
 fixed=0
 for key,mask in single.items():
  if key not in slots:fixed|=mask
 base=fixed.bit_count();limit=158-base
 arr=[];raw=1
 for key in slots:
  raw*=len(pools[key])
  residuals={m&~fixed for m in pools[key] if (m&~fixed).bit_count()<limit}
  arr.append((key,sorted(residuals)))
 arr.sort(key=lambda x:len(x[1]))
 (_,a),(_,b),(_,c),(_,d)=arr
 pair=triple=checks=0;best=158
 for x in a:
  for y in b:
   xy=x|y
   if xy.bit_count()>=limit:pair+=1;continue
   for z in c:
    xyz=xy|z
    if xyz.bit_count()>=limit:triple+=1;continue
    for w in d:
     checks+=1
     best=min(best,base+(xyz|w).bit_count())
 return {'slots':list(slots),'base':base,'cut':limit,'raw':raw,
         'residual_counts':[len(v) for _,v in arr],
         'pair_pruned':pair,'triple_pruned':triple,
         'fourth_checks':checks,'minimum':best}

def run():
 chosen,early,late,pools,single=build()
 assert len(chosen)==24 and len(early)==len(late)==10
 h7=[k for k in late if k.startswith('7:')]
 h8=[k for k in late if k.startswith('8:')]
 h9=[k for k in late if k.startswith('9:')]
 groups={
  'H7_H7_H7':[(e,*triple) for e in early for triple in combinations(h7,3)],
  'H7_H7_H9':[(e,*a,*b) for e in early for a in combinations(h7,2) for b in combinations(h9,1)],
  'H7_H7_H8_FIRST_210':[(e,*a,*b) for e in early for a in combinations(h7,2) for b in combinations(h8,1)][:210],
 }
 allrows={};summary={}
 for kind,sets in groups.items():
  rows=[test(s,pools,single) for s in sets]
  assert all(r['minimum']==158 for r in rows)
  stats=(len(rows),*(sum(r[k] for r in rows) for k in ('raw','pair_pruned','triple_pruned','fourth_checks')))
  assert stats==EXPECTED[kind],(kind,stats,EXPECTED[kind])
  allrows[kind]=rows
  summary[kind]={'groups':len(rows),'raw':stats[1],'pair_pruned':stats[2],
                 'triple_pruned':stats[3],'fourth_checks':stats[4],'minimum':158}
  print('PASS',kind,stats,flush=True)
 report={'schema':'EC49FCE_PARTIAL_370_EXACT_V1','scientific_pin':PIN,
         'frozen_generator_commit':'5b10f1c296cb8826d4b69f6fd83dba89d765df1c',
         'witness_commit':'b3b43ef6abe2fd816d979792d18a67ee5d0aad50',
         'model':'native ordered signed X6 prefix, L421/M732 BRC, frozen 9-state DFA',
         'exact_groups':370,'full_family_groups':1200,'minimum_each':158,
         'summary':summary,'per_family':allrows,
         'next':'H7_H7_H8 remaining indices 210..239; other late triples'}
 (HERE/'EXACT_REPORT_EC49FCE_370.json').write_text(json.dumps(report,indent=2)+'\n')
 print('PASS_ALL',sum(x['groups'] for x in summary.values()))
if __name__=='__main__':run()

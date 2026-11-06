"""Exact 150 four-slot signed-X6 prefix-neighborhood checks. Python 3.10+."""
from itertools import combinations
from frozen_model import build
from pathlib import Path
import json

chosen, early, late, pools, single = build()
h7=[k for k in late if k.startswith('7:')]
h8=[k for k in late if k.startswith('8:')]
h9=[k for k in late if k.startswith('9:')]
groups={
 'H7_H7_H8_TAIL30':[(e,*a,b) for e in early for a in combinations(h7,2) for b in h8][210:],
 'H7_H9_H9':[(e,a,*b) for e in early for a in h7 for b in combinations(h9,2)],
 'H8_H8_H8':[(e,*t) for e in early for t in combinations(h8,3)],
 'H8_H9_H9':[(e,a,*b) for e in early for a in h8 for b in combinations(h9,2)]
}
assert [len(x) for x in groups.values()]==[30,40,40,40]
assert len({tuple(sorted(s)) for v in groups.values() for s in v})==150

def exact(slots):
 fixed=0
 for k,v in single.items():
  if k not in slots:fixed|=v
 base=fixed.bit_count();limit=158-base
 arr=[];raw=1
 for k in slots:
  raw*=len(pools[k]);r={v&~fixed for v in pools[k] if (v&~fixed).bit_count()<limit}
  arr.append((k,sorted(r)))
 arr.sort(key=lambda q:len(q[1]))
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
 return {'slots':list(slots),'base':base,'strict_cut':limit,'raw':raw,
         'reduced_counts':[len(q) for _,q in arr],
         'pair_pruned':pair,'triple_pruned':triple,
         'fourth_checks':checks,'minimum':best}

def run():
 report={'schema':'EC49FCF_150_SIGNED_X6_EXACT_V1',
 'scientific_input_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'frozen_generator_commit':'5b10f1c296cb8826d4b69f6fd83dba89d765df1c',
 'reference_witness_edges':158,'per_family':{},'summary':{}}
 for name,sets in groups.items():
  rows=[exact(s) for s in sets]
  assert all(x['minimum']==158 for x in rows),(name,'improvement found')
  report['per_family'][name]=rows
  report['summary'][name]={'groups':len(rows),
    'raw':sum(x['raw'] for x in rows),
    'pair_pruned':sum(x['pair_pruned'] for x in rows),
    'triple_pruned':sum(x['triple_pruned'] for x in rows),
    'fourth_checks':sum(x['fourth_checks'] for x in rows),'exact_minimum':158}
  print('PASS',name,report['summary'][name],flush=True)
 assert sum(v['groups'] for v in report['summary'].values())==150
 assert sum(v['raw'] for v in report['summary'].values())==19261307520000
 assert sum(v['fourth_checks'] for v in report['summary'].values())==602298
 out=Path(__file__).with_name('EC49FCF_150_CERTIFICATE.json')
 out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return report
if __name__=='__main__':run()

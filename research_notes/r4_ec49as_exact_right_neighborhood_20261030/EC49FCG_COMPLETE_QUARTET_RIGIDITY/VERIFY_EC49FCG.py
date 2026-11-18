"""EC49FCG exact four-slot certificate, frozen signed native X6 paths.
Run: python VERIFY_EC49FCG.py H8H8H9
     python VERIFY_EC49FCG.py H7H8H8 --start 0 --stop 160
     python VERIFY_EC49FCG.py H7H8H8 --start 160 --stop 240
     python VERIFY_EC49FCG.py H7H8H9 --start 0 --stop 180
     python VERIFY_EC49FCG.py H7H8H9 --start 180 --stop 320
"""
from itertools import combinations
from pathlib import Path
from time import perf_counter
import argparse,json,sys
sibling=Path(__file__).resolve().parent.parent/'EC49FCF_EARLY1_LATE3_150'
if not sibling.exists():sibling=Path(__file__).resolve().parent  # local source copy
sys.path.insert(0,str(sibling))
from frozen_model import build
WITNESS=158
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
chosen,early,late,pools,single=build()
h7=[s for s in late if s.startswith('7:')]
h8=[s for s in late if s.startswith('8:')]
h9=[s for s in late if s.startswith('9:')]
GROUPS={
 'H8H8H9':[(e,*p,b) for e in early for p in combinations(h8,2) for b in h9],
 'H7H8H8':[(e,a,*p) for e in early for a in h7 for p in combinations(h8,2)],
 'H7H8H9':[(e,a,b,c) for e in early for a in h7 for b in h8 for c in h9]
}
assert [len(GROUPS[k]) for k in ('H8H8H9','H7H8H8','H7H8H9')]==[120,240,320]
def reindex(families):
 """Replace old bit indices by a bijection of the active prefix universe."""
 positions=set()
 for family in families:
  for v in family:
   while v:
    bit=v&-v;positions.add(bit.bit_length()-1);v^=bit
 translation={p:i for i,p in enumerate(sorted(positions))}
 out=[]
 for family in families:
  new=set()
  for v in family:
   q=0
   while v:
    bit=v&-v;q|=1<<translation[bit.bit_length()-1];v^=bit
   new.add(q)
  out.append(sorted(new))
 return out,len(positions)
def exact(slots,method='fast'):
 fixed=0
 for slot,mask in single.items():
  if slot not in slots:fixed|=mask
 base=fixed.bit_count();cut=WITNESS-base;raw=1;arrays=[]
 for slot in slots:
  raw*=len(pools[slot])
  arrays.append((slot,{(v&~fixed) for v in pools[slot]
                            if (v&~fixed).bit_count()<cut}))
 arrays.sort(key=lambda item:len(item[1]))
 (a,b,c,d),universe=reindex([arr for _,arr in arrays]);best=WITNESS
 pair_pruned=triple_pruned=checks=0;possible_pairs=0
 for x in a:
  for y in b:
   xy=x|y;n=xy.bit_count()
   if n>=cut:pair_pruned+=1;continue
   if method=='bound':
    # Any improving quartet must make each remaining path contribute
    # at most cut-1-|xy| fresh prefixes beyond xy.
    allowance=cut-1-n
    cc=[z for z in c if (z&~xy).bit_count()<=allowance]
    if not cc:continue
    dd=[w for w in d if (w&~xy).bit_count()<=allowance]
    if not dd:continue
    possible_pairs+=1
   else:
    cc,dd=c,d
   for z in cc:
    xyz=xy|z
    if xyz.bit_count()>=cut:triple_pruned+=1;continue
    for w in dd:
     checks+=1
     best=min(best,base+(xyz|w).bit_count())
 return {'slots':list(slots),'method':method,'minimum':best,'fixed_edges':base,
         'cut':cut,'candidate_product':raw,'prefix_universe':universe,
         'pruned_pool_sizes':[len(q) for q in (a,b,c,d)],
         'pair_pruned':pair_pruned,'triple_pruned':triple_pruned,
         'possible_pairs':possible_pairs,'last_checks':checks}
def run(family,start=0,stop=None):
 assert family in GROUPS
 group=GROUPS[family]
 if stop is None:stop=len(group)
 assert 0<=start<stop<=len(group)
 t=perf_counter();rows=[]
 for j in range(start,stop):
  # Use equivalent necessary C/D-extension pruning for two large cases.
  method='bound' if family=='H7H8H8' and j in (208,209) else 'fast'
  row=exact(group[j],method)
  assert row['minimum']==WITNESS,(family,j,row)
  rows.append(row)
  if (j+1)%20==0:print('PASS',family,j+1,'elapsed',round(perf_counter()-t,3),flush=True)
 data={'schema':'EC49FCG_PARTIAL_OR_COMPLETE_EXACT_V1','pin':PIN,'family':family,
       'range':[start,stop],'baseline':WITNESS,'records':rows}
 output=Path(__file__).with_name(f'EC49FCG_{family}_{start}_{stop}.json')
 output.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
 print('COMPLETE',family,len(rows),'raw',sum(r['candidate_product'] for r in rows),
       'minimum',min(r['minimum'] for r in rows),'saved',output,flush=True)
 return data
if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('family',choices=GROUPS)
 parser.add_argument('--start',type=int,default=0)
 parser.add_argument('--stop',type=int,default=None)
 args=parser.parse_args();run(args.family,args.start,args.stop)

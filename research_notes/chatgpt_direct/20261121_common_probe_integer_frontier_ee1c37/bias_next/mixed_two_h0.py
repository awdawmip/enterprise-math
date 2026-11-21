from pathlib import Path
from collections import Counter
import struct,json,time
import os
ROOT=Path(os.environ['PROBE_PREPARED']);OUT=Path(os.environ['PROBE_OUTPUT'])
raw=(ROOT/'obs').read_bytes();pair=[int.from_bytes(raw[i:i+32],'little')for i in range(0,125*125*32,32)];lo=(1<<125)-1
pts=lambda m:[i for i in range(125)if m>>i&1]
def cd(m):
 ids=pts(m);C=D=0
 for x in ids:
  h=0
  for y in ids:h|=pair[125*x+y]
  C+=h.bit_count();D+=(h&lo).bit_count()-(h>>125).bit_count()
 return C,D
def shift(i,x):return ((i//25+x//25)%5)*25+((i//5%5+x//5%5)%5)*5+(i%5+x%5)%5
banks={(c,sign):set()for c in (1042,1059)for sign in(-1,1)}
for l,h,c in struct.iter_unpack('<QQQ',(ROOT/'B11').read_bytes()):
 if c not in (1042,1059):continue
 m=l+(h<<64);d=cd(m)[1]
 if abs(d)!={1042:142,1059:179}[c]:continue
 ids=pts(m)
 for x in range(125):banks[c,1 if d>0 else -1].add(sum(1<<shift(i,x)for i in ids))
assert all(len(b)==(750 if c==1042 else 1500)for(c,s),b in banks.items())
parents=[int(a)+(int(b)<<64)for a,b in map(str.split,(ROOT/'parent').read_text().splitlines()[:250])]
frames=[(0,i)for i,m in enumerate(parents)if not m&parents[0]];assert len(frames)==100;results=[];st=time.monotonic()
for sign in (-1,1):
 for fi,frame in enumerate(frames):
  core=0
  for i in frame:assert not core&parents[i];core|=parents[i]
  high=sorted(m for m in banks[1059,sign]if not m&core);mid=sorted(m for m in banks[1042,sign]if not m&core);adj=[sum(1<<j for j,n in enumerate(high)if not m&n)for m in high];nodes=[0];completed=[0];best=[-1,None,None,None]
  def low_best(candidates,used,picked,high_chosen):
   nodes[0]+=1
   if len(picked)>best[0]:best[:]=[len(picked),used,picked.copy(),high_chosen.copy()]
   for j,m in enumerate(candidates):
    if len(picked)+len(candidates)-j<=best[0]:break
    low_best([n for n in candidates[j+1:]if not m&n],used|m,picked+[m],high_chosen)
  def high_search(eligible,left,used,chosen):
   nodes[0]+=1
   if not left:
    completed[0]+=1;low_best([m for m in mid if not m&used],used,[],chosen);return
   while eligible.bit_count()>=left:
    b=eligible&-eligible;i=b.bit_length()-1;eligible-=b
    high_search(eligible&adj[i],left-1,used|high[i],chosen+[high[i]])
  high_search((1<<len(high))-1,0,0,[])
  results.append({'sign':sign,'frame':fi,'high_candidates':len(high),'mid_candidates':len(mid),'0_high_packings':completed[0],'maximum_additional_142':best[0],'nodes':nodes[0],'witness_high':None if best[3]is None else[str(x)for x in best[3]],'witness_union':None if best[1]is None else str(best[1]),'witness_142':None if best[2]is None else[str(x)for x in best[2]]})
res={'complete':True,'cases':results,'0_high_packings':sum(r['0_high_packings']for r in results),'max_additional_142':max(r['maximum_additional_142']for r in results),'nodes':sum(r['nodes']for r in results),'seconds':time.monotonic()-st};(OUT/'mixed_two_h0_result.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items()if k!='cases'})

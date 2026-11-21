from pathlib import Path
from collections import Counter
from hashlib import sha256
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
banks={-1:set(),1:set()}
for l,h,c in struct.iter_unpack('<QQQ',(ROOT/'B11').read_bytes()):
 if c!=1059:continue
 m=l+(h<<64);d=cd(m)[1]
 if abs(d)!=179:continue
 ids=pts(m)
 for x in range(125):banks[d//179].add(sum(1<<shift(i,x)for i in ids))
assert all(len(b)==1500 for b in banks.values())
parents=[int(a)+(int(b)<<64)for a,b in map(str.split,(ROOT/'parent').read_text().splitlines()[:250])]
frames=[tuple(map(int,l.split())) for l in (ROOT/"f4_52").read_text().splitlines()];assert len(frames)==35
results=[];st=time.monotonic()
for sign,bank in banks.items():
 for frame_no,frame in enumerate(frames):
  core=0
  for i in frame: assert not core&parents[i];core|=parents[i]
  rows=sorted(m for m in bank if not m&core);adj=[sum(1<<j for j,n in enumerate(rows)if not m&n)for m in rows];nodes=[0]
  def sort_color(P):
   vs=[];cs=[];c=0
   while P:
    c+=1;A=P
    while A:
     b=A&-A;i=b.bit_length()-1;vs.append(i);cs.append(c);P^=b;A^=b;A&=~adj[i]
   return vs,cs
  def search(P,k):
   nodes[0]+=1
   if not k:return []
   vs,cs=sort_color(P)
   for i,c in zip(vs[::-1],cs[::-1]):
    if c<k:return None
    w=search(P&adj[i],k-1)
    if w is not None:return [i]+w
    P^=1<<i
   return None
  for k in range(4,-1,-1):
   w=search((1<<len(rows))-1,k)
   if w is not None:break
  seen=core
  for i in w:
   assert not seen&rows[i];seen|=rows[i];assert cd(rows[i])==(1059,179*sign)
  results.append({'sign':sign,'frame':frame_no,'candidates':len(rows),'maximum':k,'nodes':nodes[0],'witness':[str(rows[i])for i in w]})
result={'complete':True,'canonical_four_mother_frames':len(frames),'cases':results,'maximum':max(r['maximum']for r in results),'counts':dict(Counter(r['maximum']for r in results)),'nodes':sum(r['nodes']for r in results),'seconds':time.monotonic()-st,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'four_mothers_result.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='cases'})

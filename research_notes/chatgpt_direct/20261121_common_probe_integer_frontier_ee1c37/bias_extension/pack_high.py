from pathlib import Path
import sys,json,time
p=Path(sys.argv[1]); target=int(sys.argv[2]);ls=p.read_text().splitlines();rows=[int(a)+(int(b)<<64)for a,b in map(str.split,ls[1:])];assert len(rows)==int(ls[0]);adj=[sum(1<<j for j,n in enumerate(rows)if not m&n)for m in rows];nodes=0

def color_sort(P):
 vertices=[];colors=[];c=0
 while P:
  c+=1;allowed=P
  while allowed:
   b=allowed&-allowed;i=b.bit_length()-1;vertices.append(i);colors.append(c);P^=b;allowed^=b;allowed&=~adj[i]
 return vertices,colors

def search(P,k):
 global nodes
 nodes+=1
 if not k:return []
 vs,cs=color_sort(P)
 for v,c in zip(vs[::-1],cs[::-1]):
  if c<k:return None
  sub=search(P&adj[v],k-1)
  if sub is not None:return [v]+sub
  P^=1<<v
 return None
st=time.monotonic();w=search((1<<len(rows))-1,target);res={'target':target,'candidate_count':len(rows),'found':w is not None,'nodes':nodes,'seconds':time.monotonic()-st,'witness_masks':None if w is None else[str(rows[i])for i in w]};print(json.dumps(res),flush=True)

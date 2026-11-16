"""R652 exact rank and lossless typed-boundary recovery on bidirected 4-port network."""
from itertools import combinations
from fractions import Fraction
from collections import deque
import json

def rankQ(cols):
 a=[[Fraction(x) for x in row] for row in zip(*cols)];r=0
 for j in range(len(cols)):
  k=next((i for i in range(r,len(a)) if a[i][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];t=a[r][j]
  for i in range(r+1,len(a)):
   if a[i][j]:
    f=a[i][j]/t
    for h in range(j,len(cols)):a[i][h]-=f*a[r][h]
  r+=1
  if r==len(a):break
 return r

def rank2(cols):
 piv={}
 for z in cols:
  while z:
   p=z.bit_length()-1
   if p in piv:z^=piv[p]
   else:piv[p]=z;break
 return len(piv)

pairs=list(combinations(range(4),2));pc=[]
for a in range(4):
 for b in range(4):
  if a!=b:
   x=[int((a,b)==(i,j))-int((a,b)==(j,i)) for i,j in pairs]+[int(k==a) for k in range(4)]
   pc.append(x)
assert rankQ(pc)==10

def connected_graphs(n):
 edges=list(combinations(range(n),2))
 for mask in range(1<<len(edges)):
  E=[e for i,e in enumerate(edges) if mask>>i&1]
  adj=[set() for _ in range(n)]
  for a,b in E:adj[a].add(b);adj[b].add(a)
  seen={0};q=[0]
  while q:
   for v in adj[q.pop()]:
    if v not in seen:seen.add(v);q.append(v)
  if len(seen)==n:yield E,adj

def classify(n,E,adj):
 color={0:0};q=deque([0]);bip=True
 while q:
  v=q.popleft()
  for w in adj[v]:
   if w not in color:color[w]=1-color[v];q.append(w)
   elif color[w]==color[v]:bip=False
 arcs=[(a,b) for a,b in E]+[(b,a) for a,b in E]
 adjp=[set() for _ in range(8*n)];columns=[]
 for a,b in arcs:
  for i in range(4):
   for j in range(4):
    u=4*a+i;v=4*n+4*b+j
    columns.append((1<<u)|(1<<v));adjp[u].add(v);adjp[v].add(u)
 seen=set();comps=[]
 for v in range(8*n):
  if v in seen:continue
  seen.add(v);q=[v];comp=[]
  while q:
   z=q.pop();comp.append(z)
   for w in adjp[z]:
    if w not in seen:seen.add(w);q.append(w)
  comps.append(sorted(comp))
 expect=8*n-(2 if bip else 1)
 assert len(comps)==(2 if bip else 1)
 assert rank2(columns)==expect
 return bip,arcs,comps,expect

def recover(n,arcs,comps,twice=False):
 p=[[0]*4 for _ in range(n)];Om=[[[0]*4 for _ in range(4)] for _ in range(n)]
 rin=[[0]*4 for _ in range(n)];rout=[[0]*4 for _ in range(n)]
 events=[('P',c,i,j) for c in range(n) for i,j in ((0,1),(1,0),(2,3))]
 events += [('T',c,a,d,b) for c,d in arcs for a,b in ((0,1),(2,3))]
 if twice:events=events[::-1]*2
 for e in events:
  if e[0]=='P':
   _,c,a,b=e;p[c][a]+=1;Om[c][a][b]+=1;Om[c][b][a]-=1
  else:
   _,c,a,d,b=e;rout[c][a]+=1;rin[d][b]+=1
 r=[v for x in rout for v in x]+[v for x in rin for v in x]
 omit={max(c) for c in comps}
 saved=[Om[c][i][j] for c in range(n) for i,j in pairs]+[v for x in p for v in x]+[r[i] for i in range(8*n) if i not in omit]
 back=r[:]
 for comp in comps:
  lost=max(comp);sign=lambda k:(1 if k<4*n else -1)
  back[lost]=-sign(lost)*sum(sign(i)*r[i] for i in comp if i!=lost)
 assert back==r
 assert len(saved)==18*n-len(comps)
 q=[[p[c][i]-sum(Om[c][i]) for i in range(4)] for c in range(n)]
 I=[[p[c][i]+rin[c][i] for i in range(4)] for c in range(n)]
 O=[[q[c][i]+rout[c][i] for i in range(4)] for c in range(n)]
 assert sum(map(sum,I))==sum(map(sum,O))

summary={};checked=0;graphs=0
for n in range(2,6):
 c={"bipartite":0,"nonbipartite":0,"transfer_ranks":{}}
 for E,adj in connected_graphs(n):
  bip,arcs,comps,r=classify(n,E,adj)
  c['bipartite' if bip else 'nonbipartite']+=1
  c['transfer_ranks'][str(r)]=c['transfer_ranks'].get(str(r),0)+1
  recover(n,arcs,comps);recover(n,arcs,comps,True)
  checked+=2;graphs+=1
 c['connected_graphs']=c['bipartite']+c['nonbipartite'];summary[str(n)]=c
assert graphs==771 and checked==1542
assert [summary[str(n)]['bipartite'] for n in range(2,6)]==[1,3,19,195]
assert [summary[str(n)]['nonbipartite'] for n in range(2,6)]==[0,1,19,533]
print(json.dumps({'marker':'R652_BIDIRECTED_NETWORK_BIPARTITE_LIFT_RANK_EXACT_PASS','local_pass_rank':10,'connected_graphs':graphs,'mixed_reconstruction_histories':checked,'by_n':summary,'rank':'18n-2 if bipartite, else 18n-1'},ensure_ascii=False,indent=2))

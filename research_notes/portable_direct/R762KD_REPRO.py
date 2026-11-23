"""R762KD: exact integer certificate for three flexible singleton supports."""
from itertools import combinations
from math import comb

P=[p for p in combinations(range(6),2) if p!=(0,1)]
I={p:i for i,p in enumerate(P)}
F=[(0,1,i) for i in range(2,6)]
C=[s for s in combinations(range(6),3) if s not in F]
E={s:list(combinations([I[p] for p in combinations(s,2) if p in I],2)) for s in C+F}
assert len(P)==14 and len(C)==16

def v(e):
 a,b=e
 return (1<<a if a<13 else 0)^(1<<b if b<13 else 0)

def parity():
 # 8192 even boundaries; one-edge choices from each of 16 flexible triangles.
 ways=[1]+[0]*8191; parents=[]
 for s in C:
  nxt=[0]*8192; pred={}
  for m,z in enumerate(ways):
   if not z: continue
   for j,e in enumerate(E[s]):
    t=m^v(e);nxt[t]+=z
    if t not in pred:pred[t]=(m,j)
  parents.append(pred);ways=nxt
 assert sum(ways)==3**16 and (min(ways),max(ways))==(3072,6819)
 target=0
 for s in F:target^=v(E[s][0])
 chosen={};x=target
 for i in reversed(range(16)):
  x,j=parents[i][x];chosen[C[i]]=E[C[i]][j]
 assert x==0
 return ways,chosen

def cut_check():
 clusters=[{I[(0,i)],I[(1,i)]} for i in range(2,6)]+[{I[p]} for p in combinations(range(2,6),2)]
 index={j:i for i,b in enumerate(clusters) for j in b}
 cross=[]
 for mask in range(1,1<<9):
  k=sum(any(((mask>>index[a])&1)!=((mask>>index[b])&1) for a,b in E[s]) for s in C)
  cross.append(k)
 assert (len(cross),min(cross),cross.count(4))==(511,4,6)
 return cross

def realize(s,n,chosen):
 if n==1:return [chosen]
 others=[e for e in E[s] if e!=chosen]
 if n%2==0:base=others
 else:base=[chosen,others[0],others[0]]
 return base+[E[s][0]]*(n-len(base))

def test_graph(counts,chosen):
 events=[]
 for s in F:events += [E[s][0]]*counts[s]
 for s in C:events += realize(s,counts[s],chosen[s])
 d=[0]*14; graph=[set() for _ in P]
 for a,b in events:
  d[a]+=1;d[b]+=1;graph[a].add(b);graph[b].add(a)
 assert all(k>0 and k%2==0 for k in d)
 seen={0};todo=[0]
 for a in todo:
  for b in graph[a]:
   if b not in seen:seen.add(b);todo.append(b)
 assert len(seen)==14 and len(events)==sum(counts.values())
 return len(events)

def main():
 cut_check(); ways,chosen=parity()
 tests=0
 for D in combinations(C,3):
  R=[s for s in C if s not in D]
  for Tforce in combinations(F,2):
   for T in (R[:5],R[-5:]):
    counts={s:(3 if s in Tforce else 1) for s in F}
    counts.update({s:(1 if s in D else 3 if s in T else 2) for s in C})
    assert test_graph(counts,chosen)==42
    tests+=1
 assert tests==6720
 print({'parity_targets':len(ways),'min_preimages':min(ways),'max_preimages':max(ways),
        'min_cut_colors':4,'checked_42_graphs':tests,
        'deduced_labeled_42':comb(4,2)*comb(16,3)*comb(13,5),
        'marked_44_to_42':5*comb(4,2)*comb(16,3)*comb(13,5),
        'failures':0})
if __name__=='__main__':main()

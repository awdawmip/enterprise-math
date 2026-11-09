"""EC49FFU: exact one-key Hh signed-X6 prefix-tree dynamic program.
H2 words ce/ec/ed/de are fixed. Every allowed Hh word is enumerated;
their four low signatures must use one full key K=(x,y,z).
Original BRC nine-state DFA and signed native microsteps imported from
the same-directory VERIFY_EC49FFU.py at the frozen science pin.
"""
from VERIFY_EC49FFU import A,T,S,O,B,signed
import json,sys
SIG=(1,2,4,8)

def words(h,k):
 x,y,z=k
 n=[z-1,0,0,z,h+1-y-2*z,h+1-x];d=x+y-h-1
 if min(n[0],n[3],n[4],n[5],d)<0:return
 def rec(w,q):
  if not any(n):
   if S[q] in SIG:yield (w,S[q])
  else:
   for j in range(6):
    if n[j]:
     n[j]-=1
     yield from rec(w+O[j],T[q][j])
     n[j]+=1
 for c in range(d+1):
  n[1]=c;n[2]=d-c
  yield from rec('',0)

def keys(h):
 for z in range(1,1+h//2):
  for x in range(1,h+2):
   for y in range(1,h+2):
    if x+y>=h+2 and h+1-y-2*z>=0:yield (x,y,z)

def solve(h,k):
 # Baseline H2 is mandatory; a signed-prefix edge already present costs zero.
 base=set()
 for w in B.values():
  p=[]
  for a in signed(w):
   p.append(a);base.add(tuple(p))
 assert len(base)==28
 tree=[{}];edge=[0];end=[0];nwords=0
 for w,s in words(h,k):
  nwords+=1;v=0;p=[]
  for a in signed(w):
   p.append(a)
   if a not in tree[v]:
    u=len(tree);tree[v][a]=u;tree.append({})
    edge.append(0 if tuple(p) in base else 1);end.append(0)
   v=tree[v][a]
  end[v]|=1<<SIG.index(s)
 if not nwords:return None,0,len(tree)
 dp=[None]*len(tree)
 for v in range(len(tree)-1,-1,-1):
  q=end[v];d={0:0};t=q
  while t:
   d[t]=0;t=(t-1)&q
  for u in tree[v].values():
   nxt=d.copy()
   for i,ci in d.items():
    for j,cj in dp[u].items():
     if j and not(i&j):
      m=i|j;val=ci+cj+edge[u]
      if val<nxt.get(m,1<<60):nxt[m]=val
   d=nxt
  dp[v]=d
 return (28+dp[0][15] if 15 in dp[0] else None),nwords,len(tree)

def classify(h):
 rows=[]
 for k in keys(h):
  m,n,nodes=solve(h,k)
  rows.append(dict(key=list(k),cost=m,candidate_words=n,trie_nodes=nodes))
 good=[r for r in rows if r['cost'] is not None]
 m=min(r['cost'] for r in good)
 return dict(h=h,legal_keys=len(rows),feasible_keys=len(good),
   candidate_words=sum(r['candidate_words'] for r in rows),
   minimum=m,minimizers=[r['key'] for r in good if r['cost']==m],rows=rows)

if __name__=='__main__':
 runs=[classify(int(x)) for x in sys.argv[1:]] if len(sys.argv)>1 else [classify(8),classify(9)]
 print(json.dumps(dict(scope='H2 mandatory four original words; all Hh four signatures share one key',
                      runs=runs),indent=2))

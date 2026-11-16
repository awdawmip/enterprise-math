from collections import Counter
from itertools import combinations
import itertools

def paired(P,rots,bad,pair,class_cost):
 inv=[25*(-(i//25)%5)+5*(-(i//5%5)%5)+(-(i%5)%5) for i in range(125)]
 cycles=[[i,j]for i,j in enumerate(inv) if i<j];store=[]
 def rec(start,s,v,q):
  for j in range(start,len(cycles)):
   a,b=cycles[j];bmask=1<<b;amask=1<<a
   if any((bad[a][x]|bad[b][x])&q or bad[a][b]>>x&1 for x in v):continue
   w=v+[a,b];c=class_cost(w,pair);m=q|amask|bmask
   store.append((set(w),c))
   rec(j+1,s+2,w,m)
 rec(0,0,[],0)
 records=[]
 for k,g in enumerate(rots):
  ix={}
  for i in range(125):
   if i in ix:continue
   j=i;idx=max(ix.values(),default=-1)+1
   while j not in ix:ix[j]=idx;j=g[j]
  best={}
  for row,c in store:
   shifted={g[x]for x in row}
   if not row.isdisjoint(shifted):continue
   sup=sum(1<<j for j in {ix[x]for x in row});m=sum(1<<j for j in row)
   if sup not in best or c<best[sup][0]:best[sup]=c,m
  (P/f'duo{k}').write_text(''.join(f'{q} {c} {m%2**64} {m>>64}\n'for q,(c,m)in sorted(best.items())))
  records.append([len(store),len(best)])
 return records

def fixed(P,rots,bad,pair,class_cost):
 records=[]
 for t,g in enumerate(rots):
  cycles=[];ix={}
  for i in range(125):
   if i in ix:continue
   q=[];j=i
   while j not in q:q.append(j);ix[j]=len(cycles);j=g[j]
   cycles.append(q)
  E={};counts=Counter()
  def rec(start,q,points):
   for idx in range(start,32):
    v=points+cycles[idx];s=len(v)
    if s>13 or any(bad[a][b]>>c&1 for a,b,c in itertools.combinations(v,3)):continue
    m=q|(1<<idx);cost=class_cost(v,pair);E[m]=cost;counts[s]+=1
    rec(idx+1,m,v)
  rec(0,0,[])
  (P/f'fix{t}').write_text(''.join(f'{q} {c}\n'for q,c in sorted(E.items())))
  records.append(len(E))
 return records

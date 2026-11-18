#!/usr/bin/env python3
"""Independent signed-X6 full nine-history exact Fraction rank and witness audit."""
import sys,json
from fractions import Fraction
from collections import Counter
P={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START=[('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0)]
BUCKET=['N','A','B','AB','BA']
def expanded(w):return [v for ch in w for v in P[ch]]
def fingerprint(w):
 out=[]
 for name,p0 in START:
  p=p0;b=name
  for s in expanded(w):
   if p==1 and s==2:
    if b=='N':b='A'
    elif b=='B':b='BA'
   elif p==2 and s==1:
    if b=='N':b='B'
    elif b=='A':b='AB'
   p=s
  out.append(BUCKET.index(b))
 return out
def rank(words):
 os=[fingerprint(w) for w in words]
 A=[[Fraction(int(os[j][i]==k)) for j in range(len(words)) for k in range(5)] for i in range(9)]
 rank=0
 for col in range(len(A[0])):
  idx=next((i for i in range(rank,9) if A[i][col]),None)
  if idx is None:continue
  A[rank],A[idx]=A[idx],A[rank]
  d=A[rank][col];A[rank]=[v/d for v in A[rank]]
  for j in range(rank+1,9):
   q=A[j][col]
   if q:A[j]=[A[j][k]-q*A[rank][k] for k in range(len(A[j]))]
  rank+=1
  if rank==9:break
 return rank
def audit(ws):
 pres=set();keys=set();sigs=set();counts=[]
 for hs,words in sorted(ws.items(),key=lambda kv:int(kv[0])):
  h=int(hs);assert len(words)==len(set(words));assert rank(words)==9,(h,words)
  for w in words:
   assert len(w)==h
   ss=expanded(w);ct=Counter(ss)
   assert tuple(ct[i]-ct[-i] for i in (1,2,3))==(2,0,0)
   keys.add(tuple(ct[i] for i in (1,2,3)))
   sigs.add(tuple(fingerprint(w)))
   for q in range(1,len(ss)+1):pres.add(tuple(ss[:q]))
  counts.append((h,len(words),len(pres)))
 assert len(keys)==5 and len(sigs)==6
 return len(pres),sorted(keys),counts
source=sys.argv[1] if len(sys.argv)>1 else 'EXACT_WITNESSES_EC49FDT.json'
obj=json.load(open(source))
assert obj['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
out=[]
for i,row in enumerate(obj['rows']):
 cost,keys,counts=audit(row['witness'])
 assert cost==row['objective']==row['dual_bound'] and row['solver_status']==0 and row['mip_gap']==0
 assert [c[1] for c in counts]==[3,2,2,4,2,4,4,2]
 out.append({'case':i,'cost':cost,'keys':keys,'window_path_counts_and_cumulative_costs':counts})
print(json.dumps({'schema':'EC49FDT_INDEPENDENT_EXACT_FRACTION_AUDIT','science_pin':obj['science_pin'],'passed':len(out),'cases':out},indent=2))

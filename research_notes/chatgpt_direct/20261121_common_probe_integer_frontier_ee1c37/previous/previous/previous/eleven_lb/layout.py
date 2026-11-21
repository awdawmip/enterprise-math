from pathlib import Path
from itertools import product
from collections import defaultdict
import sys
from costs import partitions
mins=[0,0,12,36,72,120,201,292,419,557,744,936,1104,1296]
em=[*mins[:8],460,608,768,936,1104,1296]
pr=[*mins[:8],419,557,744,1008,1244,50000]
U=[0,13,26,39,52,65,78,85,96,102,112,119,121,125]
def cases(ceiling):
 found={}
 for sizes in partitions(125,11):
  if sum(mins[s]for s in sizes)>ceiling or sizes.count(13)>=3:continue
  keys=sorted(set(sizes));counts=[sizes.count(s)for s in keys]
  for n in product(*(range(k+1)if s<13 else(0,)for s,k in zip(keys,counts))):
   P=tuple(s for s,j in zip(keys,n)for _ in range(j));E=tuple(s for s,k,j in zip(keys,counts,n)for _ in range(k-j))
   if len(P)<4 or len(P)==4 and sum(P)<=41 or any(sum(E[-i:])>U[i]for i in range(1,len(E)+1)):continue
   ns=E.count(12);nb=E.count(13)
   if ns+nb>=7:continue
   floor=sum(pr[s]for s in P)+sum(em[s]for s in E)
   for nc in range(ns+1):
    if nc+nb>4:continue
    raw=floor+12*(ns-nc)
    cutoff=max(raw,11036)if nc+nb>=4 else raw
    if cutoff<=ceiling:
     if P not in found:found[P]=[{},set()]
     prices,dem=found[P];dem.add(E)
     for s in set(P):prices[s]=max(prices.get(s,0),pr[s]+ceiling-raw)
 return {k:(prices,[min(sum(e[:j])for e in dem)for j in range(1,len(next(iter(dem)))+1)])for k,(prices,dem)in found.items()}
if __name__=='__main__':
 for p,(v,d) in sorted(cases(int(sys.argv[1])).items()):print(p,v,d)

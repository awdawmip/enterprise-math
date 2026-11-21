from pathlib import Path
import sys
from itertools import product
mins=[0,0,12,36,72,120,201,292,419,557,744,936,1104,1296]
em=[*mins[:8],460,608,768,936,1104,1296]
pr=[*mins[:8],419,557,744,1008,1244,50000]
U=[0,13,26,39,52,65,78,85,96,102,112,119,121,125]
def cases(cap, partitions):
 for sizes in partitions(125,11):
  if sum(mins[s]for s in sizes)>cap or sizes.count(13)>=3:continue
  keys=sorted(set(sizes));cc=[sizes.count(x)for x in keys]
  for nn in product(*(range(c+1)if x<13 else(0,)for x,c in zip(keys,cc))):
   P=tuple(s for s,n in zip(keys,nn)for _ in range(n));E=tuple(s for s,c,n in zip(keys,cc,nn)for _ in range(c-n))
   if len(P)<4 or len(P)==4 and sum(P)<=41 or any(sum(E[-i:])>U[i]for i in range(1,len(E)+1)):continue
   a,b=E.count(12),E.count(13)
   if a+b>=7:continue
   floor=sum(em[s]for s in E)+12*max(0,a+b-4);mc=floor+sum(pr[s]for s in P)
   if mc<=cap:yield P,E,floor

from REPRO_STAGE511B import *
import json
stats=[]
for h in (1,2):
 for cap in (0,1):
  groups={}; roots=collisions=0; witness=None
  for n in range(2,8):
   for xs in product(range(4),repeat=n):
    word=tuple(((0,2)[x//2],x%2,i) for i,x in enumerate(xs))
    R=(n-1,n-2)
    sig,_=compressed(word,h,R,(1,3),(0,2),cap)
    res=future_signature(word,h,R,(1,3),(0,2))
    key=(n,sig)
    if key in groups:
     collisions+=1
     if groups[key][0]!=res:
      witness={'first':groups[key][1],'second':xs,'n':n,'h':h,'cap':cap};break
    else:groups[key]=(res,xs)
    roots+=1
   if witness:break
  stats.append({'h':h,'cap':cap,'roots':roots,'collisions':collisions,'witness':witness})
print(json.dumps(stats,indent=2))

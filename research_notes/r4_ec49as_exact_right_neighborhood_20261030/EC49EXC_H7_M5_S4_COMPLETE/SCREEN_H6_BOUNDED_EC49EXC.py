#!/usr/bin/env python3
from VERIFY_EC49ER import *
from VERIFY_EC49ES import bounded_opt
from collections import Counter
import json,time,sys,os
s=time.time();fs=fibers()
report=json.load(open('EC49EXC_SCREENED.json'))
arr=report['unresolved']
respath='EC49EXC_H6_BOUNDED_COMPLETE.json'
out=json.load(open(respath)) if os.path.exists(respath) else {}
limit=int(sys.argv[1]) if len(sys.argv)>1 else len(arr)
for i,row in enumerate(arr[:limit]):
 k=tuple(tuple(p) for p in row['h3to6'])
 ks=':'.join(','.join(map(str,p)) for p in k)
 if ks not in out:
  info=bounded_opt(fs,k,71)
  out[ks]=info['E']
 if (i+1)%20==0:
  json.dump(out,open(respath,'w'))
  print('H6 bounded',i+1,'/',len(arr),'elapsed',round(time.time()-s,2),'below72',sum(v is not None for v in out.values()),flush=True)
json.dump(out,open(respath,'w'))
print('DONE',len(out),'below72',sum(v is not None for v in out.values()),'elapsed',time.time()-s,flush=True)

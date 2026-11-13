#!/usr/bin/env python3
from math import comb,gcd
from functools import reduce
from pathlib import Path
import json,hashlib
def B(n,k):return comb(n,k) if 0<=k<=n else 0
def C(k):return B(2*k,k)//(k+1) if k>=0 else 0
def raw(r,s):return B(r+s,2*s)*sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))
def cat(r,s):
 k=(r-1)//2
 return B(r+s,2*s)*sum(B(s-1,2*q)*4**q*C(k-q) for q in range(k+1))
P=Path(__file__).resolve().parent; rows=[]; checks=0; meta=[]
for r in range(5,100,2):
 a=[raw(r,r-i) for i in range(r-1)]
 assert a==[cat(r,r-i) for i in range(r-1)] and all(v>0 for v in a)
 g=reduce(gcd,a);a=[v//g for v in a];checks+=len(a)
 meta.append({'r':r,'gcd':str(g),'maxbits':max(a).bit_length()})
 rows.append(str(r)+' '+str(len(a))+' '+' '.join(map(str,a)))
by=('\n'.join(rows)+'\n').encode()
(P/'R441_INPUTS.txt').write_bytes(by)
(P/'R441_INPUT_META.json').write_text(json.dumps({'checks':checks,'rows':meta,'sha256':hashlib.sha256(by).hexdigest()},indent=2)+'\n')
print('INPUT_PASS',len(rows),checks,hashlib.sha256(by).hexdigest())

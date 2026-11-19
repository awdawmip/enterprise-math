#!/usr/bin/env python3
"""Independent NumPy exact audit of PREFIX945 W19 vs all earlier families.
Reads C++ generated W19 and historic sorted IDs. Independent CSR builds W19 separately.
"""
import json,hashlib
from pathlib import Path
import numpy as np
L,H,C=262145,524287,131072
N=1<<32
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'

def read(name,size):
 a=np.fromfile(name,dtype='<u8')
 assert len(a)==size,(name,len(a),size)
 assert np.all(a[1:]>a[:-1]),name
 assert int(a[-1])<C*C,name
 return a

def member(a,q):
 pos=np.searchsorted(a,q)
 result=np.zeros(len(q),dtype=bool)
 ok=pos<len(a)
 result[ok]=a[pos[ok]]==q[ok]
 return result

def bzs_v(ids):
 a=L+2*(ids//C).astype(np.int64);b=L+2*(ids%C).astype(np.int64)
 BZS=(b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))|(((a//np.gcd(a,b))*b)<N)
 vals=np.arange(L,H+1,2,dtype=np.int64);r=np.ones(C,dtype=np.int64)
 S=np.zeros(C,dtype=bool);D=np.zeros(C,dtype=bool)
 for step in range(1,53):
  r=(2*r)%vals
  hit=(r==1)|(r==vals-1)
  if step<=31:S|=hit
  else:D|=hit&~S
 D&=~S
 assert int(S.sum())==24 and int(D.sum())==91
 BZS|=S[(b-L)//2]
 Z=np.unique(np.concatenate([vals[D],np.array([262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287],dtype=np.int64)]))
 assert len(Z)==104
 Zmap=np.zeros(C,dtype=bool);Zmap[(Z-L)//2]=1
 Tmap=np.zeros(C,dtype=bool);Tmap[(77081*np.arange(1024,dtype=np.int64)+12345)%C]=1
 V=Zmap[(a-L)//2]|Zmap[(b-L)//2]|((a>=500001)&Tmap[(b-L)//2])|((b>=500001)&Tmap[(a-L)//2])
 return BZS,V

def audit():
 W=read('PREFIX945_W19.bin',12701275)
 NEW=read('PREFIX945_NEW19.bin',6315834)
 bz,v=bzs_v(W)
 remain=~bz
 res={'BZS':int(bz.sum())}
 prior=[('U','PREFIX928_R6_SORTED_PAIR_IDS.bin',5295478),('V',None,0),
 ('W2','W2.bin',30211412),('W3','W3.bin',19413088),('D4','D4_sorted_cpp.bin',1793182),('W5','W5.bin',15406809),('D6','D6.bin',1771013),('W7','W7.bin',14698334),('D8','D8.bin',4043794),('W9','W9.bin',15456919),('D10','D10.bin',1736455),('W11','W11_REGEN.bin',13144330),('W13','W13.bin',12993739),('W15','PREFIX944_W15.bin',16762415),('W17','PREFIX944_W17.bin',15136736)]
 for label,filename,cnt in prior:
  if label=='V':ms=v[remain]
  else:ms=member(read(filename,cnt),W[remain])
  res[label]=int(ms.sum())
  idx=np.flatnonzero(remain)
  remain[idx[ms]]=False
 res['NEW']=int(remain.sum())
 assert np.array_equal(W[remain],NEW)
 assert sum(res.values())==len(W)
 samples=np.linspace(0,len(W)-1,1001,dtype=np.int64)
 assert all(any(((19*(L+2*(int(W[s])//C)))^(1<<j))-(1<<i)>0 and
    (((19*(L+2*(int(W[s])//C)))^(1<<j))-(1<<i))%(L+2*(int(W[s])%C))==0
    for i in range(19) for j in range(19)) for s in samples)
 result={'schema':'PREFIX945_R6_INDEPENDENT_PRIORITY_V1','scientific_pin':PIN,
   'scope':'FULL_DOMAIN_PRIORITY_BUCKETS_PLUS_1001_SAMPLED_WITNESSES; FULL_CANDIDATE_INDEPENDENT_CSR_IN_SEPARATE_RUN',
   'k':19,'unique':len(W),'priority':res,'net_new':len(NEW),'updated_union':7577727669+len(NEW),
   'not_in_certificates':C*C-(7577727669+len(NEW)),
   'sha_W':hashlib.file_digest(open('PREFIX945_W19.bin','rb'),'sha256').hexdigest(),
   'sha_NEW':hashlib.file_digest(open('PREFIX945_NEW19.bin','rb'),'sha256').hexdigest(),
   'status':'ALL_FULL_DOMAIN_PRIORITY_ASSERTIONS_PASSED'}
 Path('PREFIX945_R6_INDEPENDENT_PRIORITY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':audit()

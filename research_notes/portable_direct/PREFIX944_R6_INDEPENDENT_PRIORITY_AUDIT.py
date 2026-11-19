#!/usr/bin/env python3
"""Independent NumPy audit: source candidate set membership, priority partition and sample witnesses.
Exact full-domain priority audit reads C++ generated sorted W15/W17 IDs; it does not regenerate them.
Full raw witness totals are independently certified via prior PREFIX-942 CRT/floor-sum computation.
"""
import json,hashlib
from pathlib import Path
import numpy as np
L,H,C=262145,524287,131072
N=1<<32
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
inputs=[('U','PREFIX928_R6_SORTED_PAIR_IDS.bin',5295478),('W2','W2.bin',30211412),('W3','W3.bin',19413088),('D4','D4_sorted_cpp.bin',1793182),('W5','W5.bin',15406809),('D6','D6.bin',1771013),('W7','W7.bin',14698334),('D8','D8.bin',4043794),('W9','W9.bin',15456919),('D10','D10.bin',1736455),('W11','W11_REGEN.bin',13144330),('W13','W13.bin',12993739)]

def read(name, size):
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

def analyze(k,prior_union,previous):
 W=read(f'PREFIX944_W{k}.bin',{15:16762415,17:15136736}[k]); NEW=read(f'PREFIX944_NEW{k}.bin',{15:6732916,17:6467873}[k])
 bz,v=bzs_v(W)
 remain=~bz
 result={'BZS':int(bz.sum())}
 for label, filename, cnt in previous:
  if label=='V':ms=v[remain]
  else:ms=member(read(filename,cnt),W[remain])
  result[label]=int(ms.sum())
  indices=np.flatnonzero(remain)
  remain[indices[ms]]=False
 assert np.array_equal(W[remain],NEW),(k,'NEW mismatch')
 result['NEW']=len(NEW)
 assert sum(result.values())==len(W)
 samples=np.unique(np.linspace(0,len(W)-1,1001,dtype=np.int64))
 assert all(any((k*(L+2*(int(W[s])//C))^(1<<j))-(1<<i)>0 and
                 ((k*(L+2*(int(W[s])//C))^(1<<j))-(1<<i))%(L+2*(int(W[s])%C))==0
                 for i in range(19) for j in range(19)) for s in samples)
 return {'k':k,'raw_reused_from_prior_CRT':{15:20708178,17:19318164}[k], 'unique':len(W),'priority':result,'net_new':len(NEW),
 'previous_union':prior_union,'updated_union':prior_union+len(NEW),'outside':C*C-prior_union-len(NEW),
 'sha_W':hashlib.file_digest(open(f'PREFIX944_W{k}.bin','rb'),'sha256').hexdigest(),
 'sha_NEW':hashlib.file_digest(open(f'PREFIX944_NEW{k}.bin','rb'),'sha256').hexdigest(),
 'sample_witnesses_exactly_verified':len(samples)}

order=inputs[:1]+[('V','',0)]+inputs[1:]
a=analyze(15,7564526880,order)
b=analyze(17,a['updated_union'],order+[('W15','PREFIX944_W15.bin',16762415)])
out={'schema':'PREFIX944_R6_INDEPENDENT_PRIORITY_AUDIT_V1','scientific_pin':PIN,
 'scope':'FULL_SORTED_CANDIDATE_PRIORITY_AND_PARTITION_INDEPENDENT_NUMPY_AUDIT_PLUS_DETERMINISTIC_WITNESS_SAMPLE; NOT_INDEPENDENT_CANDIDATE_SET_GENERATION',
 'k15':a,'k17':b,'status':'ALL_ASSERTIONS_PASSED'}
Path('PREFIX944_R6_INDEPENDENT_PRIORITY_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

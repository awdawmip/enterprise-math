#!/usr/bin/env python3
# PREFIX-933 independent NumPy exact census, run with U W2 W3 D4 binary arguments.
import sys, hashlib, json
import numpy as np
Q,M,N=262145,131072,1<<32
assert len(sys.argv)==5
U,W2,W3=[np.fromfile(p,dtype='<u8') for p in sys.argv[1:4]]
assert (len(U),len(W2),len(W3))==(5295478,30211412,19413088)
a=np.arange(Q,524288,2,dtype=np.int64);rows=[];ct=np.zeros(9,dtype=np.int64)
for j in range(19):
 y=np.bitwise_xor(4*a,1<<j)
 for i in (range(19) if j==0 else (0,)):
  h=1<<i;d=y-h
  for t in range(1,9):
   b,r=np.divmod(d,t);ok=(r==0)&(b>=Q)&(b<=524287)&((b&1)==1)
   if not np.any(ok):continue
   assert np.all(y[ok]%b[ok]==h%b[ok]);ct[t]+=int(ok.sum())
   rows.append((np.nonzero(ok)[0].astype(np.uint64)*M+((b[ok]-Q)//2).astype(np.uint64)))
raw=np.concatenate(rows);ids=np.unique(raw).astype('<u8')
assert np.array_equal(ids,np.fromfile(sys.argv[4],dtype='<u8'))
r=np.ones(M,dtype=np.int64);early=np.zeros(M,dtype=bool);late=np.zeros(M,dtype=bool)
for k in range(1,53):
 r=(2*r)%a;hit=(r==1)|(r==a-1)
 if k<=31:early|=hit
 else:late|=hit
D=a[late&~early];S=a[early];assert (len(D),len(S))==(91,24)
L=np.unique(np.concatenate([D,[262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287]]))
T=np.unique(Q+2*((77081*np.arange(1024,dtype=np.int64)+12345)%M))
assert len(L)==104 and len(T)==1024
av=Q+2*(ids//M).astype(np.int64);bv=Q+2*(ids%M).astype(np.int64)
B=(bv<33*((N+av-1)//av))|(av<33*((N+bv-1)//bv))|early[(ids%M).astype(np.int64)]|(((av//np.gcd(av,bv))*bv)<N)
V=np.isin(av,L)|np.isin(bv,L)|((av>=500001)&np.isin(bv,T))|((bv>=500001)&np.isin(av,T))
def member(s,q):
 p=np.searchsorted(s,q);return (p<len(s))&(s[np.minimum(p,len(s)-1)]==q)
u,w2,w3=member(U,ids),member(W2,ids),member(W3,ids)
assert not np.any(B&u)
part={'BZS':int(B.sum())};m=~B
for label,x in [('U',u),('V',V),('W2',w2),('W3',w3)]:
 part[label]=int(np.count_nonzero(m&x));m &= ~x
part['new']=int(m.sum());assert sum(part.values())==len(ids)
first=int(ids[np.flatnonzero(m)[0]])
print(json.dumps({'raw':len(raw),'unique':len(ids),'by_t':ct[1:].tolist(),
 'sha256':hashlib.sha256(ids.tobytes()).hexdigest(),
 'partition':part,'union':7530824145+part['new'],
 'first_new':[Q+2*(first//M),Q+2*(first%M)]},indent=2))

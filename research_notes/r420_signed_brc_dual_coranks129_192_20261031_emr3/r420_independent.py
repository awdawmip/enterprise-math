#!/usr/bin/env python3
"""Independent direct-binomial cross-check of R420 signed corank certificates.
Does not import the certificate generator. Only exact integer operations.
"""
import json,hashlib,sys
from math import comb
from pathlib import Path

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def delta_direct(r,q):
 m=r-q
 return sum(comb(m,k)*(choose(2*q,r-2*k)-choose(2*q,r-2*k-1))
            for k in range(m+1))

def ev(coeff,x):
 z=0
 for a in reversed(coeff):z=z*x+int(a)
 return z

counts={'rows':0,'coefficients':0,'raw_turan':0,'raw_delta':0}
for name in sys.argv[1:]:
 p=Path(name)
 data=json.loads(p.read_text())
 assert data['schema']=='R420_DUAL_BRC_CORANK_EXACT_V1'
 for row in data['rows']:
  m=row['m'];counts['rows']+=1
  A=row['num_coeffs'];counts['coefficients']+=len(A)
  assert len(A)==4*m+6 and row['num_degree']==4*m+5
  assert not row['num_nonpositive_exponents']
  assert all(int(c)>0 for c in A)
  assert hashlib.sha256(','.join(A).encode()).hexdigest()==row['num_sha256']
  for s in (3,5,17,257,1024):
   x=s-3;r=s+m
   vals=[]
   for q in (s-1,s,s+1):
    v=delta_direct(r,q)
    vals.append(comb(r+q,2*q)*v)
    counts['raw_delta']+=1
   D=vals[1]*vals[1]-vals[0]*vals[2]
   assert D>0,(m,s,'nonpositive')
   N=row['N'];Q=row['Q']
   for h,q in enumerate((s-1,s,s+1)):
    assert delta_direct(r,q)*ev(Q[h],x)==comb(2*q,q)*ev(N[h],x),(m,s,q)
   C=comb(r+s,2*s)*comb(2*s,s)
   den=(s+1)**2*(2*s+m)*(m+1)*ev(Q[1],x)**2*ev(Q[0],x)*ev(Q[2],x)
   assert D*den==C*C*ev(A,x),(m,s,'Turan identity mismatch')
   counts['raw_turan']+=1
 print('VALIDATED',p.name,'rows',len(data['rows']),
       'file_sha256',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
print('R420_INDEPENDENT_PASS',counts)

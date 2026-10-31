#!/usr/bin/env python3
"""R420: exact fixed-corank m=r-s signed BRC auxiliary Turan certificates.
Entire computation is exact Python integers; this is not native X6.
"""
from math import comb
import json,hashlib,sys,time
from pathlib import Path

def add(a,b):
 o=[0]*max(len(a),len(b))
 for i,c in enumerate(a):o[i]+=c
 for i,c in enumerate(b):o[i]+=c
 return o

def sub(a,b):return add(a,[-c for c in b])
def mul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  if c:
   for j,d in enumerate(b):o[i+j]+=c*d
 return o

def prod(*a):
 o=[1]
 for q in a:o=mul(o,q)
 return o

def scaled(a,k):return [k*c for c in a]

def hori(h,m):
 """delta(r,q)/binom(2q,q)=N_h(x)/Q_h(x), q=x+3+h, r=x+3+m."""
 mq=m-h
 assert mq>=0
 q0=3+h
 L=mq+1
 prefix=[[1]]
 for d in range(L):prefix.append(mul(prefix[-1],[q0-d,1]))
 suffix=[None]*(L+1);suffix[L]=[1]
 for d in range(L-1,-1,-1):suffix[d]=mul([q0+d+1,1],suffix[d+1])
 atoms=[mul(prefix[d],suffix[d]) for d in range(L+1)]
 N=[0]*(L+1)
 for k in range(mq+1):
  d1=abs(mq-2*k);d2=abs(mq-2*k-1)
  v=comb(mq,k)
  for i in range(L+1):N[i]+=v*(atoms[d1][i]-atoms[d2][i])
 return N,suffix[0]

def cert(m):
 assert m>=1
 Nminus,Qminus=hori(-1,m)
 Nzero,Qzero=hori(0,m)
 Nplus,Qplus=hori(1,m)
 factor1=prod([4,1],[4,1],[m+6,2])
 factor2=prod([3,1],[3,1],[m+7,2])
 num1=scaled(prod(factor1,Nzero,Nzero,Qminus,Qplus),m+1)
 num2=scaled(prod(factor2,Nminus,Nplus,Qzero,Qzero),m)
 numerator=sub(num1,num2)
 denominator=scaled(prod(factor1,Qzero,Qzero,Qminus,Qplus),m+1)
 assert len(numerator)==len(denominator)
 while numerator[-1]==0 and len(numerator)>1:numerator.pop()
 assert all(c>0 for c in denominator)
 nonpositive=[i for i,c in enumerate(numerator) if c<=0]
 return {'m':m,'num_degree':len(numerator)-1,'den_degree':len(denominator)-1,
         'num_coeff_count':len(numerator),'num_nonpositive_exponents':nonpositive,
         'num_coeffs':[str(z) for z in numerator],
         'num_sha256':hashlib.sha256(','.join(map(str,numerator)).encode()).hexdigest(),
         'den_sha256':hashlib.sha256(','.join(map(str,denominator)).encode()).hexdigest(),
         'den_positive':all(c>0 for c in denominator),
         'N':[Nminus,Nzero,Nplus], 'Q':[Qminus,Qzero,Qplus]}

def main():
 hi=int(sys.argv[1]) if len(sys.argv)>1 else 160
 lo=int(sys.argv[2]) if len(sys.argv)>2 else 129
 rows=[]
 t0=time.time()
 for m in range(lo,hi+1):
  r=cert(m);rows.append(r)
  print('R420',m,'numdeg',r['num_degree'],'count',r['num_coeff_count'],
        'nonpos',r['num_nonpositive_exponents'],'time',round(time.time()-t0,2),flush=True)
 obj={'schema':'R420_DUAL_BRC_CORANK_EXACT_V1','s_lower':3,'m_range':[lo,hi],'rows':rows}
 path=Path(__file__).with_name(f'R420_DUAL_EVIDENCE_{lo}_{hi}.json')
 path.write_text(json.dumps(obj,separators=(',',':'))+'\n')
 print('R420_END',lo,hi,'total_positive',sum(r['num_coeff_count'] for r in rows),
       'sha256',hashlib.sha256(path.read_bytes()).hexdigest())

if __name__=='__main__':main()

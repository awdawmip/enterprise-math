#!/usr/bin/env python3
"""Exact finite verifier, original frozen R462 signed BRC K at theta=0."""
import itertools,json,math
from fractions import Fraction
def C(n,k):return math.comb(n,k) if 0<=k<=n else 0
def K(i):
 d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
 p=[0]*(i+15)
 for r in range(1,5):
  n=i+1-r
  if n>=0:
   for j in range(n+1):p[i-1+j]-=d[r-1]*C(n,j)
 while len(p)>1 and not p[-1]:p.pop()
 return p
def mul(p,q):
 z=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  if a:
   for j,b in enumerate(q):z[i+j]+=a*b
 return z
def nu(p):return next((i for i,x in enumerate(p) if x),None)
def coef(p,h):return p[h] if h<len(p) else 0
def jet(p,d):return tuple(p[:d+1]+[0]*max(0,d+1-len(p)))
def deconv(y,d):
 a=[]
 for n in range(d+1):a.append((Fraction(coef(y,n))-3*(a[-1] if a else 0))/2)
 return a
ks=[K(i) for i in range(1,13)]
assert [nu(p) for p in ks]==list(range(12))
assert [p[nu(p)] for p in ks]==[2,-1,-8,-11,6,53,106,119,83,36,9,1]
assert ks[0]==[2,3]
perms=list(itertools.permutations(range(6)))
assert len(perms)==720
bad=[1,0,0,2,97]
badp=[mul(bad,p) for p in ks]
sigs=[(coef(badp[2*j],8),coef(badp[2*j+1],3)) for j in range(6)]
assert sigs==[(0,4),(394,-11),(561,0),(561,0),(83,0),(0,0)]
assert len({tuple(sigs[j] for j in pi) for pi in perms})==360
samples=[("unit",[1]),("bad_common_gain",bad),("shifted",[0,0,1,1,0,2]),("signed_shift",[0,-3,0,1])]
cases=[]
for name,A in samples:
 r=nu(A)
 positive=[mul(A,ks[2*j]) for j in range(6)]
 assert [nu(p) for p in positive]==[r+2*j for j in range(6)]
 for d in [r-1,r,r+1,r+2,r+4,r+6,r+7,r+8,r+10,r+12]:
  if d<0:continue
  sig=[jet(p,d) for p in positive]
  n=len({tuple(sig[j] for j in pi) for pi in perms})
  k=max(0,min(6,(d-r)//2+1)) if d>=r else 0
  assert n==math.factorial(6)//math.factorial(6-k),(name,d,n)
  cases.append(dict(sample=name,r=r,d=d,visible=k,orientations=n))
 d=r+12
 assert deconv(mul(A,ks[0]),d)==list(map(Fraction,jet(A,d)))
evidence=dict(schema="EM_R625_COMMON_GAIN_TOMOGRAPHY_EXACT_V1",status="AUTHOR_SIDE_EXACT_COMPUTATION",frozen_commit="18783e01e3646c72b7aab3b16d3f565e83e6446f",theta=0,samples=[dict(name=name,gain_coefficients=A) for name,A in samples],raw_packet_collision=dict(A=bad,signatures=sigs if False else [(0,4),(394,-11),(561,0),(561,0),(83,0),(0,0)],distinct_codes=360,total_codes=720),jet_cases=cases,case_count=len(cases),orientation_checks_per_case=720,deconvolution_checks=len(samples),marker="R625_COMMON_GAIN_VALUATION_TOMOGRAPHY_EXACT_PASS")
print(json.dumps(evidence,ensure_ascii=False,indent=2))

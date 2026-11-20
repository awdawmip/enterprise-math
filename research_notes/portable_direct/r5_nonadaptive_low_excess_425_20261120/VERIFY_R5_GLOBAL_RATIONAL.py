#!/usr/bin/env python3
"""Exact all-excess rational R5 generator; validates via direct early enumeration.

Place unchanged frozen EXACT_R5_ALL_101_BUDGETS.json,
RESULT_R5_MIXED_ERASURE_RIGIDITY.json and the companion
VERIFY_R5_LOW_EXCESS_425.py in the same directory.
stdlib only. Python arbitrary-precision integer operations.
"""
from pathlib import Path
from functools import lru_cache
import hashlib, json, importlib.util
P=Path(__file__).resolve().parent
SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
assert hashlib.sha256((P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()).hexdigest()==SHA
prior=json.loads((P/"RESULT_R5_MIXED_ERASURE_RIGIDITY.json").read_text())
S=[set(x) for x in prior["minimal_sets"]]
assert S==[set(range(214,219)),{214,*range(216,222)},{215,*range(216,222)},set(range(223,291)),set(range(296,313))]
OTHER=sorted(set(range(214,315))-set.union(*S))
assert OTHER==[222,291,292,293,294,295,313,314]

def add(x,y):return [a+b for a,b in zip(x,y)]
def sub(x,y):return [a-b for a,b in zip(x,y)]
def shift(x,s,N):return [0]*s+x[:N+1-s] if s<=N else [0]*(N+1)
def mul(x,y,N):
 z=[0]*(N+1); ys=[(j,b) for j,b in enumerate(y) if b]
 for i,a in enumerate(x):
  if not a:continue
  for j,b in ys:
   if i+j>N:break
   z[i+j]+=a*b
 return z
@lru_cache(None)
def unrestricted(prices,N):
 z=[0]*(N+1);z[0]=1
 for p in prices:
  for i in range(p,N+1):z[i]+=z[i-p]
 return tuple(z)
@lru_cache(None)
def exact_count(prices,n,N):
 z=[[0]*(N+1) for _ in range(n+1)];z[0][0]=1
 for p in prices:
  for c in range(1,n+1):
   for t in range(p,N+1):z[c][t]+=z[c-1][t-p]
 return tuple(z[n])
@lru_cache(None)
def at_least(prices,n,N):
 z=list(unrestricted(prices,N))
 for j in range(n):z=sub(z,exact_count(prices,j,N))
 return z

def partial_H(s,N):
 if not s:return list(unrestricted((214,215,219,220,221),N))
 d=lambda k:at_least((219,220,221),k,N)
 g214=list(unrestricted((214,),N));g215=list(unrestricted((215,),N))
 out=shift(mul(mul(g214,g215,N),d(0),N),429*s,N)
 for b in range(s):out=add(out,shift(mul(g214,d(s-b),N),214*s+215*b,N))
 for a in range(s):out=add(out,shift(mul(g215,d(s-a),N),215*s+214*a,N))
 for a in range(s):
  for b in range(s-a,s):out=add(out,shift(d(max(s-a,s-b)),214*a+215*b,N))
 return out
def early_rational(m,N):
 cprices=(216,217,218)
 z=mul(at_least(cprices,m,N),partial_H(0,N),N)
 for c in range(m):z=add(z,mul(exact_count(cprices,c,N),partial_H(m-c,N),N))
 return z

def early_direct(m,N):
 # Independent early incidence check: counts a,b,c,d and exact
 # price-option multisets in the two 3-price groups.
 out=[0]*(N+1);C=(216,217,218);D=(219,220,221)
 for a in range(N//214+1):
  for b in range(N//215+1):
   if 214*a+215*b>N:continue
   for c in range(N//216+1):
    for d in range(N//219+1):
     if min(a+b+c,a+c+d,b+c+d)<m:continue
     off=214*a+215*b
     if off+216*c+219*d>N:continue
     out=add(out,shift(mul(exact_count(C,c,N),exact_count(D,d,N),N),off,N))
 return out

spec=importlib.util.spec_from_file_location("low425",P/"VERIFY_R5_LOW_EXCESS_425.py")
low=importlib.util.module_from_spec(spec);spec.loader.exec_module(low)
out={"schema":"R5_ALL_EXCESS_RATIONAL_FINITE_CROSSCHECK_V1","science_sha256":SHA,
     "all_m_and_D_symbolic_proof":"GLOBAL_RATIONAL.md",
     "samples":{},"review":"NOT_REVIEWED"}
for m in (1,2,3):
 N=735*m+500
 E=early_rational(m,N)
 assert E==early_direct(m,N),m
 M=at_least(tuple(range(223,291)),m,N)
 L=at_least(tuple(range(296,313)),m,N)
 full=mul(mul(mul(E,M,N),L,N),unrestricted(tuple(OTHER),N),N)
 narrow,_=low.theoretical(m) if hasattr(low,"theoretical") else (None,None)
 if narrow is None:
  # Companion checker defines this univariate excess polynomial.
  narrow,_=low.theoretical(m) if "theoretical" in dir(low) else low.polynomial_m(m)
 assert full[735*m:735*m+426]==narrow
 out["samples"][str(m)]={
  "all_501_coefficients":True,"early_direct_match":True,
  "one_excursion_0_to_425_match":True,
  "coefficients_425_through_430":{str(d):str(full[735*m+d]) for d in range(425,431)}}
 print("PASS",m,"D 0..500; D425..430",out["samples"][str(m)]["coefficients_425_through_430"])
(P/"RESULT_R5_GLOBAL_RATIONAL.json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS frozen SHA and full all-excess rational/independent enumeration")

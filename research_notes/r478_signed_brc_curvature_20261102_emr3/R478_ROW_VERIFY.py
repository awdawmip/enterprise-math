#!/usr/bin/env python3
"""Two algebraically distinct full-row exact integer formulations for signed BRC auxiliary coefficients.
Positive Catalan coefficient and alternating Catalan coefficient are checked for *every* s.
R462 signed raw convolution is checked on a declared boundary/central sample.
"""
from math import comb
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,time
from R462_VERIFY_FROZEN_KERNEL import H_raw

def cat(k):return comb(2*k,k)//(k+1)
def h_positive(r,s,cs):
 k=(r-1)//2
 return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*cs[k-q] for q in range(min(k,(s-1)//2)+1))
def h_alt(r,s,cs):
 j=r-s
 return comb(r+s,j)*sum(comb(j,q)*(-2)**q*cs[r-q] for q in range(j+1))
def z(a,j):return a[j] if 0<=j<len(a) else 0
def minor2(a,j):return z(a,j)**2-z(a,j-1)*z(a,j+1)
def minor3(a,j):
 x=z(a,j);up=z(a,j+1);up2=z(a,j+2)
 lo=z(a,j-1);lo2=z(a,j-2)
 return x**3-2*lo*x*up+lo2*up*up+lo*lo*up2-lo2*x*up2
def put(d,x):
 assert x>=0
 b=x.to_bytes(max(1,(x.bit_length()+7)//8),'big');d.update(len(b).to_bytes(4,'big'));d.update(b)
start=time.monotonic();cres=sha256();mres=sha256();rows=[];raw_count=0;alt_count=0;total=0
for r in (281,283,285,287):
 k=(r-1)//2
 cs=[cat(t) for t in range(r+1)]
 a=[]
 for s in range(r,1,-1):
  v=h_positive(r,s,cs);av=h_alt(r,s,cs)
  assert v==av,(r,s,'alt');assert v>0,(r,s,'nonpositive');alt_count+=1
  put(cres,v);a.append(v)
 for j in range(len(a)):
  d2=minor2(a,j);d3=minor3(a,j)
  assert d2>0,(r,j,'D2',d2)
  assert d3>0,(r,j,'D3',d3)
  put(mres,d2);put(mres,d3)
 for s in sorted(set((2,3,4,5,r//2,r//2+1,r-4,r-3,r-2,r-1,r))):
  assert a[r-s]==H_raw(k,s),(r,s,'signed raw');raw_count+=1
 qs=[Fraction(0)]+[Fraction(a[j-1]*a[j+1],a[j]**2) for j in range(1,len(a)-1)]+[Fraction(0)]
 ratios_above_half=sum(q>Fraction(1,2) for q in qs)
 assert all(0<=q<1 for q in qs)
 for j in range(1,len(a)-1):
  numerator=Fraction(1)-2*qs[j]+qs[j]**2*(qs[j-1]+qs[j+1]-qs[j-1]*qs[j+1])
  assert numerator == Fraction(minor3(a,j),a[j]**3)
 rows.append({'r':r,'length':len(a),'max_coefficient_bits':max(v.bit_length() for v in a),'positive_coefficients':len(a),'positive_D2':len(a),'positive_D3':len(a),'interior_q_greater_than_half':ratios_above_half})
 total+=3*len(a)
out={'schema':'R478_ROW_EXACT_V1','result':'R478_ROW_PASS','rows':rows,'positive_sign_checks':total,'all_row_coefficient_positive_vs_alternating_checks':alt_count,'sample_signed_raw_checks':raw_count,'positive_coefficients_sha256':cres.hexdigest(),'positive_minors_sha256':mres.hexdigest(),'stream_encoding':'each positive integer in ascending r then j; four-byte big-endian byte length + unsigned minimal big-endian digits; interleaved D2,D3','arithmetic':'integer exact','scientific_input':'R462 frozen signed BRC + R441 positive and alternating Catalan identities','elapsed_s':round(time.monotonic()-start,3)}
Path('R478_ROW_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('R478_ROW_PASS',json.dumps(out,ensure_ascii=False),flush=True)

#!/usr/bin/env python3
"""Exact full-row check for signed BRC auxiliary scalar r=181.
Independent integer evaluation of every coefficient and every adjacent 2x2,3x3 minor.
This confirms one finite row, not a universal infinite-r theorem.
"""
from math import comb
from hashlib import sha256
import json
from pathlib import Path
R=181

def catalan(k):return comb(2*k,k)//(k+1)
def coefficient_raw(r,s):
 h=r-s
 def c(n,j):return comb(n,j) if 0<=j<=n else 0
 return comb(r+s,2*s)*sum(comb(h,q)*(c(2*s,r-2*q)-c(2*s,r-2*q-1)) for q in range(h+1))
def coefficient_alt(r,s):
 h=r-s
 return comb(2*r-h,h)*sum(comb(h,q)*(-2)**q*catalan(r-q) for q in range(h+1))
def row(r):
 k=(r-1)//2
 cats=[catalan(j) for j in range(k+1)]
 return [comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*cats[k-q] for q in range(min(k,(s-1)//2)+1)) for s in range(r,1,-1)]
def signed3(a,j):
 def x(q):return a[q] if 0<=q<len(a) else 0
 return x(j)**3-2*x(j-1)*x(j)*x(j+1)+x(j-2)*x(j+1)**2+x(j-1)**2*x(j+2)-x(j-2)*x(j)*x(j+2)
def put(h,n):
 assert n>0
 b=n.to_bytes(max(1,(n.bit_length()+7)//8),'big');h.update(len(b).to_bytes(4,'big'));h.update(b)
a=row(R);h=sha256(); checks={'a':0,'d2':0,'d3':0,'raw':0,'alt':0}
for j,v in enumerate(a):
 assert v>0,(j,'a');checks['a']+=1;put(h,v)
 x=a[j-1] if j else 0;y=a[j+1] if j+1<len(a) else 0
 d2=v*v-x*y;d3=signed3(a,j)
 assert d2>0,(j,'d2');assert d3>0,(j,'d3')
 checks['d2']+=1;checks['d3']+=1;put(h,d2);put(h,d3)
for s in [2,3,4,5,(R+1)//2,R-4,R-3,R-2,R-1,R]:
 assert a[R-s]==coefficient_raw(R,s);checks['raw']+=1
 assert a[R-s]==coefficient_alt(R,s);checks['alt']+=1
assert checks=={'a':180,'d2':180,'d3':180,'raw':10,'alt':10}
result={'r':R,'strict_sign_counts':checks,'total_full_row_signs':540,'stream_sha256':h.hexdigest(),'max_coefficient_bits':max(x.bit_length() for x in a),'math_scope':'finite r=181 row exact integer check; signed BRC auxiliary scalar, not native X6','status':'AUTHOR_SIDE_EXACT_INTEGER_UNREVIEWED_NOT_ADMITTED'}
(Path(__file__).resolve().parent/'R457_ROW_EVIDENCE.json').write_text(json.dumps(result,indent=2)+'\n')
print('R457_ROW_EXACT_PASS',json.dumps(result))

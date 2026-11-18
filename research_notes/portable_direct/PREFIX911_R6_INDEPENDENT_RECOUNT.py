"""PREFIX911 independent exact recount, solving a from each odd b.
Python 3 standard library only; checked against primary C++17 census.
The full C910 union overlap is computed by the separate primary classifier.
"""
from math import gcd
import json

L,H,Q=262145,524287,131072
expected={
 (9,2):(29127,29127),(9,4):(58254,58254),(9,8):(524287,511544),
 (10,1):(26216,26216),(10,3):(34952,34952),(10,7):(344528,337038),(10,9):(480596,468945),
 (11,2):(35748,35748),(11,4):(41704,41704),(11,6):(135038,133052),(11,8):(336619,329171),(11,10):(443261,432537),
 (12,1):(21846,21846),(12,5):(43690,43690),(12,7):(174762,171641),(12,11):(411088,401158)
}
rows=[]
for (k,ell),(want_w,want_u) in expected.items():
 assert gcd(k,ell)==1 and (k-ell)%2
 seen=set(); witness=0
 for i in range(1,23):
  for s in (-1,1):
   d=(1<<i)+s
   # a=(ell*(L+2*t)+d)/k; 2*ell*t = -ell*L-d (mod k).
   rhs=-ell*L-d; factor=2*ell; g=gcd(factor,k)
   assert rhs%g==0
   mod=k//g
   first=((rhs//g)*pow(factor//g,-1,mod))%mod if mod>1 else 0
   for t in range(first,Q,mod):
    b=L+2*t; v=ell*b+d
    assert v%k==0
    a=v//k
    if not (L<=a<=H and a%2==1):continue
    x=(1-k%2) if s==1 else k%2
    y=x+k*a
    assert (x^(1<<i))==x+(1<<i) and (y^1)==y-s
    assert y-x==k*a and (y-s)-(x+(1<<i))==ell*b
    assert 0<=x<2**32 and 0<=y-s<2**32
    seen.add(((a-L)//2)*Q+((b-L)//2));witness+=1
 assert (witness,len(seen))==(want_w,want_u), (k,ell,witness,len(seen))
 rows.append([k,ell,witness,len(seen)])
print("PREFIX911_INDEPENDENT_PYTHON_RECOUNT_PASS",len(rows),"families",sum(r[2] for r in rows),"parameter witnesses")
print(json.dumps(rows))

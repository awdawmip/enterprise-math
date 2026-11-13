"""Exact R486 rank-eight sign certificate; Python stdlib only."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations
import json
P=[3261216730699546072,16617614171725128196,39981135571275965278,59929987840471208605,62011950122774190432,46375466295697379586,25437085269009257482,10099174417966445101,2730166725879517000,397945196379591544,-20979292415325312,-24086513791259568,-4849976616018944,-264799997573120,52977820893184,7660421054464]
DEN=1344322432933390310400000000
B=lambda n,j:comb(n,j) if 0<=j<=n else 0
C=lambda k:comb(2*k,k)//(k+1)
def raw(k,t):
 r=2*k+1
 return 0 if t<2 or t>r else B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1)) for q in range(r-t+1))
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def prod(items):
 z=[F(1)]
 for x in items:z=mul(z,x)
 return z
def ev(p,k):
 z=F(0)
 for x in p[::-1]:z=z*k+x
 return z
def pt(t):
 z=[F(0)]
 for q in range((t-1)//2+1):
  fac=[]
  for h in range(q):fac.extend(([-h,1],[1-h,1]))
  for ell in range(2-t,t+2):
   if ell not in range(1-2*q,1):fac.append([ell,2])
  z=add(z,[F(B(t-1,2*q)*4**q,factorial(2*t))*v for v in prod(fac)])
 return z
p={t:pt(t) for t in range(2,11)};D=[[F(1)]]
for m in range(1,9):
 z=[F(0)]
 for l in range(1,m+1):z=add(z,[(-1)**(l-1)*v for v in prod([p[l+2]]+[p[2]]*(l-1)+[D[m-l]])])
 D.append(z)
Q8=[F(x,DEN) for x in prod([[0,1]]*8+[[1,1]]*8+[[2,1]]+[[1,2]]*8+[[3,2]]*8+[P])]
assert len(Q8)==49 and D[8]==Q8
shift=[sum(P[i]*B(i,j)*9**(i-j) for i in range(j,16)) for j in range(16)]
assert all(x>0 for x in shift)
small=[int(ev(P,k)) for k in range(1,10)]
assert all(x>0 for x in small[:5]) and all(x<0 for x in small[5:8]) and small[8]>0
for k in range(1,101):
 for t in range(2,11):assert ev(p[t],k)*C(k)==raw(k,t)
def det(a):
 a=[row[:] for row in a];n=len(a);sgn=1;d=1
 for i in range(n-1):
  if a[i][i]==0:
   t=next((j for j in range(i+1,n) if a[j][i]),None)
   if t is None:return 0
   a[i],a[t]=a[t],a[i];sgn=-sgn
  z=a[i][i]
  for j in range(i+1,n):
   for h in range(i+1,n):
    x=a[j][h]*z-a[j][i]*a[i][h];assert x%d==0;a[j][h]=x//d
   a[j][i]=0
  d=z
 return sgn*a[-1][-1]
ks=list(range(1,21))+[22,24,30,49,50,64,100,101];examples={}
for k in ks:
 a=[[raw(k,3+i-j) for j in range(8)] for i in range(8)]
 x=det(a);assert x==ev(D[8],k)*C(k)**8
 assert (x>0 if k<=5 or k>=9 else x<0)
 if k in (5,6):
  y=0
  for perm in permutations(range(8)):
   term=1
   for i in range(8):term*=a[i][perm[i]]
   y+=(-1)**sum(perm[i]>perm[j] for i in range(8) for j in range(i+1,8))*term
  assert x==y
 if k in (5,6,8,9):examples[str(k)]=str(x)
print(json.dumps({'status':'R486_EXACT_PASS','scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f','P8_ascending':P,'shift9_ascending':shift,'P8_k1_to9':small,'polynomial_coefficients_checked':49,'raw_coefficients_checked':900,'det_8x8_checked':28,'permutation_crosschecks':2,'examples':examples,'rank8_asymptotic_constant':str(D[8][-1]/2**48),'arithmetic':'exact int/Fraction','admission':'AUTHOR_SIDE_UNREVIEWED'},sort_keys=True,indent=2))

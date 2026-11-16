from fractions import Fraction as Q
from math import comb, factorial
from itertools import permutations
import json

def B(n,j): return comb(n,j) if 0<=j<=n else 0
def cat(k): return comb(2*k,k)//(k+1)
def raw(k,t):
 r=2*k+1
 if t<2 or t>r: return 0
 return B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1)) for q in range(r-t+1))
def add(a,b):
 c=[Q(0)]*max(len(a),len(b))
 for i,x in enumerate(a): c[i]+=x
 for i,x in enumerate(b): c[i]+=x
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def mul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[i+j]+=x*y
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def prod(a):
 z=[Q(1)]
 for x in a:z=mul(z,x)
 return z
def val(a,k):
 z=Q(0)
 for x in reversed(a):z=z*k+x
 return z
def p(t):
 z=[Q(0)]
 for q in range((t-1)//2+1):
  f=[]
  for h in range(q):f.extend(([-h,1],[1-h,1]))
  for ell in range(2-t,t+2):
   if ell not in range(1-2*q,1):f.append([ell,2])
  z=add(z,[Q(B(t-1,2*q)*4**q,factorial(2*t))*x for x in prod(f)])
 return z
def det_bareiss(a):
 a=[list(x) for x in a];n=len(a);d=1;sgn=1
 for i in range(n-1):
  if not a[i][i]:
   t=next((v for v in range(i+1,n) if a[v][i]),None)
   if t is None:return 0
   a[i],a[t]=a[t],a[i];sgn=-sgn
  pivot=a[i][i]
  for j in range(i+1,n):
   for h in range(i+1,n):
    z=a[j][h]*pivot-a[j][i]*a[i][h]
    assert z%d==0
    a[j][h]=z//d
   a[j][i]=0
  d=pivot
 return sgn*a[-1][-1]
def det_perm(a):
 total=0
 for v in permutations(range(6)):
  x=1
  for i in range(6):x*=a[i][v[i]]
  total+=(-1)**sum(v[i]>v[j] for i in range(6) for j in range(i+1,6))*x
 return total
p={t:p(t) for t in range(2,9)}
D=[[Q(1)]]
for m in range(1,7):
 z=[Q(0)]
 for l in range(1,m+1):
  a=prod([p[l+2]]+[p[2]]*(l-1)+[D[m-l]])
  z=add(z,[(-1)**(l-1)*x for x in a])
 D.append(z)
P=[-187539930626,-763341392369,-1420784519035,-1592056245820,-1176221747345,-588627961757,-194130880828,-36905522140,-1311418640,1160905120,280076288,25137152]
R=prod([[0,1]]*6+[[1,1]]*6+[[2,1]]+[[1,2]]*6+[[3,2]]*6+[P])
R=[-Q(x,834132787488000000) for x in R]
assert D[6]==R and len(R)==37
shift=[sum(P[i]*B(i,j)*6**(i-j) for i in range(j,12)) for j in range(12)]
assert all(x>0 for x in shift)
small=[int(val(P,k)) for k in range(1,7)]
assert all(x<0 for x in small[:5]) and small[5]>0
for k in range(1,81):
 for t in range(2,9):assert val(p[t],k)*cat(k)==raw(k,t)
ks=list(range(1,21))+[22,24,30,49,50,64,100,101]; examples={}
for k in ks:
 a=[[raw(k,3+i-j) for j in range(6)] for i in range(6)]
 x=det_bareiss(a)
 assert x==val(D[6],k)*cat(k)**6 and (x>0 if k<=5 else x<0)
 if k in (1,5,6,8,49,101):assert det_perm(a)==x
 if k in (5,6):examples[str(k)]=str(x)
assert D[6][-1]/2**36==Q(-6137,3416607897550848000000)
print(json.dumps({'status':'R484_EXACT_PASS','source_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f','polynomial_coefficients_checked':37,'P6_shift6_ascending':shift,'P6_1_through_6':small,'raw_coefficient_checks':560,'raw_6x6_determinants':len(ks),'raw_720_term_determinants':6,'examples':examples,'rank6_limit':'-6137/3416607897550848000000','arithmetic':'exact integers and Fraction','admission':'author-side, unreviewed'},sort_keys=True,indent=2))

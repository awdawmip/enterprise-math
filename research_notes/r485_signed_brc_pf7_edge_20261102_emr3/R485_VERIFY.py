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
 for v in permutations(range(7)):
  x=1
  for i in range(7):x*=a[i][v[i]]
  total+=(-1)**sum(v[i]>v[j] for i in range(7) for j in range(i+1,7))*x
 return total
p={t:p(t) for t in range(2,10)}
D=[[Q(1)]]
for m in range(1,8):
 z=[Q(0)]
 for l in range(1,m+1):
  a=prod([p[l+2]]+[p[2]]*(l-1)+[D[m-l]])
  z=add(z,[(-1)**(l-1)*x for x in a])
 D.append(z)
P=[-29805338732234, -136621097296679, -291737569778430, -382570714263327, -339883998538875, -212728270929918, -93910389665213, -27963761747840, -4704506770764, 5857224720, 208514618592, 46684954752, 3891097600, 57327616]
R=prod([[0,1]]*7+[[1,1]]*7+[[2,1]]+[[1,2]]*7+[[3,2]]*7+[P])
R=[-Q(x,1276223164856640000000) for x in R]
assert D[7]==R and len(R)==43
shift=[sum(P[i]*B(i,j)*6**(i-j) for i in range(j,14)) for j in range(14)]
assert all(x>0 for x in shift)
small=[int(val(P,k)) for k in range(1,7)]
assert all(x<0 for x in small[:5]) and small[5]>0
for k in range(1,101):
 for t in range(2,10):assert val(p[t],k)*cat(k)==raw(k,t)
ks=list(range(1,21))+[22,24,30,49,50,64,100,101]; examples={}
for k in ks:
 a=[[raw(k,3+i-j) for j in range(7)] for i in range(7)]
 x=det_bareiss(a)
 assert x==val(D[7],k)*cat(k)**7 and (x>0 if k<=5 else x<0)
 if k in (1,5,6,49):assert det_perm(a)==x
 if k in (5,6):examples[str(k)]=str(x)
assert D[7][-1]/2**42==Q(-3499,20909640333011189760000000)
print(json.dumps({'status':'R485_EXACT_PASS','source_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f','polynomial_coefficients_checked':43,'P7_shift6_ascending':shift,'P7_1_through_6':small,'raw_coefficient_checks':800,'raw_7x7_determinants':len(ks),'raw_5040_term_determinants':4,'examples':examples,'rank7_limit':'-3499/20909640333011189760000000','arithmetic':'exact integers and Fraction','admission':'author-side, unreviewed'},sort_keys=True,indent=2))

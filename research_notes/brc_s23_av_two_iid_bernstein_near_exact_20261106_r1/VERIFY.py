from fractions import Fraction as F
K=[[F(x,1000000) for x in row] for row in (
 (0,0,0,996872,3128,0),
 (88614,435270,375797,521,91861,7937),
 (711899,154264,133837,0,0,0))]
LO=F(9,49); HI=LO+F(1,1500000)
def P(a,c):
 z=(1-a)*c; u=1-a-z
 return (a,z,u)
def E(a,c):
 a,z,u=P(a,c)
 t=(a*a,2*a*z,2*a*u,z*z,2*z*u,u*u)
 w=(z*z,2*z*(1-z),(1-z)**2)
 return tuple(t[j]-sum(w[i]*K[i][j] for i in range(3)) for j in range(6))
M=((F(1),F(0),F(0)),(-F(1,2),F(2),-F(1,2)),(F(0),F(0),F(1)))
A=(F(1,2),F(11,16),F(7,8))
V=[[E(a,c) for c in A] for a in A]
B=tuple(tuple(tuple(sum(M[i][p]*V[p][q][j]*M[k][q]
 for p in range(3) for q in range(3)) for j in range(6))
 for k in range(3)) for i in range(3))
def half(x):
 a,b,c=x; m=(a+2*b+c)/4
 return (a,(a+b)/2,m),(m,(b+c)/2,c)
def split(B,axis):
 L=[[[F(0)]*6 for _ in range(3)] for _ in range(3)]
 R=[[[F(0)]*6 for _ in range(3)] for _ in range(3)]
 for fixed in range(3):
  for j in range(6):
   z=[B[i][fixed][j] for i in range(3)] if axis==0 else [B[fixed][i][j] for i in range(3)]
   x,y=half(z)
   for i in range(3):
    if axis==0:L[i][fixed][j],R[i][fixed][j]=x[i],y[i]
    else:L[fixed][i][j],R[fixed][i][j]=x[i],y[i]
 return L,R
def bound(B):
 assert all(sum(B[i][k])==0 for i in range(3) for k in range(3))
 return max(sum(max(F(0),v) for v in B[i][k]) for i in range(3) for k in range(3))
def run():
 assert all(sum(row)==1 and min(row)>=0 for row in K)
 p=P(F(1,2),F(1,2));q=P(F(5,7),F(7,8))
 assert p[1]==q[1]==F(1,4)
 assert sum(abs(x*y-u*v) for x,y,u,v in
 ((p[i],p[j],q[i],q[j]) for i in range(3) for j in range(3)))/2==F(18,49)
 stack=[(B,0)];nodes=leaves=depth=0;hi=F(0)
 while stack:
  b,d=stack.pop();nodes+=1;depth=max(depth,d);t=bound(b)
  if t<=HI:leaves+=1;hi=max(hi,t);continue
  assert d<16
  for x in split(b,0):
   for y in split(x,1):stack.append((y,d+1))
 assert (nodes,leaves,depth)==(49,37,11)
 print('PASS_S23_AV_TWO_IID_NEAR_EXACT_BERNSTEIN_FRACTION_20261106')
 print('lower',LO,'upper',HI)
 print('certified_nodes',nodes,'leaves',leaves,'maximum_depth',depth)
 print('largest_accepted_bound',hi)
if __name__=='__main__':run()

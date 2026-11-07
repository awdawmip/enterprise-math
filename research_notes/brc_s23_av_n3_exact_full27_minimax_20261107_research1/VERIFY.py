from fractions import Fraction as F
from math import comb, factorial, lcm
H=[(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]
m=[factorial(3)//(factorial(x)*factorial(y)*factorial(z)) for x,y,z in H]
K=[[0,0,0,0,0,0,1,0,0,0],[0,F(3,10),0,F(7,10),0,0,0,0,0,0],
   [0,F(21,100),F(9,25),F(157,22050),F(27,100),F(7,100),0,F(3,50),F(1,50),F(127,44100)],
   [F(18,25),F(6,25),F(919,37044),F(14069,926100),0,0,0,0,0,0]]
d=F(5211,21952)
assert sum(m)==27 and all(min(row)>=0 and sum(row)==1 for row in K)
def target(a,c):
 z=(1-a)*c;b=(1-a)*(1-c)
 return [v*a**x*z**y*b**zz for (x,y,zz),v in zip(H,m)]
def res(a,c):
 z=(1-a)*c;w=[comb(3,k)*z**(3-k)*(1-z)**k for k in range(4)];q=target(a,c)
 return [q[j]-sum(w[k]*K[k][j] for k in range(4)) for j in range(10)]
def tv(v):return sum(max(0,x) for x in v)
p=(F(1,2),F(1,2));q=(F(5,7),F(7,8))
assert tv([x-y for x,y in zip(target(*p),target(*q))])==2*d
assert tv(res(*p))==tv(res(*q))==d
U=[[F(1),0,0,0],[-F(5,6),3,-F(3,2),F(1,3)],
   [F(1,3),-F(3,2),3,-F(5,6)],[0,0,0,F(1)]]
V=[[comb(3,i)*F(p,3)**i*(1-F(p,3))**(3-i) for i in range(4)] for p in range(4)]
assert all(sum(U[i][k]*V[k][j] for k in range(4))==(i==j) for i in range(4) for j in range(4))
n=[F(1,2)+F(i,8) for i in range(4)]
r=[[res(a,c) for c in n] for a in n]
B=[[[sum(U[i][p]*U[j][q]*r[p][q][h] for p in range(4) for q in range(4))
      for j in range(4)] for i in range(4)] for h in range(10)]
D=lcm(*(v.denominator for h in B for row in h for v in row))
B=[[[int(D*v) for v in row] for row in h] for h in B]
L=[[[0]*4 for _ in range(4)] for _ in range(10)]
R=[[[0]*4 for _ in range(4)] for _ in range(10)]
for h in range(10):
 for j in range(4):
  p=[B[h][i][j] for i in range(4)]
  e=[3*p[i]+4*p[i+1] for i in range(3)];f=[3*e[i]+4*e[i+1] for i in range(2)]
  g=3*f[0]+4*f[1]
  left=[343*p[0],49*e[0],7*f[0],g];right=[g,7*f[1],49*e[2],343*p[3]]
  for i in range(4):L[h][i][j]=left[i];R[h][i][j]=right[i]
def slack(T):
 return [[d-F(sum(max(0,T[h][i][j]) for h in range(10)),343*D)
          for j in range(4)] for i in range(4)]
S=[slack(L),slack(R)]
assert min(v for T in S for row in T for v in row)==0
assert all(v>=0 for T in S for row in T for v in row)
print('PASS_S23_N3_FULL27_EXACT_MINIMAX_TWO_BERNSTEIN_RECTANGLES_20261107')
print('delta_3',d,'multiplicities',m,'row_sums',[sum(row) for row in K])
for name,T in zip(('left_a_1/2_5/7','right_a_5/7_7/8'),S):
 print(name)
 for row in T: print(' | '.join(map(str,row)))

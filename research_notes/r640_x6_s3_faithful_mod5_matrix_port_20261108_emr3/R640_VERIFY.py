"""R640: exact GL2(F5) faithful representation of X6 V39 S3 port."""
from itertools import product
P=5
I=((1,0),(0,1));R=((0,-1),(1,-1));S=((0,1),(1,0))
def mm(A,B):
 return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%P for j in range(2)) for i in range(2))
def powm(A,n):
 x=I
 for _ in range(n):x=mm(x,A)
 return x
def gp(a,b):
 return ((a[0]+(-1)**a[1]*b[0])%3,(a[1]+b[1])%2)
def rho(g):return mm(powm(R,g[0]),powm(S,g[1]))
G=list(product(range(3),range(2)))
assert powm(R,3)==I and powm(S,2)==I and mm(mm(S,R),S)==powm(R,2)
assert len({rho(g) for g in G})==6
mulchecks=0
for a,b in product(G,repeat=2):
 assert rho(gp(a,b))==mm(rho(a),rho(b));mulchecks+=1
assoc=0
for a,b,c in product(G,repeat=3):
 assert gp(gp(a,b),c)==gp(a,gp(b,c))
 assert mm(mm(rho(a),rho(b)),rho(c))==mm(rho(a),mm(rho(b),rho(c)))
 assoc+=1
updates=0
for a,b in product(G,repeat=2):
 j=(7,-3);ja=(2,-1);jb=(-2,5)
 assert (j[0]+ja[0]+jb[0],j[1]+ja[1]+jb[1])==(7,1)
 assert mm(rho(b),mm(rho(a),I))==rho(gp(b,a))
 updates+=1
a=(0,1);b=(1,1)
assert gp(a,b)==(2,0) and gp(b,a)==(1,0)
assert rho(gp(a,b))!=rho(gp(b,a))
for n in range(1,5):
 modulus=5**n
 assert all((2*k)%modulus and (3*k)%modulus for k in range(1,modulus))
print('R640_X6_S3_FAITHFUL_MOD5_MATRIX_PORT_PASS',6,mulchecks,assoc,updates)

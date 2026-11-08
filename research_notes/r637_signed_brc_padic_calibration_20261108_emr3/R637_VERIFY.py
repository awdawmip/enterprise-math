"""R636 compact reproducible exact signed BRC rank-two reference witness."""
from math import comb
from itertools import permutations,combinations

def b(n,k):return comb(n,k) if 0<=k<=n else 0
def norm(a):
 a=list(a)
 while len(a)>1 and not a[-1]:a.pop()
 return a
def add(*rows):
 z=[0]*max(map(len,rows))
 for r in rows:
  for i,v in enumerate(r):z[i]+=v
 return norm(z)
def mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]+=a*b
 return norm(z)
def prod(rows):
 p=[1]
 for x in rows:p=mul(p,x)
 return p
def shift(x,n):return [0]*n+list(x)
def scale(x,k):return norm([v*k for v in x])
def sub(x,y):return add(x,scale(y,-1))
def divint(x,d):
 assert d and all(v%d==0 for v in x)
 return norm([v//d for v in x])
def ord5(x):return next((i for i,v in enumerate(x) if v%5),10**9)
def K(i):
 ds=(-b(4,i)+b(2,i-1),b(5,i-1)-b(5,i-2),b(7,i-2),-b(9,i-3))
 return add(*([shift([-v*b(i+1-j,q) for q in range(i+2-j)],i-1) for j,v in enumerate(ds,1) if v and i+1-j>=0] or [[0]]))

c=(0,5,1,2,3,4); P=[K(i) for i in range(1,13,2)]; M=[K(i) for i in range(2,13,2)]
U=[P[j][2*j:] for j in range(6)];V=[M[j][2*j+1:] for j in range(6)]
assert [x[0] for x in U]==[2,-8,6,106,83,9]
assert [x[0] for x in V]==[-1,-11,53,119,36,1]
W=scale(prod([z for j in range(6) for z in (U[j],V[j])]),12)

# R637: complete coefficientwise mod 5**N pair selection proof checks.
def coeff(x,i):return x[i] if i<len(x) else 0
def v5(n):
 assert n
 k=0
 while n%5==0:n//=5;k+=1
 return k
H0=[7,0,3,1];H1=[-2,4,0,5]
B=[add(H0,scale(H1,z)) for z in c]
checks=0;pair_info=[]
for r,s in combinations(range(6),2):
 delta=c[s]-c[r];e=v5(delta);mod=5**(e+1)
 pair_info.append((r+1,s+1,e,mod))
 for a in (1,2,4):
  depth=a+8
  for pi in permutations(range(6)):
   Y=[add(B[x],mul(shift([1,pi[x]+1],a),P[pi[x]])) for x in range(6)]
   rr=[coeff(B[r],i)%mod for i in range(depth+1)]
   rs=[coeff(B[s],i)%mod for i in range(depth+1)]
   u=delta//5**e;inv=pow(u%5,-1,5)
   h1=[((((rs[i]-rr[i])%mod)//5**e)*inv)%5 for i in range(depth+1)]
   h0=[(rr[i]-c[r]*h1[i])%5 for i in range(depth+1)]
   assert h0==[coeff(H0,i)%5 for i in range(depth+1)]
   assert h1==[coeff(H1,i)%5 for i in range(depth+1)]
   recovered=[]
   for x in range(6):
    jet=[(coeff(Y[x],i)-h0[i]-c[x]*h1[i])%5 for i in range(depth+1)]
    k=next((i for i,z in enumerate(jet) if z),None)
    recovered.append(5 if k is None else (k-a)//2)
   assert tuple(recovered)==pi
   checks+=1
assert checks==32400
# Complete two-reference collision: all twelve Z[t] outputs coincide,
# references at axes 1,2 agree mod5 but are different modulo25.
a=1;vv=[a+2*j for j in range(6)];CC=[shift(W,k) for k in vv]
r=0;s=1;p=4;q=5;h=c[p]-c[r]
T=divint(sub(CC[p],CC[q]),h)
for x in range(6):
 k=q if x==p else p if x==q else x
 F=add(shift([h],vv[x]),shift([c[r]-c[x]],vv[p]),shift([c[x]-c[r]],vv[q]))
 assert not any(F[:vv[k]])
 Q=F[vv[k]:]
 assert Q[0]%5
 Ap=scale(shift(mul(prod([z for j in range(6) for typ,z in enumerate((U[j],V[j])) if (j,typ)!=(k,0)]),Q),a),12//h)
 Am=scale(shift(mul(prod([z for j in range(6) for typ,z in enumerate((U[j],V[j])) if (j,typ)!=(k,1)]),Q),a-1),12//h)
 hx=scale(T,c[x]-c[r])
 assert ord5(Ap)==a and ord5(Am)==a-1
 assert add(mul(Ap,P[k]),hx)==CC[x]==add(mul(Am,M[k]),hx)
assert all((5*z)%5==0 for z in T) and any((5*z)%25 for z in T)
print('R637_5ADIC_CALIBRATION_PRECISION_TAX_EXACT_PASS',checks,'pairs',len(pair_info))
print(pair_info)

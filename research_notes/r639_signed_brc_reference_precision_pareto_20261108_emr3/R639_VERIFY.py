"""R639 exact integer-polynomial reproduction; R462 signed K input."""
from itertools import combinations,permutations
from math import comb
c=(0,5,1,2,3,4)
def B(n,k):return comb(n,k) if 0<=k<=n else 0
def trim(z):
 while len(z)>1 and z[-1]==0:z.pop()
 return z
def add(*rows):
 z=[0]*max(map(len,rows))
 for r in rows:
  for k,v in enumerate(r):z[k]+=v
 return trim(z)
def sc(x,n):return trim([n*v for v in x])
def sh(x,n):return [0]*n+list(x)
def mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,u in enumerate(x):
  for j,v in enumerate(y):z[i+j]+=u*v
 return trim(z)
def prod(xs):
 z=[1]
 for x in xs:z=mul(z,x)
 return z
def K(i):
 ds=(-B(4,i)+B(2,i-1), B(5,i-1)-B(5,i-2), B(7,i-2),-B(9,i-3))
 return add(*([sh([-v*B(i+1-j,q) for q in range(i+2-j)],i-1) for j,v in enumerate(ds,1) if v and i+1-j>=0] or [[0]]))
p=[K(j) for j in range(1,13,2)];m=[K(j) for j in range(2,13,2)]
u=[p[j][2*j:] for j in range(6)];v=[m[j][2*j+1:] for j in range(6)]
assert [x[0] for x in u]==[2,-8,6,106,83,9]
assert [x[0] for x in v]==[-1,-11,53,119,36,1]
z=prod([f for j in range(6) for f in (u[j],v[j])]);assert z[0]%5
h0=[7,0,3,1,2,6];h1=[-2,4,0,5,7];h2=[11,0,-3,5]
h=[add(h0,sc(h1,t),sc(h2,t*t)) for t in c]
def at(x,k):return x[k] if k<len(x) else 0
def read_bg(S,a):
 d=a+8; special=len(S)==3 and 0 in S and 1 in S
 if not special:
  T=next(q for q in combinations(S,3) if len({c[x]%5 for x in q})==3)
  out=[]
  for x in range(6):
   row=[]
   for k in range(d+1):
    value=0
    for j,t in enumerate(T):
     num=1;den=1
     for w in T:
      if w!=t:num=num*(c[x]-c[w])%5;den=den*(c[t]-c[w])%5
     value+=num*pow(den,-1,5)*at(h[t],k)
    row.append(value%5)
   out.append(row)
  return out
 T=list(S);A=[[1,c[t],c[t]**2] for t in T]
 (a0,b0,d0),(a1,b1,d1),(a2,b2,d2)=A
 D=a0*(b1*d2-d1*b2)-b0*(a1*d2-d1*a2)+d0*(a1*b2-b1*a2)
 adj=[[b1*d2-d1*b2,d0*b2-b0*d2,b0*d1-d0*b1],
      [d1*a2-a1*d2,a0*d2-d0*a2,d0*a1-a0*d1],
      [a1*b2-b1*a2,b0*a2-a0*b2,a0*b1-b0*a1]]
 assert D%5==0 and D%25 and D!=0
 coef=[]
 for i in range(3):
  rr=[]
  for k in range(d+1):
   numer=sum(adj[i][j]*(at(h[T[j]],k)%25) for j in range(3))%25
   assert numer%5==0
   rr.append((numer//5*pow((D//5)%5,-1,5))%5)
  coef.append(rr)
 return [[sum(c[x]**i*coef[i][k] for i in range(3))%5 for k in range(d+1)] for x in range(6)]
recovery=collisions=identities=refs=0
for r in range(7):
 for S in combinations(range(6),r):
  bad=r==3 and 0 in S and 1 in S
  if r>=3:
   for a in (1,2,4):
    bg=read_bg(S,a);d=a+8
    assert all(bg[x][k]==at(h[x],k)%5 for x in range(6) for k in range(d+1))
    for pi in permutations(range(6)):
     recovered=[]
     for x,j in enumerate(pi):
      Y=add(h[x],mul(sh([x%4+1,x+2,1],a),p[j]))
      corrected=[(at(Y,k)-bg[x][k])%5 for k in range(d+1)]
      first=next((k for k,vv in enumerate(corrected) if vv),None)
      recovered.append(5 if first is None else (first-a)//2)
     assert tuple(recovered)==pi;recovery+=1
  if r<=2 or bad:
   missing=[x for x in range(6) if x not in S];l,q=missing[-2:]
   roots=[c[x] for x in S if not (bad and x==1)]
   def g(t):
    ans=1
    for b in roots:ans*=t-b
    return ans
   gp,gq=g(c[l]),g(c[q]);assert gp%5 and gq%5
   for a in (1,2,4):
    vv=[a+2*j for j in range(6)]
    W=sc(z,gp);T=mul(sh(add([1],sh([-1],vv[q]-vv[l])),vv[l]),z)
    target=[sh(W,k) for k in vv]
    for x in range(6):
     j=q if x==l else l if x==q else x
     F=add(sh([gp],vv[x]),sh([-g(c[x])],vv[l]),sh([g(c[x])],vv[q]))
     assert all(t==0 for t in F[:vv[j]])
     Q=F[vv[j]:];assert Q[0]%5
     AP=sh(mul(prod([f for k in range(6) for side,f in enumerate((u[k],v[k])) if (k,side)!=(j,0)]),Q),a)
     AM=sh(mul(prod([f for k in range(6) for side,f in enumerate((u[k],v[k])) if (k,side)!=(j,1)]),Q),a-1)
     H=sc(T,g(c[x]))
     assert add(mul(AP,p[j]),H)==target[x]
     assert add(mul(AM,m[j]),H)==target[x]
     identities+=2
    for x in S:
     H=sc(T,g(c[x]));assert (all(vv%5==0 for vv in H) if bad else all(vv==0 for vv in H))
     if bad and x==1:assert any(vv%25 for vv in H)
     refs+=1
    collisions+=1
assert (recovery,collisions,identities,refs)==(90720,78,936,144)
for a in (1,2,4):
 for j in (4,5):
  assert all(at(mul(sh([1],a),p[j]),k)==0 and at(mul(sh([1],a-1),m[j]),k)==0 for k in range(a+8))
print('R639_COMPLETE_REFERENCE_PRECISION_PARETO_EXACT_PASS',recovery,collisions,identities,refs)

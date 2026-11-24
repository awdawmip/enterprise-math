from functools import lru_cache
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
def solve(a,u):
 h=4+11*a;c=6+15*a
 x=[6*a+2,5*a+1,4*a+1,a,a+1,0,a+1,2*a+1,3*a+1,3*a+1] if u==394 else [6*a+2,5*a+2,4*a+2,a+1,a,0,a,2*a,3*a+1,3*a+1]
 p=3*a+1;x[0]-=p;x[1]-=p
 S=[3]*p+[1<<t for t in range(10) for _ in range(x[t])];m=len(S)
 states=[]
 for v in F:
  H=sum(1<<j for j,s in enumerate(S) if s&v);b=H.bit_count()
  if b==h:states.append((v,H))
  elif b==h-1:
   assert v==u; states.append((v,H));states.extend((v,H|1<<j) for j in range(m) if not(H>>j&1))
  else: assert b>h
 N=len(states); D=m-h+1
 qs={}
 for t in range(10):
  for j in range(m):
   mask=sum(1<<i for i,(v,H) in enumerate(states) if v>>t&1 and not H>>j&1)
   if mask and mask!=(1<<N)-1:qs[mask]=(t,j)
 policy={}
 @lru_cache(None)
 def win(A,d):
  n=A.bit_count()
  if n<=1:return True
  if d<=0 or n>1<<d:return False
  opts=set()
  for q in qs:
   z=A&q; b=A^z
   if z and b and max(z.bit_count(),b.bit_count())<=1<<(d-1):opts.add((max(z.bit_count(),b.bit_count()),min(z,b),max(z,b)))
  for _,z,b in sorted(opts):
   if win(z,d-1) and win(b,d-1):policy[A,d]=(z,b);return True
  return False
 ok=win((1<<N)-1,D)
 print(a,u,m,N,D,ok,win.cache_info().misses,flush=True)
 if ok:
  for i in range(N):
   A=(1<<N)-1;d=D
   while A.bit_count()>1:
    z,b=policy[A,d];q=next(q for q in qs if A&q in (z,b));t,j=qs[q];v,H=states[i];A=(A&q) if (v>>t&1 and not H>>j&1) else A&~q;d-=1
   assert A==1<<i
for a in range(1,5):
 for u in (394,673):solve(a,u)

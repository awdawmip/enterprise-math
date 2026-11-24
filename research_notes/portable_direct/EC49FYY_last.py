from functools import lru_cache
from itertools import combinations
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
def solve(u,sm,t):
 h=15;D=17;x=[8,6,5,1,2,0,2,3,4,4] if u==394 else [8,7,6,2,1,0,1,2,4,4];x[0]-=4;x[1]-=4
 S=[3]*4+[1<<r for r in range(10) for _ in range(x[r])];m=len(S);j=S.index(sm);S[j]^=1<<t
 states=[]
 for v in F:
  if not(v>>t&1) or S[j]&v:continue
  H=sum(1<<i for i,s in enumerate(S) if s&v);b=H.bit_count()
  if b>h:continue
  free=[i for i in range(m) if i!=j and not H>>i&1]
  for k in range(h-b+1):
   for E in combinations(free,k):states.append((v,H|sum(1<<i for i in E)))
 N=len(states); idx={s:i for i,s in enumerate(states)}; stars=[]
 for v,H in states:
  stars.append(sum(1<<idx[v,H|1<<i] for i in range(m) if not H>>i&1 and (v,H|1<<i) in idx))
 qs=set(sum(1<<i for i,(v,H) in enumerate(states) if v>>r&1 and not H>>k&1) for r in range(10) for k in range(m));qs.discard(0);qs.discard((1<<N)-1)
 calls=0
 @lru_cache(None)
 def win(A,d):
  nonlocal calls
  calls+=1
  if calls>150000:raise TimeoutError
  n=A.bit_count()
  if n<=1:return True
  if d<=0 or n>1<<d:return False
  a=A;ex=0
  while a:
   low=a&-a;a^=low;s=(A&stars[low.bit_length()-1]).bit_count()
   if s>d:return False
   if s==d:
    if ex:return False
    ex=low
  opts=set()
  for q in qs:
   z=A&q;b=A^z
   if z and b and (not ex or z&ex) and max(z.bit_count(),b.bit_count())<=1<<(d-1):opts.add((max(z.bit_count(),b.bit_count()),min(z,b),max(z,b)))
  return any(win(z,d-1) and win(b,d-1) for _,z,b in sorted(opts))
 try: ok=win((1<<N)-1,D)
 except TimeoutError:ok='UNKNOWN'
 print(u,sm,t,N,ok,calls,flush=True)
for u in (394,673):
 x=[8,6,5,1,2,0,2,3,4,4] if u==394 else [8,7,6,2,1,0,1,2,4,4];x[0]-=4;x[1]-=4
 for sm,t in [(3,0),(3,1)]+[(1<<t,t) for t in range(10) if x[t]]:solve(u,sm,t)

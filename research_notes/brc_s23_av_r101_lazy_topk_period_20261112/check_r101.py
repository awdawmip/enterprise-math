from fractions import Fraction as Q
from math import floor,ceil,gcd
import random,json,os
SEED=10120261112
rng=random.Random(SEED)
def frac(v): return v-(v.numerator//v.denominator)
def member(t,sig,z):
 j,x,a,b=sig
 s=frac(x+(t-j)*z)
 A,B=frac(a*z),frac(b*z)
 return (A<=s<B if A<B else (s>=A or s<B)) if A!=B else False
def ranked(E,sig,z,k=None):
 res=sorted((u for u in E if member(u[0],sig,z)),reverse=True)
 return tuple(res if k is None else res[:k])
def cached_update(parent_top,D,A,sig,z,k):
 s=set(u for u in parent_top if u not in D)
 s.update(u for u in A if member(u[0],sig,z))
 return tuple(sorted(s,reverse=True)[:k])
def finite_cuts(E,sig,L,U):
 j,x,a,b=sig
 cuts={L,U}
 for t,_ in E:
  for c,d in [(a,Q(0)),(b,Q(0)),(t-j,x),(t-j-a,x),(t-j-b,x),(a-b,Q(0))]:
   if c==0: continue
   lo=min(c*L+d,c*U+d);hi=max(c*L+d,c*U+d)
   for n in range(ceil(lo),floor(hi)+1):
    z=(Q(n)-d)/c
    if L<=z<=U:cuts.add(z)
 return sorted(cuts)
def reps(cuts):return sorted(set(cuts)|{(a+b)/2 for a,b in zip(cuts,cuts[1:])})
def gcdf(E,sig):
 j,x,a,b=sig;g=gcd(abs(a),abs(b))
 for t,_ in E:g=gcd(g,abs(t-j))
 return g
stats={"seed":SEED,"cases":0,"exact_point_assertions":0,"finite_interval_atoms_checked":0,"top_k_values":0,"same_time_branch_histories":0,"large_N_boundaries":{},"sharpness_checks":0}
for _ in range(260):
 sig=(rng.randint(-2,2),Q(rng.randint(-6,6),rng.randint(1,7)),rng.randint(-5,5),rng.randint(-5,5))
 ids=list({(rng.randint(-5,7),rng.randint(0,9)) for i in range(10)})
 E=set(ids[:rng.randint(4,9)])
 if not E:E={ids[0]}
 D=set(rng.sample(sorted(E),rng.randint(0,min(3,len(E)))))
 A=set()
 target=rng.randint(1,3)
 while len(A)<target:
  u=(rng.randint(-6,8),rng.randint(0,12))
  if u not in E:A.add(u)
 F=(E-D)|A
 if len({t for t,b in E})<len(E):stats["same_time_branch_histories"]+=1
 L,U=Q(-2),Q(2)
 pr=reps(finite_cuts(E|A,sig,L,U))
 points=pr +[Q(rng.randint(-17,17),rng.randint(1,15)) for i in range(8)]
 for k in range(1,5):
  for z in points:
   got=cached_update(ranked(E,sig,z,k+len(D)),D,A,sig,z,k)
   expect=ranked(F,sig,z,k)
   assert got==expect,(sig,E,D,A,k,z,got,expect)
   stats["exact_point_assertions"]+=1
  stats["top_k_values"]+=1
 stats["finite_interval_atoms_checked"]+=len(pr)
 stats["cases"]+=1
for k in range(1,5):
 for d in range(1,5):
  ids={(0,b) for b in range(k+d)}
  D={(0,b) for b in range(k,k+d)}
  sig=(0,Q(1,4),0,1)
  assert ranked(ids,sig,Q(1,2),k+d)==tuple(sorted(ids,reverse=True))
  kth=ranked(ids-D,sig,Q(1,2),k)[-1]
  assert kth==sorted(ids,reverse=True)[k+d-1]
  stats["sharpness_checks"]+=1
for N in (7,31,127,509):
 sig=(0,Q(1,4),0,N);E={(N,0)};F=E|{(1,0)}
 assert gcdf(E,sig)==N and gcdf(F,sig)==1
 for m in range(N):
  inside=Q(8*m+7,8*N);outside=Q(8*m+3,8*N)
  assert ranked(E,sig,inside,1)==((N,0),)
  assert ranked(F,sig,inside,1)==((N,0),)
  assert not ranked(E,sig,outside,1)
  assert ranked(F,sig,outside,1)!=((N,0),)
 stats["large_N_boundaries"][str(N)]={"old_period_denominator":N,"new_period_denominator":1,"disjoint_old_winner_components":N,"min_winner_identity_transitions":2*N-1}
print("R101_PASS",stats["cases"],stats["exact_point_assertions"],stats["sharpness_checks"],stats["large_N_boundaries"]["509"]["disjoint_old_winner_components"])
os.makedirs("/mnt/data/em_r101",exist_ok=True)
with open("/mnt/data/em_r101/verification_r101.json","w") as f:json.dump(stats,f,sort_keys=True,indent=2)

# X6 R287 — lazy exact mixed-circuit feasibility with source certificates

2026-11-28. Independent informed TASK_RESEARCH; author proof and computation, NOT_REVIEWED. Native read r2-20261128-0510-x6-read SUCCEEDED at 2026-11-27T21:11:09.560139Z, Source 8317983762710c2cee05bbb705875529da3970e1, NO_CANONICAL_PUBLICATION_DIRECTORY. Actual owner/own researcher binding not established; no CLAIM or control mutation. Global entry snapshot bfbfdb6a09f4083542feca6a080e8841fb36a4d7 verified by both entry blob matches. P000 V5 and global V4, ACTIVE worldview, joint/residual fidelity, portable protocol retained. Auxiliary coefficient algebra on the frozen BRC observer, not a new native arithmetic/physical residual calculation.

## Scope and exact pins
R286@6df86a3cfc7f0b73bd8a083f2c3f52c8122cdf34:research_notes/portable_direct/2026-11-28_r2_x6_r286_signed_circuit_dictionary_factorized_slack.md; R285@7403583b0ed8aeffeb5d70744b93660c12c7cc9d; R284@b1dcb5bc4869113730d936e03be15ebc926a2ba1f. Frozen R247 exact full ref 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md, blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa. R286's literal ref missed "33"; corrected by commit search and immutable read, not a repin. Same 51 endpoints, 98 directed germs, 44 projective normals (R286), frozen support splits. Retain R247/R285 capacity prerequisites and original BRC relation masks. Strict sixth frontier unchanged [5350,0], 422650/667787 checked, 2954 survivors, 245137 unprocessed. K6 remains 1–2.

## Theorem: finite lazy mixed projection decision and short certificates
Let finite rational mixed rows be u_i*x+b_i(y) >=_i 0, x in R^3, y in R^2; strict/weak flags; equalities represented by two weak rows. For each minimal positive circuit lambda of the u_i, the projected row is sum lambda_i b_i(y) >=_lambda 0, strict iff at least one positive-weight row is strict. Include zero normals as singleton circuits. By R285 these finitely many rows characterize the projection exactly. R286 supplies a separation oracle without Cartesian expansion: in each active oriented normal class select the minimum normalized slack at y, ties in favor of a strict row; test each active circuit's weighted sum. If violated, return the actual minimizer row identities and positive combination. With no violation, y belongs to the exact projected region. Positivity of circuit weights proves the minimum factorization, including strictness at a zero minimum.

Start with no cuts (or arbitrary finite slope restrictions, with the corresponding scope). At each iteration solve the accumulated mixed two-variable system exactly for a rational witness y, or report infeasible. If the oracle returns no violation, accept y; by R285 an intercept x exists and rational FM reconstructs it. If a violated circuit is returned, append its original valid projected inequality. The cut excludes the current y and cannot duplicate a normalized row of identical strictness already imposed. Since finitely many original row tuples exist, finitely many cuts exist. Exact finite termination follows; the algorithm decides nonemptiness of the full projected region, but does not enumerate its boundary. The implementation's <1000 guard is an experiment budget, not the theorem's termination bound. A guard hit is incomplete, never an exclusion. Every cut retains original row identities, scales and flags. Original rows and branch identities remain necessary for future intercept-dependent constraints; future slope-only constraints may be included and feasibility rerun. This is a scoped decision algorithm, not destructive state compression.

For infeasibility without external slope restrictions: the finite mixed projected halfspaces are convex, whether open or closed. By finite Helly in R^2 an inclusion-minimal infeasible cut subset has at most three rows. Each cut comes from at most four original rows (R285), so their source union of at most 12 rows is infeasible in the original five variables. Greedily delete source rows while exact infeasibility persists. By finite Helly in R^5 the resulting inclusion-minimal source core contains at most six original rows. Deletion needs one pass: a row once necessary stays necessary when other rows are deleted. Equality sides count separately. This gives a source-level certificate independent of the enumeration order or total number of raw rows. With added external slope restrictions include those rows in the certificate and count them separately. The implementation checks both source union and reduced core via direct mixed FM. The mathematical bound applies to all finite mixed systems; no claim it is attained in X6.

Cost: finite worst-case iteration bound is number of distinct normalized circuit cuts, potentially large. An oracle uses O(N+G^4) fixed-size tests per call, with cached unsigned direction circuits, where N is number of raw rows and G active projective groups; integer bit costs and exact 2D solve are additional. The current witness solver is mixed FM, not a measured R284 speedup. Larger initial attempt hit execution time limit; no results credited from it. The small completed experiments below do not imply acceptable full-word runtime. Optimization: use R284 envelope solver for 2D witness generation; cache active circuit lists, choose stronger violated cuts where useful; preserve cut/source identity.

## Executed exact evidence
Local Python Fraction/integer execution in auxiliary coefficient space. 40 arbitrary small row systems, 12 sampled true-word subsets: 51 feasible, 1 infeasible, 6 added cuts, max 1, max source core 1. Every accepted small system reconstructed a rational intercept at returned slope. All compared to direct mixed 5-variable FM.

Frozen sixth pencil B=0,t!=0 has 12 finite values D/t:
0,68/3,34,153/4,99/2,51,66,88,132,153,198,306.
For each nonempty consecutive nonpositive block [l,h], choose roots on the boundary sample or in the adjoining gaps. For l=h choose both roots at the sample (zero), or one on each side (negative); for l<h independently choose each boundary root at sample or adjacent gap. For all-positive choose both roots below the first sample. These produce exactly 1+2n+4*n(n-1)/2 = 1+2n^2=289 distinct words, all realizable; strict convexity excludes every other weak word (R275). Exhaustively checked all 289 realizable endpoint words with the lazy oracle, direct FM and reconstructed original fiber. Zero same-pencil germ rows in this frozen pencil test: no claim of within-pencil germ coverage. 100 deterministic random ternary assignments also checked, all infeasible. Combined 389 systems: 857 cuts, maximum 5, max projected infeasible core 2, max source core 3.

Cross-pencil zero-germ test: 24 actual Q=D(D+e*t+f*B) word subsets each consisting of three endpoint rows and two cross-pencil zero-start germ rows (48 germ rows total); all feasible, verified by direct FM. Added an opposite strict row to each subset (24 deliberately contradictory systems), all infeasible, verified by direct FM. Combined 48 systems: 26 cuts, maximum 2, max projected core 1, max source core 2.

Total completed systems 489 (=52+389+48), 364 feasible, 125 infeasible, 889 added cuts, 1251 active circuit tests (excludes zero-normal checks). No discrepancies. This is full local weak endpoint dictionary coverage and bounded mixed cross-pencil testing, not full 51-endpoint/98-germ word search, not full projected-region enumeration, not BRC capacity classification. Strict sixth prefix unchanged. General mixed root classification and independent review open.

## Reproducer
Python 3.9+ (Fraction and integer exact arithmetic; standard library). Below is the locally executed algorithm and deterministic test inputs, with duplicated fiber-check code factored into a function and disabled full-word branch omitted. Source row arrays and tests are retained. Actual completed local outputs reported above; code transcription in this note is not claimed as a separate executed environment. Earlier larger trials timed out, not credited.

```python
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, prod
from functools import reduce,lru_cache
import random,json
# Exact frozen R247 endpoints, with R286's two support splits below.
raw='''0,1,12:1,17,391;0,1,11:1,17,391;2,5,73:2,5,5;1,9,74:1,9,69;1,9,74:3,17,187;1,9,69:1,0,51;2,5,5:1,0,0;2,5,73:1,0,34;6,15,158:1,1,23;2,5,47:3,0,68;6,15,154:19,28,440;0,1,0:1,17,22;0,1,0:1,17,61;1,9,74:1,4,74;0,1,0:1,30,126;1,4,152:1,4,74;0,0,1:1,17,22;1,4,152:1,30,126;1,17,69:1,9,69;0,1,0:1,17,9;0,1,0:3,77,235;0,1,0:1,17,87;1,4,100:3,77,235;0,1,0:3,40,38;0,1,0:2,5,5;3,1,116:1,17,22;0,1,0:3,38,40;2,5,47:3,53,25;0,1,0:3,53,25;0,1,0:2,34,83;1,4,74:3,17,187;0,1,11:1,30,126;0,1,0:2,73,395;0,1,18:1,17,595;1,4,74:1,0,66;1,17,217:1,0,132;1,17,61:1,11,55;1,4,100:1,0,88;1,17,69:1,11,55;1,9,69:1,11,55;1,9,225:1,0,153;3,1,116:4,0,153;2,5,112:2,34,83;1,4,230:1,0,198;2,8,109:2,0,99;1,17,595:1,0,306;1,4,230:2,73,395'''
def prim(a):
 d=reduce(gcd,a,0); return tuple(x//d for x in a) if d else tuple(a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(cross(a,b),c)
def sign(x):return (x>0)-(x<0)
P=[];G=[]
for z in raw.split(';'):
 a,b=[tuple(map(int,p.split(','))) for p in z.split(':')]
 n=prim(cross(a,b));n=tuple(x*sign(next(x for x in n if x)) for x in n)
 parts=[(a,b)]
 if n==(51,2,-1):parts=[((1,9,69),(3,17,187)),((2,5,112),(1,0,51))]
 if n==(17,-1,0):parts=[((0,0,1),(1,17,391)),((1,17,69),(1,17,22))]
 for a,b in parts:
  assert dot(a,n)==dot(b,n)==0
  a,b=prim(a),prim(b)
  for p in (a,b):
   if p not in P:P.append(p)
  i,j=P.index(a),P.index(b);G.extend(((i,j),(j,i)))
assert(len(P),len(G))==(51,98)
def ep(p):
 t,B,D=p;return(t*t,t*B,B*B,t*D,B*D,D*D)
def pol(p,q):
 t,B,D=p;T,U,V=q;return(2*t*T,t*U+B*T,2*B*U,t*V+D*T,B*V+D*U,2*D*V)
rows=[ep(p) for p in P]+[pol(P[i],P[j]) for i,j in G]
def signed(r):
 i,s,t=r;return(tuple(s*x for x in rows[i]),t)
def clean(L):
 M={}
 for a,t in L:
  a=prim(a)
  if not any(a[:-1]):
   if a[-1]<0 or a[-1]==0 and t:return None
  else:M[a]=M.get(a,False) or t
 return list(M.items())
def solve(L,n):
 L=clean(L)
 if L is None:return None
 if not n:return ()
 pos=[(a,t) for a,t in L if a[0]>0];neg=[(a,t) for a,t in L if a[0]<0]
 Z=[(a[1:],t) for a,t in L if not a[0]]
 for a,s in pos:
  for b,t in neg:Z.append((tuple(a[0]*v-b[0]*u for u,v in zip(a[1:],b[1:])),s or t))
 y=solve(Z,n-1)
 if y is None:return None
 lo=max((-F(dot(a[1:-1],y)+a[-1],a[0]) for a,t in pos),default=None)
 hi=min((-F(dot(a[1:-1],y)+a[-1],a[0]) for a,t in neg),default=None)
 x=(lo+hi)/2 if lo is not None and hi is not None else lo+1 if lo is not None else hi-1 if hi is not None else F(0)
 w=(x,)+y
 assert all((z:=dot(a[:-1],w)+a[-1])>0 or z==0 and not t for a,t in L)
 return w
@lru_cache(None)
def circuit(V):
 if len(V)==3:
  a,b,c=V
  if det(a,b,c):return None
  z=next(i for i,x in enumerate(cross(a,b)) if x)
  return prim((cross(b,c)[z],cross(c,a)[z],cross(a,b)[z]))
 a,b,c,d=V;w=(det(b,c,d),-det(a,c,d),det(a,b,d),-det(a,b,c))
 return prim(w) if all(w) else None
checks=0
def separate(R,y):
 global checks
 groups={}
 for j,r in enumerate(R):
  a,t=signed(r);u=a[:3];d=reduce(gcd,u,0);z=dot(a[3:5],y)+a[5]
  if not d:
   if z<0 or z==0 and t:return ((prim(a[3:]),t),(j,))
   continue
  s=sign(next(x for x in u if x));v=tuple(x//(d*s) for x in u);key=(v,s);m=F(z,d)
  old=groups.get(key)
  if old is None or (m,not t)<(old[0],not old[1]):groups[key]=(m,t,j,a,d)
 def test(M,w):
  global checks
  checks+=1;z=sum(abs(c)*m[0] for m,c in zip(M,w));t=any(m[1] for m in M)
  if z>0 or z==0 and not t:return None
  D=prod(m[4] for m in M);a=tuple(sum(abs(c)*(D//m[4])*m[3][k] for m,c in zip(M,w)) for k in range(6))
  assert not any(a[:3]);return ((prim(a[3:]),t),tuple(m[2] for m in M))
 V=sorted(set(v for v,s in groups))
 for v in V:
  if (v,1) in groups and (v,-1) in groups:
   z=test([groups[v,1],groups[v,-1]],(1,1))
   if z:return z
 for n in (3,4):
  for J in combinations(V,n):
   w=circuit(J)
   if not w:continue
   for s in (1,-1):
    M=[groups.get((v,s*sign(c))) for v,c in zip(J,w)]
    if all(m is not None for m in M):
     z=test(M,w)
     if z:return z
 return None
def lazy(R):
 C=[];seen=set()
 while True:
  y=solve([c[0] for c in C],2)
  if y is None:
   core=C[:]
   for i in range(len(core)-1,-1,-1):
    trial=core[:i]+core[i+1:]
    if solve([c[0] for c in trial],2) is None:core=trial
   assert len(core)<=3
   ids=sorted(set(j for c in core for j in c[1]))
   assert len(ids)<=12 and solve([signed(R[j]) for j in ids],5) is None
   for i in range(len(ids)-1,-1,-1):
    trial=ids[:i]+ids[i+1:]
    if solve([signed(R[j]) for j in trial],5) is None:ids=trial
   assert len(ids)<=6
   return False,len(C),len(core),len(ids),None
  z=separate(R,y)
  if z is None:return True,len(C),0,0,y
  assert z[0] not in seen
  seen.add(z[0]);C.append(z)
  assert len(C)<1000
rng=random.Random(28720261128)
st={'arbitrary':0,'real_subsets':0,'full_words':0,'feasible':0,'infeasible':0,'cuts':0,'max_cuts':0,'max_projected_core':0,'max_source_core':0,'full_word_details':[]}
def record(z):
 ok,n,c,r,y=z;st['feasible' if ok else 'infeasible']+=1;st['cuts']+=n;st['max_cuts']=max(st['max_cuts'],n);st['max_projected_core']=max(st['max_projected_core'],c);st['max_source_core']=max(st['max_source_core'],r)
def fiber(R,y):
 L=[]
 for r in R:
  a,t=signed(r);b=dot(a[3:5],y)+a[5];L.append((tuple(b.denominator*x for x in a[:3])+(b.numerator,),t))
 assert solve(L,3) is not None
def verify(R):
 z=lazy(R);ref=solve([signed(r) for r in R],5);assert z[0]==(ref is not None);record(z)
 if z[0]:fiber(R,z[-1])
for k in range(40):
 R=[]
 for i in rng.sample(range(149),rng.randrange(3,5)):
  s=rng.choice((-1,0,1))
  if s:R.append((i,s,bool(rng.randrange(2))))
  else:R.extend(((i,1,False),(i,-1,False)))
 verify(R);st['arbitrary']+=1
for k in range(12):
 e,f=-rng.randrange(90),-rng.randrange(30);q=(0,0,0,e,f,1);S=[sign(dot(ep(p),q)) for p in P];R=[]
 for i,s in enumerate(S):
  if s:R.append((i,s,True))
  else:R.extend(((i,1,False),(i,-1,False)))
 for i,(a,b) in enumerate(G):
  if S[a]:continue
  h=sign(dot(rows[51+i],q));s=h or S[b]
  if s:R.append((51+i,s,S[b]!=s))
  else:R.extend(((51+i,1,False),(51+i,-1,False)))
 verify(rng.sample(R,6));st['real_subsets']+=1
print(json.dumps(st|{'circuit_checks':checks,'cached_direction_circuits':circuit.cache_info().currsize,'endpoint_count':len(P),'germ_count':len(G)},indent=2))
I=sorted([i for i,(t,B,D) in enumerate(P) if B==0 and t!=0],key=lambda i:F(P[i][2],P[i][0]))
Y=[F(P[i][2],P[i][0]) for i in I];assert len(I)==12
N=len(I); J=set(I); seen_words=set(); local={'words':0,'germ_rows':0,'random':0,'random_infeasible':0,'cuts':0,'max_cuts':0,'max_projected_core':0,'max_source_core':0}
def word(r0,r1):
 q=(r0*r1,0,0,-r0-r1,0,1);S=[sign(dot(ep(p),q)) for p in P];key=tuple(S[i] for i in I);assert key not in seen_words;seen_words.add(key);R=[]
 for i in I:
  s=S[i]
  if s:R.append((i,s,True))
  else:R.extend(((i,1,False),(i,-1,False)))
 for k,(i,j) in enumerate(G):
  if i not in J or j not in J or S[i]:continue
  h=sign(dot(rows[51+k],q));s=h or S[j]
  if s:R.append((51+k,s,S[j]!=s));local['germ_rows']+=1
  else:R.extend(((51+k,1,False),(51+k,-1,False)));local['germ_rows']+=2
 z=lazy(R);assert z[0] and solve([signed(r) for r in R],5) is not None
 local['words']+=1;local['cuts']+=z[1];local['max_cuts']=max(local['max_cuts'],z[1]);fiber(R,z[-1])
word(Y[0]-2,Y[0]-1)
for l in range(N):
 for h in range(l,N):
  L=(Y[l-1]+Y[l])/2 if l else Y[0]-1
  H=(Y[h]+Y[h+1])/2 if h+1<N else Y[-1]+1
  if l==h:
   word(L,H);word(Y[l],Y[l])
  else:
   for a,b in product((L,Y[l]),(H,Y[h])):word(a,b)
assert local['words']==1+2*N*N
for k in range(100):
 R=[]
 for i in I:
  s=rng.choice((-1,0,1))
  if s:R.append((i,s,True))
  else:R.extend(((i,1,False),(i,-1,False)))
 z=lazy(R);assert z[0]==(solve([signed(r) for r in R],5) is not None)
 local['random']+=1;local['random_infeasible']+=not z[0];local['cuts']+=z[1];local['max_cuts']=max(local['max_cuts'],z[1]);local['max_projected_core']=max(local['max_projected_core'],z[2]);local['max_source_core']=max(local['max_source_core'],z[3])
print(json.dumps({'local':local,'circuit_checks_total':checks,'cached_direction_circuits':circuit.cache_info().currsize,'sixth_endpoint_values':[str(x) for x in Y]},indent=2))
crossstats={'samples':0,'germ_rows':0,'contradictory':0,'cuts':0,'max_cuts':0,'max_projected_core':0,'max_source_core':0}
for k in range(24):
 e,f=-rng.randrange(90),-rng.randrange(30);q=(0,0,0,e,f,1);S=[sign(dot(ep(p),q)) for p in P];E=[];H=[]
 for i,s in enumerate(S):
  if s:E.append((i,s,True))
  else:E.extend(((i,1,False),(i,-1,False)))
 for i,(a,b) in enumerate(G):
  if S[a] or P[a][0]*P[b][1]==P[a][1]*P[b][0]:continue
  h=sign(dot(rows[51+i],q));s=h or S[b]
  if s:H.append((51+i,s,S[b]!=s))
  else:H.extend(((51+i,1,False),(51+i,-1,False)))
 if not H:continue
 T=rng.sample(E,3)+rng.sample(H,min(2,len(H)));z=lazy(T);assert z[0] and solve([signed(r) for r in T],5) is not None
 crossstats['samples']+=1;crossstats['germ_rows']+=len(T)-3;crossstats['cuts']+=z[1];crossstats['max_cuts']=max(crossstats['max_cuts'],z[1])
 i,s,t=T[-1];U=T+[(i,-s,True)];z=lazy(U);assert not z[0] and solve([signed(r) for r in U],5) is None
 crossstats['contradictory']+=1;crossstats['cuts']+=z[1];crossstats['max_cuts']=max(crossstats['max_cuts'],z[1]);crossstats['max_projected_core']=max(crossstats['max_projected_core'],z[2]);crossstats['max_source_core']=max(crossstats['max_source_core'],z[3])
print(json.dumps({'cross_germ':crossstats,'total_circuit_checks':checks},indent=2))
```

## Next
Integrate lazy oracle into actual multi-pencil mixed word search with BRC capacity pruning. Optimize full-word feasibility and retain source cores/witnesses. Continue strict-sixth at [5350,0] without repeating prior prefix. Activity association and independent review pending.

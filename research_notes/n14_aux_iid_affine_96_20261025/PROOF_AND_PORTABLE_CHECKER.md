# N14 finite iid Stage96 — exact affine minimax segment, sharp endpoint, executable author certificate

Status: **AUTHOR COMPUTATION-ASSISTED PROOF / NOT INDEPENDENTLY REVIEWED / NOT NATIVE CLAIM OR RESULT**. Date: 2026-10-25. This is an external finite positive-rational iid model; it is **not** a Heartbeat/P000/X6 theorem.

## Provenance and exact task

GLOBAL_KNOWLEDGE_V1: main@a23e21ac467a11ceef7eeb4902ba931bc48c21a5. Enterprise Math source read: main@b9413f641e648746b70eddefae7501961acaec0d, with Stage95 research at research_notes/n14_aux_iid_affine_95_20261025/, and later head 8a4461254f2f49e8b43bf33cd250476e65692a96. Original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched the startup projection. ACTIVE worldview, BRC guidance, and current docs/PORTABLE_RESEARCH_PROTOCOL.md were read. The predecessor Stage95 result is an author-side (not independently admitted) exact theorem and remains an explicit premise.

We test P=(1/8,1/24,5/6) against Q=(1/12,1/12,5/6) with iid symbols 0,1,2, all randomized ordered-history stopping/decision policies with horizon T<=14, both errors eP=P(decide Q), eQ=Q(decide P) bounded by alpha, objective V14(alpha)=inf max(E_P T,E_Q T). At the inherited Stage95 endpoint,
alpha95=5172538007321621243/14900301753911083008,
V95=24246605376738068699/1862537719238885376,
and B=(12,0,1) has probability s95=24710766480088847/41779200000000000 of immediately deciding Q rather than continuing. At A95=(10,1,2), immediate Q is frozen; A94=(10,5,1) has immediate P.

## Theorem (exact real interval, conditional on the inherited Stage95 endpoint)

Set eta96=18633875/77605738301620224, Gamma96=38115/13. For **every real** 0<=delta<=eta96,

V14(alpha95+delta) = V95 - Gamma96*delta.

The new endpoint is

alpha96 = 5172538010899325243/14900301753911083008,
V96 = 24246604065543953699/1862537719238885376.

The same Stage96 supporting line cannot be attained to the right of alpha96, even among all ordered-history randomized tests. We do **not** determine V14 for alpha>alpha96 here.

### Exact universal Bellman lower bound

At count state v=(n,a,b), a=count(symbol 0), b=count(symbol 1), every word has Q/P likelihood ratio 2^(a+b)/3^a. At K96=19683/13, set lambda_Q=K96, lambda_P=72+(8/9)*K96=18432/13, Gamma96=lambda_P+lambda_Q. The terminal P-action has P-conditional weighted cost lambda_Q*2^(a+b)/3^a; terminal Q-action has cost lambda_P. The continue cost is 1+sum_i P_i D(child_i). Thus by backward induction,

D(v)=min{lambda_Q*2^(a+b)/3^a, lambda_P, 1+sum_i P_i D(child_i)}

with continuation omitted at n=14. This induction applies to arbitrary path-dependent randomized policies, because each history's conditional future is iid and its likelihood ratio depends only on (n,a,b). Therefore

D(root) <= E_P T+lambda_P eP+lambda_Q eQ <= max(E_P T,E_Q T)+Gamma96*alpha,

so V14(alpha) >= D(root)-Gamma96*alpha for all alpha.

Exact standard-library Fraction computation covers all 680 states and 1,240 nonselected-action gaps, finding 1,238 strictly positive, 2 exactly zero, 0 negative. Smallest strictly positive gap: 791/19968. Only ties: A=(14,7,4), Q/P terminal actions; B=(12,0,1), continue/Q. Root exact value:

D(root)=11745466653426138401273/11394348400049651712.

The chosen action at A is Q at the left endpoint, and at B continue for the Bellman certificate. Both ties can be randomized.

### Typed positive branch carrier, true ordered histories

Keep each ordered word as a provenance label with positive exact pair (P(word),Q(word)); concatenate by multiplying and combine disjoint alternatives by adding. This implements an appropriate BRC-style positive-weight branch carrier, not signed or phase cancellation and not native BRC-Shor.

Although A=(14,7,4) has 120,120 nominal count-compatible words, actual first-reaching histories under the frozen minimizing policy number 11,467. Their masses are

pA=1433375/150289495621632,
qA=1433375/160489808068608.

The B first-arrival has 12 ordered histories, masses
pB=48828125/725594112,
qB=48828125/362797056.

Continuing from B under the unique frozen minimizers gives conditional vector (P-error,Q-error,E_P extra-time,E_Q extra-time)=(63/64,1/144,9/8,13/12), with 5 terminal suffix words. Put

E=pB*(1-63/64)=48828125/46438023168,
H=qB*(1/144)=48828125/52242776064.

The B path has no symbol 0 among the first 12 observations, so it cannot precede A, which would require seven symbol-0 observations within just two more steps; A is terminal and cannot precede B. Hence these decision-randomization cones are disjoint.

### Balanced primal construction for every real u

Let u in [0,1] be the probability of changing A from immediate Q to immediate P. Let s be the immediate-Q probability at B, with all other actions frozen. By the disjoint ordered cones,

eP = alpha95 - pA*u + E*(s-s95),
eQ = alpha95 + qA*u - H*(s-s95).

The unique balance eP=eQ requires s=s95+h96*u, where

h96=(pA+qA)/(E+H)=9712549/1044480000000,

and then eP=eQ=alpha95+eta96*u, with

eta96=E*h96-pA=qA-H*h96=18633875/77605738301620224>0.

The endpoint s96=s95+h96=8237051660682949/13926400000000000 lies in (0,1), as does every intermediate s(u); hence every real u in [0,1] is valid, including irrational u.

Independent exact forward/backward recurrence yields

(E_P T-E_Q T)|u=0 = 2415929098096422265/3725075438477770752 > 0,
(E_P T-E_Q T)|u=1 = 2415931526233672265/3725075438477770752 > 0.

All four performance metrics depend affinely on u because randomization cones do not interact. Therefore E_P T>E_Q T for every real u. Every used action is a Bellman minimizer; equality in the universal lower bound holds, proving the entire affine minimax segment and its endpoint values.

### Strict right-sharpness for all ordered histories

Suppose the same Bellman supporting line attained the minimax value at some alpha>alpha96. Both multipliers are strictly positive, so equality would require eP=eQ=alpha and every action used with positive P mass to have zero Bellman gap. The verified strict-gap table permits mixing only at A and B. If different ordered words with the same counts have different randomization probabilities, they may be replaced by their P-arrival weighted average at that count state, without changing any of the four metrics: Q/P is constant within that count fiber, and conditional iid futures are identical. The A and B cones do not overlap. Thus every equality policy has effective 0<=u,s<=1 and obeys the two displayed affine error equations. Balance forces s=s95+h96*u and alpha=alpha95+eta96*u<=alpha96, contradiction. Finite-horizon randomized occupation measures form a compact polytope and the minimum is attained, so the argument excludes an unattained-infimum equality as well.

## Reproducible author calculations (Python 3 standard library)

The full local research packet additionally contains two separately written author implementations: derive96.py uses bottom-up Bellman plus forward masses, and crosscheck96.py uses recursive Bellman plus explicit DFS over all 11,467 ordered first-hit paths. Both agree at the two endpoints and interior rational diagnostics. The *continuum* theorem comes from the exact affine proof, not a finite grid. The following compact, independently executed portable verifier repeats the main exact identities (runs without the other files):

~~~python
from fractions import Fraction as F
from functools import cache
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
A=(14,7,4);B=(12,0,1);K=F(19683,13);LP=72+F(8,9)*K;LQ=K
alpha=F(5172538007321621243,14900301753911083008)
V=F(24246605376738068699,1862537719238885376)
s95=F(24710766480088847,41779200000000000)
def child(v,i):
 n,a,b=v;return n+1,a+(i==0),b+(i==1)
@cache
def bell(v):
 n,a,b=v;cost={'P':LQ*F(2**(a+b),3**a),'Q':LP}
 if n<N:cost['C']=1+sum((P[i]*bell(child(v,i))[0] for i in range(3)),F())
 x=min(cost.values());act=next(t for t in ('C','P','Q') if t in cost and cost[t]==x)
 if v==A:act='Q'
 assert cost[act]==x
 return x,act,cost
def fwd(u,s):
 mass={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  future=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in mass.items():
   v=n,a,b
   if v==A:ep+=p*(1-u);eq+=q*u;continue
   if v==B:ep+=p*s;p*=1-s;q*=1-s
   else:
    z=bell(v)[1]
    if z=='Q':ep+=p;continue
    if z=='P':eq+=q;continue
   assert n<N
   tp+=p;tq+=q
   for i in range(3):
    key=(a+(i==0),b+(i==1));x,y=future[key]
    future[key]=x+p*P[i],y+q*Q[i]
  mass=future
 assert not mass
 return ep,eq,tp,tq
def first(v):
 mass={(0,0):(F(1),F(1),1)}
 for n in range(v[0]):
  future=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,c) in mass.items():
   if bell((n,a,b))[1]!='C':continue
   for i in range(3):
    key=(a+(i==0),b+(i==1));x,y,z=future[key]
    future[key]=(x+p*P[i],y+q*Q[i],z+c)
  mass=future
 return mass.get(v[1:],(F(),F(),0))
def check():
 gap=[];ties=[]
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=n,a,b;d,z,opts=bell(v)
    for alt,c in opts.items():
     if alt==z:continue
     gap.append(c-d)
     if c==d:ties.append((v,z,alt))
 assert len(gap)==1240 and gap.count(0)==2
 assert min(x for x in gap if x>0)==F(791,19968)
 assert set(ties)=={(A,'Q','P'),(B,'C','Q')}
 pa,qa,ha=first(A);pb,qb,hb=first(B)
 assert (ha,hb)==(11467,12)
 assert pa==F(1433375,150289495621632)
 assert qa==F(1433375,160489808068608)
 E=pb/F(64);H=qb/F(144);h=(pa+qa)/(E+H);eta=E*h-pa
 assert h==F(9712549,1044480000000)
 assert eta==F(18633875,77605738301620224)
 for u in (F(),F(1,3),F(1)):
  ep,eq,tp,tq=fwd(u,s95+h*u)
  assert ep==eq==alpha+eta*u
  assert tp==V-(LP+LQ)*eta*u and tp>tq
  assert tp+LP*ep+LQ*eq==bell((0,0,0))[0]
 print('PASS: 680 states, 1240 comparisons, Stage96 exact affine identities')
if __name__=='__main__':check()
~~~

## Next scientific unit (Stage97 candidate, not theorem)

After freezing terminal A96 to immediate P and keeping B's continuation tie, exact affine K-policy gap scanning nominates the first crossing below K96 at

K97_candidate=893307577584960/619337901137,
A97=(4,4,0), with continue/decide P tie.

This is only a DUAL candidate, not an established positive primal interval. Next: enumerate genuine A97 first arrivals and continuation suffix risks, check interaction with B, derive balancing controls, all 680 Bellman states and 1240 gaps, and prove or refute a full real Stage97 primal interval and right-sharpness. Preserve Stage96 exact source and the Stage95 author predecessor.

## Actual access and admission limits

Native task list gave CONTROL_QUOTA. The session registration action for this run returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false, for a dedicated read-only native identity; no active owner, native Researcher session, CLAIM, Result freeze or independent review was verified. This **author research note** is ordinary GitHub source evidence only, not an alternative native CLAIM/Result or access-bypass. No confidential credentials or permissions are changed. The supplied exact model is not a claim about native six-axis Cell dynamics.

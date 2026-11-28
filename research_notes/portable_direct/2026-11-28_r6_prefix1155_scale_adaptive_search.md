# PREFIX-1155 — exact critical scale envelopes and scale-adaptive integer search

2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH. Own original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, managed custody not revoked; no formal CLAIM or shared Task mutation. Owner inventory r6-20261128-1751-owner-read SUCCEEDED/error=null, INV-3c4199d0fda2209c14ae484f660a6c15, as_of 2026-11-28T09:52:22.056175+00:00, 547 tasks, LEASED filter empty; Source a98073c587c88151d898215240344db9e570688e and event issue unchanged at completion. This snapshot grants no write authority. Global main entry at 7c8776bdd2d83004888fba0463d8926165033a62; frozen P000 V5 and companions f42f2906d77f24085c123f3ccfe9667d41caa96d. Auxiliary spectral algebra, not native geometry. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Input and scope

Continue [PREFIX-1154](https://github.com/awdawmip/enterprise-math/blob/a7d260988e28ac43b2d3cda1505e9e19708b650f/research_notes/portable_direct/2026-11-28_r6_prefix1154_signed_scale_obstruction.md), blob dc8f688a193c9a1b5b0503e795d49aa2ed731bde. Predecessor evidence archive SHA256 204ed788185736b8d900f64b7de60861030aacb45731c37060371ff258d4d325; inherited PREFIX1154_SHA256SUMS passed. fixture1141.json SHA256 cb38649b5a98a767b9658c9792af8d21f66b1c2f9290d1e7160b6cc602b6481a; section1154.json 178472aba386cc14ae500acfc70eb7e3b5aa5ccc31601e399c0c8ae3aa8ee885; rebase1154.json 880dc341211300c44601cda8c41259bc08619dbd2bf506f3538c2596353775f0. compact1154.py was rerun successfully in the discovery scripts and reconstructs the 18 vertices from inherited observations; verify1154.py / predecessor evidence bind the vertices. No new raw moments, observations or anchor. All exceptional-integer conclusions remain conditional on inherited Stage46, anchor, q0, signed affine transfer and primitive reduction hypotheses.

## Fixed normals theorem and critical scale

Let P denote the inherited 18-vertex convex outer section translated by (r,u), L0=10^114, k>=1. The necessary rational parameter domain at L=k L0 is D(k)=P+[-K/(k L0)^2,0] x [0,H/(k L0)]. For each outward edge normal (a,b) of P, add the four signed coordinate axes to the set J. Write z=max_{(x,y) in P}(a x+b y). Then D(k) is exactly the intersection of the halfspaces a x+b y <= z+max(0,-a) K/(k L0)^2+max(0,b) H/(k L0). Proof: support functions add under Minkowski addition. A supporting face of a sum is the sum of the exposed faces in each summand. A nondegenerate edge of a two-dimensional sum requires at least one nondegenerate edge in a summand, so its normal is in J. Thus all facet constraints occur among the displayed inequalities; the extra constraints are valid. No claim of equality with the full 15-row fiber.

For a fixed line (q,p,h), put d=a p/q+b h/q-z, A=max(0,-a) K/L0^2, B=max(0,b) H/L0. For d>0 the exact boundary condition is d k^2-B k-A<=0. Its positive threshold is (B+sqrt(B^2+4 A d))/(2d) (zero if A=B=0); directions with d<=0 impose no upper bound. The admissible scale interval is the intersection of the resulting closed intervals, restricted to k>=1. Equivalently, compare rational endpoints using the polynomial without evaluating a square root. Domains are nested, so a strict exclusion at k0 holds for every k>=k0. Exact rational checks bracket the three previous candidates' maximum scale in the *polygon outer model* in [1.160,1.161), [1.993,1.994), [4.076,4.077). Therefore at L>=4.077*10^114 the three lines are excluded, and q>10^79, improving the previous sufficient multiplier 8. Full-fiber thresholds could be lower; polygon feasibility does not prove full-fiber feasibility.

## Adaptive exact search

For integer unimodular V, W=V^-1, let n=V(q,p,h). The extremal values of each row (a,b,c) of V over q in [q0,Q] and (p/q,h/q) in D(k) are computed by the support of D(k) and the two endpoints q0,Q. Round inward to the integer bounding interval. After multiplication by q>0 each facet is linear in n; clear positive denominators and divide by positive gcd. For every pair of integer values on the two shortest axes, intersect all inequalities with the interval on the third axis using exact integer ceiling/floor. This covers the whole original integer population, followed by inherited gcd(q,p)=1. A rational LLL rebase in the maximum-triangle observation metric was used for k=8,32,128,256,512,1024 (4,5,10,10,11,11 iterations); the final fixed V/W from k=1024 then verifies all listed scales independently of LLL. An exploratory full-box run at larger Q timed out; no exclusions were inferred from that run. The exact interval-elimination verifier completed.

Results (k, Q, total points, primitive points, min primitive q or none):
4.077, 10^79, 0, 0, none;
8, 10^80, 172, 102, 10029718470287781637054824792445792353024806865489078828100397213143665328863739;
32, 10^80, 41, 25, 35189995502097523129830419442737793158028107858274324355390826822350485499542381;
128, 10^80, 10, 6, 56512868835665083278102462001304794132487706731037447119949012678989903721636037;
256, 10^80, 4, 3, 71643427397187043133823231859151002584466200858333613819139045075053058563450940;
512, 10^80, 1, 1, 86773985958709002989544001716997211036444694985629780518329077471116213405265843;
1024, 3*10^80, 36, 28, 125973346871229282264155038589815043869899072622051324550531021198729414550431799;
10^4, 10^81, 134, 91, 306276613216500803658641883910294129025231017007820359832454018521135185087844457;
10^6, 10^81, 1, 1, 777162954560943253733202274097457264193854034605071070067744313049015905524684450;
10^8, 3*10^81, 1, 1, 2542512772914539892912953344305685071111626040561341592566888111496564716664067486;
10^10, 3*10^81, 0, 0, none.

In particular L>=10^124 gives b-a>=q>3*10^81, with only 423 outer loop pairs in the final fixed basis. Uniform L>=10^114 bound remains PREFIX-1154 q_min. No new uniform dyadic window calculation. The conditional staircase can be used at actual eligible scales. Continuous terminal 4.72478e43 unchanged. Next: seek stronger coupled scale constraints from the actual Stage46 pair geometry, verify full signed fibers for the new small-scale candidates, and extend search at large scales. Anchor exit, independent review, unbounded separation and B_fix,odd(32) open.

## Compact reproduction

Run in the verified extracted PREFIX-1154 directory. First run predecessor compact1154.py and verify1154.py to check inherited section; then run this compact verifier. It uses only exact integer/rational arithmetic. Executed compact1155.py SHA256 a9a767589bc4aa3ea84c7cdf0177eda1be3b2e4af7d5635d4753a75186aa61a0, log b1fa9e9265d81628db675f0ebaf8612059aa6ebd5a265c3e290a2516ec707522. Full discovery, partial timeout log, separate verification, and exact candidate outputs retained in local evidence archive.
 
```python
from fractions import Fraction as F
from itertools import product
from math import ceil,floor,gcd,lcm,prod
import json
D=json.load(open('fixture1141.json')); L=int(D['L']); K,H,r,u=map(F,(D['K'],D['H'],D['r0'],D['u']));q0=int(D['q0']); assert L==10**114
P=[(F(x)+r,F(y)+u) for x,y in json.load(open('section1154.json'))['vertices']]
assert len(P)==18
J=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P,P[1:]+P[:1])];assert all(a*x+b*y<=z for a,b,z in J for x,y in P)
J += [(a,b,max(a*x+b*y for x,y in P)) for a,b in ((1,0),(-1,0),(0,1),(0,-1))]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def supports(k):return [(a,b,z+max(0,-a)*K/(L*k)**2+max(0,b)*H/(L*k)) for a,b,z in J]
def inside(line,k):
 q,p,h=line;return all(a*p+b*h<=q*z for a,b,z in supports(k))
old=json.load(open('rebase1154.json'));lines=old['runs'][-1]['lines'];assert len(lines)==3
for line,lo in zip(lines,(1160,1993,4076)):
 assert inside(line,F(lo,1000)) and not inside(line,F(lo+1,1000))
 print('critical',line[0],lo,lo+1)
# Complete exact integer bounding box; extrema from signed support directly.
def search(k,Q,V,W):
 assert all(type(x)==int for M in (V,W) for row in M for x in row)
 assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*W)))
 box=[]
 for a,b,c in V:
  lo=min(a+b*x+c*y for x,y in P)+min(0,-b*K/(L*k)**2)+min(0,c*H/(L*k));hi=max(a+b*x+c*y for x,y in P)+max(0,-b*K/(L*k)**2)+max(0,c*H/(L*k));box.append((ceil(min(q0*lo,Q*lo)),floor(max(q0*hi,Q*hi))))
 cs=[]
 for a,b,z in supports(F(k)):
  row=[a*W[1][i]+b*W[2][i]-z*W[0][i] for i in range(3)];den=lcm(*(x.denominator for x in row));row=[int(x*den) for x in row];g=gcd(*row);cs.append([x//g for x in row] if g else row)
 # Enumerate two shortest axes; derive exact interval on third from each integer inequality.
 cs=[(W[0],Q),([-x for x in W[0]],-q0)]+[(row,0) for row in cs]
 pts=[];ls=[];outer=0
 i,j,k0=sorted(range(3),key=lambda i:box[i][1]-box[i][0])
 for x,y in product(range(box[i][0],box[i][1]+1),range(box[j][0],box[j][1]+1)):
  outer+=1;lo,hi=box[k0]
  for v,t in cs:
   rhs=t-v[i]*x-v[j]*y
   if v[k0]>0:hi=min(hi,rhs//v[k0])
   elif v[k0]<0:lo=max(lo,-((-rhs)//v[k0]))
   elif rhs<0:break
   if lo>hi:break
  else:
   for z in range(lo,hi+1):
    n=[0]*3;n[i]=x;n[j]=y;n[k0]=z;assert all(dot(v,n)<=t for v,t in cs)
    q,p,h=[dot(w,n) for w in W];pts.append((q,p,h))
    if gcd(q,p)==1:ls.append((q,p,h))
 ls.sort();return box,outer,len(pts),ls
V=[[280298927560080223480722151835321420045479420,-13073623392197607236536093307323275562132534,383669456588018457893976517919277843],[1541171933679435429254773030377287307687259921,-71882894845908801142142463754016554941522233,-288620873277088023072816095121777764],[-1441793828922551799495755791699733151924114232,67247737673028203235698709286978026778296959,-1373309703248336785713599115020093114]]
W=[[118126577762564344774870869068010004363929100723881982110987660540899296956223238,7846769108664937489284169521805039505969971898169342439543360657830117594208561,31352591803855341785326867351012793327484405738252201592658583069783083550957395],[2532638164885114202292434895988889663605085026771182248689793991630838073793821242,168235017826313077854724959038314825948264166663328057596805012627551971707847696,672200719554516203079058968846079080324233640624585097567059131373004937832847283],[11711188278925887214640063631246996688733699078092296855712915679301070859297160183,777936618104220694442276014114669628009974652045829426554109852883075914656540108,3108327631274363383378668303287979688078083448002288268515806290793968948834424954]]
for k,Q,count,first in [(F(4077,1000),10**79,0,None),(8,10**80,102,10029718470287781637054824792445792353024806865489078828100397213143665328863739),(32,10**80,25,35189995502097523129830419442737793158028107858274324355390826822350485499542381),(128,10**80,6,56512868835665083278102462001304794132487706731037447119949012678989903721636037),(256,10**80,3,71643427397187043133823231859151002584466200858333613819139045075053058563450940),(512,10**80,1,86773985958709002989544001716997211036444694985629780518329077471116213405265843),(1024,3*10**80,28,125973346871229282264155038589815043869899072622051324550531021198729414550431799),(10**4,10**81,91,306276613216500803658641883910294129025231017007820359832454018521135185087844457),(10**6,10**81,1,777162954560943253733202274097457264193854034605071070067744313049015905524684450),(10**8,3*10**81,1,2542512772914539892912953344305685071111626040561341592566888111496564716664067486),(10**10,3*10**81,0,None)]:
 b,o,n,ls=search(k,Q,V,W);assert len(ls)==count and (ls[0][0] if ls else None)==first;print('PASS',k,Q,b,o,n,len(ls),first,flush=True)
```

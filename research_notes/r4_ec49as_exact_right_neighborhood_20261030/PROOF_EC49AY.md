# EC49AY — exact postcritical causal BRC optimum on the entire real interval

Date: 2026-10-30. Author-side mathematical proof with exact computations. Status: PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Model and exact theorem

This statement is ONLY about the strictly positive auxiliary 18+18 P/Q probability BRC observer of EC49AV–AX; it is not a signed/phase BRC, native X6, three-dimensional research slice or Heartbeat World dynamics claim. Uniform hidden w=0,1,2; first-stage c=0,1,2,3,STOP with costs (1,1,2,2,0); observed u∈{0,1} has probability t(w,u)=1/2+(2u-1)(1-w)η; paid sensor output z∈{0,1,2}. First-stage rows x[w,c] sum to 1, and sum_{w,c}cost(c)x[w,c]=43/16, so expected first cost C1=43/48. The sensor's independent coin p(c,u) sees only (c,u), costs exactly C2=13/16, and final acceptance can use only paid realized (c,u,z). Let q_z=x[z,c]t(z,u)/3, T=sum_z q_z and V=sum_z[43q_z-16T]_+/172. Then the optimal accepted score H=α-(177/172)β is sum_{c<4,u}p(c,u)V(c,u).

Let η* be the unique real root in [75/206,2/5] of
D(η)=17272336η^4−20409088η^3+3509368η²+3245760η−991743,
already rigorously bracketed in EC49AX by 0.3942483<η*<0.3942484. Put
h(η)=77/688+(674η−175)/16512
and
G(η)=[4156η²−3936η+1121−344(1−2η)√(19−26η)]/[16512(1+2η)].

**THEOREM.** For EVERY REAL η∈[η*,2/5] and EVERY lawful real causal behavioral first-stage strategy, observation-only stochastic sensor purchase and terminal acceptance,
H≤h(η)+G(η).
Equality is achieved by the explicit lawful strategy below. G(η*)=0 and G(η)>0 for η>η*. Combining the earlier proved pieces gives the exact all-real value:
Hmax=77/688 for 0≤η≤175/674;
Hmax=h(η) for 175/674≤η≤η*;
Hmax=h(η)+G(η) for η*≤η≤2/5.
In particular Hmax(2/5)=15451/123840−√215/2160≈0.1179774572906928. This is strictly larger than EC49AX's rational counterexample 594127/5036160 by 2387/351360−√215/2160>0.

## Proof: globally complete finite geometry and one radical tangency identity

(1) Existing COMPLETE reduction, exact scope. EC49AV proved an optimizer exists with at most five positive x entries and at most one fractional purchase probability on a positive paid fiber: fix an optimal p and maximize a convex function of x at a vertex of the three row equations plus action and purchase-cost equations; then optimize p as a one-constraint box LP. This preserves the real causal model. EC49AW proved the four independent base equations yield precisely 168 nondegenerate vertices and 924 edges; all optimal representatives are covered. Of the 924, exactly 720 have paid mass below C2 throughout and are infeasible. EC49AX established exact four-corner rational purchase-price upper certificates on 196 of the remaining 204 clipped edges, proving H≤h(η) for every real η in [75/206,2/5]. The 196 price witnesses are reproducible by the existing published VERIFY_EC49AX.py. Separate convexity in x and η is used successively, not joint convexity. The remaining EIGHT edges have identical complete affine q-observation signatures, with observable fiber and within-fiber label permutations, so one representative covers all eight. Therefore an exact optimum above h can occur only on this exceptional family.

(2) Optimal sensor knapsack on the exceptional edge. Parameter 0≤t≤1:
x[0,:]=((11−8t)/16,0,t/4,0,(5+4t)/16),
x[1,:]=(0,1,0,0,0), x[2,:]=(1,0,0,0,0).
Paid mass is (43−4t)/48, so the exact withheld mass must be (1−t)/12. EC49AX's exact sign and score-density cross-product inequalities prove the weakest positive-mass paid fiber is (c=0,u=1). All other paid fibers are bought completely; only this fiber has a fractional purchase coin, p(0,1)=1−(1−t)/(12T1), where
T1=(d−ft)/96, d=27−10η, f=8+16η.
The score sign of (c=0,u=1,z=2) changes at r_score(η)=(19η−4)/(2(2η+1)). All other relevant score signs are fixed. Write
a=344(1−4η²)>0,
b=2436η²+1568η−1201,
c=2060η²−5096η+1769,
M=a t²+b t+c.
For 0≤t≤r_score the EXACT gap g(t,η)=h−H_best equals M/[2064(d−ft)]. For r_score≤t≤1 the exact gap is (43−54η)(1−t)/2064≥0. These two closed forms and the lawful purchasing optimality are prior exact author results, tested directly by VERIFY_EC49AX.py.

(3) NEW global minimization, no floating point. Define r=√(19−26η), and t_opt=(d−4r)/f. The following universal identity holds in the algebraic ring Q[η,r,t]/(r²−19+26η):
M(t,η)+2064G(η)(d−ft)=a(η)(t−t_opt(η))².
Explicit denominator clearing and symbolic expansion leave the residual
86(2η−1)(26η+r²−19)/(2η+1)=0;
VERIFY_SYMBOLIC_EC49AY.py checks that polynomial identity, independently of any η grid. Since d−ft>0 for η∈[η*,2/5], we have the exact square certificate
g(t,η)+G(η)=a(t−t_opt)²/[2064(d−ft)]≥0
for every real t in the whole first branch, equality at t=t_opt.

(4) The tangent is actually attainable. EC49AX rigorously proved η*>197/500. For 197/500≤η≤2/5, exact rational estimates give 293/100<r<3, 23≤d≤1153/50, 1788/125≤f≤72/5, whence 0<t_opt<(567/50)/(1788/125)<4/5. Also η>197/500>28/79 implies r_score>4/5, so t_opt lies STRICTLY in the first branch. There T1=r/24>1/12≥(1−t_opt)/12; thus p(0,1)=1−2(1−t_opt)/r belongs to (0,1), and the other paid fibers are bought with probability 1. Exact C2 holds, and the accepted positive-score events depend only on realized purchased observations. The square certificate reaches equality, proving Hmax=h+G on all eight exceptional edges; the other 196 satisfy H≤h≤h+G. At η* the old W bound remains globally tight and D(η*)=0 makes G=0. For η>η* EC49AX constructed t_num=−b/(2a) in the first branch with M(t_num)<0, hence G>0. This proves the claimed phase boundary and strict improvement throughout the open right interval.

(5) New exact algebraic witness at η=2/5. Set t_opt=115/72−√215/18 and
x[0,:]=(-1/9+√215/36,0,115/288−√215/72,0,205/288−√215/72),
x[1,:]=(0,1,0,0,0), x[2,:]=(1,0,0,0,0).
Buy all positive-mass paid fibers except (c=0,u=1) with probability
p(0,1)=4/9+√215/36.
Accept only purchased observable triples:
(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0).
Direct exact Q(√215) computation gives C1=43/48, C2=13/16,
α=581/1440−√215/2160, β=13/48,
H=15451/123840−√215/2160.
The minimum gap in this case satisfies
g(t,2/5)−g(t_opt,2/5)=3(t−t_opt)²/[10(115−72t)]≥0.
At EC49AX's rational t=3/4 the difference is strictly positive.

## Executed evidence and admission boundary

Actual run of VERIFY_EC49AY.py (Python standard library) imports the PRE-EXISTING published sibling VERIFY_EC49AX.py and rechecks the 168/924/720/196/8 exact partition, four-corner prices at η=2/5, identical residual signatures, rational tangent coefficients, exact Q(√215) sign/arithmetic, observation-only probabilities, costs, α, β and final H. Actual run of VERIFY_SYMBOLIC_EC49AY.py (SymPy 1.14.0) verifies the full-parameter polynomial identity and endpoint simplification. See EXACT_REPORT_EC49AY.json for the output. Analytic hypotheses and complete reductions are displayed above; code execution and Git SHA are not independent mathematical review. This is an author-side portable theorem, UNREVIEWED / NOT_ADMITTED. There is no source-native session, CLAIM, Result, independent Driver disposition, formalization or validated signed BRC/X6 transfer. P000 and ACTIVE worldview are unchanged.

NEXT EC49AZ: test η=21/50 beyond the existing 196-edge certificate rectangle; locate the next true strategy switch or prove another exact interval, and separately establish a typed observation-preserving map to signed BRC/X6 before making any native/physical claim.
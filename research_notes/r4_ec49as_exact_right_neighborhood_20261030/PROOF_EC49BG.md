# EC49BG — Exact all-real causal optimum through the endpoint

2026-10-30. Author-side analytic proof with exact Fraction/SymPy verification. Status: PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Scope strictly the 18+18-leaf auxiliary positive-probability BRC observer; not native signed/phase BRC, X6, three-dimensional slices or Heartbeat dynamics. At eta=1/2 the observation channel is in its nonnegative-kernel closure, while eta<1/2 has strictly positive probabilities.

## Statement and complete model

The hidden label w∈{0,1,2} is uniform. The first-stage row-stochastic action c∈{0,1,2,3,STOP} has costs (1,1,2,2,0), with sum_wc cost(c)x[w,c]=43/16 (mean first budget 43/48). Observation u∈{0,1} has P_eta(u|w)=1/2+(2u−1)(1−w)eta. On a paid action c<4, set q_w=x[w,c]P_eta(u|w)/3, T=Σ_w q_w, V=Σ_w[43q_w−16T]_+/172. The purchase probability p(c,u)∈[0,1] is a function ONLY of the observed (c,u) and satisfies ΣpT=13/16. After buying, terminal acceptance depends only on (c,u,z). Its optimal value is H=alpha−(177/172)beta=ΣpV.

**Theorem:** For every real 99/200≤eta≤1/2, over ALL lawful real randomized causal strategies,
Hmax(eta) = F(eta) =
(2752eta²+42eta+1397−172(1−2eta)sqrt(19−26eta))/(8256(1+2eta)).
The value is attained by a lawful observation-only fractional-purchase policy on a designated exceptional edge.

## 1. The exact sparse-to-edge reduction

Fix an optimal (x,p) and keep p fixed. Row sums, first cost and purchased mass constrain x by at most five independent affine equalities. Since V is a sum of positive parts of affine functions of x, H=ΣpV is convex in x. Thus a fixed-p maximizing vertex exists with at most five positive first-action entries. In the original polytope cut from three 5-action simplices by the exact first cost, the face supported on those ≤5 entries has dimension at most one: three row sums and the first-cost relation give rank four on any support admitting positive feasible x (or smaller support gives dimension zero). Hence at least one global maximizer lies on an ORIGINAL first-cost-cut vertex or edge. This argument preserves the paid-mass equality; it does not maximize over independently chosen hidden-label-dependent purchases.

An exact rational enumeration of the original row-simplex facets gives 168 vertices and 924 edges. Every edge is obtained as the intersection of the first-cost hyperplane with a two-dimensional face of the product of row simplices (one row supports three actions while the others are fixed, or two rows support two actions and the last is fixed). On 720 edges the available paid mass is below 13/16 everywhere and sensor budget is impossible. Of 204 eligible edges, 196 are ordinary and eight have one common exceptional observable signature. The full enumerator is in the **actually executed**, losslessly gzipped/base64 script VERIFY_EC49BG.py.gz.b64.

## 2. New uniform observation-cost dual across 196 ordinary edges

Write eps=1/2−eta∈[0,1/200] and C=351/2752. For any lambda≥0, every legal purchase satisfies
H ≤ D_lambda(x,eta) = lambda*(13/16)+Σ_{c,u}[V_eta(c,u)−lambda*T_eta(c,u)]_+.
Indeed p(V−lambda*T)≤[V−lambda*T]_+ fiberwise. D_lambda is convex in x at fixed eta and lambda. Hence its maximal value on a given first-action edge is attained at an endpoint; on a purchase-feasible clipped edge it suffices to check both rational clipped endpoints. This remains valid even if an endpoint itself is not purchase-feasible: the dual inequality is unconditional on x.

**New exact price:** lambda(eps)=27/172−eps/2>0. Across 196 ordinary edges there are exactly 160 distinct rational clipped endpoints. The 24 atomic scores 43q_w−16T at each endpoint are affine in eps: 7680 exact endpoint sign comparisons show every sign is fixed throughout the real interval. Accordingly V is affine in eps and each of the eight residuals g=V−lambda*T is quadratic. Each quadratic's two boundary values and any rational interior extremum were checked exactly: 616 residuals are nonnegative, 212 nonpositive and 452 identically zero; none crosses zero. Therefore the eight positive-part terms combine into an *exact polynomial* for every clipped endpoint v:
D_lambda(v,1/2−eps) = C−K_v*eps−L_v*eps².

The 160 endpoint pairs (K_v,L_v) form exactly the following 17 classes; the number after semicolon is multiplicity:
(19/192,0;12), (7/64,3/32;8), (1/8,0;2), (25/192,−1/32;8),
(7/48,0;8), (1/6,0;4), (11/64,−7/96;8), (37/192,−7/96;8),
(19/96,0;16), (41/192,−11/96;4), (23/96,0;12), (13/48,−1/8;8),
(7/24,−1/6;4), (7/24,0;8), (1/3,−1/6;8), (35/96,0;36),
(13/32,0;6).
Every one has K_v≥19/192 and K_v+L_v/200≥19/192, as verified by exact fractions. Since K_v+L_v*eps is affine, this proves the bound for ALL real eps in the interval:
Hordinary ≤ C−(19/192)eps.
It is sharp: buy *every* positive paid observable fiber under
x[0,:]=(0,7/16,0,0,9/16),
x[1,:]=(1,0,0,0,0),
x[2,:]=(0,3/4,0,1/4,0).
The first cost is 43/48, paid mass 13/16 and the optimal observed terminal score is exactly C−19eps/192 throughout the interval (atomic score signs checked at both rational endpoints).

## 3. Exceptional eight-edge continuous optimization

Their full multisets of observable (T,V) fiber pairs agree up to observable-fiber reindexing. The exact checker verifies that identity on all eight edges as polynomial identities, with 864 bilinear corner sign checks over t∈[0,1] and eta∈[99/200,1/2]. It suffices to treat the canonical edge:
x[0,:]=((11−8t)/16,0,t/4,0,(5+4t)/16);
x[1,:]=(0,1,0,0,0); x[2,:]=(1,0,0,0,0), 0≤t≤1.

Here the lowest benefit-per-unit-mass paid fiber is (c,u)=(0,1). Its mass T1=(27−10eta−(8+16eta)t)/96. Factorized exact density comparisons V(c,u)*T1−V(0,1)*T(c,u) for the five other nonzero paid fibers are:
(0,0): (2eta−1)(2eta+1)(8t−27)(8t+5)/36864;
(1,0): −(2eta−1)/144; (1,1): −(2eta−1)/144;
(2,0): t(2eta−1)²/576;
(2,1): −t(2eta−1)(2eta+1)/576.
All are ≥0 on the full rectangle. The lawful optimal purchase rule is p(0,1)=1−(1−t)/(12T1), p=1 at every other positive paid fiber; 0≤p≤1 and ΣpT=13/16 identically. Terminal acceptance depends only on observed triples (c,u,z) and uses
{(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)}.
Every score sign defining this selection is certified across the entire rectangle.

Exact symbolic simplification yields
H(t,eta)=77/688+(674eta−175)/16512−(a*t²+b*t+c)/[2064(d−f*t)],
where a=344(1−4eta²), b=2436eta²+1568eta−1201,
c=2060eta²−5096eta+1769, d=27−10eta, f=8+16eta.
Define N(t)=−a*f*t²+2a*d*t+b*d+f*c. Then
dH/dt=−N(t)/[2064(d−f*t)²].
For eta<1/2, N'(t)=2a(d−ft)>0. Moreover
N(3/4)=43(2eta−1)(484eta²−508eta+137)<0,
N(4/5)=(43/25)(2eta−1)(12996eta²−13084eta+3009)>0
through the specified real interval. Hence unique maximum at
t*(eta)=(27−10eta−4sqrt(19−26eta))/(8(1+2eta))∈(3/4,4/5).
Exact substitution verifies H(t*,eta)=F(eta). At eta=1/2 every canonical t attains C=F(1/2).

## 4. Sharp global comparison and endpoint differential

Direct exact identity with eps=1/2−eta and s=sqrt(6+26eps):
C−F(1/2−eps)=eps(2+s−8eps)/[48(1−eps)].
Since (5/2+7eps/2)²−(6+26eps)=(1−34eps+49eps²)/4>0 for 0≤eps≤1/200, we have s≤(5+7eps)/2 and
F(1/2−eps)≥C−3eps/32=C−18eps/192.
For eps>0 this **strictly exceeds** the sharp ordinary value C−19eps/192. Together with the exhaustive 720 infeasible / 196 ordinary / eight exceptional partition, it proves Hmax=F globally for all real eta∈[99/200,1/2], including the endpoint.

The formerly only bracketed loss slope is now exact:
lim_{eta↑1/2}[C−Hmax(eta)]/(1/2−eta)=(2+sqrt(6))/48.
Also F''(1/2)=1/4−19sqrt(6)/144. Hence
C−Hmax(1/2−eps)=(2+sqrt(6))*eps/48+(19sqrt(6)−36)*eps²/288+O(eps³).

## 5. Reproducible evidence and qualification

The published VERIFY_EC49BG.py.gz.b64 is the exact complete Python 3 + SymPy script executed for this result: decompress with base64 and gzip; run python VERIFY_EC49BG.py > check.json. The results are in EXACT_REPORT_EC49BG.json. Its 168/924 exhaustive enumeration, 160 clipped endpoints, 17 polynomial classes, 1280 exact rational quadratic sign tests, 7680 atomic checks and 864 symbolic signature checks support the specified finite algebraic reductions; the universal real interval proof uses the displayed convexity, quadratic-sign and closed-form identities, not numerical grid interpolation.

Inputs: GLOBAL_KNOWLEDGE_V1 canonical main 85921ed2579d2f4329cda5c554edc1d47538d137; Enterprise Math main 5e4de2f5a2d55d1fe7d0a558b69c5342fbdd8574; predecessor Draft PR #1730 head c72a02eed9cd8ba00127957dea09ac720c642b59. User-protected P000 and ACTIVE worldview unchanged. Native status v0.6.11: DIRECTED_RESEARCH authority_granted=false; owner lookup CONTROL_QUOTA. No native session/CLAIM/Result, independent Driver review or admission. A positive-mass auxiliary theorem is not a signed/phase BRC or native X6 theorem; an independent typed preservation proof remains necessary.

Next: EC49BH independent audit of sparse-to-edge lemma, full exact phase-diagram synthesis and separately typed native BRC/X6 bridge obligations.
# EC49FUM — Complete 15-trial minimax detector atlas and strict width monotonicity

Date: 2026-11-20 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_CROSSCHECKED / INHERITED_PHASE_CERTIFICATES / PARENT_DEPENDENT / NOT_REVIEWED**.

## Scientific scope

This is a new gluing, boundary-classification and monotonicity theorem about the previously frozen **BRC16943 clipped-price binary count observer**. The scientific input pin remains fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Previous author-proved phase theorems are EC49FUH (PR #2829), EC49FUI (#2830), EC49FUJ (#2832), EC49FUK (#2834), and EC49FUL (#2836). Their original proofs and Bernstein/integer certificates are reused, not rerun here. The joint/native X6 price-origin provenance remains at the parent layer; the only studied projection is the explicitly declared 15-bit binary observation.

Fix 15 conditionally independent observations given one shared finite nuisance e≤E=1048576/18958647 under both H− and H+, with equal hypothesis priors. Let θ=(1−ae)^{-1}∈(0,θ_E], a=2807259/163840; θ=0 denotes the limiting e→−∞ state only. Write

\[
\beta=\frac3{637},\quad \eta=\frac{141024}{1653649},\quad
u_E=\frac{4822040484}{8132285009},\quad
u_I=\frac{21829245984}{45529434409},
\]
\[
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\quad
u(\theta)=\frac{21829245984}{45529434409-456083905\theta}.
\]
Then T_E=(1−x)(1+ηx), T_I=(1−x)(1−βx); under H− the count K is Bin(15,1−T) and under H+ is Bin(15,1−uT). For j=1,…,15 define

\[
F_j(z)=\sum_{k=0}^{j-1}\binom{15}{k}(1-z)^kz^{15-k},\qquad
D_j(s,x)=F_j(T_s)-F_j(u_sT_s).
\]

The test φ_j=1{K≥j} has equal-prior error (1−D_j)/2.

## Theorem A — exact whole-width atlas and all boundary rules

Define the nuisance crossover c by D_1(E,c)=D_1(I,c) (unique, 2797/10^7<c<2798/10^7). Define for j=1,…,14 the unique endpoint-Bayes switch b_j by

\[
L_j(b_j)=1,\qquad
L_j(x)=\left(\frac{1-u_ET_E(x)}{1-T_E(x)}\right)^ju_E^{15-j},
\quad b_{15}=1.
\]

The previous certificates establish 0<c<b_1<⋯<b_14<1. Here b_1 is x_B in EC49FUH, with 2956/10^7<b_1<2957/10^7. All b_2,…,b_14 rational isolating brackets are inherited from EC49FUJ/K/L and rechecked in the companion Fraction program.

For the composite minimax error V(x), over **all randomized decisions on the complete 15-bit output**, the complete partition is:

1. For 0≤x≤c, the pure K≥1 test is minimax and V(x)=(1−D_1(E,x))/2.
2. For c<x<b_1, let A=D_1(E,x), I=D_1(I,x), and d_s=P_s^+(K=1)−P_s^−(K=1). Then
\[
\alpha(x)=1-\frac{A-I}{d_E-d_I}\in(74/75,1),\qquad
D_*(x)=\frac{I d_E-A d_I}{d_E-d_I},\qquad
V(x)=\frac{1-D_*(x)}2.
\]
The unique optimal permutation-invariant count rule declares H− at K=0, H+ at K≥2, and chooses H+ with probability α at K=1. A matching least-favorable *limiting* nuisance mixture has weight λ_E=−d_I/(d_E−d_I) at E, and the remainder at θ=0.
3. For each j=2,…,15 and b_{j−1}<x<b_j, the pure K≥j test is minimax, with V(x)=(1−D_j(E,x))/2.
4. The endpoint values are V(0)=u_E^{15}/2 and V(1)=1/2.

At c the unique minimax rule is pure K≥1. At each b_j for j=2,…,14, every endpoint-Bayes rule that assigns H− below K=j, H+ above K=j, and any average randomization probability in [0,1] at K=j is minimax; all minimax rules have that form (possibly asymmetric among otherwise equiprobable count-j strings).

**One exceptional switch:** at b_1 define
\[
\alpha_B=1-\frac{D_1(E,b_1)-D_1(I,b_1)}{-d_I(b_1)},
\qquad 0<\alpha_B<1.
\]
Exactly the rules that choose H− at K=0, H+ at K≥2, and average H+ probability 0≤α≤α_B at K=1 are minimax. Numerically α_B≈0.994880060675603. Both the left-limit randomized test (α=α_B) and the right-limit K≥2 test (α=0) are optimal at b_1. The value there is (1−D_1(E,b_1))/2=(1−D_2(E,b_1))/2.

**Algebraic formula for every count boundary.** Put v_j=u_E^{(15-j)/j}. Then
\[
T_E(b_j)=\frac{1-v_j}{1-u_Ev_j},\qquad j=1,\ldots,14,
\]
with b_j the unique x∈(0,1) solving T_E(x)=(1−x)(1+ηx). Consequently every switch is algebraic, and D_j(E,b_j)=D_{j+1}(E,b_j).

### Gluing and exact rule-set proof

The open intervals are the stated theorems of EC49FUH/I/J/K/L. At b_j (j≥2) the count-j likelihood ratio equals one, so the adjacent pure rules differ only at count j and both attain the endpoint E Bayes lower bound. Convexity of worst-case risk makes every mixture minimax. Conversely any minimax test must attain that admissible endpoint lower bound and therefore agree with its strict Bayes decisions away from the tied count.

At b_1 the endpoint E Bayes rule has a tie only at K=1. EC49FUJ establishes the right-phase K≥2 rule (α=0) as minimax; continuity of the EC49FUI saddlepoint rule as x↑b_1 gives α=α_B as another minimax test. Their convex combinations give [0,α_B]. For α>α_B, the θ=0 limiting discrimination is strictly *below* the E discrimination, raising worst-case risk above the endpoint Bayes bound. EC49FUJ supplies the strict margin D_2(I,b_1)−D_2(E,b_1)>1/20000, proving α_B>0; c<b_1 proves α_B<1. At c the endpoint Bayes rule is unique, and its E/I discrimination gaps coincide. At other switches the two adjacent expressions coincide because the signed count-j mass vanishes. Therefore V is continuous on [0,1].

## Theorem B — strict increase of minimax error with detector width

\[
\boxed{0\le x<y\le1\quad\Longrightarrow\quad V(x)<V(y).}
\]

Thus the exact atom-only detector x=0 is globally optimal among this observer family, with error
\[
\boxed{\min_{0\le x\le1}V(x)=\tfrac12
\left(\frac{4822040484}{8132285009}\right)^{15}
\approx0.00019689918839899036.}
\]
For strictly positive width, this value is an unattained infimum as x↓0. This statement depends on the fixed inherited conditional observer law.

**First-count region.** D_1(E,x)=T_E(x)^{15}(1−u_E^{15}); T_E'(x)<0 on (0,1), so D_1 decreases.

**All pure j≥2 regions.** For p_E=1−T_E, r_E=1−u_ET_E,
\[
\frac{dD_j(E,x)}{dx}
=F'_j(T_E)T'_E(x)[1-L_{j-1}(x)],\quad
F'_j(z)=15\binom{14}{j-1}z^{15-j}(1-z)^{j-1}.
\]
In the interior of the j-th region L_{j−1}(x)<1, F'_j>0 and T'_E<0. Hence D_j strictly decreases.

**Randomized region.** Let D_{\alpha,s}=αD_1(s,x)+(1−α)D_2(s,x), λ=−d_I/(d_E−d_I). The saddlepoint equations give D_{\alpha,E}=D_{\alpha,I}=D_* and λd_E+(1−λ)d_I=0. Differentiating the convex combination cancels derivatives of α and λ:
\[
D_*'(x)=\lambda\,\partial_xD_{\alpha,E}
       +(1-\lambda)\,\partial_xD_{\alpha,I}.
\]
For c<x<b_1<3/10000, at both endpoint parameters s∈{E,I}, the exact constants imply
\[
0<u_s<3/5,\quad999/1000<T_s<1,\quad
0<1-T_s<1/1000,\quad 9/10<-T'_s<2.
\]
Consequently,
\[
\partial_xD_1(s,x)=15T_s^{14}T_s'(1-u_s^{15})<-13
\]
because 15(999/1000)^{14}(9/10)(1−(3/5)^{15})>13. As F'_2(z)=210z^{13}(1−z),
\[
|\partial_xD_2(s,x)|
\le420\{1/1000+(3/5)^{14}\}<1.
\]
With the earlier uniform 74/75<α<1,
\[
\partial_xD_{\alpha,s}
<-\frac{74}{75}\,13+\frac1{75}<0.
\]
Both endpoint partial derivatives are negative, so D_*'<0. Continuity at the algebraic switches completes the global strict monotonicity proof.

At every b_j (j=2,…,14), the new threshold phase has zero **right derivative** of V, as L_j(b_j)=1, while the preceding phase has strictly positive left derivative; the same holds at b_1 with the randomized left phase. The nuisance crossover c has a change of slope because the limiting least-favorable nuisance support expands. These are statistical observer-level statements only.

## Exact reproducibility, provenance and remaining work

The companion standard-library Fraction script EC49FUM_N15_ATLAS_CHECK.py rechecks the c crossing and all 14 rational b_j isolating intervals, ordering, signed-mass identities, the strict rational derivative bounds, and endpoint formulas. **Local execution: PASS.** The prior interval-wide rational/Bernstein certificates are relied upon by their exact statements; this crosscheck does not independently re-execute them. The mathematical result is **AUTHOR_PROVED / EXACT_FRACTION_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

Research provenance: EM-DIRECT-8454C6, original SID MCP-44cfc4e6f2094f96861854ebefc77e84. This is independent portable Source research and asserts no new formal Task publication, CLAIM, Result or Review. No other owner's state has been modified.

Next: extend the atlas and least-favorable support analysis to arbitrary n; investigate whether support size >2 can arise; compare the count-only observer with a typed source/provenance-aware readout and an explicit fiber-preservation map. Separately audit inherited clip-law evidence before any native physical interpretation.

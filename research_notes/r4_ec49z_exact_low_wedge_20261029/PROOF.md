# EC49Z — Exact low-discrimination wedge and asymmetric supporting boundaries

Date: 2026-10-29. Scientific status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**.

Predecessor: EC49Y Draft PR #1678, immutable scientific commit cf6a95079b3d82102ed4848b37348187c0f5b05a. Frozen reading pins: GLOBAL_KNOWLEDGE_V1 main@dc3a71895e4c6e6fa56aaa2f2745429666022a05 and Enterprise Math main@0fdb227486889538a5229e9fd279239bba96fadc.

## 1. Model and theorem

Histories and terminal values are w,z in {0,1,2}, binary signal u in {0,1}, with positive rational laws
\[
 Q(w,z)=1/9,\quad P(w,z)=\begin{cases}1/6&z=w\\1/12&z\ne w,\end{cases}
 \quad t_w(u)=1/2+(2u-1)\sigma_w/200,\ \sigma=(1,0,-1).
\]
The source joint leaves are R(w,u,z)=R(w,z)t_w(u). All 18 leaves per source are strictly positive, and both sources have identical (w,u) marginals.

At known w, choose STOP or one of codes A0,A1,B0,B1. A costs 1, B costs 2; retain the code and its one-bit suffix, but erase w. After seeing u, choose whether to buy S at cost 1 to see z. STOP acceptance may depend on original w; no-S acceptance may depend on (code,u), and sensed acceptance on (code,u,z). All behavioral randomization is source-blind and uses fresh independent coins, without an ex-ante persistent seed. Fix **both source-specific stage costs** to C1=43/48 and C2=7/8, and write alpha=P(accept), beta=Q(accept), delta=alpha-beta.

**Exact sector theorem.** For every real 0<=delta<=17/288, the *whole* fixed-cost behavioral acceptance section is precisely
\[
 \boxed{\{(\alpha,\beta):\beta=\alpha-\delta,\quad 3\delta\le\alpha\le1-3\delta\}.}\tag{T}
\]
Every rational point is realized by rational independent-coin behavioral probabilities. The value delta_0=17/288 is the largest delta for which the **lower line** alpha=3delta is attainable. However, the **upper line** alpha=1-3delta is attainable for every real 0<=delta<=delta_*=59/576, the complete nonnegative discrimination range proved by EC49X. The lower boundary *above* 17/288 remains open.

The submaximal rational section delta=1/18 is thus *exactly* 1/6<=alpha<=5/6, beta=alpha-1/18.

## 2. Universal source-likelihood wedge

Each raw leaf has likelihood ratio P/Q equal to 3/2 for z=w and 3/4 for z!=w. STOP and no-S terminal observations have ratio 1. Source-blind random action and any terminal coarsening mix positive leaf measures, so every complete terminal atom has ratio between 3/4 and 3/2, irrespective of the legal real behavioral probabilities. For the acceptance event E and its complement:
\[
 \alpha\le(3/2)\beta,\qquad 1-\alpha\ge(3/4)(1-\beta).
\]
Substitute beta=alpha-delta: necessarily
\[
 \boxed{3\delta\le\alpha\le1-3\delta.}\tag{1}
\]
No independent-sampling or policy convexity assumption is needed for this measure inequality.

## 3. A sharp restriction on the lower-line equality

Let x_{wc} be the prefix probability of code c at w, h_w=1-\sum_c x_{wc}, b_w=x_{w,B0}+x_{w,B1}, b=\sum_wb_w, and s_{cu} the probability of buying S after (c,u). All prefix sums below are raw *per-history* row sums, before the prior factor 1/3. The exact stage costs imply
\[
 \sum_{w,c}x_{wc}+b=3C_1=43/16,\quad
 \sum_{w,c,u}x_{wc}t_w(u)s_{cu}=3C_2=21/8.
\]
Putting m=\sum_{w,c,u}x_{wc}t_w(u)(1-s_{cu})>=0 gives b+m=1/16, hence b<=1/16; also
\[
 \sum_wh_w=5/16+b,\qquad \sum_w(h_w+b_w)=5/16+2b\le7/16<1.\tag{2}
\]
Thus for each w, h_w+b_w<1, so **each of the three histories buys some A-code with positive probability**. There are only two A labels, implying that at least one A label is shared by two distinct histories, and at most one A label is *pure*. A paid label is pure if its prefix x has positive support at exactly one w. Any pure A label carries raw probability mass at most 1; the sum of all pure B mass is bounded by b. Therefore the total pure-code prefix mass M satisfies
\[
 \boxed{M\le1+b\le17/16.}\tag{3}
\]

Since every signal likelihood t_w(u)>0, seeing u cannot eliminate an occupied history from a paid code. A sensed terminal atom (c,u,z) has P/Q ratio **3/2 if and only if c is pure with unique history w=z**. STOP/no-S atoms have ratio 1, and any non-pure paid atom has ratio strictly less than 3/2. If alpha=3delta, then alpha=(3/2)beta, so every accepted atom with positive acceptance probability must have extremal ratio 3/2. Hence acceptance can occur only on the diagonal z=w of a pure sensed code. Such a code with raw mass x yields at most x/18 discrimination, because the difference of joint P-Q masses on its diagonal is (1/6-1/9)x=x/18 after summing u. As a result
\[
 \delta\le M/18\le17/288.\tag{4}
\]
In particular for every legal delta>17/288, **alpha>3delta**. This is an all-real impossibility proof, independent of any finite grid computation.

The statement is deliberately *asymmetric*: ratio 3/4 can arise on a mixed code carrying two histories when z is the third, absent history; one must not falsely require pure codes for the upper-boundary equality.

## 4. A single fixed causal prefix realizes the entire exact sector

Use the following prefix distributions in order A0,A1,B0,B1,STOP:
\[
 w=0:(1,0,0,0,0),\quad
 w=1:(0,1,0,0,0),\quad
 w=2:(0,9/16,1/16,0,3/8).
\]
Always buy S on a paid path. The source-specific costs are C1=43/48, C2=7/8. A0 is pure w=0; B0 is pure w=2. Their raw combined paid mass is 17/16.

Let d be any real in [0,17/288] and t=d/(17/288)=288d/17.

**LOW policy:** Reject everywhere, except accept independently with probability t at A0,z=0 and B0,z=2 (both pure diagonal). It gives
\[
 (\alpha_L,\beta_L)=(17t/96,17t/144)=(3d,2d).
\]
**HIGH policy:** Accept everywhere (including STOP), except independently reject with probability t at A0,z!=0 and B0,z!=2 (pure offdiagonal). It gives
\[
 (\alpha_H,\beta_H)=(1-17t/96,1-17t/72)=(1-3d,1-4d).
\]
For any lambda in [0,1], set the **single terminal Bernoulli acceptance probability at each observable atom** to lambda times its LOW acceptance probability plus (1-lambda) times its HIGH acceptance probability. All other decisions use the **same** fixed prefix and always-S policy. This is a valid policy with independent terminal coins, *not* an ex-ante shared-seed mixture. It realizes
\[
 \alpha=\lambda(3d)+(1-\lambda)(1-3d),\qquad \beta=\alpha-d.
\]
Thus all points in (T) occur. Given rational alpha,d, both t and lambda=(1-3d-alpha)/(1-6d) are rational, as d<=17/288<1/6. Combined with (1), this proves the exact sector and rational implementability.

## 5. Global sharpness of the upper line (not a mirror of the lower line)

The mixed A1 code is supported on histories {1,2}; hence its z=0 terminal atoms have P/Q ratio 3/4, just like the offdiagonal atoms in pure codes. On the *same fixed prefix*, accept everywhere except reject independently with probability q in [0,1] when any one of these occurs:
- A0, z=1 or z=2;
- A1, z=0;
- B0, z=0 or z=1.

All are exactly ratio-3/4 atoms. From the joint source laws, total raw rejection mass before thinning is
\[
 R_P=(2/12)1+(1/12)(25/16)+(2/12)(1/16)=59/192,
\]
\[
 R_Q=(2/9)1+(1/9)(25/16)+(2/9)(1/16)=59/144.
\]
For delta=q(59/576), the accepted pair is
\[
 (\alpha,\beta)=(1-59q/192,\ 1-59q/144)=(1-3\delta,\ 1-4\delta).\tag{5}
\]
This establishes the upper supporting line for *all* 0<=delta<=59/576, using only independent fresh terminal rejection coins. At q=1, (5) is exactly EC49Y's maximal-discrimination face endpoint (133/192,85/144). At rational delta, the policy parameter q is rational.

Equations (1),(4),(5) yield a genuine **asymmetric transition** at delta=17/288: below it the *entire* likelihood-ratio wedge is feasible, while above it the lower supporting line ceases to be attainable but the upper remains feasible until the full EC49X optimum. No lower-boundary formula beyond this threshold is claimed.

## 6. Verification, provenance, limits

The executed Python Fraction checker VERIFY.py verifies all 18 strictly positive rational leaves of each source and their normalization, the exact costs, the pure prefix mass, 20 rational section samples at four d values and five lambda values each, and the global upper-boundary witness at five rational d values including 59/576. EXACT_REPORT.json is the generated report. The **universal all-real** statements follow from §§2–5, not from finite sampling.

Typed BRC reuse is limited to source-labelled **positive rational branch measures**, full (w,u,z) provenance and observer fibers. A signed contrast between P and Q is **not a native signed BRC amplitude**. Nothing here proves a native X6 coordinate/torsor map, 3D slice embedding, or heartbeat dynamics; P000 and ACTIVE worldview remain unchanged. Native research admission and independent Driver review have not occurred.

External comparison (not used as proof): Anderson–Montúfar, ICML 2026, semi-algebraic value-function sets for memoryless POMDP policies, https://proceedings.mlr.press/v306/anderson26a.html ; Main–Randour, LICS 2026, mixing strategy payoff sets, https://doi.org/10.4230/LIPIcs.LICS.2026.68 . The latter permits persistent ex-ante mixtures, which are not admitted by the erased-W model here. No research priority or independent novelty judgment is claimed.

**Current control:** direct context returned authority_granted=false and owner/task listing returned CONTROL_QUOTA. A native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus this is author-side portable science only, without a canonical CLAIM, Result, RA, Source checkpoint, independent review or project admission. See NEXT_TASK.md for the exact post-threshold lower-boundary question.

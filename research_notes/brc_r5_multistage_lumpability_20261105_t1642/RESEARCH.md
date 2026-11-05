# R5 — Multi-stage observer-lumpability and exact convexity of real behavioral images

Date: 2026-11-05, Asia/Shanghai. Author-side portable TASK_RESEARCH. Frozen scientific pins (unchanged): GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Research question

R5 asks for a strictly positive finite P/Q stopping BRC for which FULL and seedless LR have equal complete O4 convex hulls but different **actual** randomized-behavior O4 images. The predecessor `bb25847ee1837b47bb99a347b029f4604d0b98cd:research_notes/brc_r5_three_stage_image_convexity_20261105_t1540/RESEARCH.md` proved convexity in a two-decision-gate model. Does adding a **nonterminal LR merger followed by another split** itself allow real-image nonconvexity?

## Theorem: arbitrary finite horizon, downstream observer-lumpable model

Let `H>=2` be any finite horizon; hidden source h has strictly positive prior Q and P weight w_h (sum 1), and all sources start at (t,r)=(1,1). FULL observes h plus (t,r); seedless LR observes only (t,r). At every t<H the observer may stop, freely declare P/Q, or continue; at H it must declare. At each decision key, arbitrary real behavioral randomization probabilities in [0,1] are allowed, but no extra persistent common random seed. Define O4=(e_P,e_Q,T_P,T_Q) with e_P=P(declare Q), e_Q=Q(declare P), T_P=E_P(tau), T_Q=E_Q(tau).

On continuing from t=1, source h has a strictly positive Q transition row `K_{1,h}(r')` on shared finite ratio alphabet R_2, with row sum 1 and ratio mean 1. On continuing from any t>=2, the conditional Q transition to the next ratio `r'` is a strictly positive row `K_t(r,r')` **identical for all sources and every earlier path arriving at observed (t,r)**, with row sum 1 and mean r. The P transition row is `(r'/r)K_t(r,r')`. Multiple different observed histories may merge at a nonterminal LR ratio, then split again. First-step source-dependent kernels are allowed.

**Conclusion:** Both actual real behavioral observation images `O4(seedless LR)` and `O4(FULL)` are compact convex polytopes. Therefore
`conv O4(FULL)=conv O4(seedless LR) <=> O4(FULL)=O4(seedless LR)`.

### Exact proof for seedless LR

Let `m_t(r)` be active Q mass at observed key (t,r), `c_t(r)` its continued Q mass, and `d_t(r)` the Q mass stopping and declaring P. Put `Kbar_1(r')=sum_h w_h K_{1,h}(r')`. Every policy induces the following *linear* finite constraints:
```
m_1(1)=1, m_1(r)=0 at other first-time ratios
0 <= c_t(r) <= m_t(r)
0 <= d_t(r) <= m_t(r)-c_t(r)
c_H(r)=0
m_2(r')=c_1(1)*Kbar_1(r')
m_{t+1}(r')=sum_{r in R_t} c_t(r)*K_t(r,r') for t>=2.
```
The first recursion holds because the source-blind observer has one action at (1,1), hence all sources have the same t=1 continuation probability. The later recursions hold because every incoming hidden history to the same (t,r) has the same outgoing kernel. These constraints bound a polytope.

Conversely, given *any* feasible point of this polytope, define behavioral continuation probability `a_t(r)=c_t(r)/m_t(r)` at positive active mass and conditional P declaration probability `b_t(r)=d_t(r)/(m_t(r)-c_t(r))` when the stopping mass is positive; set either to 0 at zero denominator. All lie in [0,1], and forward recursion reconstructs exactly the given occupancy. Thus this is the image of **genuine individual** seedless LR behavioral policies, not merely a convex-hull relaxation.

The four observations are affine:
```
e_Q=sum_{t,r} d_t(r)
e_P=sum_{t,r} r*(m_t(r)-c_t(r)-d_t(r))
T_Q=sum_{t,r} m_t(r)
T_P=sum_{t,r} r*m_t(r).
```
Each active P mass equals r times its Q mass by the likelihood martingale rows. Affine images of bounded polytopes are compact convex polytopes, and an occupancy convex combination is realized by a *single* reconstructed behavioral policy without a persistent seed.

### Proof for FULL

Apply exactly the same mass/continued/declared variables separately to each visible source h, with `m_1^h(1)=w_h`, `m_2^h(r')=c_1^h(1)K_{1,h}(r')`, and subsequent common K_t recursions. Independent feasible occupancy polytopes for each h form a product polytope; each source-indexed policy is recovered from the same conditional ratio inverses. Aggregate O4 is a linear image of this product polytope, so it too is compact and convex. Seedless policies are admissible FULL policies that ignore h. Since both sets equal their convex hulls, the displayed equivalence follows. QED.

### Interface meaning

Nonterminal mergers and re-splittings are fully allowed; **downstream conditional observer-lumpability** is the sufficient convexification property. At a nonlumpable merger, the hidden-history mixture and the outgoing kernel can depend on earlier stopping choices, so a fixed linear flow recursion cannot be inferred from this proof. Nonlumpability is a candidate mechanism, not an asserted universal nonconvexity result. The branch weights and path provenance are retained until an exact observer-safe quotient is justified. This uses the existing positive-weighted BRC carrier and is an external O4 observer calculation, not a native X6 dynamics theorem; P000 and ACTIVE worldview are unchanged.

## Exact four-stage positive example

Two sources have weights (2/5,3/5), stage-2 ratios R2=(1/2,1,3/2), and Q rows K1[A]=(1/4,1/2,1/4), K1[B]=(3/8,1/4,3/8). Common stage-2 to stage-3 kernel on R3=(1/4,1,7/4):
```
1/2 -> (3/4,1/6,1/12)
1   -> (1/4,1/2,1/4)
3/2 -> (1/12,1/6,3/4)
```
Common stage-3 to stage-4 kernel on R4=(1/8,1,15/8):
```
1/4 -> (25/28,1/14,1/28)
1   -> (1/4,1/2,1/4)
7/4 -> (1/28,1/14,25/28).
```
All rows have strictly positive entries, sum to 1 and have exact LR mean equal to their input ratio. **Each t=2 key reaches the common nonterminal key (3,1)** with positive probability. That shared key may continue to three distinct terminal likelihood ratios; its downstream kernel is the same for all incoming paths. The hidden source is nontrivial because K1 differs.

Actual local execution: Python 3 standard library `Fraction` checker verifies positivity, martingale rows, and exact real-policy occupancy mixture inversion for 120 pairs of seedless LR policies and 120 pairs of FULL policies with rational probabilities. All 240 reconstructions and all four observed coordinates passed. `EXACT_OUTPUT.txt` contains the actual run result; the analytic proof, not the sample test, establishes the theorem for arbitrary H.

## Next unit

Construct a strictly positive rational four-stage model where two incoming histories merge at a *nonterminal* (t,r) but retain distinct conditional outgoing likelihood distributions. Choose two seedless LR real-behavior strategies; use exact polynomial feasibility or real quantifier elimination to certify whether their O4 midpoint belongs to **any** real randomized seedless LR strategy. If a nonconvexity witness is obtained, analyze the stronger FULL/LR full-hull equality separately. Preserve unrestricted stopping and P/Q declaration choices, actual hidden provenance, P000, frozen pins and author/reviewer boundaries. R5 mother objective is open.

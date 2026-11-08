# PREFIX-613-R2 — Exact four-sparse native BRC probe for blind gate words

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR-SIDE EXACT PROOF + EXECUTED ORIGINAL-48-PHASE RATIONAL CHECKER; independent Driver review pending.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-612-R2 PR #1842 @2860d3fb1662fa3412b099995f98fac61f551489, PREFIX-608, original STAR phase-sum law.

## Exact problem and observer

Use the original native X6 STAR with 48 ordered phases, 96 bit ports and 576 labeled actions, with fixed axis weights (1,1,1,1,0,0) and an arbitrary gate word g_1,...,g_n in nonnegative reals. Upstream branch provenance is retained; this result concerns the original 48-phase linear-sum observation, not labeled port-path histories.

Two synchronized experiments start at arbitrary unknown nonnegative v and v+lambda*d. The direction d is a known nonnegative 48-vector, lambda>0 is unknown. The runs use the same unknown gate word. Read phase 3 after every gate in both runs and also phase 4 after the first gate (zero-based indices).

Let Q(g) be the frozen exact 48-dimensional phase-sum transfer and w_t=Q(g_t)...Q(g_1)(lambda*d), w_0=lambda*d. Because the runs share the gates their contrast evolves exactly by Q. The only gate-dependent entries are Q(g)[3,4], Q(g)[14,4], Q(g)[15,4], each g+3; every other nonzero entry is constant. Therefore

    w_t[3] = (g_t+3)*w_(t-1)[4] + 2*w_(t-1)[16] + 2*w_(t-1)[20],
    w_1[4] = lambda*(d[11]+d[26]+d[35]),
    Q(g')-Q(g) = (g'-g)*(e_3+e_14+e_15)*e_4^T.

All nonzero coefficients of Q(g) are positive for g>=0.

## Theorem 613.1: exact sharp four-support criterion

Define pairwise-disjoint native phase sets

    G0={4},
    G1={11,26,35},
    G2={32,40,44},
    G3={14,23,47}.

For any n>=4, the following are equivalent:

(A) The nonnegative known direction d has supp(d) intersecting each G0,G1,G2,G3.
(B) For every lambda>0, every nonnegative gate word and arbitrary unknown nonnegative common base v, all n gates and lambda can be uniquely reconstructed from n scalar contrasts at phase 3 after each gate plus one phase-4 scalar contrast after the first gate.

Moreover, if any intersection is empty, there is an unobservable gate among the first four steps even when the *complete 48-phase contrast at every time* is supplied. Taking v=0 gives two distinct full raw two-run experiments with exactly identical complete phase observations. Thus four nonzero original phase locations are necessary and sufficient for uniform arbitrary-word gate recovery (n>=4).

### Exact proof

For k>=0 let R_k denote the support in original input coordinates of row e_4^T Q(g_k)...Q(g_1). Since all nonzero transition weights are strictly positive, R_k is independent of the numerical nonnegative gates. The exact frozen STAR successor graph and 16 terminal zero rows give:

    R0 = {4}
    R1 = {11,26,35}
    R2 = {32,40,44}
    R3 = {14,23,47}
    R4 = {4,8,20}
    R5 = R1, R6 = R2, R7 = R3, R8 = R4, etc.

Only 26 in R1, 40 in R2, 14 in R3 and 4 in R4 have nonzero source rows; the active four-cycle is 4 -> 26 -> 40 -> 14 -> 4. Every other member of these row supports is terminal. The recurrence therefore repeats from R1 every four steps (verified directly from the frozen 48-phase STAR definitions by the accompanying checker).

For nonnegative d and positive lambda, positivity gives

    w_k[4]>0  iff  supp(d) intersects R_k.

Meeting G0,...,G3 is hence equivalent to w_k[4]>0 for every k>=0: the period-0 support R0 is included in R4, while the three other residue supports repeat. Condition (A) in particular ensures kappa=d[11]+d[26]+d[35]>0; phase-4 first-gate contrast Z gives lambda=Z/kappa. Inductively, knowing w_(t-1) and the observed phase-3 contrast Y_t=w_t[3], recover

    g_t = (Y_t - 2*(w_(t-1)[16]+w_(t-1)[20])) / w_(t-1)[4] - 3,
    w_t = Q(g_t)*w_(t-1).

The denominator is strictly positive at every step for all nonnegative gates, including zero, so reconstruction is globally unique. n+1 difference scalars use 2(n+1) original readouts from two experiments.

For necessity, if d misses G_r for r=0,1,2 or 3, then w_r[4]=0. By the displayed rank-one difference law, replacing g_(r+1) by ANY different nonnegative gate leaves w_(r+1) unchanged and therefore leaves all later phase contrasts unchanged under identical future gates. This remains true even if the full 48-phase differences are observed. Choose v=0: the first run stays zero and the second run has identical full phase outputs under both gate words, proving the stronger raw-output indistinguishability. Since the four sets are disjoint, fewer than four support sites necessarily miss one set. This proves (A) iff (B) and sharpness.

## Corollary 613.2: an explicit minimum-support probe

    d = e_4 + e_11 + e_32 + e_14.

This legal nonnegative native 48-phase source difference has exactly four nonzero original coordinates, one in each class. It calibrates lambda from the additional first phase-4 readout Z=lambda. Its initial excitations satisfy

    (w_0[4],w_1[4],w_2[4],w_3[4])=lambda*(1,1,2,4).

For t>=1 the active four-cycle yields the exact scalar identity

    w_(t+4)[4]=4*(g_(t+1)+3)*w_t[4],

so all denominators stay positive for arbitrarily long nonnegative gate words. This strengthens PREFIX-612's positive uniform increment by reducing the controlled input support from 48 native coordinates to the sharp minimum of four, with the same two fixed sensor locations (phase 3 after all gates, phase 4 once).

## Executed exact checks and interface boundary

Standalone Python/SymPy checker independently builds native STAR 48 phases from frozen equations; verifies exact Q row laws, rank-one gate dependence, all R0..R8 sets and periodicity, exact inverse recovery for nonnegative integer/rational gates, unknown nonnegative sources, and unknown positive probe scales. It also constructs four separate full-48-phase indistinguishability witnesses for omitted support groups. Observed evidence: 243 exactly recovered gates, 11,664 exact contrast coordinate equalities, 1,536 full-state lower-bound witness coordinate equalities and 19 four-step excitation equalities; every executed assertion passed. Arbitrary-length theorems are based on the displayed exact support graph and induction; tests are implementation/witness checks.

Method resolution: original native BRC STAR phase-sum transfer, PREFIX-608 excitation and PREFIX-612 calibration; REUSE_APPLIED and COMPOSE_APPLIED. No acceptance or higher-dimensional path-provenance equivalence is asserted. Separate formal Native Result and independent Driver review are pending.

Next concrete unit: minimize the algorithmic state needed to update w[4], w[16], w[20] for the four-sparse probe and count initialization, bit-length, exact arithmetic and output recovery; also classify sparse probes when the first phase-4 calibration read is unavailable.

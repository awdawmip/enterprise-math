# R5 — Nonlumpable four-stage merger: nonconvex real LR image and an observer-hierarchy separation

2026-11-05, Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother question and provenance

The R5 mother question asks for a strictly positive finite P/Q stopping BRC with complete four-observer FULL/LR convex-hull equality but different actual **real-behavior** observation images. The frozen science pins are GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. This continues predecessor enterprise-math@1abcfe76aeaae453912d186e5f96ae0c5a0a8104, research_notes/brc_r5_multistage_lumpability_20261105_t1642/RESEARCH.md. That predecessor establishes convexity when the future kernel at a merged observable LR key is history-independent; here the downstream kernel is history-sensitive.

The carrier is a finite positive weighted BRC over P/Q histories. The observer keeps only (time, likelihood ratio); it erases incoming path provenance. This is an auxiliary observer experiment, not an asserted native X6 dynamics law. All internal decision keys allow STOP+declare P, STOP+declare Q, or CONTINUE, and stage four requires a declaration. All behavioral probabilities are arbitrary real numbers in [0,1]; no extra persistent common random seed is available. O4=(e_P,e_Q,T_P,T_Q), e_P=P(declare Q), e_Q=Q(declare P), and T_L=E_L(tau).

## Exact positive model S

Time 1 has ratio 1. On continuation, time 2 ratios R2=(3/4,5/4) have Q weights (1/2,1/2). Time 3 ratios R3=(1/2,1,3/2) have conditional Q rows:

    from time-2 3/4: (13/20,1/5,3/20)
    from time-2 5/4: (1/40,9/20,21/40).

Time 4 ratios R4=(1/10,1,19/10) have Q rows:

    from time-3 1/2: (509/900,382/900,9/900)
    from time-3 3/2: (9/900,382/900,509/900)
    from time-3 1, having arrived from time-2 3/4: (1/90,44/45,1/90)
    from time-3 1, having arrived from time-2 5/4: (67/162,14/81,67/162).

For an r-to-s transition define the P row as Q(s|history)*s/r. Every Q row has strictly positive entries, sums to one, and has ratio mean r; hence every corresponding P row is also positive and normalized. Both time-2 histories reach the **same** nonterminal time-3 ratio 1 with positive mass, but future conditional probabilities depend on the incoming history. The seedless LR observer cannot condition its time-3 action on that previous path.

## Theorem A: the actual real seedless LR image is nonconvex

Choose support direction n=(-1,-1,-3/25,+1/50) on O4 and per-stage Q-cost c(r)=3r/25-1/50. The Bayes declaration loss at ratio r is min(r,1), and E_Q[c(r_next)|r]=c(r) by the likelihood-ratio martingale.

At time-3 ratios 1/2 and 3/2, the terminal Bayes information gain is 9/1000, strictly less than respective extra time costs c(1/2)=1/25 and c(3/2)=4/25. Every support optimizer stops there. At the shared time-3 ratio 1, the gain from continuing is 1/100 from predecessor 3/4 and 67/180 from predecessor 5/4. Subtracting c(1)=1/10 yields advantages -9/100 and 49/180.

The time-2 baseline continuation advantages (before time-3 continuation) are respectively 1/200 and -47/400. Let a,b in [0,1] be the two time-2 continuation probabilities. The continuation probability z at the shared time-3 key must be common for both histories. Optimizing z gives an exact incremental support value relative to stopping at time two:

    F(a,b)=1/2 * ((a/200-47*b/400)
                    + max(0,-9*a/500+49*b/400))
          =1/2 * max(a/200-47*b/400,
                      -13*a/1000+b/200).

The first affine form is maximized uniquely over the unit square at (a,b)=(1,0), value 1/200. The second is maximized uniquely at (0,1), also value 1/200. Therefore max F=1/400. For the first branch z=0 is forced; for the second z=1 is forced. With both time-2 nodes stopped after time-1 continuation, support equals -43/40, so the global maximum is -43/40+1/400=-429/400. Stopping at time 1 yields -11/10, strictly smaller. Hence every global maximizer continues at time one and has one of precisely two time-2 and shared-time-3 action patterns. Bayes declaration ties at ratio 1 can vary the error coordinates but not the time coordinates.

Explicit maximizing policy A continues at time one, continues only from time-2 ratio 3/4, stops throughout time three, and uses Bayes declarations (Q for r<1, P for r>1, choose Q at r=1). Policy B continues at time one, continues only from time-2 ratio 5/4, continues from time-3 ratio 1 but stops at the other time-3 ratios, and uses the same Bayes declaration rule. They produce exactly

    W_A=(21/80,23/40,19/8,5/2)
    W_B=(773/1800,16/45,57/20,109/40).

Both satisfy n·W=-429/400. Their midpoint

    W_mid=(2491/7200,67/144,209/80,209/80)

also lies in the exposed supporting hyperplane. Any real behavioral policy that attained W_mid would therefore maximize the same objective, forcing its time coordinates to equal either (19/8,5/2) or (57/20,109/40), neither of which equals (209/80,209/80). Contradiction. Thus W_mid is in conv O4(LR;S) but not in the actual O4(LR;S). This is a proof for **all** real behavioral probabilities, not a finite grid search.

## Theorem B: source-only versus genuinely full-history observers — a necessary distinction

An identical-law two-label lift of S defines a **restricted source-only FULL_H** class: draw H=A or B with weight 1/2 under P and Q; conditionally on each H run exactly S. FULL_H observes H but, like LR, does **not** retain the earlier stage-2 route when acting at the shared (3,1) key. If L=O4(seedless LR;S), then

    O4(LR;S×H)=L,
    O4(FULL_H;S×H)={ (x+y)/2: x,y in L }.

It follows that conv O4(FULL_H)=conv O4(LR), while W_mid belongs to the real FULL_H image and not the real LR image. This is an exact **source-only observer variant** and supplies a constructive label-based convexification principle.

For the R5 mother question, however, the stronger **full-history FULL_HIST** observer may retain the earlier route at the nonterminal merger. Under that actual route-aware observation class, the same model has a strict **convex-hull separation**, so the source-only lift must not be mistaken for a solution to the full-history R5 target.

Indeed, let FULL_HIST continue at time 1, continue from BOTH time-2 ratios 3/4 and 5/4, and at time-3 ratio 1 stop when the incoming time-2 ratio was 3/4 but continue when it was 5/4. Stop at the other time-3 nodes and use the Bayes declarations everywhere (Q for ratios below 1, P above 1, choose Q at 1). The resulting exactly evaluated vector is

    W_hist=(1141/3600,31/72,129/40,129/40),

with n·W_hist=-107/100. The seedless LR support maximum in Theorem A is -429/400. Hence

    h_FULL_HIST(n)-h_LR(n) >= (-107/100)-(-429/400)=1/400>0.

This is an exact separating-direction certificate: for this path-sensitive model, the complete FULL_HIST/LR convex hulls **differ**. It isolates the distinction between two kinds of extra information: a source label that randomizes independent conditional LR policy choices, and an incoming route that changes the optimal continuation decision at a merged LR key. The latter already creates a positive support-function gap here.

Theorem A remains a general-real-strategy nonconvexity witness. The R5 target with FULL observing the entire route remains open. If the frozen R5 task instead expressly defines FULL as source-only, the above restricted lift is a complete exact mathematical construction at that scope. In either case, theorem admission and frozen task interpretation belong to current canonical review authority.

## Exact verification and next inquiry

The independent full-history witness uses a route-conditional action at the shared node, and was evaluated in an additional local Python Fraction calculation. Its vector and 1/400 gap are explicitly given in Theorem B. The 5832-policy exhaustive count refers to LR only, and the full-history calculation is analytic/direct rather than an exhaustive FULL policy enumeration.



VERIFY.py is Python 3 stdlib Fraction. It verifies the positive P/Q row identities, Bellman coefficients, both explicit four-vectors, their midpoint, and exhaustively evaluates 3*(3^2)*(3^3)*(2^3)=5832 deterministic LR strategies. It finds maximum -429/400 and exactly two distinct timing pairs among all 18 maximizing deterministic strategies. These checks corroborate, but do not replace, the all-real analytic proof. EXACT_OUTPUT.txt records the actual run. NEXT_TASK.md requests review of FULL information scope and an all-directions hull-equality route under the frozen R5 semantics.

BRC reuse: positive rational branch weights and labeled incoming path ports are retained until observer-safe quotienting; the irreducible future-kernel residual at (3,1) is the nonconvexity mechanism. No P000 change, Foundation promotion or independent Driver review is implied.

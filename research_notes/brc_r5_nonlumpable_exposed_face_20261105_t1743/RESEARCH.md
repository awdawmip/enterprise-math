# R5 — Nonlumpable four-stage merger: a nonconvex real LR image and a full-hull-equal two-source lift

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

## Theorem B: two identical-law source labels yield complete full-hull equality but different real images

Form S×H by drawing a genuinely observable-to-FULL source label H=A or B, with weight 1/2 under BOTH P and Q, and then running exactly S independently of which label was drawn. Each source's conditional experiment is identical, but the model retains the nonlumpable path-dependent transition inside S. FULL additionally observes H; LR only observes (time,r).

Let L=O4(seedless LR;S). Because the two source conditional laws are identical,

    O4(seedless LR;S×H)=L,
    O4(FULL;S×H)={ (x+y)/2: x,y in L }.

The latter contains L (take x=y) and is contained in conv(L), proving the **complete** four-dimensional convex-hull identity

    conv O4(FULL;S×H) = conv O4(seedless LR;S×H).

FULL takes policy A on source label A and B on source label B and attains W_mid. Theorem A proves W_mid is unattainable by a single seedless LR real behavioral policy. Thus the actual real images **differ** despite exact full-hull equality.

Scope: the two source labels have equal conditional observable laws; the model's *route-dependent* future laws are genuinely different at the shared nonterminal key. This settles the hull-versus-real-image phenomenon for an admissibility class permitting duplicate conditional source laws with nonlumpable path history. If the exact frozen R5 task additionally demands that the source-conditional experiments themselves differ, the heterogeneous-source strengthening remains an independent open condition requiring exact taskbook verification. No task admission or closure is asserted by author proof.

## Exact verification and next inquiry

VERIFY.py is Python 3 stdlib Fraction. It verifies the positive P/Q row identities, Bellman coefficients, both explicit four-vectors, their midpoint, and exhaustively evaluates 3*(3^2)*(3^3)*(2^3)=5832 deterministic LR strategies. It finds maximum -429/400 and exactly two distinct timing pairs among all 18 maximizing deterministic strategies. These checks corroborate, but do not replace, the all-real analytic proof. EXACT_OUTPUT.txt records the actual run. NEXT_TASK.md requests a review of the frozen source admissibility and the possible genuinely heterogeneous-source extension.

BRC reuse: positive rational branch weights and labeled incoming path ports are retained until observer-safe quotienting; the irreducible future-kernel residual at (3,1) is the nonconvexity mechanism. No P000 change, Foundation promotion or independent Driver review is implied.

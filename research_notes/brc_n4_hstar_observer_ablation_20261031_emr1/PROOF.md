# BRC N=4: exact lawful H* observer ablation — time and BU sensor

2026-10-31. AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen model and scope

This is a direct continuation of Enterprise Math PR #1757, immutable predecessor 29b40fe084d7b7382fcfa7e5207011bcacc312c3, especially its lawful H* policy and strictly positive 16-leaf BRC N=4 double experiment. This note concerns **one fixed lawful policy H*** and four explicit *public* observation channels. It does not assert an all-policy, physical X6 or formal Task Result theorem.

Six distinct prepared conditional rows, ordered AU_Q, AU_P, AV, BU_Q, BU_P, BV and columns AU0,AU1,AV,BU0,BU1,BV, equal 1/20 times

    [10,10, 0, 0, 0, 0]
    [ 9,11, 0, 0, 0, 0]
    [ 0, 0,20, 0, 0, 0]
    [ 0, 0, 0,10,10, 0]
    [ 0, 0, 0, 2,18, 0]
    [ 0, 0, 0, 0, 0,20].

The duplicated AV_P/Q and BV_P/Q preparations also count in the eight-input scoring maximum. The original P/Q leaf weights per K are AU P=(9,11), Q=(10,10); AV P=(5,5), Q=(20,20); BU P=(3,27), Q=(15,15); BV P=(30,30), Q=(15,15). Each of the two laws has 16 positive leaves and total raw weight 240. K is an independent fair terminal bit. BU-only sensor Z is J xor Bernoulli(epsilon), with real 0 <= epsilon <= 1/2, and Z=bottom outside BU.

Fix lawful policy H*: continue at stage 1; at stage 2 stop **only AV** with terminal Decision Q; continue AU,BU,BV; at stage 3 terminate and decide P on AU and BU, Q on BV. The AU/BU stage-2 continuation kernels agree and the stage-3 decisions are constant on equal contemporaneous likelihood-ratio classes (the duplicated BV nodes decide Q). The policy uses no unseen K. This is lawful under S2 and S23 as defined in the predecessor.

Four channels: O_TZ=(T,Decision,Z), O_T=(T,Decision), O_Z=(Decision,Z), O_0=Decision. Removing Z explicitly removes both its bit and its **presence flag**; only the specified projected public record is visible. Removing T does not modify H*'s stopping decisions.

For a fixed channel A and fixed H*, the reconstruction objective is

    R_k(H*,A;epsilon) = inf_{E,D stochastic, E with k columns}
          max_{eight prepared inputs x} TV(P_A(.|x), (E D)(.|x)).

The encoder is common across preparations, selected before the outcome. The decoder is common for this fixed policy; randomized encoders/decoders are allowed. This is distribution reconstruction, not recovery of the actual realized sample.

## Theorem (all real 0 <= epsilon <= 1/2)

| public record | disjoint provenance blocks G | R1 | R2 | exact code states for epsilon<1/2 | exact states for epsilon=1/2 |
|---|---:|---:|---:|---:|---:|
| (T,Decision,Z) | 4 | 3/4 | 1/2 | 5 | 4 |
| (T,Decision) | 3 | 2/3 | 1/2 | 3 | 3 |
| (Decision,Z) | 3 | 2/3 | 1/2 | 4 | 3 |
| Decision | 2 | 1/2 | 0 | 2 | 2 |

The sensor contributes a genuinely distinct *conditional distribution* direction for epsilon<1/2; stop time distinguishes AV from BV. The joint effect is not the sum of two independent bits, and deleting either is a scope-typed observer quotient, not identification of native X6 Cells.

## Proof 1: exact response matrix and distinguishability

Let a=(3,P,bottom), v=(2,Q,bottom), b=(3,Q,bottom), u0=(3,P,0), u1=(3,P,1). Full H* response rows are delta_a for AU_Q/AU_P, delta_v for AV, delta_b for BV, and BU_Q/BU_P supported on u0,u1 with respective probabilities

    q_BU = (1/2, 1/2)
    p_BU = (1/10+(4/5)epsilon, 9/10-(4/5)epsilon).

The BU internal total variation is (2/5)(1-2epsilon), exactly. In O_TZ, the supports of AU,AV,BU,BV are four disjoint provenance blocks. Removing Z merges AU and BU into the same (3,P) atom, yielding three blocks AV / AU+BU / BV. Removing T merges AV and BV into (Q,bottom), yielding three blocks AV+BV / AU / BU. Removing both yields two atoms, Decision=P on AU+BU and Q on AV+BV. No free source label is supplied to the observer.

## Proof 2: sharp single-code minimax

For G input laws on disjoint support sets U_1,...,U_G, every one-symbol decoder d has sum_i d(U_i)<=1. Some i has d(U_i)<=1/G. Since the true input law is entirely supported on U_i, TV(P_i,d)>=1-1/G.

For upper bounds, use a decoder with uniform 1/G mass on each of the G displayed blocks, with a fixed rational conditional b_BU=(1/5,4/5) on BU's observed bit when Z remains. Crucially, for **both** BU preparations and every epsilon in [0,1/2],

    (1/2)*b_BU(z0)=1/10 <= min(1/2,1/10+(4/5)epsilon),
    (1/2)*b_BU(z1)=2/5  <= min(1/2,9/10-(4/5)epsilon).

Thus allocating at most 1/2 to the BU reference gives a coordinatewise submeasure of either true BU law. Each pure-atom provenance block also carries a pointwise submeasure of weight 1/G. The overlap of each true input and the decoder is therefore exactly 1/G; its TV error is exactly 1-1/G. This attains the four R1 values, uniformly in all real epsilon.

## Proof 3: sharp two-code minimax

For G=4 the disjoint-support packing inequality gives R2 >= 1-2/4=1/2 for arbitrary stochastic E,D. For G=3 a *majority decoder lemma* improves the naive packing bound. If TV(P_i,(ED)_i)<1/2 for three pairwise disjoint U_i, then (ED)_i(U_i)>1/2. Consequently at least one decoder row D_j has D_j(U_i)>1/2. A probability row cannot assign >1/2 mass to two disjoint blocks. Two decoder rows therefore cannot attain <1/2 error on three such inputs. Hence R2>=1/2 for G=3, again for arbitrary randomized encoding.

Explicit deterministic encoders and randomized decoders attain these bounds:

* Full channel, G=4: encode AU/AV -> L, D_L=(delta_a+delta_v)/2; BU/BV -> R, D_R=(b_BU+delta_b)/2. The BU half-submeasure inequality above makes every true group's TV exactly 1/2.
* No Z, G=3: encode AV/AU/BU -> L, D_L=(delta_AV+delta_AU)/2, and BV -> R with exact delta_BV. BU and AU are the **same public output**; maximum TV is 1/2.
* No T, G=3: encode AV/BV/AU -> L, D_L=(delta_Q+delta_AU)/2; BU -> R, D_R=b_BU. The first three source inputs attain 1/2; BU_Q has TV 3/10 and BU_P has TV |1/10+(4/5)epsilon-1/5|<=3/10.
* Neither T nor Z, G=2: encode AU/BU and AV/BV separately, decode their P or Q decisions exactly, giving R2=0.

These are **legal stochastic decoders** for the fixed H*, not new stopping strategies. The explicit constructions give the upper bounds for every epsilon, and the disjoint-support/majority lemmas give the lower bounds.

## Proof 4: sharp exact-state threshold

If a common k-state factorization reproduces the full six-row response exactly, rank(P_A)=rank(E D)<=k. Conversely, each channel here has exactly rank(P_A) distinct output prototype rows, so a deterministic encoder choosing the appropriate prototype row and using that row as decoder achieves exact reconstruction with rank(P_A) states.

For O_TZ, the three pure AU,AV,BV atoms are independent, and the BU 2-by-2 block has determinant

    det([[1/2,1/2],[1/10+(4/5)epsilon,9/10-(4/5)epsilon]])
       = (2/5)(1-2epsilon).

Thus rank=5 for epsilon<1/2, rank=4 at epsilon=1/2. O_T has exactly three distinct delta rows and rank 3. O_Z has two distinct pure atoms and the same BU block, giving rank 4/3 across the epsilon endpoint. O_0 has only the two distinct delta decisions, rank 2. All stated minimum exact k values follow; no numerical rank threshold, assumption of nonnegative-rank equality, or finite-precision inference is used.

## Actual arithmetic evidence and mathematical boundary

VERIFY.py (Python standard-library Fraction, actually executed) reconstructs the 16 positive leaves under both laws, all six prepared conditional rows, the H* causal observation map and all four projections; it checks exact matrix ranks and constructive decoder TV bounds for epsilon=0,1/8,1/4,1/2, 4 channels x 6 prepared rows = 96 exact input-observer comparisons. RUN_EVIDENCE.txt is its execution output. The continuous-epsilon and arbitrary stochastic-encoder statements are **analytic** above; the finite tests are audits only.

This is an author-side finite BRC observation theorem. Classical TV/data processing, stochastic matrix rank and disjoint-support reasoning are used; no novelty claim about general Blackwell/Le Cam theory, native P000 X6 physical dynamics, Heartbeat time calibration, actual sensor physics, formal Result, independent review or Foundation acceptance follows. Path provenance and joint-observer semantics are retained in the underlying model.

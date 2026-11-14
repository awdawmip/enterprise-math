# R5 — Exact finite-tag overlap theorem: full-history information deficit at a shared BRC gate

2026-11-05 (Asia/Shanghai) · AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen objective and input

The R5 mother question asks whether strictly positive finite P/Q stopping BRC admits identical COMPLETE four-observer convex hulls for FULL_HIST and seedless LR, with unequal actual real-behavior observation sets. The observation is O4 = (P[declare Q], Q[declare P], E_P[tau], E_Q[tau]); behavioral probabilities range over all reals in [0,1], without a persistent external seed.

Scientific pins are unchanged: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Predecessors: the shared-gate Bellman reduction e121e1927232baee2e5b49863c72c01d406010ed, and model S/finite stochastic tag formula a737b271c871375d90b8bf06e0e63469526fbfed. Current norm policies are read separately from those frozen scientific sources.

BRC carrier: positive P/Q branch masses, labeled incoming histories i and their provenance up to a nonterminal merged gate. Available downstream operations: stop/continue and P/Q terminal declarations. The allowed observation is stated explicitly; collapsing history i into tag y is not presumed to preserve future operations.

## Exact theorem: tag-support criterion and computable positive gap

Fix a four-observer support direction n. Assume the **globally optimized full stopping problem** for that direction really admits the exact Bellman reduction

    J = C + sum_{i=1}^m w_i a_i (A_i + u_i z_i)

where m is finite, w_i>0, the upstream choices a_i∈[0,1] are independently controllable at distinguishable incoming keys, A_i,u_i∈R, and downstream full-history choices z_i∈[0,1]. A finite tag Y appears after upstream selection with row-stochastic channel T(y|i)≥0; conditional on incoming history it is independent of upstream randomization and affects only the permitted downstream choice. A tagged observer instead selects one z_y∈[0,1] per tag output and history i receives t_i=Σ_y T(y|i)z_y. The conditional tag kernel agrees under P/Q given incoming history, so the tag does not alter likelihood ratios.

Write [x]_+=max(0,x), M_i=max(0,A_i,A_i+u_i). Define

    I_- = {i : A_i>0 and u_i<0}
    I_+ = {i : A_i+u_i>0 and u_i>0}
    supp(T_i) = {y : T(y|i)>0}.

Then the following statements hold for **all real behavioral probabilities**.

**(A) Exact finite deficit.**

    D(n)=h_FULL(n)-h_TAG(n)
        = min_{S⊆Y} Σ_i w_i{M_i-[A_i+u_i T(S|i)]_+} ≥ 0,

where T(S|i)=Σ_{y∈S}T(y|i). This requires at most 2^|Y| binary tag selectors, not a probability-grid approximation.

**(B) Exact zero-loss criterion.**

    D(n)=0  iff
    (⋃_{i∈I_-}supp(T_i)) ∩ (⋃_{j∈I_+}supp(T_j)) = ∅.

An empty active class is allowed. In words, tag outputs used by strictly stopping active histories and strictly continuing active histories must have disjoint support. The criterion is combinatorial and depends only on zero/nonzero tag probabilities, not on their magnitudes.

**(C) Quantitative overlap certificate.** For each y, define

    b_-(y) = Σ_{i∈I_-}w_i min(A_i,-u_i)T(y|i)
    b_+(y) = Σ_{j∈I_+}w_j min(A_j+u_j,u_j)T(y|j).

Then

    D(n) ≥ B(n):=Σ_{y∈Y}min(b_-(y),b_+(y)) ≥ 0.

Thus any positive-overlap tag symbol shared by an active stop and an active continue history forces strict FULL-versus-TAG four-observer convex-hull separation at n. The same is true for any finite **everywhere-positive** channel whenever both classes are nonempty. For an explicit pair i∈I_-,j∈I_+, the lower bound can be restricted to

    Σ_y min(w_i min(A_i,-u_i)T(y|i),
            w_j min(A_j+u_j,u_j)T(y|j)).

The group bound is at least as strong as this pairwise bound. The theorem is scoped to one complete global Bellman reduction and does not assert that every proposed BRC model has such a reduction on every support direction.

### Proof

For fixed tagged decisions z=(z_y), maximizing the independently controllable upstream a_i gives

    C + Σ_i w_i[A_i+u_i Σ_y T(y|i)z_y]_+.

This is convex in z on [0,1]^|Y|, hence its maximum is attained at a binary cube vertex. Such vertices identify subsets S⊆Y. FULL independently optimizes each pair (a_i,z_i), giving C+Σ_iw_i M_i. Subtracting the two expressions proves (A).

All deficits M_i-[A_i+u_i t_i]_+ are nonnegative. If M_i=0 then the affine expression at both t=0 and t=1 is nonpositive, so the deficit is zero for every t∈[0,1]. If u_i=0 it is constant. Otherwise, the unique t maximizing a positive payoff is t=0 exactly on I_- and t=1 exactly on I_+. Consequently zero total deficit requires one S with T(S|i)=0 for all i∈I_- and T(S|j)=1 for all j∈I_+. Since tag masses are nonnegative, the first means S contains no symbol emitted by the stop class, the second means it contains every symbol emitted by the continue class. Such an S exists exactly when their support unions are disjoint, proving (B).

For i∈I_-, and t_i∈[0,1],

    M_i-[A_i+u_it_i]_+
    = min(A_i,(-u_i)t_i)
    ≥ min(A_i,-u_i)t_i.

For j∈I_+,

    M_j-[A_j+u_jt_j]_+
    = min(A_j+u_j,u_j(1-t_j))
    ≥ min(A_j+u_j,u_j)(1-t_j).

Set t_i=T(S|i), sum positive weighted contributions, exchange finite sums, and obtain for every S

    Σ_y [b_-(y) 1(y∈S)+b_+(y)1(y∉S)]
    ≥ Σ_y min(b_-(y),b_+(y)).

Minimizing over S proves (C). Every active multiplier is strictly positive, so any shared tag support produces a strictly positive bound. QED.

### Algorithmic meaning

At an already-certified direction n, the exact test for zero FULL/TAG support gap needs O(m|Y|) arithmetic operations (classify histories and intersect supports). An exact positive rational lower bound B requires the same order of operations. Exact subset optimization as implemented can take O(2^|Y|m|Y|). These are arithmetic-operation counts, not a full bit-complexity bound. For rational BRC trees and linear Bellman coefficients, this can be combined with exact rational feasibility on individual four-dimensional sign cones. All alternative globally optimal stop/terminal decisions and cone boundaries must be included before claiming all-direction hull equality.

## Rational exact checks and model S reuse

In the fully specified, previously verified strictly positive BRC model S, the fixed support direction is n=(-1,-1,-3/25,1/50). Its certified Bellman coefficients are

    C=-43/40; w=(1/2,1/2);
    A=(1/200,-47/400); u=(-9/500,49/400).

A binary symmetric history tag has T_1=(1-eta,eta), T_2=(eta,1-eta), 0≤eta≤1/2. The two active histories require opposite gates. The new universal formula produces the inexpensive explicit bound B=eta/200, strictly positive for eta>0, and equality at eta=1/2. The previous exact subset formula gives

    D= min(281*eta/4000, 1/400).

At eta=0, disjoint supports recover FULL exactly. At eta=10/281, D=1/400 and B=1/5620. For strictly positive 0<eta≤1/2, FULL has a certified support advantage over the tagged observer.

For an independently checked THREE-history positive ternary channel, set w=(1/3,1/2,1/6), A=(1/7,-1/5,1/9), u=(-1/3,3/10,0), with T rows (1/2,1/3,1/6), (1/6,1/2,1/3), (1/4,1/4,1/2). Exact enumeration gives h_FULL-C=439/3780, h_TAG-C=37/540, D=1/21, B=9/280. Replacing the channel rows by the three separate unit vectors gives D=B=0. Four-history checks include neutral and inactive histories and verify zero-defect versus strict-overlap cases.

**Important validation scope:** The additional three-/four-history examples are exact conditional gate-coefficient checks, not newly built complete P/Q stopping trees. The fully positive BRC tree application is the inherited model S. No external literature novelty priority is asserted.

## Executed evidence

Ran Python 3 standard library fractions.Fraction program VERIFY.py on 2026-11-05. Enumerated all binary downstream selectors for seven rational crossover rates, the 3-history positive and disjoint channels and three 4-history channels. Verified exact support extrema, deficit formulas, support-disjointness equivalence, overlap lower bounds and predecessor S support values; all assertions passed. Exact stdout in EXACT_OUTPUT.txt. The analytic proof above, not those finite checks, supports arbitrary finite m, finite Y, and all real behavior probabilities.

The predecessor's complete model-S tree enumerator was not rerun in this turn: its prior verified source at immutable EM a737b271c871375d90b8bf06e0e63469526fbfed is relied on for the model-S Bellman reduction. For any new tree, verify that reduction over all other actions first. No formal CLAIM, Result, Driver review, mathematical admission, Foundation or P000 change is inferred from this authored proof.

## Next research unit

Construct the complete rational four-observer Bellman sign-cone arrangement for a small strictly positive BRC, accounting for all terminal declarations and upstream stop alternatives. For each valid cone derive the exact global C(n), A_i(n), u_i(n); solve strict rational feasibility for conflicting active gate choices with shared tag support. One feasible n yields a positive support difference certificate and dual-norm four-observer distance lower bound. If none, check every cone and boundary for a hull-equality certificate; only then independently test real-behavior image nonconvexity. The R5 mother objective remains OPEN.

BRC reuse decision: REUSE_APPLIED (positive history/provenance carrier, exact observer descent criterion, prior shared gate and finite-tag formula).
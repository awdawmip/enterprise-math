# PREFIX-794 / R6 — Exact future-observer-safe CRT residual under localized provenance toggles

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_LINEAR_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Predecessor: PREFIX-793 exact capacitated 2×b×c joint CRT fiber; PREFIX-792 binary parity ambiguity. Historical attribution: EM-DIRECT-E77192, RA-66BBE259AEE1AD543D9454A3 (27 historic checkpoints before this result). These historical labels do not grant a new authenticated session, CLAIM or review.

## Exact question

Does the pairwise count observer from PREFIX-793 remain sufficient after a future operation that changes one *jointly addressed source cell*? We study a precisely defined, reversible finite-path operation and derive an exact observer descent criterion. This is an external typed positive-integer complete-path BRC histogram model, not a native X6 transition.

Let H=Z_{≥0}^{\{0,1\}×B×C} be nonnegative named-complete-path multiplicities, with B={0,...,b−1}, C={0,...,c−1}. For n in H define the three pairwise margins

    P_(a,i)=Σ_j n_(a,i,j),
    Q_(a,j)=Σ_i n_(a,i,j),
    R_(i,j)=Σ_a n_(a,i,j).

Write L(n)=(P,Q,R). Set K_(i,j)=R_(i,j) and x_(i,j)=n_(0,i,j), so n_(1,i,j)=K_(i,j)−x_(i,j). The BRC carrier is a positive-integer count histogram, not signed amplitude. We retain the joint CRT direction associated with all three factors.

## Theorem 794.1 — Future observation reveals one discarded joint coordinate

For a selected (i,j), define the local source-aware involution τ_(i,j) by exchanging n_(0,i,j) and n_(1,i,j), leaving every other complete-path type unchanged. This is an actual bijection of H, and τ_(i,j)^2 is the identity. The post-update pairwise observer L(τ_(i,j)n) obeys

    Δ_(i,j) := P'_(0,i)−P_(0,i)
             = Q'_(0,j)−Q_(0,j)
             = n_(1,i,j)−n_(0,i,j)
             = K_(i,j)−2x_(i,j).

Consequently the pre-update joint cell is reconstructed by

    x_(i,j)=(K_(i,j)−Δ_(i,j))/2.

Proof: Only the two entries at (i,j) are exchanged. Their sum K is fixed, their difference reverses, and exactly one summand in the affected a=0 row and column changes; this gives all displayed equalities. As the histogram is integral, K and Δ have matching parity, and the quotient is exact. Applying the swap twice restores the initial histogram. QED.

The already known pairwise marginals determine all row sums r_i=Σ_j x_(i,j) and column sums s_j=Σ_i x_(i,j). Observing Δ_(i,j) for the (b−1)(c−1) cells with i<b−1 and j<c−1 in **separate independent experiments, each starting from the same initial histogram**, determines those x entries; the final column of the first b−1 rows and final row of the first c−1 columns are recovered by their sums, and the last corner by either remaining sum. Thus **the complete 2×b×c joint CRT count histogram is exactly reconstructed** from initial L and these future observations. This is an explicitly finite-horizon and operation-specific sufficiency result. It does not require any path-name reconstruction.

## Theorem 794.2 — Exact linear observer-descent and minimal scalar repair rank

Let V=Q^d carry arbitrary nonnegative integer states N^d. Let L:V→Q^m be a rational linear observer and T:V→V a rational linear state update (in applications T should preserve the stated population; integer permutations satisfy this). Fix a finite horizon h>=1. Then the tuple (L(Tn),...,L(T^h n)) is determined by L(n) for **every** n∈N^d if and only if

    ker_Q L ⊆ ker_Q (L T^k)    for all 1≤k≤h,

equivalently, rowspace_Q(L T^k) ⊆ rowspace_Q(L) for all k. When this holds, the future observations factor through L as linear maps on its image.

The minimum number of independent additional *rational scalar linear measurements* of the initial state needed to determine L at all these times equals

    rank_Q([L; LT; ...; LT^h]) − rank_Q(L).

Proof. If each row of LT^k lies in the row space of L, the linear factorization is explicit. Conversely if kernel inclusion fails, choose a rational d in ker L with LT^k d nonzero for some k. Multiply by a common denominator to make d integral. Choose an integer vector z with all components larger than |d_i|; then z and z+d are both nonnegative integer states, yield identical L values, and have different future readings. This contradicts universal descent. Let W be the row span of the vertically stacked future observers and L. Any augmented observer whose rowspace contains W needs at least dim W−rank L new independent rows; choose a basis of a complement of rowspace L in W to attain the bound. QED.

For **several alternative operations** τ_e, evaluated separately on the same initial histogram, replace the stack of powers with [L; Lτ_e for each selected e]. It is these separate-experiment maps that the checker applies. The rank statement is about independent rational linear measurements, and does not claim a universal bit-encoding lower bound.

## Corollary 794.3 — The eight-dimensional mod-30 correlation residual is fully observable through eight toggles

For b=3,c=5 the full 2bc histogram has d=30 coordinates. The pairwise observer L has rank

    rank(L)=bc+b+c−1 = 22,

so its kernel has rank (b−1)(c−1)=8. A single cell toggle at (0,0) raises stacked observer rank to 23. The eight independent toggles at cells (i,j) with 0≤i<2, 0≤j<4 yield

    rank([L; Lτ_(i,j) for all 8 cells])=30.

Hence the eight scalar joint coordinates lost by pairwise CRT counts are both sufficient and rank-necessary **when the goal is to retain the full joint histogram under the chosen family of future local source-aware operations**. One such toggle can distinguish a hidden correlation but cannot necessarily recover all eight.

A sharper concrete witness uses PREFIX-792's parity-even histogram (one path at 000,011,101,110) and parity-odd histogram (one path at 001,010,100,111). Their initial P,Q,R are identical all-ones 2×2 tables. After τ_(0,0), the observed P'_(0,0) is 0 for the even parity histogram and 2 for the odd parity histogram. Thus L does not factor the single future localized toggle.

By contrast, any operation induced only by independent permutations of the three factor alphabets sends pairwise tables to permuted pairwise tables. Its L-after-update therefore factors exactly through L, giving a positive future-safe compression example.

## Validation, source and remaining issue

Checker: `research_notes/portable_direct/PREFIX794_R6_FUTURE_SAFE_CRT_TOGGLE_CHECK.py`.
Structured result: `research_notes/portable_direct/PREFIX794_R6_FUTURE_SAFE_CRT_TOGGLE_RESULTS.json`.
A Python 3 standard-library implementation verifies all 2025 small complete count cubes in two independent finite input families, every selected toggle's delta/reversal, reconstruction from (b−1)(c−1) deltas, 991 compatible tables of the 2×3×5 uniform-capacity instance, the parity counterexample, and ranks 22→23→30 through exact Fraction Gaussian elimination; 45,744 integer assertions are counted. Returned status: `ALL_CHECKS_PASS PREFIX794 FUTURE_SAFE_TOGGLE_CRT`. Finite checks validate the declared instances; the universal claims follow from the proofs.

Scope: positive integer complete-path CRT counts and declared finite localized operations. No native Cell/Link/Port event is thereby certified. The frozen X6 scientific input, active six-axis+time ontology, genuine temporal causal ordering, branch identity and signed source types remain available for later typed correspondence testing.

Next: acquire a **source/target-admitted** native X6 BRC path observer and exact legal event update; determine whether any joint source-conditioned swap or its typed analogue is admissible. If yes, test the rank criterion against actual declared future operations and explicitly retain the necessary joint residual coordinates; if not, derive an operation that is natively admissible without presupposing a synthetic local toggle. Study compressed transfer of the transportation fiber for repeatable finite horizons rather than assuming all pairwise reductions are safe.

# R5: exact advice libraries for finite-state coupled suffix languages

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.

## Object and exact inherited dependency

Work in the auxiliary one-dimensional integer event-index-center model with radius 2, base event gaps (3,2,2,3,(2,1)^m), m>=1, n=5+2m events, K=m+3 chosen centers. A center set is feasible if every event lies within distance 2 of a chosen event-index center; minimize the sum of nearest-center integer distances. Closure a shortens gap 0 by 1, closure b shortens gap 3 by 1. Masks t are 0,a,b,ab.

The all-m optimal-family product theorem from PR #2427, commit 669c96f388bb2d84ef297e9a2ee09a5751c97353, file research_notes/portable_direct/r5_nonisolating_pair_block_20261115/COUPLED_21_UNBOUNDED_SWITCH_THEOREM.md establishes F_t(m)=G_t x {0,1}^l with l=m-1; the optimum cost is m+4 for each mask, and the seven-event core family sizes are (5,12,9,17). Each suffix bit selects one index from a separate designated pair. Core and suffix supports are disjoint; replacement distance is exactly delta(C+H,D+J)=|C\D|+Hamming(H,J).

Introduce an ADDITIONAL shared feasibility constraint: admissible suffix words belong to an arbitrary nonempty X subseteq {0,1}^l. Its rule is the same for all four closure masks. The constrained optimum cost is still m+4, and the complete constrained optimum family is G_t x X, because the unrestricted optimal configurations containing these suffixes remain feasible and all unrestricted optima are already known.

This defines a genuinely coupled suffix-admissibility extension of the auxiliary model; it is not asserted to be induced by the unmodified integer-cover geometry. No native X6 transfer is claimed.

For r>=0 define kappa_t(X,r) to be the minimum number of OLD constrained optimal configurations in a library L such that every NEW constrained optimal configuration is at replacement distance <=r from some element of L. The quantifiers are min_L forall_new exists_old_in_L. Let Q(X) be the graph with vertex set X, joining suffixes at Hamming distance exactly 1. Let i(X) denote its number of isolated vertices.

## Theorem (all l and all nonempty X)

For every integer l>=0 and nonempty X subseteq {0,1}^l,

* kappa_0(X,0) = 5|X|.
* kappa_b(X,1) = 2|X|.
* kappa_a(X,2) = kappa_ab(X,2) = |X| + i(X).

At l=0, X={empty word}, i(X)=1 and kappa_a=kappa_ab=2. For the full cube at l>=1, i(X)=0 and the earlier formula kappa_a=kappa_ab=max(2,2^l) follows.

### Exact seven-event core certificate

Old core family, written as concatenated zero-based event indices:
G_0 = {0125,0135,0235,0245,0246}.
Distinguished old cores D_L=0135, D_R=0246.
Distinguished new cores C_*=1346, C_L=1235, C_R=1246.

All three new cores belong to G_a and G_ab. Their exact distances satisfy:
delta(C_*,G_0)=(3,2,3,3,2), in the displayed G_0 order;
(delta(C_L,D_L),delta(C_L,D_R))=(1,3);
(delta(C_R,D_L),delta(C_R,D_R))=(3,1).

For every C in G_a or G_ab, one of these conditions holds: delta(C,D_L)<=1; delta(C,D_R)<=1; or delta(C,D_L)=delta(C,D_R)=2.
Neither C_L nor C_R is an old core.

For G_b, the cores 0136 and 0146 have unique old cores within distance 1, respectively D_L and D_R. Every G_b core is within distance 1 of at least one of D_L,D_R.

This finite core certificate is checked by enumerating all 35 four-center subsets of seven events for each mask with exact integer arithmetic; see VERIFY_COUPLED_SUFFIX_REPAIR.py.

### Proof: radius-two lower bound

Fix H in X. A radius-two repair of C_*+H must use an old core D_L or D_R, each already at core distance 2, and thus MUST use suffix H itself. There must be at least one stored old configuration at each suffix, yielding |X|.

If H is isolated in Q(X), every other J in X has Hamming(H,J)>=2. Since neither C_L nor C_R is an old core, both have core distance at least 1 from any old core, and therefore cannot be repaired within radius 2 from a stored configuration with suffix J different from H. They must both be repaired inside the H fiber. The one entry required by C_*+H is D_L+H or D_R+H. By the distance pairs (1,3),(3,1), this single entry necessarily fails one of C_L+H and C_R+H. Hence every isolated suffix requires at least two stored entries. Different suffix fibers are disjoint, proving kappa_a,kappa_ab >= |X|+i(X).

### Proof: radius-two upper bound

For each nonisolated H, store exactly one old configuration: D_L+H if the Hamming weight of H is even, and D_R+H if odd. At each isolated H, store both D_L+H and D_R+H. Library size is exactly |X|+i(X).

Each nonisolated H has a neighbor J differing in one bit, so opposite parity; hence both old core choices D_L,D_R are represented at suffix distance <=1 from H. At isolated H, both occur at suffix distance zero. For a new core C with delta(C,D_L)<=1, choose the available nearby D_L; total distance <=1+1=2. The D_R case is symmetric. For a new core whose distances to both are 2, select whichever old configuration the library stores with the SAME suffix H. It has distance exactly 2. The three core classes cover all new cores for masks a and ab, proving kappa_a,kappa_ab <= |X|+i(X). Equality follows.

### Proof: b and original masks

For mask b, at each suffix H the new cores 0136 and 0146 each force respectively D_L+H and D_R+H within radius 1, using uniqueness of the old core and the zero remaining suffix-distance allowance. Hence at least two stored entries per H. Keeping both at every H covers all G_b by the finite core certificate. Thus kappa_b(X,1)=2|X|. For mask 0, a radius-zero library must contain every old optimum, exactly 5|X|. QED.

## Exact classification of minimum radius-two libraries without isolates

Suppose i(X)=0. The C_* forcing lemma means every minimum library has exactly one entry per H, using either D_L or D_R. Color H by this choice. The two special cores C_L and C_R require that the CLOSED graph-neighborhood of every H contain BOTH colors. Conversely, that two-color condition supplies nearby D_L and D_R and, with the third core class, covers every new core. Thus minimum libraries for masks a and ab are in bijection with 2-colorings of the induced Hamming-one graph Q(X) having both colors in each closed neighborhood (a 2-domatic partition). Parity coloring always gives one when there are no isolated vertices. For isolated X, the formula remains exact, with the constructive library above; no classification of alternative isolated-fiber old pairs is claimed.

## Fibonacci finite-state coupled example

For l>=1, impose no adjacent suffix ones:
X_l={H in {0,1}^l: no substring 11}.
Let N_l=|X_l|. The two-state transfer matrix [[1,1],[1,0]] on ending-bit counts gives N_0=1, N_1=2, N_l=N_(l-1)+N_(l-2)=F_(l+2) with F_0=0,F_1=1. Every H in X_l has a Hamming-one neighbor in X_l: flip any existing 1 to 0, or if H is all-zero flip one 0 to 1. Consequently i(X_l)=0 and

kappa_a(X_l,2)=kappa_ab(X_l,2)=F_(l+2),
kappa_b(X_l,1)=2F_(l+2),
kappa_0(X_l,0)=5F_(l+2).

The leading exponential base of the optimal radius-two library changes from 2 (unrestricted bits) to golden ratio phi=(1+sqrt(5))/2 under this regular-language coupling. The parity construction remains explicit.

For l=3 and X={000,111}, both suffix vertices are isolated, |X|=2, i(X)=2, hence kappa_a=kappa_ab=4. The correction term is mathematically necessary.

## Verification and boundary

The accompanying standard-library Python program recomputes all 35 seven-event candidate center sets for each mask, checks core distances, and directly tests optimal witness libraries on EVERY nonempty X at lengths l=0..3: 1+3+15+255 = 274 languages, both a and ab and the b construction. It also checks the Fibonacci-language counts/isolate status for l=1..15, with direct radius-two library coverage through l=8, and outputs an exact JSON report. Result: PASS_R5_GRAPH_COUPLED_SUFFIX_EXACT_ADVICE. Universal quantifiers come from the proofs above and the inherited full-family product theorem, not finite extrapolation. Independent scientific review remains NOT_REVIEWED.

Open problem: replace the common admissible-language restriction with a genuinely weighted finite-state suffix coupling that changes the optimum value or its optimizer factorization. Determine the minimum sufficient residual observer and whether a finite transfer-kernel or weighted-graph correction replaces |X|+i(X).

Source provenance:
- Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
- Product lemma: 669c96f388bb2d84ef297e9a2ee09a5751c97353.
- Core data and previous all-m advice formula: 83530809d4a6105fa8c11c520f920815ada7b206, research_notes/portable_direct/r5_exact_advice_library_20261115/EXACT_RADIUS_TWO_REPAIR_ADVICE_THEOREM.md.
- No external-literature claim. Exact integer arithmetic, graph parity and a two-state transfer matrix only.

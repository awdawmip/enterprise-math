# R5: blind recourse grows linearly while adaptive recourse stays constant

Date: 2026-11-15. Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Derived model: auxiliary one-dimensional integer indexed-center observer, radius 2, **not** a native six-dimensional X6 claim.

## Exact model and inherited structural lemma

For integer `m >= 1`, start with event gaps `(3,2,2,3,(2,1)^m)`, `n=5+2m` events and `K=3+m` distinct centers selected from event indices. A center configuration covers each event within integer distance 2; among feasible configurations minimize total nearest-center distance. Closure masks `t=0,a,b,ab` shorten the zero-based gaps 0 and/or 3 from 3 to 2. All four optimal costs equal `m+4`.

The previously proved full-family product lemma (R5 PR #2427, immutable input `669c96f388bb2d84ef297e9a2ee09a5751c97353`, file `research_notes/portable_direct/r5_nonisolating_pair_block_20261115/COUPLED_21_UNBOUNDED_SWITCH_THEOREM.md`) says

`F_t(m) = {C union H: C in G_t, H in {0,1}^{m-1}}`

where each suffix bit selects exactly one distinct index from a designated event pair and core/suffix supports are disjoint. The core families `G_0,G_a,G_b,G_ab` have sizes `5,12,9,17`. In this product representation the equal-cardinality replacement distance is additive:

`delta(C union H, D union J) = |C\D| + Hamming(H,J)`.

This inherited full-family product lemma is a load-bearing input; the present results are unconditional given the lemma and the declared auxiliary model.

## Theorem A: exact quantifier-order separation for every m

Let `A_t(m)=max_{S in F_t(m)} min_{T in F_0(m)} delta(S,T)` be repair *after* the new optimum is known, and let `B_t(m)=min_{T in F_0(m)} max_{S in F_t(m)} delta(S,T)` be the cost of precommitting to one old optimum before learning which new optimum appears.

For all integers `m >= 1`, the exact values are

| closure t | adaptive A_t(m) | one precommitted old optimizer B_t(m) |
|---|---:|---:|
| 0 | 0 | m+1 |
| a | 2 | m+2 |
| b | 1 | m+1 |
| ab | 2 | m+2 |

For any `t in {a,b,ab}`, the exact adaptivity advantage is `B_t(m)-A_t(m)=m`.

**Proof.** Put `l=m-1`. For any new `C,H`, the old family contains `D,H` for every old core `D in G_0`; choosing identical suffix minimizes the nonnegative suffix distance. Consequently `A_t(m)=A_t(1)`. For a *fixed* old pair `D,J`, the new family includes every new core `C in G_t` and all suffix words `H in {0,1}^l`, including the bitwise complement of `J`. Thus
`max_{C,H} delta(C union H,D union J) = l + max_{C in G_t}|C\D|`.
Minimize over `D in G_0` to obtain `B_t(m)=l+B_t(1)`. Complete seven-event core enumeration gives `A_t(1)=(0,2,1,2)` and `B_t(1)=(2,3,2,3)`; explicit exact input/verification is in `VERIFY_R5_BLIND_RECOURSE.py`. Substitute. QED.

The additional reverse-order quantity `min_{S in F_t} max_{T in F_0} delta(S,T)` also grows as `m+1` for all four masks; this is a different quantifier order.

## Theorem B: exponentially many precomputed old configurations are required for constant-radius repair

A nonadaptive **library** is a precommitted subset `L subseteq F_0(m)`; after a new optimal set `S` is observed, one may choose a matching old configuration from `L`. Define

`kappa_t(m,r) = min {|L|: every S in F_t(m) has some T in L with delta(S,T)<=r}`.

For every integer radius `r >= 0`, every nonempty closure family `F_t(m)`, and `l=m-1`,

`kappa_t(m,r) >= ceil(2^l / V(l,r))`, where `V(l,r)=sum_{j=0}^{min(l,r)} binom(l,j)`.

**Proof.** Fix any one new core `C in G_t` and vary its entire `2^l`-element suffix fiber. A fixed library element `D,J` can repair `C,H` only when `Hamming(H,J) <= r-|C\D| <= r`. This Hamming ball contains at most `V(l,r)` suffix words. Covering all `2^l` new suffixes requires the stated number of library elements. This uses no independence assumption on which library centers are selected. QED.

In particular, preserving the adaptive worst repair radius `r=2` for `t=a,ab` requires at least `ceil(2^(m-1)/(1+(m-1)+binom(m-1,2)))` precommitted old optima for `m>=3`. Radius `r=1` for `t=b` requires at least `ceil(2^(m-1)/m)` entries.

### Stronger exact b-closure theorem

In fact `kappa_b(m,1) = 2^m` for every integer `m >= 1`.

Write the seven-event old core family as
`G_0={0125,0135,0235,0245,0246}` (four digits are distinct zero-based event indices). The b-only new core contains `C_1=0136` and `C_2=0146`. The **only** old cores at distance <=1 from `C_1` and `C_2` respectively are `D_1=0135` and `D_2=0246`. Therefore, for *each* suffix word `H`, a library attaining radius 1 must contain both `D_1 union H` and `D_2 union H`, since any suffix mismatch would add at least one to the already unit core distance. This forces `2*2^l=2^m` entries. Conversely, direct inspection of all nine new b-core sets verifies that each lies at core distance <=1 from at least one of `D_1,D_2`. Taking both core choices for every suffix yields the matching library of exactly `2^m` entries. QED.

This strengthens the generic Hamming-ball bound by using the actual irreducible core observer.

## Exhaustive finite verification and evidence

`VERIFY_R5_BLIND_RECOURSE.py` independently enumerates every `K`-subset of `n` event indices for each closure mask and `m=1..6`, applies exact radius-2 feasibility and integer total-cost optimization, and evaluates all stated min/max quantifiers. It asserts the full-family counts `(5,12,9,17)*2^(m-1)`, core unique nearest-old witnesses for b, and the all-m transfer identities on that finite window. Outcome: `PASS_R5_BLIND_RECOURSE`.

`VERIFY_R5_RECOURSE_LIBRARY.py` exhaustively tests **every library subset at each smaller cardinality** until first feasible for `m=1..3`. Minimal library sizes at the adaptive radii `(r_0,r_a,r_b,r_ab)=(0,2,1,2)` are:

| m | kappa_0(m,0) | kappa_a(m,2) | kappa_b(m,1) | kappa_ab(m,2) |
|---:|---:|---:|---:|---:|
| 1 | 5 | 2 | 2 | 2 |
| 2 | 10 | 2 | 4 | 2 |
| 3 | 20 | 4 | 8 | 4 |

Outcome: `PASS_EXACT_R5_RECOURSE_LIBRARY`. These are exact finite computations; no formula for the a/ab library sizes outside these three m is asserted.

Both scripts use Python standard-library integer arithmetic, no floating point, and save their exact result JSON. The unbounded theorems are human proofs using the previously saved product decomposition and the explicitly enumerated constant-size core, not extrapolations from m<=6.

## Observer meaning and next problem

The quotient that forgets suffix choice retains the adaptive nearest-old repair distance, but is not sound for the **blind precommitment**, full pairwise distance, or finite-library observables. This is a concrete residual-fidelity boundary: a representation can be exact for one quantifier order and incomplete for another.

Next: derive exact or sharp asymptotic `kappa_a(m,2)` and `kappa_ab(m,2)` using the labeled core-to-core distance matrix and covering codes of the suffix Hamming cube. An alternative is a finite-state transfer kernel for coupled non-product suffixes, retaining the provenance of branch choices. No P000/native X6 promotion, formal Task/CLAIM/Result, or independent review is claimed.

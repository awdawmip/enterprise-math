# X6 triadic interaction V18: pair-shadow no-go, 5D pure-triadic sector and canonical trade projector

Status: `FREE_RESEARCH / EXACT INCIDENCE-BRC DERIVATION + FINITE CHECK / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_SIGNED_TRIADIC_DECOMPOSITION_BRC_V2_20260906.md`;
- current BRC observer/provenance discipline;
- `T3_TYPED_INCIDENCE_CIRCUIT` applicability to incidence defects.
Checker: `experiments/x6_triadic_interaction_defect_v18_20260906/check_triadic_interaction_defect.py`.

## 1. Question

V2 proves that weights factorized over individual signed axes cannot distinguish two triadic decomposition routes with the same macro force counts.

The next possible simplification is pair interaction:

> if a law retains every pairwise co-occurrence count between the six native axes, is that enough to reconstruct the triad decomposition or to assign a route-sensitive weight?

The answer is still no. The lost sector is exactly five-dimensional over Q, has a canonical S6-symmetric defect projector, and already appears in the smallest nontrivial four-event trades.

## 2. Pair-shadow incidence map

Let

`T = { S subset {1,...,6} : |S|=3 }`, `|T|=20`,

and

`E = { e subset {1,...,6} : |e|=2 }`, `|E|=15`.

A triad-type count vector is

`n in Z^20`

(or `N_0^20` for an actual unordered decomposition).

Define the pair-shadow map

`P:Z^20 -> Z^15`

by

`(Pn)_e = sum_{S superset e} n_S`.

So `(Pn)_{ij}` counts how many triad events contain the axis pair `{i,j}`.

The matrix entries are simply

`P[e,S]=1 iff e subset S`.

Every triad contributes exactly three pair incidences.

## 3. Rank theorem: pair data loses exactly five rational degrees

The row Gram matrix `G=P P^T` has:

- diagonal entry `4`, because a fixed pair extends to a triple in four ways;
- off-diagonal entry `1` when two pairs share one axis;
- off-diagonal entry `0` when two pairs are disjoint.

Thus `G=4I+A_L`, where `A_L` is the adjacency matrix of the line graph of `K6`.

Exact finite diagonalization gives positive eigenvalues

`12` with multiplicity 1,

`6` with multiplicity 5,

`2` with multiplicity 9.

Hence

`rank(P)=15`.

Therefore

`K_pair := ker(P) subset Q^20`

has dimension

`20-15=5`.

This is the exact **pure triadic route sector invisible to all pair shadows**.

No continuum or carrier geometry is used; this is finite incidence algebra on the 20 admitted three-axis types.

## 4. Fifteen canonical 4<->4 trades indexed by perfect matchings

A perfect matching `M` of the six axes partitions them into three disjoint pairs:

`M={{a0,b0},{a1,b1},{a2,b2}}`.

There are exactly 15 such perfect matchings.

For `epsilon=(epsilon0,epsilon1,epsilon2) in {0,1}^3`, define the transversal triple

`S_epsilon={ choose a_r if epsilon_r=0, choose b_r if epsilon_r=1 : r=0,1,2 }`.

Split the eight transversals by parity:

`T_M^+={S_epsilon : epsilon0+epsilon1+epsilon2 even}`,

`T_M^-={S_epsilon : epsilon0+epsilon1+epsilon2 odd}`.

Each side contains four triads.

Every pair joining two different matching blocks appears exactly once on the `+` side and exactly once on the `-` side; matching edges themselves appear on neither side.

Therefore the signed trade vector

`v_M = sum_{S in T_M^+} e_S - sum_{S in T_M^-} e_S`

satisfies

`P v_M=0`.

So each perfect matching gives an exact 4-triad versus 4-triad pair-shadow collision.

Example for matching `{{0,5},{1,4},{2,3}}`:

one side can be written

`{012,034,135,245}`

and the other

`{013,024,125,345}`.

Both have macro axis degree

`D=(2,2,2,2,2,2)`

and exactly the same pair co-occurrence counts, but they are different triad decompositions.

## 5. Minimality and complete m=4 collision classification

Exhaustive finite enumeration of unordered triad multisets gives:

- event count `m=1`: no pair-shadow collision;
- `m=2`: no collision;
- `m=3`: no collision;
- `m=4`: first collisions occur.

At `m=4` there are exactly

`15`

ambiguous pair-shadow fibers, each of cardinality exactly two.

They are precisely the fifteen perfect-matching trades above.

Equivalently, every minimal ambiguous shadow is the edge set of `K6` with one perfect matching removed: 12 pair incidences, each occurring once.

Thus the smallest pairwise observer failure is completely classified.

This is a finite exact theorem; no asymptotic claim is involved.

## 6. The fifteen minimal trades generate the full integer defect lattice

The integer kernel

`ker_Z(P)={z in Z^20 : Pz=0}`

has rank five.

Exact integer elimination gives a saturated five-coordinate kernel section. Relative to it, five of the perfect-matching trade vectors form a `5x5` matrix of determinant `-1`.

Therefore those five trades form a Z-basis of `ker_Z(P)`.

Consequently all fifteen perfect-matching trades generate the entire integer pair-shadow defect lattice:

`ker_Z(P)=span_Z{v_M : M perfect matching}`.

Interpretation boundary:

this is an algebraic lattice-generation statement. It does not assert that any two nonnegative decompositions in one fiber can always be connected by a sequence of elementary trades while staying nonnegative at every intermediate step; that Markov-connectivity question is separate.

This is the natural point of contact with the existing typed incidence-circuit calculus T3.

## 7. Canonical S6-symmetric tight-frame projector

Every `v_M` has squared Euclidean coefficient norm

`||v_M||^2=8`.

Define the symmetric operator on `R^20`

`F = sum_M v_M v_M^T`

over all 15 perfect matchings.

Exact integer multiplication gives

`F^2=24 F`,

`rank(F)=5`,

and `im(F)=ker(P)`.

Hence

`Pi_tri := F/24`

is the orthogonal projector onto the five-dimensional pure-triadic sector `K_pair`.

Equivalently the fifteen trade vectors form a `24`-tight frame for `K_pair`.

This projector is canonical under S6: relabeling axes merely permutes the perfect matchings and sends trade lines to trade lines, leaving `F` unchanged.

So no arbitrary choice of five kernel coordinates is required for the symmetric defect readout.

## 8. Pair-factorized log weights and the exact triadic defect norm

Let `theta_S` be an additive/log weight attached to each triad type.

A purely pair-factorized additive law has

`theta_S = sum_{e subset S, |e|=2} lambda_e`,

or in matrix form

`theta=P^T lambda`.

Because `im(P^T)=ker(P)^perp`, the following are equivalent:

1. `theta` is pair-factorizable over real pair potentials;
2. `Pi_tri theta=0`;
3. `v_M dot theta=0` for all fifteen perfect matchings.

Define the algebraic triadic interaction defect

`D3(theta)=||Pi_tri theta||^2`.

The tight-frame identity gives the exact symmetric formula

`D3(theta) = (1/24) sum_M (v_M dot theta)^2`.

Thus `D3>=0` and

`D3=0 iff theta is pair-factorizable`.

`D3` is an algebraic defect norm. It is **not** automatically a physical energy.

## 9. Multiplicative positive weights

For positive weights `w_S`, define the perfect-matching trade ratio

`H_M(w)= product_{S in T_M^+} w_S / product_{S in T_M^-} w_S`.

If `w_S` factorizes over positive real pair weights,

`w_S=product_{e subset S} q_e`,

then every pair exponent cancels across the trade and

`H_M(w)=1`

for all M.

Conversely, over positive real numbers, if all fifteen trade ratios equal one then `log w` has zero trade defect and therefore lies in `im(P^T)`, so a positive real pair factorization exists.

For positive rational weights, a further arithmetic/integrality obstruction may remain even when all `H_M=1`; that is isolated in the next stage rather than hidden inside this real/log theorem.

## 10. BRC consequence: pairwise interaction laws cannot universally select routes

Any full decomposition weight built only from pair factors depends on the decomposition through `Pn` alone.

Therefore two branches separated by one of the 4<->4 trades receive exactly the same pair-factorized weight.

So:

`PAIRWISE INTERACTION WEIGHT + SAME MACRO INPUT`

cannot universally resolve triadic decomposition provenance.

The first exact counterexamples occur at four atomic events, and the entire invisible defect lattice is generated by those minimal trades.

A route-sensitive law must retain at least some component in the five-dimensional pure-triadic sector, use triad-type interactions directly, retain richer event/path provenance, or introduce another relation outside pair shadow.

## 11. Current frontier

Closed here:

- exact pair-shadow rank 15 and five-dimensional pure triadic kernel;
- complete minimal `m=4` collision classification;
- 15 perfect-matching 4<->4 trades;
- integer-kernel generation by those trades;
- canonical `24`-tight S6-symmetric projector;
- exact pair-factorization defect norm;
- pairwise route-selection no-go.

Next arithmetic refinement:

for **positive rational** triad weights, classify when zero trade defect still fails to admit rational pair factors because pair exponents require roots. This becomes an exact prime-valuation/SNF obstruction rather than another continuous interaction degree.

No Foundation promotion, physical-energy interpretation or external novelty claim is made.

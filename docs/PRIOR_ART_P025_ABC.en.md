# P025 ABC Radical-Support / Witness-Space Prior-Art Boundary

Status: `ACTIVE PRIOR-ART MAP / NONCANONICAL`  
Verified: 2026-08-09

## 1. Mason–Stothers and the Wronskian route

Baek and Lee's Lean 4 formalization exposes the classical short proof of Mason–Stothers particularly clearly: `f/rad(f)` divides the derivative; `a+b+c=0` makes the three Wronskians a common witness; the product of the three multiplicity residuals therefore divides that witness; and a Wronskian degree-capacity bound yields control by radical degree [SRC-BAEK-LEE-2024-MASON-LEAN].

P025 may reinterpret this chain as

`residual -> common witness -> witness capacity -> support bound`,

but derivatives, radicals, Wronskians, Mason–Stothers, and their formalizations are not Enterprise Math discoveries.

## 2. Pasten: relation-conditioned arithmetic derivatives on integers

Pasten directly studies the integer derivative bridge: arithmetic derivations satisfy a Leibniz rule and are constrained for a selected relation `a+b=c`; Geometry of Numbers supplies controlled-size derivations, and sufficiently small derivations are linked precisely to the abc conjecture [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES].

P025 therefore cannot claim as novel that:

- abc should admit an integer derivative analogue;
- a derivative should simultaneously interact with multiplication and a selected `a+b=c` relation;
- an integer Wronskian can absorb `n/rad(n)`-type multiplicity residual;
- abc can be reframed as the search for sufficiently small arithmetic derivatives.

The full-text audit strengthens this boundary further.

### 2.1 Pasten already proves the full residual-product divisibility used in P025 Supplement 04

In the proof of Pasten's arithmetic Wronskian inequality, he explicitly shows that

`a/rad(a)`, `b/rad(b)`, and `c/rad(c)`

all divide the same nonzero Wronskian and then uses pairwise coprimality to conclude that their product divides that Wronskian [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES].

Therefore the statement recorded in P025 Supplement 04 as `M | W`, with

`M=(a/rad(a))(b/rad(b))(c/rad(c))`,

is **ADOPTED PRIOR ART / REINTERPRETATION**, not a new P025 theorem. The normalized project coordinate

`eta=|W|/M`

may still be useful as a precision diagnostic, but its integrality rests directly on Pasten's proved divisibility.

### 2.2 Valuation-exponent arithmetic is also explicit prior art

Pasten's lattice argument explicitly uses the prime-adic valuation exponents `v_p(abc)` inside derivative-coordinate divisibility/size estimates; in particular the proof exploits divisibility involving `v_p(abc)` times derivative coordinates to force norm lower bounds [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES].

Accordingly, P025 must not claim as new the general observation that prime factors or sizes of valuation exponents can affect arithmetic-derivative witnesses.

What remains under investigation is narrower: the exact normalization of those data into the cross-minor gcd `eta_min`, the prime-local obstruction spectrum attached to that normalized quotient, and their task-relative precision interpretation. These remain `NOVELTY_UNVERIFIED`.

### 2.3 What the focused audit did not find

The focused read/search of Pasten's paper did not find a formulation of:

- `eta_min` as the normalized positive generator of the Wronskian image;
- `eta_min = content(alpha_hat ∧ beta_raw)/M`;
- the closed cross-support formula `gcd R e_p e_q/(g p q)`;
- the prime-local absorption-obstruction spectrum;
- the `mu / eta_min / nu / Pareto frontier` certificate-precision decomposition.

This absence is **not evidence of originality**. These objects remain `NOVELTY_UNVERIFIED` until a broader literature audit is completed.

## 3. Exceptional-set route

Bernert, Browning, Lichtman, and Teräväinen obtain a power-saving count for abc-exceptional triples satisfying `rad(abc)<c^(1-epsilon)` [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]. Runbo Li subsequently obtains the stronger exponent `O(X^(56/85+epsilon))` [SRC-LI-2025-ABC-EXCEPTIONAL].

Thus the fact that bad states can be quantitatively sparse is prior number theory. P025's possible contribution is only the quotient/collapse reinterpretation: whether scale-dependent exceptional incidence should become a reusable semantic level between exact safety and unrestricted failure.

## 4. Derivation, lattice, and optimization generalizations have broad prior art

Kikteva studies an ABC-type generalization for locally nilpotent derivations [SRC-KIKTEVA-2023-ABC-DERIVATION]. Merely replacing the ordinary derivative in Mason–Stothers by a more abstract derivation is therefore not a valid P025 novelty boundary.

Likewise, Smith normal form, determinantal divisors, exterior/Pluecker coordinates, Bezout and integer syzygies, Dickson/Pareto antichains, affine lattice optimization, closest-vector language, and linear Diophantine optimization are mature mathematics. Their use inside P025 is tooling, not a priority claim.

## 5. Numerical-semigroup / Apéry / factorization-length boundary

Supplements 16–17 transport signed block-access into a numerical-semigroup defect problem. The surrounding mathematics is already substantial prior art and must remain outside P025 novelty claims.

Chapman, Dugan, Gaskari, Lycan, Mendoza De La Cruz, O'Neill, and Ponomarenko study generalized `p`-lengths of factorizations for numerical semigroups, explicitly including `p=infinity`, and obtain asymptotic/eventual structure using Apéry-set methods [SRC-CHAPMAN-ETAL-2024-P-LENGTHS]. Therefore P025 does **not** claim as new:

- `L_infinity` factorization length;
- Apéry-set residue compression;
- eventual quasipolynomial / affine-periodic behavior of extremal numerical-semigroup factorization invariants.

Garcia, Omar, O'Neill, and Yih study factorization statistics for a **specified list of generators that need not be minimal** [SRC-GARCIA-OMAR-ONEILL-YIH-2019-FACTOR-LENGTH-II]. This is especially relevant to P025 because distinct prime-labelled certificate coordinates may carry equal or semigroup-redundant coefficient values. Accordingly, P025 also does not claim as novel the general principle that factorization geometry/statistics can depend on the chosen labelled/nonminimal generator list rather than only on the generated monoid.

What Supplements 16–17 currently retain as `NOVELTY_UNVERIFIED` is narrower:

- the exact change of variables `y=r*1-x` taking signed `L_infinity` certificate access into a bounded nonnegative semigroup-defect problem;
- the use of `ceil(L_j/2)` as the task-complete tail-certification coordinate induced by that signed transform;
- the finite `tail signature + exception table` interface as an exact representation of the entire nonnegative certificate-access response;
- the integration of these objects with P023 task-relative precision rather than a claim to new numerical-semigroup theory.

Focused search not finding the same packaged interface is not evidence of priority.

## 6. Current project-specific candidates

After the stronger prior-art audit, P025 provisionally keeps only the following **combined interfaces / normalized diagnostics** as `NOVELTY_UNVERIFIED`:

1. express radical-forgotten multiplicity as an explicit finite/integer residual while preserving its relationship to future certificate languages;
2. normalize Pasten's Wronskian residual divisibility into `eta=|W|/M` and study the exact image floor `eta_min`;
3. encode that floor by a scaled exterior/determinantal signature and then by closed support/valuation and block-content formulas;
4. resolve `eta_min` into prime-local obstruction coordinates, while explicitly treating valuation-exponent arithmetic itself as Pasten prior art;
5. separate certificate existence radius `mu`, arithmetic floor `eta_min`, floor-access radius `nu`, and the full norm/absorption Pareto frontier;
6. quantify the gap between a valid constructive Bezout certificate and the minimum task-relative access precision;
7. exploit special abc row structure to reduce access to affine/Diophantine/blockwise preimage problems;
8. transport high-dimensional block access into an Apéry-controlled signed defect problem, while treating Apéry and `L_infinity` factorization mathematics as prior art;
9. compress the resulting access state according to the declared future language: image content, candidate Apéry branches, certified tail, or finite exact response;
10. reuse P023 query-generated precision and A3/A4 antichain semantics rather than duplicate generic mother theorems;
11. keep scale-dependent exceptional incidence as a separate possible semantic axis rather than fold it into exact witness control.

A dedicated broad priority search for an equivalent general architecture has not yet been completed. No “first”, “original”, or similar priority claim is permitted.

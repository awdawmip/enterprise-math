# PREFIX-1006 — Exact integer transfer for all eleven marked BRC-collision orbits

Date: 2026-11-22 (+08). Status: AUTHOR_COMBINATORIAL_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. This note is portable scientific evidence, not a formal Result or mathematical Review.

## Scientific input and observation

Preserve frozen P000 V5 at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` and the ACTIVE X6 six-axis Cell-torsor semantics. Inherited Stage46 typed Z2 BRC signed port kernel is `C(h,j)=1/6−[h=j]`; initial incoming-neighbour port `−e1`. The undirected Link `{anchor,anchor+e1}` is blocked by absorption in both directions. Observation: first interior grade (one negative native step), final Cell and last incoming-neighbour port jointly, with signed branch accumulation in each fibre before squaring and adding probabilities.

Imported [PREFIX-1005 exact BRC observer theorem](https://github.com/awdawmip/enterprise-math/blob/1e5cb76e806d3da352ba68f9e160474095950c93/research_notes/portable_direct/2026-11-22_r6_prefix1005_marked_collision_orbit_reduction.md): for all n>=5, `36^n M^L_(n,1)=sum_(alpha=0)^10 K_alpha(n) H_(n-4)(delta_alpha)` with the eleven specified orbit representatives and quadratic integer coefficients. The present work optimizes exact post-observer collision evaluation; no intermediate path, phase, port or Link state is identified.

## Theorem 1006.1 — exact imbalance transfer for marked collisions

For arbitrary d>=1, delta in Z^d with sum(delta)=0, and m>=0, write

`H_m^(d)(delta)=sum_{a_1+...+a_d=m} Mult(m;a) Mult(m;a+delta)`,

where invalid multinomials are zero. Let `D_s=sum_(i=1)^s delta_i`, and for `s=1,...,d`

`T_s(r)=sum_{a_1+...+a_s=r} [r! (r+D_s)! / product_i(a_i! (a_i+delta_i)!)]`,

with invalid negative factorial arguments treated as zero; `T_s(r)=0` if `r+D_s<0`. Then

```text
T_1(r) = 1 if r+delta_1>=0, otherwise 0

T_s(r) = sum_(a=0)^r binom(r,a) binom(r+D_s,a+delta_s) T_(s-1)(r-a),   s>=2

H_m^(d)(delta) = T_d(m)     (because D_d=0).
```

Out-of-range binomial coefficients are zero. Every value is a nonnegative integer.

**Proof.** Count ordered pairs of words on the first s labels, with lengths r and r+D_s and per-label counts differing by delta_i. When the final label occurs a times in the first word, it occurs a+delta_s times in the second. Choosing these positions contributes the two displayed binomial coefficients. The remaining word-pair counts use the first s−1 labels with lengths r−a and r−a+D_(s−1), exactly T_(s−1)(r−a). These are disjoint exhaustive cases. For s=1 the admissible pair is unique. Induction establishes the recurrence, nonnegative integrality and the terminal identity. QED.

To evaluate a fixed delta through r=m, each of d rows requires O(m²) integer summands with one previous and one current length-(m+1) row. Thus **O(d m²) arithmetic operations and O(m) stored integers** per delta, before the cost of big-integer binomial construction/multiplication. In comparison, direct enumeration inspects `binom(m+d−1,d−1)` candidate compositions, which grows as m^5 for d=6. Eleven PREFIX-1005 orbit representatives are evaluated independently in this exact scheme.

## Theorem 1006.2 — root-lattice transfer and an orbit-closure obstruction

Let S=sum_i z_i and U=sum_i z_i^(-1) in the formal Laurent ring of X6 *chart-displacement* variables. As `H_m(delta)=CT[z^delta S^m U^m]`, coefficient extraction from `SU=sum_(i,j) z_i/z_j` proves

```text
H_(m+1)(delta) = sum_(i=1)^6 sum_(j=1)^6 H_m(delta+e_i−e_j).
```

The eleven PREFIX-1005 orbits are not closed under this elementary transfer. Starting at `delta=(-3,0,0,0,0,3)`, its `i=6,j=1` summand is `H_m((-4,0,0,0,0,4))`, a strictly positive term for m>=4 that is outside the eleven orbit types. Therefore a naive eleven-coordinate nearest-neighbour recursion is not justified. This does *not* rule out a different, eliminated holonomic recurrence; Theorem 1006.1 provides a proven exact evaluator in the meantime.

## Theorem 1006.3 — exact nonnegative collision envelope

For every m>=0 and zero-sum delta,

`0 <= H_m(delta) <= H_m(0)=A_6(m)`,

strictly when delta is nonzero. Extend `f(a)=Mult(m;a)` by zero off the finite simplex. Then H_m(delta) is the scalar product of f with its translate by delta. Cauchy–Schwarz and equal norms prove the weak bound; equality for nonzero delta would require a finite, nonzero, nonnegative f to be proportional to its nontrivial translate, impossible. This bounds the final collision observer only, not intermediate signed BRC amplitudes.

## Actual exact verification

The accompanying Python-3 checker uses integer binomials and the typed PREFIX-1005 final-observer coefficients. Checked: all eleven orbit representatives against independent direct composition sums for m=0..8 (99 exact comparisons); the earlier first-orbit identity `30H_m(e_i−e_j)=A_6(m+1)−6A_6(m)` for m=0..11; root-lattice transfer at m=0..5 for delta=(-2,0,0,0,0,2); and the complete eleven-orbit Link-masked first-interior mass at n=5,6,7,8,9,10,12,14,16,20 against the PREFIX-1005 prior certificate (all equal). Fresh exact n=30,50,100 and the eleven m=100 marked-collision values are provided in the result certificate.

New exact example:
`M^L_(30,1) = 13933171984643229314612138251752792090355 / 169700270766282144060148445395050707866877952`.

**Execution boundary:** The code is a new exact *post-BRC combinatorial evaluation* of a pre-established typed Z2 BRC joint-port observer. It is not a fresh native Stage46 dynamical run or heartbeat calibration. The proof is author-checked, not independently reviewed.

## Next

Seek an autonomous shorter holonomic recurrence for these eleven marked sequences by sound eliminations, rather than assuming the orbit list is invariant under the SU root-lattice transfer. Separately analyze two-negative-step (k=2) first-five-step blocked-Link prefixes, keeping complete Z2 branch/Cell/port history before any final readout. The mother problem `B_fix,odd(32) in {19,20}` remains open.

Historical R6 provenance: `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`; no current-session authenticated researcher authority, CLAIM, Activity mutation or Result/Review promotion is asserted.

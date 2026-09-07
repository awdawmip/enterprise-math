# BRC Activation Frontier — Coppersmith Cell Benchmark

Status: `RESEARCH FRONTIER / EXTERNAL-BASELINE TIGHTENING + EXACT SCALE CONSEQUENCES / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_PRECISION_DEFICIT_WINDOW_WALL_FRONTIER_20260908.md`
Source snapshot before write: `main@bc1960dd56c73c5fce63ba72368c5c7ac062f45d`

## 0. Correction/tightening of the benchmark

The parent precision-deficit note correctly derived the benchmark for a **square-root block-product backend**: if an unresolved factor window has width `H`, generic BSGS/product evaluation gives roughly `sqrt(H)` scale, so matching `N^(1/5)` would require about `N^(-1/10)` relative magnitude localization.

That is not the strongest known deterministic interval-search baseline.

Harvey–Hittmeir's deterministic r-power divisor interval method (Research in Number Theory 8 (2022), Article 94), specialized to ordinary factors `r=1`, gives a sharper search cost for a prescribed interval near the balanced factor scale. This note updates the active comparison baseline without invalidating the parent's explicitly backend-specific calculation.

---

## 1. External interval theorem specialized to balanced semiprimes

Their Proposition 3.2 searches all divisors `p` in an interval

`T <= p <= T'`

in time

`O(((T'-T)/T * N^(theta(1-theta)) + 1) * polylog(N))`,

where

`theta = log(T)/log(N)`

for `r=1`.

For balanced semiprimes and an interval centered at factor scale,

`T=Theta(sqrt(N))`,

so

`theta=1/2+o(1)`

and

`N^(theta(1-theta))=N^(1/4+o(1))`.

Writing interval width `H=T'-T`, the cost becomes

`O((H/N^(1/4) + 1) * polylog(N))`

throughout the balanced central range, up to fixed-band/subpolynomial effects.

This is strictly stronger than the square-root-in-H block baseline once `H=o(sqrt(N))`.

---

## 2. Coppersmith-cell interpretation

The same interval theorem can be viewed as partitioning the balanced factor line into cells of width about

`N^(1/4)`.

Each such cell can be searched in polynomial time by the underlying Coppersmith/LLL small-root machinery. A wider interval of width `H` costs essentially the number of cells needed to cover it:

`CELL_COUNT(H) = Theta(H/N^(1/4))`

up to polylogarithmic factors.

This is a natural BRC observer decomposition:

- population: the unresolved factor interval;
- branches: Coppersmith-size cells;
- per-cell observer: whether that cell contains a divisor of N;
- recoalescence goal: find the unique positive cell / factor without visiting all cells.

Thus the strongest current target is no longer merely compressing integer products inside one block. It is **collapsing many factor-location cells while retaining enough cell provenance to identify a positive branch**.

---

## 3. Revised precision threshold for exponent one fifth

With the stronger interval baseline, matching an `N^(1/5)` power scale requires

`H/N^(1/4) <= N^(1/5)`.

Therefore

`H <= N^(9/20)`.

Since `p=Theta(N^(1/2))`, this is

`H/p <= N^(-1/20)`.

On a fixed factor-ratio band, the parent relation `H=Theta(p*delta)` converts this to

`delta <= N^(-1/20)`.

Thus a magnitude preconditioner need only remove about a factor `N^(1/20)` from the balanced search width to bring the interval-Coppersmith backend to exponent one fifth.

For an `n`-bit modulus, `N^(1/20)` corresponds to roughly `n/20` bits of growing localization. For 895-bit RSA-270 this is about 45 bits.

This supersedes the 90-bit figure **only as the strongest external-backend comparison**. The 90-bit figure remains correct for the square-root-block backend derived in the parent note.

---

## 4. Polynomial-time cell boundary

When

`H = O(N^(1/4) / polylog(N))`

in the balanced factor region, one Coppersmith-scale interval suffices and the factor can be recovered in polynomial time under the known theorem's explicit parameter regime.

Thus there are three useful localization regimes:

1. `H=Theta(N^(1/2))`: no growing magnitude information; interval search sits at the classical `N^(1/4)` power scale;
2. `H≈N^(9/20)`: roughly the threshold where the interval backend reaches `N^(1/5)` power scale;
3. `H≈N^(1/4)`: factor location is narrow enough for one polynomial-time Coppersmith cell.

This gives the BRC program quantitative milestones instead of a vague requirement to 'learn more bits'.

---

## 5. Consequence for collision/local residues

The collision-local route currently provides only fixed-modulus information (`S^2 mod2880` for RSA-270) plus fixed construction-family congruences/prefixes. These do not imply a real interval of relative width `N^(-1/20)`.

Therefore they do not meet the ~45-bit growing-magnitude benchmark.

However a **growing modular** factor restriction could in principle play the same candidate-density role as a shrinking real interval if an exact algorithm exploits it. This must not be confused with the present fixed modulus. Any future local-orbit selector should therefore be scored by the size of the factor-candidate class it removes, not merely by the existence of a nontrivial residue identity.

The useful target is a growing information budget of order at least

`(1/20) log_2 N`

bits/classes if the goal is to change the deterministic power benchmark through preconditioning alone.

This is a heuristic information-count translation of the exact interval-width formula, not an information-theoretic lower bound.

---

## 6. Revised A/B attack split

### A. Cell-collapse constructor

Given `Theta(H/N^(1/4))` Coppersmith-searchable cells, evaluate a provenance-preserving collective observer that identifies a positive cell in sublinear-in-cell-count work, without reconstructing a factor by another method.

A simple OR over cell existence is not enough after positive detection unless the positive cell/factor can be localized without replaying all cells; branch provenance or an exact group-testing repair coordinate is required.

### B. Growing preconditioner

Derive either:

- an archimedean factor interval of width `H<=N^(9/20-o(1))`; or
- a growing modular/coset restriction that produces a comparable reduction in candidate density and has a proven factor-search backend.

Fixed prefixes, moduli and finite shadow classes are only constant-factor reductions and remain below threshold.

---

## 7. BRC observer warning: Boolean cell OR is not sufficient for localization

The previous divisor-lattice note proved that within one certified factor interval, Boolean unit/nonunit is enough **for one threshold test** because a positive gcd returns the factor directly.

If we instead split a wide range into many Coppersmith cells and collapse them all to one Boolean OR, a positive result only says that some cell contains `p`; it does not identify which cell. Future localization therefore requires either:

- labeled cell provenance;
- a logarithmic family of separating group tests whose total construction cost is genuinely sublinear;
- or an aggregate whose value algebraically decodes the positive cell/factor.

So the global multi-cell observer is stronger than the one-block Boolean lease. Collapsing provenance too early would recreate the exact information-loss mistake BRC policy forbids.

---

## 8. Stronger kill condition

A candidate no longer counts as progress merely because it beats `sqrt(H)` product work. It must be compared against the Harvey–Hittmeir interval bound in the same factor-location regime.

Kill if:

- it is asymptotically no better than `H/N^(1/4)` polynomial-time cells near `sqrt(N)`;
- its gain comes from a factor interval that was already supplied as hidden information;
- it collapses many cells to Boolean support but cannot recover cell identity without replay;
- it uses a fixed modular restriction and reports it as a growing candidate-density reduction.

Retain only a new collective cell operator or a growing N-only preconditioner whose full construction cost beats this tightened baseline.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.
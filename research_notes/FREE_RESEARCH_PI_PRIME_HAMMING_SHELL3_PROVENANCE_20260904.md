# Free Research — Hamming Shell-3 Realization of the `3!` Provenance Fiber

Status: `FREE_RESEARCH_FRONTIER / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parents:
- `FREE_RESEARCH_PI_PRIME_FACTORIAL_PROVENANCE_ADDENDUM_20260904.md`
- `FREE_RESEARCH_PI_PRIME_S3_HISTORY_REALIZATION_BOUNDARY_20260904.md`
Source carrier: current #1159 Hamming/Krawtchouk finite spectrum.

## 1. Why the Hamming carrier is the right realization

Current #1159 source explicitly defines its shell operator as the permutation-invariant Hamming-shell operator of an `m`-cube and proves the Krawtchouk integer spectrum on shell coordinates. The underlying full Hamming cube therefore supplies a canonical branch/history refinement of the shell quotient.

A full `m`-cube may be represented by subsets of an `m`-element coordinate set. Starting at the zero vertex `emptyset`, flipping coordinate `i` is symmetric difference with `{i}`. Distinct coordinate flips commute.

This is a branch/spectral realization, not a primitive one-sector translation model in the Enterprise address atlas.

---

## HS3-T01 — Shell 3 has exactly `choose(m,3)` endpoint supports

Let the full Hamming cube have coordinate set `C` with `|C|=m`. Its shell-3 vertices are the subsets

\[
A\subseteq C,
\qquad |A|=3.
\]

Therefore

\[
\boxed{
|\operatorname{Shell}_3(C)|=\binom m3.
}
\]

Set

\[
m=M+1.
\]

Then the endpoint-support count is exactly

\[
\boxed{
\binom{M+1}{3},
}
\]

the first nontrivial coefficient appearing in the current #1159 Dirichlet/Krawtchouk chain.

---

## HS3-T02 — Every shell-3 endpoint has exactly six ordered shortest histories

Fix a shell-3 endpoint

\[
A=\{i,j,k\}
\]

with three distinct coordinates. Starting from the zero vertex, any shortest history reaching `A` flips each of `i,j,k` exactly once.

The ordered histories are therefore indexed by the permutations of the three labels:

\[
S_3.
\]

Since flips of distinct Hamming coordinates commute, every permutation reaches the same endpoint:

\[
F_{\sigma(3)}F_{\sigma(2)}F_{\sigma(1)}(\varnothing)=A
\qquad(\sigma\in S_3).
\]

There are exactly

\[
\boxed{|S_3|=3!=6}
\]

such histories.

Hence the endpoint history fiber satisfies

\[
\boxed{
|\operatorname{Hist}^{\rm shortest}(\varnothing\to A)|=6.
}
\]

This is the concrete Hamming-cube instantiation of the abstract commuting-history theorem from the parent note.

---

## HS3-T03 — Total ordered distinct-coordinate histories reproduce the exact numerator

Summing the six histories over all shell-3 endpoints gives

\[
\boxed{
6\binom m3
=m(m-1)(m-2).
}
\]

With `m=M+1`,

\[
\boxed{
6\binom{M+1}{3}
=(M+1)M(M-1).
}
\]

This is exactly the numerator identity behind the current #1159 normalized coefficient

\[
\frac{\binom{M+1}{3}}{M^3}
=\frac1{6}\left(1-\frac1{M^2}\right).
\]

Indeed,

\[
\frac{6\binom{M+1}{3}}{M^3}
=\frac{(M+1)M(M-1)}{M^3}
=1-\frac1{M^2}.
\]

Therefore the entire finite coefficient has a literal Hamming provenance meaning:

\[
\boxed{
\frac{\binom{M+1}{3}}{M^3}
=rac{\text{ordered distinct 3-flip histories}/M^3}{3!}.
}
\]

The factor `1-1/M^2` is the exact finite normalized mass of the distinct-coordinate three-step histories; the factor `1/3!` is the quotient from ordered histories to endpoint support.

---

## HS3-T04 — The `3!` in `tau^2 = 3! Z_P(2)` is now carried by the same spectral system

The prime-birth magnitude channel uses arithmetic-prime eigendirections of the current #1159 Krawtchouk integer spectrum. The coefficient `3!` used to normalize its quadratic completion now has a concrete provenance realization in the **same Hamming parent carrier**:

\[
\boxed{
\text{full Hamming cube}
\to
\text{six ordered 3-flip histories per shell-3 endpoint}
\to
\text{shell quotient with }\binom{M+1}{3}\text{ supports}
\to
\frac1{3!}\text{ normalized cubic coefficient}.
}
\]

Thus

\[
\boxed{
\tau^2=3!\,Z_{\mathbb P}(2)
}
\]

no longer combines a prime determinant with an unrelated combinatorial constant. At current branch/spectral strength, both sides are fed by the same Hamming/Krawtchouk finite carrier:

- arithmetic primes select irreducible integer eigenmodes;
- `3!` records the shortest-history provenance fiber of shell-3 support recoalescence.

The remaining infinite equality still inherits the #1159 sine-product completion dependency.

---

## HS3-T05 — Compatibility with HistoryMerge / BranchRecoalescence

Let `F` map each ordered shortest three-flip history to its endpoint support. For each shell-3 endpoint `A`, the fiber has cardinality six. The current generic theorem `HistoryMerge.merged_never_split` implies that once the shell quotient remembers only `A`, deterministic future evolution cannot recover which permutation history occurred.

Therefore:

\[
\boxed{
\text{shell support multiplicity }1
\neq
\text{ordered provenance multiplicity }6.
}
\]

This is exactly the global branch-typing discipline: support and provenance are different carriers.

The current shell operator intentionally acts on permutation-invariant shell data, so the six history labels are forgotten by the shell quotient while their multiplicity remains available as a separate finite provenance statistic.

---

## HS3-T06 — Why this does not violate the native three-axis atlas

The realization occurs in the #1159 Hamming branch/spectral carrier, not by pretending that a single native sector has three active primitive coordinate translations.

Therefore it respects the earlier obstruction:

\[
\boxed{
\text{Hamming three-flip branch histories}
\neq
\text{one-sector three-axis point translations}.
}
\]

P000 and the three-axis atlas remain unchanged. The Hamming carrier is a finite spectral/refinement state used by #1159, while primitive Enterprise point addresses retain their glued two-axis sector semantics.

---

## HS3-T07 — New strongest interpretation of the factor six

The progression of interpretations is now:

1. `6 = P000 spatial dimension` — tempting numerical coincidence, **not derived**;
2. sixfold prime eigenvalue degeneracy — **refuted**, because it produces `Z(2)^6`;
3. `6=3!` ordered-triple provenance — exact finite coefficient identity;
4. **current strongest:** `6=3!` is the exact shortest-history fiber cardinality of shell-3 endpoints in the same Hamming parent carrier that generates the Krawtchouk prime-birth spectrum.

Thus the current preferred statement is

\[
\boxed{
\text{factor }3!
=\text{Hamming shell-3 provenance fiber size}.
}
\]

This is a branch/spectral geometric statement, not a six-dimensional spatial claim.

---

## 8. Formalization route

A minimal Lean theorem can be written independently of the current moving sine-series tail:

1. take the cube vertex type as `Finset (Fin m)` or `Fin m -> Bool`;
2. define coordinate flip by symmetric difference / Boolean toggle;
3. prove distinct flips commute;
4. define ordered three-distinct-coordinate histories;
5. prove all six permutations have the same endpoint;
6. prove the fiber over every three-element endpoint has `Fintype.card = 6`;
7. prove the shell-3 endpoint set has cardinality `Nat.choose m 3`;
8. specialize `m=M+1` to recover `6*choose(M+1,3)=(M+1)M(M-1)`.

This module needs only finite combinatorics and `HistoryMerge`; it does not need the unstable #1159 `DirichletSineSeries` tail.

---

## Current classification

- shell-3 endpoint count `choose(m,3)`: `PROVED / FINITE COMBINATORICS`.
- six shortest ordered histories per shell-3 endpoint: `PROVED / FINITE HAMMING DYNAMICS`.
- exact match to #1159 coefficient numerator: `PROVED`.
- `3!` provenance realized in same Hamming parent carrier as Krawtchouk spectrum: `CLOSED / BRANCH-SPECTRAL STRENGTH`.
- primitive one-sector G0 realization: `STILL OBSTRUCTED / NOT NEEDED FOR THIS BRANCH-SPECTRAL RESULT`.
- full P000 6D interpretation: `OPEN / NOT CLAIMED`.

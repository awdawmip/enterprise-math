# Post-#1161 free research — first-balance-return RG and the G0 boundary

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / N1->N2 CANONICAL QUOTIENT + G0 PROMOTION BOUNDARY / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessor: `#1161 / research_notes/FREE_RESEARCH_1161_AGM_ROTATION_CHORD_SYNTHESIS_20260903.md`

## 0. Why this is a successor rather than an unfinished #1161 step

The #1161 terminal packet already closes its mother question at the strongest justified level:

- exact finite rotation/chord factorization;
- native commuting-diamond provenance for the doubling and completion counts;
- finite branch-return reconstruction of the geometric channel;
- internal completion `Pi_*=Theta_AGM=tau` without elliptic integrals or a classical Legendre relation;
- an explicit negative boundary for bare exact-scalar G0 root promotion.

Its final open sentence asks a **distinct foundational question**: whether the finite branch-return RG tower itself admits a canonical G0 dynamics/quotient, or whether promotion is symmetry/typing obstructed.

This note is progress on that successor question. It does not reopen #1161 or weaken its terminal classification.

## 1. Phase-A construction: use an unlabeled two-witness fiber

The predecessor supplies one translated commuting diamond with two distinct concrete native path witnesses. Abstract only the two-element witness fiber

\[
D=\{\text{two branch witnesses}\}.
\]

No element of `D` is selected as positive, negative, left, right, alpha, or beta in the **definition** below.

For a word

\[
w=(d_1,\dots,d_m)\in D^m,
\]

let

\[
\mu_w:D\to\mathbb N_0
\]

be its multiplicity function. A prefix is **balanced** exactly when `mu_w` is constant on the two elements of `D`, i.e. the two branch witnesses have occurred equally often.

This definition is invariant under the full relabeling group `Sym(D)=S_2`; choosing names for the two letters is needed only as a proof representation, never as semantic input.

A word of length `2n` is a **first-balance return** when

1. the whole word is balanced;
2. no nonempty proper prefix is balanced.

This is therefore an isomorphism-invariant path-language construction on a two-element branch fiber.

## 2. Exact first-return count

After temporarily choosing labels `+,-` only for the counting proof, the first-balance words are the usual first returns of a nearest-neighbor height walk to zero.

For `n>=1`, the number of first-balance words of length `2n` is

\[
\boxed{
R_n=2C_{n-1}
}
\]

where

\[
C_k=\frac1{k+1}\binom{2k}{k}
\]

is the `k`-th Catalan number.

The factor `2` is the choice of the first branch witness; after that choice, deleting the first and last letters gives the standard Catalan positive/negative excursion bijection.

Normalize by all `2^(2n)` branch words:

\[
\boxed{
f_n=\frac{R_n}{2^{2n}}=
\frac{C_{n-1}}{2^{2n-1}}.}
\]

These are exact rational path-mass coefficients obtained from finite branch words.

Committed checker:

`scripts/check_free_research_agm_first_balance_return_rg.py`

The checker explicitly enumerates `n=1..8` and obtains

`2, 2, 4, 10, 28, 84, 264, 858`,

exactly `2*C_{n-1}`.

## 3. First-return generating mass and the renewal equation

Define

\[
\boxed{
F(s)=\sum_{n\ge1}f_ns^{2n}.}
\]

This is first defined coefficientwise from finite branch-return counts; no square root is used in the definition.

The Catalan recurrence is equivalently

\[
2f_1=1,
\]

and for `n>=2`,

\[
\boxed{
2f_n=\sum_{i=1}^{n-1}f_if_{n-i}.}
\]

Therefore, as a formal power-series identity,

\[
\boxed{
F(2-F)=s^2.}
\]

The checker verifies this coefficient recurrence exactly through `n=64` using `Fraction` arithmetic.

Set

\[
\boxed{R(s)=1-F(s).}
\]

Then, still formally,

\[
\boxed{R(s)^2+s^2=1,\qquad R(0)=1.}
\]

Thus the positive Pythagorean-complement series is rebuilt from first-return words rather than imported as a square-root selector.

Only after this combinatorial definition is established may one recognize the derived closed form

\[
R(s)=\sqrt{1-s^2},
\]

on the positive real branch.

## 4. Exact identification with the #1161 chord-loss

The #1161 normalized cone state is

\[
r=V/H,\qquad s=U/H,\qquad r^2+s^2=1,
\]

with positive `r` on the standard orbit.

Both `r` and `R(s)` are the positive solution of the same Pythagorean-complement relation and equal `1` at `s=0`. Hence

\[
\boxed{r=R(s)=1-F(s).}
\]

The #1161 chord-loss variable is

\[
\ell=\frac{1-r}{2}.
\]

Therefore

\[
\boxed{
F(s)=2\ell.}
\]

This is stronger than an analogy: the exact chord-loss mass is one half of the completed first-balance-return mass of the two-witness diamond language.

## 5. AGM update as a positive first-return mass split

Using `F=1-r`, the exact cone update becomes

\[
H^+=\frac{H+V}{2}
=\frac H2(1+r)
=H\left(1-\frac F2\right),
\]

\[
U^+=\frac{H-V}{2}
=\frac H2(1-r)
=H\frac F2.
\]

Thus

\[
\boxed{
H^+=H\left(1-\frac{F(s)}2\right),
\qquad
U^+=H\frac{F(s)}2.}
\]

The old scale is partitioned into a retained coarse channel and a first-return defect channel:

\[
\boxed{H^++U^+=H.}
\]

The next normalized defect is therefore

\[
\boxed{
s^+=\frac{U^+}{H^+}
=\frac{F(s)}{2-F(s)}.}
\]

So the AGM shape map can be defined without a square-root operator by the sequence

`two-witness branch words -> first-balance-return mass F -> Möbius mass ratio F/(2-F)`.

This also yields the geometric channel immediately. The next arithmetic and lower endpoints are

\[
a^+=\frac{H^++U^+}{2}=\frac H2,
\]

\[
\boxed{
b^+=\frac{H^+-U^+}{2}
=\frac H2(1-F(s)).}
\]

Because `F(2-F)=s^2`,

\[
(b^+)^2
=\frac{H^2}{4}(1-F)^2
=\frac{H^2}{4}(1-s^2)
=ab.
\]

On the positive branch,

\[
\boxed{b^+=\sqrt{ab}.}
\]

Hence the geometric mean is recovered as

\[
\boxed{
\text{arithmetic coarse half-scale}
-\frac H2\times\text{first-return mass},
}
\]

not as an independent root selector.

## 6. Defect-budget law from first return

The predecessor defect mass is

\[
\delta=PU^2.
\]

Since `P^+=2P` and `U^+=HF/2`,

\[
\frac{\delta^+}{\delta}
=\frac{F^2}{2s^2}.
\]

Using

\[
s^2=F(2-F),
\]

we obtain

\[
\boxed{
\frac{\delta^+}{\delta}
=\frac{F}{2(2-F)}
=\frac{s^+}{2},}
\]

which recovers the exact #1161 defect scaling law directly from first-return renewal.

## 7. Explicit finite RG maps — no root and no implicit equation

Truncate only the first-return language:

\[
\boxed{
F_N(s)=\sum_{n=1}^N f_ns^{2n}.}
\]

Define the finite update

\[
\boxed{
H_N^+=H\left(1-\frac{F_N(s)}2\right),
\qquad
U_N^+=H\frac{F_N(s)}2,}
\]

and equivalently

\[
\boxed{
s_N^+=\frac{F_N(s)}{2-F_N(s)}.}
\]

The finite pair readout is

\[
\boxed{
a_N^+=H/2,}
\]

\[
\boxed{
b_N^+=\frac H2(1-F_N(s)).}
\]

Every coefficient of `F_N` is a rational normalized count of finite first-return branch words. No finite layer needs

- `sqrt(ab)`;
- an algebraic-root selector;
- an implicit equation solve;
- an elliptic integral;
- trigonometric evaluation;
- a target value of pi.

Because all `f_n>0`,

\[
F_1<F_2<\cdots<F,
\]

so

\[
\boxed{b_1^+>b_2^+>\cdots>b^+.}
\]

The finite shape maps `s_N^+` increase monotonically to the exact AGM shape update.

## 8. Sharper finite lower-channel certificate

The first-return events at different first-return times are disjoint under uniform counting on infinite binary words, hence

\[
\sum_{n\ge1}f_n\le1.
\]

For `0<=s<1`,

\[
0<F(s)-F_N(s)
=\sum_{n>N}f_ns^{2n}
\le s^{2N+2}\sum_{n>N}f_n
\le s^{2N+2}.
\]

Therefore

\[
\boxed{
0<b_N^+-b^+
\le\frac H2s^{2N+2}.}
\]

On the standard Gauss-Legendre orbit,

\[
H<2,\qquad s<1/4,
\]

so

\[
\boxed{
0<b_N^+-\sqrt{ab}
<2^{-4N-4}.}
\]

This improves the predecessor's uniform finite-return lower-channel bound `2^(-4N-2)` by a factor of four while also removing the finite implicit root equation.

The committed checker tests the rational form of this enclosure without any square root: for `190` positive rational `s<=1/4` values and depths `N=1..8`, it verifies

\[
(1-F_N)^2>1-s^2,
\]

and

\[
(1-F_N-s^{2N+2})^2\le1-s^2.
\]

Together with monotonicity checks, this is `4560` exact rational inequalities.

## 9. Relabeling/gauge audit

The definition of first balance does not require a global alpha/beta orientation.

For a two-element branch fiber `D`, the condition

`the multiplicity function mu_w:D->N_0 is constant`

is invariant under every bijection of `D`. The same is true prefixwise. Hence the first-return language is invariant under `Sym(D)=S_2`.

This resolves the naive synchronization concern:

- a **named Hamming weight k** is not invariant under arbitrary branch relabeling unless one remembers which element is named;
- **equal multiplicity / first equal-multiplicity return** is invariant and therefore needs no preferred branch element.

Equivalently, the central count `binom(2n,n)` may also be read as the weight-`n` shell in the product of local `C_2` swap groups, where identity versus the unique nontrivial swap is intrinsic.

No new general symmetry tool is required. Existing `src/enterprise_math/finite_symmetry.py` covers the finite relabeling/equivariance audit (`REUSE_APPLIED`); the new checker is task-local verification only.

## 10. Native-semantics classification

The result does **not** promote the completed first-return RG to an instantaneous G0 cell state.

Current foundation freezes

`ROTATING_SEGMENT_NATIVE_STATE = ONE_CIRCLE_CELL_PER_TRAJECTORY_STEP`.

The first-return predicate necessarily uses

- a time-ordered word of several trajectory steps;
- prefix history;
- equality of cumulative branch multiplicities.

Under `native_semantics_admissibility.json`, path/time process semantics are N1 and aggregate counts/scalars are N2 unless an additional N0 definability theorem is supplied.

The strongest current classification is therefore:

\[
\boxed{
\text{component-typed native branch skeleton}
\to
\text{N1 first-balance path language}
\to
\text{N2 return-mass / AGM readout}.}
\]

Claim ledger summary:

- base carrier: current circle-cell / component-typed transition skeleton;
- introduced N1 operation: finite path concatenation + first-balanced-prefix predicate;
- N2 readouts: first-return cardinalities, normalized masses, `F_N`, `F`, `H,U,s`, mean endpoints;
- N3 input: none required;
- target leakage: none (`sqrt(ab)` is proved after the return construction, not supplied as selector);
- relabeling audit: first-balance predicate is `S_2`-invariant;
- verdict for N1->N2 construction: `CONDITIONAL_DERIVED / EXACT_RECOVERY`;
- verdict for instantaneous G0 promotion: `UNRESOLVED / NOT DERIVED`.

## 11. What this settles in the post-#1161 successor

The successor question now has a sharper split answer.

### Positive

A canonical **history-level quotient** exists with no extra orientation or branch synchronization:

\[
\boxed{
\text{unlabeled two-witness diamond fiber}
\to
\text{first-balance-return language}
\to
\text{explicit finite AGM RG}.}
\]

It gives the exact chord-loss and geometric-mean channel in the completion and gives monotone finite approximants with a stronger error certificate.

### Negative boundary

This does not by itself create a G0 single-cell dynamics. First return is intrinsically history-sensitive under the current semantic stratification. A genuine G0 promotion would need a theorem showing that the required cumulative/prefix information is reconstructible from the instantaneous native cell state or from an already-N0 local relation at the same semantic strength.

No such theorem is established here.

## 12. Next discriminating question

The remaining foundational question is now smaller than the one left by #1161:

> Is first-balance history **predictively compressible** to a finite local native state whose transition is definable from the current cell/incident relation alone, while preserving every future first-return mass needed by the AGM RG?

A positive answer would supply a genuine finite-state G0/N0-definability bridge. A negative answer should exhibit two native instantaneous states with identical allowed local G0 data but different future first-balance signatures, proving that some history bit is irreducible.

This is the next smallest unfinished unit. It is a new foundational successor problem, not a missing algebraic step of #1161.

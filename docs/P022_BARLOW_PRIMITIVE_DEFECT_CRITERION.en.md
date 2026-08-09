# P022 — Primitive Franel Divisors Give a Triangular Global Defect Certificate

Status: `ACTIVE RESEARCH NOTE / CONDITIONAL GLOBAL THEOREM + EXACT FINITE SPECIALIZATION`  
Owner: `program/p022-geometry-v2`  
Depends on: pure Franel-defect reduction of `(J1,J2,J3)` identifiability  
Cross-route relevance: P011 collision-polynomial identifiability; arithmetic pressure test for the global P022 route

## 1. The global problem after structural reduction

The current low-order collision problem has been reduced to the following question:

> Are the tail defect `2` and all composite Franel defects
> \[
> D_n,
> \qquad 2n-1\text{ composite},
> \]
> multiplicatively independent?

The finite theorem through segment 150 is already proved by an exact saturated valuation certificate.

For the unbounded problem, a very strong but clean sufficient condition is available: one genuinely new Franel prime divisor at every composite-boundary index.

---

## 2. Primitive Franel divisor

Call a prime `q` a **primitive divisor of `F_n`** if

\[
\boxed{q\mid F_n}
\]

but

\[
\boxed{q\nmid F_j\quad(1\le j<n).}
\]

Write

\[
e_n=v_q(F_n)>0.
\]

This is ordinary primitive-divisor language.  P022 does not claim that every Franel number has such a divisor.

---

## 3. P022-PD01 — primitive Franel divisor survives unchanged in the composite defect

Let `n` be a composite odd-boundary index:

\[
2n-1\text{ composite}.
\]

The pure defect is

\[
D_n
=
\frac{F_n}
{\prod_{j<n}F_j^{\alpha_{n,j}}}.
\]

If `q_n` is a primitive divisor of `F_n`, then every denominator term has zero `q_n`-valuation. Therefore

\[
\boxed{
v_{q_n}(D_n)=v_{q_n}(F_n)=e_n>0.}
\]

For every earlier defect `D_m` with `m<n`, both its numerator and denominator involve only Franel numbers `F_j` with `j<n`, so

\[
\boxed{
v_{q_n}(D_m)=0.}
\]

Thus `q_n` produces a valuation row whose first nonzero defect coordinate is exactly `D_n`.

---

## 4. P022-PD02 — primitive divisors triangularize the defect lattice

List the composite odd-boundary indices increasingly:

\[
n_1<n_2<\cdots.
\]

Suppose each `F_(n_r)` has a chosen primitive prime divisor `q_r`.

Order defect columns as

\[
2,D_{n_1},D_{n_2},\ldots
\]

and valuation rows as

\[
v_2,v_{q_1},v_{q_2},\ldots.
\]

The tail defect column has

\[
v_2(2)=1.
\]

Every odd primitive row has zero tail entry.  By PD01, row `v_(q_r)` has:

- zero entries on every earlier defect column;
- diagonal entry
  \[
  e_r=v_{q_r}(F_{n_r})>0.
  \]

Hence every finite prefix valuation matrix is triangular with diagonal

\[
\boxed{1,e_1,e_2,\ldots,e_R.}
\]

Its determinant is

\[
\boxed{\prod_{r=1}^{R}e_r\ne0.}
\]

Therefore every finite prefix of

\[
\{2,D_{n_1},D_{n_2},\ldots\}
\]

is multiplicatively independent.

Consequently:

\[
\boxed{
\text{if every composite-boundary }F_n
\text{ has a primitive prime divisor,}
}
\]

then the entire defect family is multiplicatively independent.

This would prove global `(J1,J2,J3)` identifiability for the Barlow checkpoint specialization.

---

## 5. P022-PD03 — simple primitive divisors give unimodularity

If in addition each chosen primitive divisor is simple,

\[
v_{q_r}(F_{n_r})=1,
\]

then every diagonal pivot is one.

Thus every finite prefix has determinant

\[
\boxed{1}
\]

in the primitive valuation coordinates.

So a **simple primitive divisor theorem** would imply not merely rational independence but an exact unimodular integer decoder for every finite checkpoint horizon.

This is stronger than required for uniqueness.

---

## 6. Exact finite example through segment 20

The composite odd-boundary indices through `20` are

\[
5,8,11,13,14,17,18,20.
\]

One choice of exact simple primitive Franel divisors is:

| segment `n` | `2n-1` | primitive prime of `F_n` |
|---:|---:|---:|
| 5 | 9 | 563 |
| 8 | 15 | 369581 |
| 11 | 21 | 337 |
| 13 | 25 | 2141 |
| 14 | 27 | 12148537 |
| 17 | 33 | 59 |
| 18 | 35 | 37 |
| 20 | 39 | 151 |

Each listed prime occurs for the first time at the declared Franel term and with valuation one.

Therefore the tail plus these eight defect columns have an exact unimodular triangular valuation certificate.

This is a finite theorem only; it is included to show the global criterion is computationally real rather than vacuous.

---

## 7. Relation to the segment-150 certificate

The current segment-150 theorem does **not** depend on having a primitive divisor for every composite index.

Indeed the historical `n=67` extension was certified by the row `v_337` even though

\[
v_{337}(D_{67})=0.
\]

That row rejected a global old-defect dependency instead of acting as a local primitive pivot.

So primitive divisors are:

- sufficient;
- structurally clean;
- not necessary for a finite independence proof.

The marker-prime saturation theorem gives a second nonlocal mechanism: private primes of **prime-boundary** Franel terms can read later central-binomial relation coefficients and help saturate the defect lattice.

Thus the full finite theory already has both local and global pivot mechanisms.

---

## 8. Literature boundary

Franel divisibility has substantial prior art:

- Lucas-type congruences and divisibility behavior for sporadic Apéry-like sequences;
- p-adic congruences and supercongruences;
- primes that divide no Franel term at all (`Type I` primes);
- tabulated prime-factor data for many Franel terms.

Current source checks include work by Zhi-Wei Sun on Franel congruences and Malik–Straub on divisibility properties of sporadic Apéry-like numbers.

No general theorem was located in the checked sources asserting that every Franel number—or every composite-boundary Franel number relevant here—has a primitive prime divisor.

That absence is **not** a novelty proof and must not be stated as impossibility or historical priority.

---

## 9. New global attack surface

The unbounded P022 problem now admits three increasingly weak routes:

### Strongest / cleanest

Prove every relevant `F_n` has a primitive prime divisor.

### Weaker

Prove every new `D_n` has a valuation prime not in the span of earlier defect valuation vectors, even if that prime already appeared in older Franel terms.

### Weakest sufficient

Prove the entire infinite defect valuation lattice has no nonzero finitely supported integer relation.

The segment-67 `337` phenomenon shows the second route can succeed even when the first route is not the row actually used by the certificate.

This hierarchy makes clear what additional number theory would close the global `(J1,J2,J3)` conjecture.

---

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_primitive_defect_criterion.py`;
- `tests/test_p022_barlow_primitive_defect_criterion.py`.

The tests verify the primitive-pivot theorem directly from Franel divisibility, the triangular zero pattern, and an exact unimodular certificate through segment 20.

# P002 — Sharp collapse-gap bound

Status: `PROVED / LEAN-CHECKED T01–T02`  
Open problem: `P002`  
Scope: ordinary mathematics

## 1. Gap definition

For \(p\ge1\), define the comparison quantity

\[
G_p(n)=n-C_p(n).
\]

This is the integer distance between the pre-collapse and post-collapse states. It is a derived relation quantity; the definition does not assert that the gap survives as a hidden state after collapse.

Let

\[
k=R_p(n).
\]

Then \(C_p(n)=k^p\), and T001 gives

\[
k^p\le n<(k+1)^p.
\]

Lean representation: `EnterpriseMath.CollapseGap.collapseGap`; the sharp basin endpoint is represented by `maxGapInBasin`.

## 2. Sharp basin bound

### P002-T01 — Sharp collapse-gap theorem

Status: `PROVED`

For every \(n\in\mathbb N\) and \(p\ge1\), with \(k=R_p(n)\),

\[
0\le G_p(n)\le (k+1)^p-k^p-1.
\]

The upper bound is sharp, and equality holds exactly at the final state of the basin:

\[
G_p(n)=(k+1)^p-k^p-1
\iff
n=(k+1)^p-1.
\]

### Proof

Since \(C_p(n)=k^p\le n\),

\[
G_p(n)=n-k^p\ge0.
\]

Because \(n<(k+1)^p\) and all states are integers,

\[
n\le (k+1)^p-1.
\]

Subtracting \(k^p\) gives

\[
G_p(n)\le (k+1)^p-k^p-1.
\]

Equality after subtraction occurs exactly when \(n=(k+1)^p-1\). That state is still in the basin of \(k^p\), so the bound is attained. ∎

Formalization: Lean-checked as `EnterpriseMath.CollapseGap.collapseGap_le_max`; sharp equality is checked as `collapseGap_eq_max_iff`.

## 3. Basin size interpretation

T008 gives

\[
|B_{p,k}|=(k+1)^p-k^p.
\]

Therefore the sharp gap bound is simply

\[
\boxed{\max_{n\in B_{p,k}}G_p(n)=|B_{p,k}|-1.}
\]

For squares,

\[
|B_{2,k}|=2k+1,
\]

so

\[
0\le G_2(n)\le2k.
\]

At \(k=141\), the basin is \(19881,\ldots,20163\), and the maximum comparison gap is

\[
20163-19881=282.
\]

## 4. Every basin offset occurs exactly once

### P002-T02 — Gap-coordinate bijection inside a basin

Status: `PROVED`

For fixed \(p\ge1\) and \(k\in\mathbb N\), the map

\[
n\longmapsto G_p(n)=n-k^p
\]

is a bijection from the basin

\[
B_{p,k}=\{k^p,\ldots,(k+1)^p-1\}
\]

onto

\[
\{0,1,\ldots,(k+1)^p-k^p-1\}.
\]

### Proof

Every basin state has the unique form

\[
n=k^p+g
\]

with

\[
0\le g\le (k+1)^p-k^p-1.
\]

For such a state \(C_p(n)=k^p\), hence

\[
G_p(n)=g.
\]

The inverse map is \(g\mapsto k^p+g\). ∎

Formalization: exact recovery of a basin state is checked by `EnterpriseMath.CollapseGap.basin_state_eq_pow_add_gap`. The bijection is kernel-checked in `∃!` form by `existsUnique_basin_state_with_gap`: every admissible gap coordinate has exactly one state in the fixed basin, with inverse state `k^p+g`.

Thus the gap can be used as an **external coordinate for comparing states within a basin** without changing the collapse map into a pair-valued state transition.

## 5. Pure-integer closed form

By the binomial theorem,

\[
(k+1)^p-k^p-1
=
\sum_{j=1}^{p-1}\binom pj k^j.
\]

So the sharp upper bound is an integer polynomial in \(k\) for each fixed positive exponent \(p\).

Examples:

\[
p=1:\quad 0,
\]

\[
p=2:\quad 2k,
\]

\[
p=3:\quad 3k^2+3k,
\]

\[
p=4:\quad 4k^3+6k^2+4k.
\]

No real-valued approximation or asymptotic estimate is required.

Formalization status: this unnumbered binomial closed-form corollary remains ordinary-proved in the present pass; `LEAN-CHECKED T01–T02` refers specifically to the two numbered P002 theorem units above.

## 6. Relation to the ontology boundary

P002 must not reintroduce the old hidden-remainder interpretation.

The theorem says that two explicit states \(n\) and \(C_p(n)\) have an integer difference \(G_p(n)\), and that this difference is a useful coordinate on the pre-collapse basin.

It does **not** change the project transition

\[
n\longmapsto C_p(n)
\]

into

\[
n\longmapsto (C_p(n),G_p(n)).
\]

Whether a physical theory should retain additional variables is a separate physical hypothesis. The ordinary mathematical map studied here remains many-to-one.

## 7. Resolution of P002

P002 is completely resolved:

\[
\boxed{
G_p(n)\le (R_p(n)+1)^p-R_p(n)^p-1
}
\]

with equality exactly at the last integer state before the next perfect \(p\)-th power.

The same result is equivalently “basin size minus one”, and the gap coordinate enumerates every location inside the basin exactly once.

P002-T01 and P002-T02 are covered by the imported warnings-fatal Lean build in `EnterpriseMath.Arithmetic.CollapseGap`.

## 8. Prior-art discipline

The proof uses only the established integer-root interval characterization and elementary integer/binomial arithmetic. No historical novelty claim is made. The exact Enterprise Math packaging remains `NOVELTY_UNVERIFIED`, while the theorem itself is `PROVED`.

# Proved Propositions for v0.1

Status labels in this file refer to ordinary mathematical proofs from the v0.1 definitions. They are not yet Lean-checked unless explicitly stated.

## T001 — Root characterization

Status: `PROVED`

For \(p\ge1\),

\[
R_p(n)=k\iff k^p\le n<(k+1)^p.
\]

This is equivalent to the defining maximum property.

Formalization: Lean-checked in `EnterpriseMath.Arithmetic.IntegerRoot.root_eq_iff`, directly reusing Mathlib's established `Nat.nthRoot` lemmas.

## T002 — Exact perfect powers

Status: `PROVED`

\[
R_p(k^p)=k.
\]

Proof: \(k^p\le k^p<(k+1)^p\), so T001 applies.

## T003 — Root monotonicity

Status: `PROVED`

If \(a\le b\), then

\[
R_p(a)\le R_p(b).
\]

Proof: every \(k\) satisfying \(k^p\le a\) also satisfies \(k^p\le b\).

## T004 — Collapse is contractive

Status: `PROVED`

\[
C_p(n)\le n.
\]

Proof: by definition, \(R_p(n)^p\le n\).

## T005 — Collapse is idempotent

Status: `PROVED`

\[
C_p(C_p(n))=C_p(n).
\]

Proof: \(C_p(n)\) is already a perfect \(p\)-th power, then apply T002.

## T006 — Fixed points are exactly perfect powers

Status: `PROVED`

\[
C_p(n)=n
\]

if and only if \(n=k^p\) for some \(k\in\mathbb N\).

## T007 — Basin interval

Status: `PROVED`

\[
C_p(n)=k^p
\]

if and only if

\[
k^p\le n<(k+1)^p.
\]

Thus each collapse basin is one consecutive integer interval.

## T008 — Basin cardinality

Status: `PROVED`

\[
|B_{p,k}|=(k+1)^p-k^p.
\]

For \(p=2\),

\[
|B_{2,k}|=2k+1.
\]

Therefore the basin of \(141^2=19881\) contains 283 states.

## T009 — Collapse monotonicity

Status: `PROVED`

If \(a\le b\), then

\[
C_p(a)\le C_p(b).
\]

Proof: combine T003 with monotonicity of \(k\mapsto k^p\) on \(\mathbb N\).

## T010 — Scale compatibility

Status: `PROVED`

For integer base \(b\ge2\),

\[
R_{p,b,s+1}(n)\operatorname{//}b=R_{p,b,s}(n).
\]

Proof: let \(k=R_{p,b,s}(n)\). Then

\[
k^p\le nb^{ps}<(k+1)^p.
\]

Multiplying by \(b^p\) gives

\[
(kb)^p\le nb^{p(s+1)}<((k+1)b)^p.
\]

Hence the finer root lies in the integer interval from \(kb\) through \((k+1)b-1\), whose integer quotient by \(b\) is \(k\).

P008 gives a second structural proof: the commuting square between the power map and multiplication by \(b\) transfers across their right adjoints, yielding the root/division identity T015 below.

## T011 — One-sided inverse law

Status: `PROVED`

\[
R_p(k^p)=k,
\]

but in general

\[
R_p(n)^p\ne n.
\]

Thus integer root is a left inverse of perfect-power formation on its image, not a two-sided inverse on all natural states.

## T012 — Merged histories never split under deterministic forward composition

Status: `PROVED`

Let

\[
F_t=T_t\circ\cdots\circ T_1.
\]

If

\[
F_t(x)=F_t(y),
\]

then

\[
F_{t+1}(x)=F_{t+1}(y).
\]

Therefore

\[
[x]_t\subseteq[x]_{t+1}.
\]

On a finite state domain,

\[
M_t(x)=|[x]_t|
\]

is nondecreasing.

Formalization: both the set inclusion and finite-cardinality monotonicity are Lean-checked in `EnterpriseMath.History.mergedClass_subset_next` and `mergedMultiplicity_mono`.

## T013 — Integer roots compose multiplicatively in the exponent

Status: `PROVED`

For \(p,q\ge1\),

\[
R_{pq}(n)=R_p(R_q(n)).
\]

Equivalently,

\[
R_{pq}=R_p\circ R_q.
\]

Proof: the power maps \(P_p(k)=k^p\) and \(P_q(k)=k^q\) have integer roots as their right adjoints. Since

\[
P_q\circ P_p=P_{pq},
\]

right adjoints compose in reverse order. This is an application of established Galois-connection theory, not a new order-theoretic principle.

Formalization: Lean-checked against the pinned mathlib snapshot in `EnterpriseMath.Arithmetic.IntegerRoot.root_mul`.

## T014 — Iterated positive integer roots commute

Status: `PROVED`

For \(p,q\ge1\),

\[
R_p(R_q(n))=R_q(R_p(n)).
\]

Proof: both sides equal \(R_{pq}(n)\) by T013 and commutativity of integer multiplication.

Formalization: Lean-checked in `EnterpriseMath.Arithmetic.IntegerRoot.root_mul_comm`.

## T015 — Root/division interchange

Status: `PROVED`

For \(p\ge1\), \(b\ge1\), and \(n\in\mathbb N\),

\[
R_p(n)\operatorname{//}b
=
R_p\!\left(n\operatorname{//}b^p\right).
\]

Equivalently, if \(D_b(n)=n\operatorname{//}b\), then

\[
D_b\circ R_p=R_p\circ D_{b^p}.
\]

Proof: multiplication by \(b\) is left adjoint to flooring division by \(b\), powering by \(p\) is left adjoint to \(R_p\), and

\[
P_p\circ M_b=M_{b^p}\circ P_p.
\]

The commuting square transfers to the right adjoints. T010 is a direct specialization.

Formalization: Lean-checked in `EnterpriseMath.Scale.root_div_scale`; T010 is Lean-checked in `EnterpriseMath.Scale.scaledRoot_succ_div`.

## Verification status

The Python reference tests computationally check T001–T010 over bounded finite domains. This supports implementation correctness but is not the proof source.

The P008 Lean layer is pinned to a specific mathlib revision and reuses Mathlib's existing `Nat.nthRoot` and Galois-connection APIs. It currently kernel-checks T001, T002, T004, T005, T006, T010, T012, T013, T014, and T015, together with project-facing generic adjoint-collapse lemmas. Lean CI builds with warnings fatal.

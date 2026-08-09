# Proved Propositions for v0.1

Status labels in this file refer to ordinary mathematical proofs from the v0.1 definitions. A proposition is Lean-checked only when explicitly stated below.

Canonical scope conventions follow `FOUNDATIONS`: \(\mathbb N=\mathbb N_0=\{0,1,2,\ldots\}\), while \(\mathbb N_{>0}\) denotes the positive integers. The physically nontrivial primitive root/collapse family starts at \(p\ge2\), while this theorem catalogue uses the exact positive-exponent algebra \(p\ge1\) whenever the stated law remains valid; its identity member is \(R_1=C_1=\operatorname{id}\).

## T001 — Root characterization

Status: `PROVED`

For \(p\ge1\),

\[
R_p(n)=k\iff k^p\le n<(k+1)^p.
\]

This is equivalent to the defining maximum property.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.root_eq_iff`.

## T002 — Exact perfect powers

Status: `PROVED`

\[
R_p(k^p)=k.
\]

Proof: \(k^p\le k^p<(k+1)^p\), so T001 applies.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.root_pow`.

## T003 — Root monotonicity

Status: `PROVED`

If \(a\le b\), then

\[
R_p(a)\le R_p(b).
\]

Proof: every \(k\) satisfying \(k^p\le a\) also satisfies \(k^p\le b\).

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.root_monotone`, derived from the power/root Galois connection.

## T004 — Collapse is contractive

Status: `PROVED`

\[
C_p(n)\le n.
\]

Proof: by definition, \(R_p(n)^p\le n\).

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.collapse_le`.

## T005 — Collapse is idempotent

Status: `PROVED`

\[
C_p(C_p(n))=C_p(n).
\]

Proof: \(C_p(n)\) is already a perfect \(p\)-th power, then apply T002.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.collapse_idempotent`.

## T006 — Fixed points are exactly perfect powers

Status: `PROVED`

\[
C_p(n)=n
\]

if and only if \(n=k^p\) for some \(k\in\mathbb N_0\). In particular, \(0\) is included and is fixed for every positive exponent.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.collapse_eq_self_iff`.

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

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.collapse_eq_pow_iff`; finite-basin membership is also checked as `EnterpriseMath.IntegerRoot.mem_basin_iff`.

## T008 — Basin cardinality

Status: `PROVED`

\[
|B_{p,k}|=(k+1)^p-k^p.
\]

For \(p=2\),

\[
|B_{2,k}|=2k+1.
\]

Therefore the basin of \(141^2=19881\) contains 283 states. For the algebraic identity case \(p=1\), every basin has cardinality \(1\).

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.basin_card`; the square and identity specializations are checked as `basin_card_square` and `basin_card_one`.

## T009 — Collapse monotonicity

Status: `PROVED`

If \(a\le b\), then

\[
C_p(a)\le C_p(b).
\]

Proof: combine T003 with monotonicity of \(k\mapsto k^p\) on \(\mathbb N_0\).

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.collapse_monotone`.

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

P008/P014 also give a structural proof through T015 below. Formalization: Lean-checked as `EnterpriseMath.Scale.scaledRoot_succ_div`.

## T011 — One-sided inverse law

Status: `PROVED`

\[
R_p(k^p)=k,
\]

but in general for nontrivial exponents \(p\ge2\),

\[
R_p(n)^p\ne n.
\]

Thus integer root is a left inverse of perfect-power formation on its image, not a two-sided inverse on all natural states when \(p\ge2\). At \(p=1\), both maps are the identity.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.root_leftInverse_pow` and `root_pow_not_two_sided`. The stronger uniform witness \(C_p(2)=1\ne2\) for every \(p\ge2\) is checked by `collapse_two_eq_one` and `collapse_two_ne_self`; the identity member is checked by `root_one` and `collapse_one`.

## T012 — Merged histories never split under deterministic forward composition

Status: `PROVED`

Use the canonical time convention

\[
F_0=\operatorname{id},
\qquad
F_{t+1}=T_t\circ F_t,
\]

so equivalently \(F_t=T_{t-1}\circ\cdots\circ T_0\) for \(t\ge1\).

If

\[
F_t(x)=F_t(y),
\]

then

\[
F_{t+1}(x)=T_t(F_t(x))=T_t(F_t(y))=F_{t+1}(y).
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

Formalization: Lean-checked in the more general heterogeneous postcomposition form as `EnterpriseMath.HistoryMerge.merged_never_split`; finite fiber inclusion and cardinality monotonicity are checked as `fiberFinset_subset_postcompose` and `fiberCard_mono_postcompose`.

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

right adjoints compose in reverse order. This uses established Galois-connection theory rather than a new order-theoretic principle.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.root_mul`.

## T014 — Iterated positive integer roots commute

Status: `PROVED`

For \(p,q\ge1\),

\[
R_p(R_q(n))=R_q(R_p(n)).
\]

Proof: both sides equal \(R_{pq}(n)\) by T013 and commutativity of integer multiplication.

Formalization: Lean-checked as `EnterpriseMath.IntegerRoot.root_mul_comm`.

## T015 — Root/division interchange

Status: `PROVED`

For \(p\ge1\), \(b\ge1\), and \(n\in\mathbb N_0\),

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

Formalization: Lean-checked as `EnterpriseMath.Scale.root_div_comm`; T010 is Lean-checked as `EnterpriseMath.Scale.scaledRoot_succ_div`.

## Verification status

The Python reference tests computationally check the original arithmetic laws over bounded finite domains; those computations support implementation correctness but are not proof sources.

The pinned Lean/mathlib layer is compiled with warnings fatal in CI. Every proposition in the base v0.1 catalogue, T001 through T015, is now covered by the imported Lean build. T003, T007, T008, T009, T011, and T012 were promoted in the incremental theorem-catalogue verification pass; their exact theorem names are recorded above.

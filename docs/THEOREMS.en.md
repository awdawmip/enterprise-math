# Proved Propositions for v0.1

Status labels in this file refer to ordinary mathematical proofs from the v0.1 definitions. They are not yet Lean-checked unless explicitly stated.

## T001 — Root characterization

Status: `PROVED`

For \(p\ge1\),

\[
R_p(n)=k\iff k^p\le n<(k+1)^p.
\]

This is equivalent to the defining maximum property.

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

## Verification status

The Python reference tests computationally check T001–T010 over bounded finite domains. This supports implementation correctness but is not the proof source.

The next formalization target is T001, T005, T010, and T012 in Lean.

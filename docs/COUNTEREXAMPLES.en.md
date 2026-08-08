# Counterexample Catalog

The purpose of this file is to prevent classical identities from entering Enterprise Math by habit.

## C001 — Root is not a two-sided inverse

Claim rejected:

\[
R_2(n)^2=n.
\]

Counterexample:

\[
n=2,\qquad R_2(2)^2=1.
\]

## C002 — Integer root is not multiplicative

Claim rejected:

\[
R_2(a)R_2(b)=R_2(ab).
\]

Counterexample:

\[
a=b=2.
\]

The left side is \(1\), while the right side is \(2\).

## C003 — Integer root is not additive

Claim rejected:

\[
R_2(a+b)=R_2(a)+R_2(b).
\]

Counterexample:

\[
a=b=1.
\]

The left side is \(1\), while the right side is \(2\).

## C004 — Pulling integer factors through a root can fail

Claim rejected:

\[
R_2(a^2b)=aR_2(b).
\]

Counterexample:

\[
a=3,\qquad b=2.
\]

The left side is \(R_2(18)=4\), while the right side is \(3\).

## C005 — Collapse is not additive

Claim rejected:

\[
C_2(a+b)=C_2(a)+C_2(b).
\]

Counterexample:

\[
a=b=2.
\]

The left side is \(4\), while the right side is \(2\).

## C006 — Collapse is not multiplicative

Claim rejected:

\[
C_2(ab)=C_2(a)C_2(b).
\]

Counterexample:

\[
a=b=2.
\]

The left side is \(4\), while the right side is \(1\).

## C007 — Collapse is not injective

Claim rejected:

\[
C_2(a)=C_2(b)\Rightarrow a=b.
\]

Counterexample:

\[
C_2(19881)=C_2(20000)=19881.
\]

## C008 — Collapse is not strictly monotone

Claim rejected:

\[
a<b\Rightarrow C_2(a)<C_2(b).
\]

Counterexample:

\[
19881<20000,
\]

but both collapse to \(19881\).

## C009 — One input scale step is not one root scale step

Claim rejected for square root:

\[
R_2(nb)\operatorname{//}b=R_2(n).
\]

Counterexample with \(n=2\) and \(b=10\):

\[
R_2(20)\operatorname{//}10=0,
\]

while

\[
R_2(2)=1.
\]

The correct square-root refinement uses \(b^2\) on the input.

## C010 — Forward collapse has no single-valued inverse

Claim rejected: there exists a function \(G\) satisfying

\[
G(C_2(n))=n
\]

for every \(n\).

Counterexample: every state from 19881 through 20163 has the same image 19881, so no single value \(G(19881)\) can recover all of them.

## C011 — Monotonicity alone does not make the maximum-formula right adjoint total

Claim rejected: every monotone map \(F:\mathbb N\to\mathbb N\) admits a total right adjoint by

\[
F^\downarrow(n)=\max\{k:F(k)\le n\}.
\]

Counterexample: let \(F(k)=0\) for every \(k\). The map is monotone, but for every \(n\),

\[
\{k:F(k)\le n\}=\mathbb N
\]

has no maximum. Thus the concrete greatest-state construction requires more than monotonicity, for example the sufficient unboundedness condition used in P008.

## C012 — Unboundedness without monotonicity does not yield the adjunction law

Claim rejected: unboundedness and \(F(0)=0\) are enough for the greatest-admissible-state formula to satisfy

\[
F(k)\le n\iff k\le F^\downarrow(n).
\]

Counterexample: define

\[
F(0)=0,\qquad F(1)=2,\qquad F(2)=1,
\]

and \(F(k)=k\) for \(k\ge3\). The map is unbounded. For \(n=1\), the greatest admissible state is \(2\), but \(1\le2\) while \(F(1)=2\not\le1\). Hence the adjunction equivalence fails.

## Contribution rule

A new algebraic identity should enter the theorem catalog only after explicit proof. If a finite counterexample exists, add it here with the smallest clear example when practical.

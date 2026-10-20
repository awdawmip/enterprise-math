# P017×P018 Generation 4 Supplement 06 — unique overlap/single-use root layer

Status: `PROVED_WIP STRUCTURAL UNIQUENESS`

This supplement isolates the root-complexity reason the fourth-root P3 layer is
special.  It does not add an analytic estimate.

## U1. Pair overlap first appears at P3

At the exact P2 root cutoff, every squarefree rough composite in the
consecutive-square interval is a semiprime `pq` with exactly one factor in the
medium band `(z_2,k]` and the other factor above `k`.  Hence its medium support
depth is

\[
c=1.
\]

There is no two-prime medium-support overlap to exploit.

At the P3 root cutoff, squarefree triple states exist as an allowed arithmetic
type.  The square-window factor-size theorem forces all three factors into the
medium band, so those states have

\[
c=3,
\]

and therefore create nontrivial pair-overlap tokens.

Thus `m=3` is the first root-complexity level at which second-order support
information can carry information not already present in the first moment.

## U2. Universal pair-token single-use persists only through P3

At the general P_m product cutoff

\[
z_m=\lfloor U^{1/(m+1)}\rfloor,
\]

a residual two-prime token satisfies

\[
D\ge(z_m+1)^2.
\]

The root-scale product argument forces every such pair token above the square
radius `k` exactly when

\[
D^2>(z_m+1)^4>U>k^2.
\]

The generic token-capacity criterion from Generation 4 is

\[
2j\ge m+1
\]

for an order-`j` token.  Setting `j=2` gives

\[
4\ge m+1,
\]

or

\[
\boxed{m\le3.}
\]

For `m>=4`, the root cutoff alone no longer forces every pair token above `k`;
pair reuse returns as a genuine structural possibility.

## U3. Unique intersection

Combine the two boundaries:

1. nontrivial medium pair-overlap requires root complexity at least P3;
2. universal single-use of every pair token requires root complexity at most
   P3.

Therefore

\[
\boxed{
P_3\text{ is the unique root layer with nontrivial pair overlap and universal pair single-use.}
}
\]

Equivalently, in the square-scale notation `X=k^2`, the fourth-root cutoff
`X^(1/4)` is uniquely selected by the intersection

`overlap has appeared` + `overlap tokens have not yet begun to reuse`.

This gives a structural explanation for the Generation-4 quadratic detector:
its new positive resource `S_2` exists for the first time exactly where it is
still a collection of globally single-use floor gates.

## U4. Relation to the two neighboring layers

- **P2 / cubic-root cutoff:** simpler factor depth, but no pair-overlap resource;
  the state-Möbius sign has already frozen on nontrivial factorizations.
- **P3 / fourth-root cutoff:** pair overlap exists, all pair tokens are
  single-use, squarefree support has the exceptional spectrum `{0,1,3}`, and
  prime detection reduces exactly to degree two.
- **P4 and shallower:** more factor-depth freedom is retained, but pair tokens
  are no longer universally single-use; the `k=35`, `1295=5*7*37` example from
  Supplement 01 already shows the loss of the P3 support-spectrum hole at the
  next layer.

Hence the fourth-root layer is not merely one convenient pre-sieve depth.  It
is the unique finite-combinatorial interface at which a second-order correction
both exists and has zero token-reuse depth.

# C87 position results: proof, certified values, and exploratory values

## Result map

`GLOBAL_POSITION_THEOREM.md` proves strict concavity and the complete
ordering of the high-precision position constant. It also states the
fixed-inventory-grid design rule: endpoint-nearest internal choices
maximize the high-precision limiting unique rate, while midpoint-nearest
choices maximize the low-precision limit. Every two fixed rational
positions at different distances from the midpoint have at least one
crossing. The theorem preserves the fixed-position, sequential limit
scope of the original-inventory bridge.

`ENDPOINT_AXIS_PROOF.md` proves \(A(x)/x^2>1/40\) on the complete
interval \(0<x\le1/8\), using exact cancellation and an explicit
Taylor remainder. It gives the endpoint expansion and a one-dimensional
certificate for midpoint curvature.

The endpoint continuation is twice continuously differentiable, but
not three times differentiable. Its exact second derivative is

\[
I''_{0+}=-\frac{2}{\zeta(2)(19/20)(21/20)(41/20)}
\left(\frac{211}{244}2^{-1/20}
-\frac{101}{122}4^{-1/20}+\frac{23}{61}\right).
\]

The noninteger \(\theta^{41/20}\) term has a certified positive
coefficient. This differentiable expansion strengthens C85's endpoint
continuity statement without changing its auxiliary endpoint identity
\(I_0=(40/41)I_2\).

## Certified endpoint values

The stored C87 family certificate contains an affine enclosure on every
one of its sixty accepted intervals:

\[
A(x)=C_j+S_j(x-x_j)+R_j(x),\qquad |R_j(x)|\le E_j.
\]

The stored total interval error is
\(E_j+|S_j|\Delta x_j\). The program
`certify_position_values.py` recovers the original outward upper bound
for \(E_j\) by subtracting exactly the outward fixed-point contribution
of \(|S_j|\Delta x_j\). This uses the recorded arithmetic construction,
not a subtraction of unrelated analytical estimates.

It then integrates the affine models against the exact positive weights
\(1/x\) and \((1+x)/x^2\). Their required moments are

\[
\int_a^b\frac{dx}{x}=\log(b/a),\qquad
\int_a^b\frac{x-x_j}{x}\,dx=(b-a)-x_j\log(b/a),
\]

\[
\int_a^b\frac{1+x}{x^2}\,dx
=\log(b/a)+1/a-1/b,
\]

\[
\int_a^b\frac{(x-x_j)(1+x)}{x^2}\,dx
=(b-a)+\log(b/a)-x_j\{\log(b/a)+1/a-1/b\}.
\]

The remainder is bounded by \(E_j\) times the mass of the positive
weight. On \([0,1/8]\), the program instead integrates
\(B(x)=a_2+b_2x^{1/20}+O(Ex)\) with its complete certified error.
No new numerical grid is used.

This proves the following convenient outward-rounded inequalities:

\[
\boxed{-0.009034<I_0-I_{1/2}<-0.003869<0,}
\]

\[
\boxed{0.01558<I'_{0+}<0.03404.}
\]

The complete 112-bit directed endpoints are stored in
`position_value_certificate.json`. These deliberately conservative
intervals reuse the mesh designed to prove global positivity. They
are not intended as a high-accuracy decimal evaluation.

## Fourteen certified positions

For a rational position \(\theta\le1/2\), let
\(q=\theta/(1-\theta)\). The same affine certificates are clipped
at \(q\) and integrated against

\[
\frac{1-\theta}{x}-\frac\theta{x^2}
\quad\text{and}\quad \frac{1+x}{x^2}.
\]

Their masses and first centered moments are elementary combinations of
rational numbers and \(\log(b/a)\). The first weight is nonnegative
on \(x\ge q\). The axis part, when needed, again uses the exact
power moments and the bound \(Ex\). Consequently all remainder
integrations preserve their sign and enclosure.

The stored table certifies \(I_\theta-I_{1/2}\) and \(I'_\theta\)
at

\[
0,\ 1/64,\ 1/32,\ 1/16,\ 1/10,\ 1/8,\ 1/6,\ 1/5,
\ 1/4,\ 1/3,\ 2/5,\ 9/20,\ 49/100,\ 1/2.
\]

Every listed position below the midpoint has a certified negative
gap and positive derivative. The midpoint has exact gap and derivative
zero. These fourteen enclosures are useful numerical consequences of
the interval family. The global theorem follows from the complete
interval family and axis proof, rather than from those fourteen points.

## Exploratory decimal table

`explore_positions.py` evaluates the same exact formula with floating
Gauss quadrature. Near the axis it evaluates a binomial remainder after
the identically vanishing constant and linear terms, avoiding loss of
the leading \(x^2\) term. A change of variable \(x=t^{20}\) resolves
the weak endpoint power. The order-32 and order-64 runs agreed in their
fourteen position gaps to within \(1.34\times10^{-14}\), but this
agreement is not an interval proof.

| Position \(\theta\) | Exploratory \(I_\theta-I_{1/2}\) |
|---|---:|
| Auxiliary endpoint \(0\) | \(-0.00645315020083\) |
| \(1/16\) | \(-0.00501175172037\) |
| \(1/8\) | \(-0.00375194665892\) |
| \(1/6\) | \(-0.00300624244553\) |
| \(1/4\) | \(-0.00174292875180\) |
| \(1/3\) | \(-0.000799531752742\) |
| \(2/5\) | \(-0.000294836022335\) |
| \(49/100\) | \(-0.00000301096187985\) |
| \(1/2\) | \(0\) |

The exploratory endpoint slope is approximately \(0.0248350749079\),
and the exploratory midpoint curvature is approximately
\(-0.0602402477573\). The rigorous intervals, including the certified
midpoint curvature \((-0.063099,-0.057382)\), remain the authoritative
numerical claims.

## Reproduction and preservation of fixed certificates

The read-only quick verifier is:

```bash
python /mnt/data/C87/positions/verify_positions.py
```

It recomputes the two stored one-dimensional radial integrals on their
existing 192-cell mesh, verifies the exact axis cancellations and
remainder, checks the complete sixty-interval coverage and source hashes,
and recomputes all fourteen integrations of existing affine models. It
does not run the adaptive family search or modify any certificate file.
Its Python `verify()` function returns the same result for the parent
bundle verifier.

Full regeneration commands are separate:

```bash
python /mnt/data/C87/positions/certify_axis_midpoint.py --n 192
python /mnt/data/C87/positions/certify_position_values.py
```

The first command rewrites `axis_midpoint_certificate.json`, including
elapsed-time metadata. Its file hash can change even when every
mathematical endpoint is identical. The second command records the
current input certificate hashes, so it should follow any such
regeneration. The parent adaptive family generator similarly rewrites
its own elapsed-time metadata. Quick verification compares mathematical
data without regenerating these fixed inputs.

The optional exploratory commands also rewrite timing metadata:

```bash
python /mnt/data/C87/positions/explore_positions.py --n 32
python /mnt/data/C87/positions/explore_positions.py --n 64
```

They are not part of the quick verifier. The local chamber JSON and
interval kernel are unchanged pinned copies from C86; their identities
are checked against the parent's C86 input records.

# D25 — Exact coupled finite Green concomitant and two-port signed cutoff

Date: 2026-11-06. Scientific status: AUTHOR-PROVED exact rational identity / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. Original SECOND-DIGIT-LIFT Task publication TP2-B6F4FC938FF94941C1B7; frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes (does not re-credit) the exact low and complementary Gauss endpoints at immutable commit 19b484a9449ef9e01b630d89123dba943be80ce0. This is a portable mathematics contribution, not a native H0/B0 run or formal Source Result.

## Exact coupled Green/Lagrange identity

For every integer m>=1 let p=6m+1 (primality not needed for the exact identity). Define rational coefficients
`d_0=1`, `d_(i+1)/d_i=(6i+1)(3i+1)/(36(i+1)^2)` (0<=i<m);
`e_1=1/10`, `e_(r+1)/e_r=36r^2/((6r+5)(3r+2))` (1<=r<m).
Put `D(z)=sum_(i=0)^m d_i z^i`, `E(z)=sum_(r=1)^m e_r z^r`, `V(z)=E(z^-1)`, `theta=z*d/dz`, and `L=36theta^2-z(6theta+1)(3theta+1)`.
Earlier exact operators establish `L D=-p(3m+1)d_m z^(m+1)`, `L V=-1+36m^2 e_m z^(-m)`.

**New theorem (exact in Q[z,z^-1]).** Define the coupled concomitant `W=D*theta(V)-V*theta(D)`. Then

```
(36-18z)*theta(W)-9z*W
   = -D+36m^2*e_m*z^(-m)*D+p*(3m+1)*d_m*z^(m+1)*V.       (G)
```

Proof: `L=(36-18z)theta^2-9z theta-z`. Subtract `V*L D` from `D*L V`; both zeroth-order terms cancel. Since `theta W=D*theta^2 V-V*theta^2 D`, the left side equals `D*L V-V*L D`. Substitute the exact endpoint identities.

For all integers k, extend `d_i=0` outside `0<=i<=m` and `e_r=0` outside `1<=r<=m`. Set `w_k=-sum_(i-r=k)(i+r)d_i e_r`, so `W=sum_k w_k z^k`. Coefficient extraction gives the exact **source-resolved finite recurrence**

```
36k*w_k-(18k-9)*w_(k-1)
 = -d_k+36m^2*e_m*d_(k+m)+p*(3m+1)*d_m*e_(m+1-k).        (G_k)
```

The three RHS populations preserve their indices and valuations: initial/low Gauss `-d_k` on k=0..m; complementary top source on k=-m..0; valuation-one p-adic low-cutoff endpoint on k=1..m. If p=6m+1 is prime, all displayed denominator factors through m are p-units, so the formula reduces coefficientwise modulo p^2 without losing the third source.

## Signed triangular observer requires its joint second port

The actual original signed Clausen correction is
`J_m=sum_(1<=r<=i<=m)(1+6(i-r))d_i e_r`.
Define, for k=0..m-1,
`c_k=sum_(i-r=k)d_i e_r`, `b_k=sum_(i-r=k)r*d_i e_r`.
Then `J_m=sum_(k>=0)(1+6k)c_k`, whereas `w_k=-k*c_k-2*b_k`. Thus for k>=1,

```
J_m=c_0 - sum_(k=1)^(m-1) ((1+6k)/k)*(w_k+2b_k).          (J-ports)
```

The c_0 channel is retained exactly; division by k is not used at k=0. The Green concomitant alone cannot be treated as the complete signed observer for a general labeled joint-coefficient population. A precise observer-fiber witness at k=0: pair weights (x1,x2) -> (x1+2t,x2-t) preserve w0=-2(x1+2x2), but change c0=x1+x2 by +t. This statement concerns the general joint-port interface, *not* a loss of mathematical uniqueness after the full original d/e sequences are supplied. In BRC terms, `(w,b,c_0)` is the scope-typed sufficient carrier for this formula.

## Executed exact arithmetic

Companion stdlib Python checker directly constructs labeled pairs (i,r), tests every coefficient of (G_k) for m=1..8 over exact Fraction, and tests all 80 primes p=6m+1 <=997 modulo p^2. It also calculates J mod p with the unchanged signed triangular cutoff. Representative [p,J mod p,w0 mod p^2,c0 mod p^2] are
[13,0,70,140], [19,6,125,43], [67,44,554,2585], [373,98,118235,90811].
Checks: ALL_CHECKS_PASS, exact rational m=1..8, 80 finite prime cases. This is evidence for the already-proved identities, not a universal numerical proof.

## Continuation and native gate

Next mathematical unit: derive an independent finite relation for the second port (b_k,c0) from the original Gauss moments/parameter jets, combine with (G_k), and test whether it yields the frozen full-p condition
`24(S_p/p)M_(2,p)-(p/3)(S_p/p)^2 = 1+2pJ_p (mod p^2)`
uniformly for p=13,19 (mod 24). Require the known nonzero signed J19=6 and J373=98. The original same-class p373 H0/B0 divided-power [X]U, native semilinear Frobenius/eta, odd Hesse/Green and independent replication remain NOT_EXECUTED/PENDING_OWNER under https://github.com/awdawmip/enterprise-math/issues/1559. Original research Source receipt `onhour11-20261106-1400-exact-research-lane-continuation` is to be reconciled by the same ID; no Source CLAIM, run, Result or admission is asserted here.

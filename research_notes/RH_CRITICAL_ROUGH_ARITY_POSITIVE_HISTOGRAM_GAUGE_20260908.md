# RH critical rough-arity positive histogram gauge

Status: `RESEARCH FRONTIER / EXACT STABLE-EULER GAUGE + RH-EQUIVALENT TRIANGULAR CRITERION / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Möbius / squarefree cells / rough factor-count parity / finite Euler gauge / Brownian cosine / critical BRC depth`

## 0. Purpose and typing

The fractional-alpha notes isolate rough factor-count parity but retain a common small-prime Möbius sign inside every branch. This note shows that, for the declared all-subscale first-cosine observer, the small-prime sign can itself be removed by an **invertible finite Euler gauge whose condition number is subpolynomial at the RH-critical cutoff**.

The result is an exact RH-equivalent criterion expressed as the parity Fourier coefficient of a completely positive finite rough-arity histogram.

This is an observer-specific T6-safe equivalence. It is not a universal deletion of small-prime provenance.

---

## 1. Remove small-prime parity

Fix y>=2. For squarefree n define

`r_y(n)=#{p|n:p>y}`.

Set

`eta_y(n)=mu(n)^2 (-1)^(r_y(n))`.

Thus eta_y is zero on nonsquarefree integers and, on squarefree Cells, its only sign is the parity of the prime factors exceeding y.

If `n=a b` is the unique prime-cut factorization with `P^+(a)<=y<P^-(b)`, then

`eta_y(n)=mu(a)^2 mu(b)`.

No small-prime sign remains.

Its Euler product is

`D_(eta_y)(s)`
`=prod_(p<=y)(1+p^-s) prod_(p>y)(1-p^-s)`.

Relative to Möbius,

`D_mu(s)=1/zeta(s)=prod_p(1-p^-s)`,

we have exactly

`D_(eta_y)(s)=C_y(s)D_mu(s)`,

where

`C_y(s)=prod_(p<=y)(1+p^-s)/(1-p^-s)`
`      =F_y(2s)/F_y(s)^2`.

Hence eta_y is a finite-prime Dirichlet-convolution gauge of mu.

Freeze:

`SMALL_PRIME_PARITY_GAUGE_REMOVAL`.

---

## 2. The gauge and its inverse have the same absolute half-line norm

Let c_y and d_y be the Dirichlet coefficients of `C_y` and `C_y^-1`.

For one prime p<=y, with x=p^-s,

`(1+x)/(1-x)=1+2x+2x^2+...`,

while

`(1-x)/(1+x)=1+2 sum_(k>=1)(-1)^k x^k`.

Therefore the local absolute coefficient series are identical. For every sigma>0,

`sum_n |c_y(n)| n^-sigma`
`=sum_n |d_y(n)| n^-sigma`
`=:K_y(sigma)`
`=prod_(p<=y)(1+p^-sigma)/(1-p^-sigma)`.

At sigma=1/2,

`log K_y(1/2)`
`=2 sum_(p<=y)p^-1/2+O(1)`
`=(4+o(1))sqrt(y)/log y`.

For the critical cutoff

`y_N=(log N)^2`,

this becomes

`log K_(y_N)(1/2)`
`=(2+o(1))log N/loglog N=o(log N)`.

Hence

`K_(y_N)(1/2)=N^o(1)`.

So both directions of the small-prime parity gauge are subpolynomially conditioned at the square-root Dirichlet weight.

---

## 3. Exact operator bound for the cosine flow on all subscales

Let

`w(x)=cos(pi x/2)`, `0<=x<=1`,

and for an arithmetic function f define

`S_f(T)=sum_(n<=T)f(n)w(n/T)`.

If `g=c*f` is Dirichlet convolution, then exactly

`S_g(T)=sum_(d<=T)c(d)S_f(T/d)`,

because

`w(dm/T)=w(m/(T/d))`.

Define the triangular square-root observer norm

`T_N(f)=sup_(1<=T<=N) |S_f(T)|/sqrt(T)`.

Then

`T_N(c*f)`
`<= [sum_d |c(d)|d^-1/2] T_N(f)`.

Applying this to the gauge and inverse gives the exact two-sided comparison

`T_N(eta_y)<=K_y(1/2)T_N(mu)`,

`T_N(mu)<=K_y(1/2)T_N(eta_y)`.

Thus at `y=y_N=(log N)^2`,

`T_N(eta_(y_N))=N^o(1) T_N(mu)`

in both directions in the epsilon-family sense.

This all-subscale norm is essential: the inverse convolution at scale N samples the same fixed-cutoff arithmetic function at scales `N/d`. A one-scale diagonal statement would not by itself be operation-safe for this inversion.

---

## 4. RH-equivalent triangular rough-parity criterion

The existing first Brownian/cosine note established

`RH <=> S_mu(T)=O_epsilon(T^(1/2+epsilon))`

for every epsilon>0.

Equivalently,

`RH <=> T_N(mu)=N^o(1)`

as N tends to infinity, where `N^o(1)` is understood in the standard full-epsilon sense.

Combining with the subpolynomial gauge condition number gives

`RH <=> T_N(eta_(y_N))=N^o(1)`,

that is,

`RH <=>`
`sup_(1<=T<=N)`
` |sum_(n<=T)eta_(y_N)(n) cos(pi n/(2T))|/sqrt(T)`
` =N^o(1)`.

Freeze interface:

`RH_CRITICAL_TRIANGULAR_ROUGH_PARITY_CRITERION`.

This is a reformulation/transport equivalence, not a proof of RH.

---

## 5. The criterion is a completely positive finite rough-arity histogram

For fixed ambient N put

`y=y_N=(log N)^2`

and

`K_N=ceil(log N/log y)`.

For every `T<=N`, a squarefree integer n<=T cannot have K_N distinct prime factors exceeding y, because that would force

`n>y^(K_N)>=N>=T`.

Define

`N_r(T;y)`
`=sum_(n<=T, mu(n)^2=1, r_y(n)=r) cos(pi n/(2T))`.

Every term is nonnegative, since the cosine weight is nonnegative on `[0,1]`. Therefore

`N_r(T;y)>=0`.

And exactly

`S_(eta_y)(T)`
`=sum_(r=0)^(K_N-1)(-1)^r N_r(T;y)`.

Thus the RH-equivalent criterion becomes

`sup_(T<=N)`
` |sum_(r<K_N)(-1)^r N_r(T;y_N)|/sqrt(T)`
` =N^o(1)`,

with

`K_N~(1/2)log N/loglog N`.

This is a positive BRC object all the way up to the final parity observer:

`POSITIVE ROUGH-ARITY HISTOGRAM -> z=-1 PARITY READOUT`.

No signed Cell mass remains inside the histogram.

---

## 6. Natural positive scale

Summing the histogram gives

`sum_r N_r(T;y)`
`=sum_(n<=T)mu(n)^2 cos(pi n/(2T))`.

By squarefree density and partial summation,

`sum_r N_r(T;y)~(12/pi^3)T`.

Hence the RH target is precisely square-root relative to the total positive histogram mass:

`|H_(T,y)(-1)|`
`<=N^o(1) sqrt(H_(T,y)(1))`,

uniformly in `T<=N`, where

`H_(T,y)(z)=sum_(r<K_N)N_r(T;y)z^r`.

This is a one-copy positive parity-coherence formulation. It should not be confused with the earlier Pair-BRC collision polynomial; the observer and positive denominator are different even though both have the same square-root target scale.

---

## 7. Exact positive prime-insertion recursion

The histogram admits a purely positive finite recursion.

Start with the squarefree y-smooth base and process primes p>y one at a time. If `F_P(T,z)` is the weighted generating polynomial after allowing rough primes only up to the current prime bound P, then adjoining a new prime p gives

`F_new(T,z)=F_old(T,z)+z F_old(T/p,z)`.

This is exact: a squarefree Cell either does not use p, or uses p exactly once, and in the latter case `w(pm/T)=w(m/(T/p))`.

At positive z this is a positive Pascal/dilation transfer. At the parity observer z=-1 it becomes

`F_new(T,-1)=F_old(T,-1)-F_old(T/p,-1)`.

Thus all signed cancellation is created only by the final character z=-1 applied to an otherwise positive prime-insertion circuit.

This recursion is another realization of

`X6 FIXED LOCAL WIDTH + SCALE-GROWING BRC DEPTH`.

Prime labels remain provenance, not native axes.

---

## 8. What this does and does not solve

This criterion removes a possible source of confusion:

- small-prime Möbius orientation is not an essential independent difficulty at the critical cutoff; it is an invertible finite Euler gauge with `N^o(1)` square-root-weight condition number;
- the hard mode can be placed entirely in the parity of the **number of rough prime factors**;
- the resulting data before the final observer are nonnegative counts.

But the final estimate is still RH-equivalent. Positivity of the transfer circuit does not imply cancellation of its parity Fourier coefficient.

In Mellin coordinates, the parity transfer product remains the `1/zeta` critical channel. Thus a proof cannot follow from positivity, total mass, or finite width alone.

The next admissible target is to compare this exact finite positive histogram/prime-insertion circuit with the continuum Buchstab--Dickman arity profile at the full critical depth, while keeping the prime-discrete error as a provenance-resolved source rather than bounding it by absolute value. The continuum parity mode already has square-root size at this depth; only the discrete source propagation remains unresolved.

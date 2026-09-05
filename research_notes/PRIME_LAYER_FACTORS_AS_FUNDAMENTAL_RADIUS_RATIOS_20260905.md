# Prime-layer completion factors are ratios of successive fundamental spectral radii

Status: `FREE_RESEARCH / EXACT FINITE-STATE CROSS-FAMILY STRENGTHENING / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Cross-family relevance: `#1158` Viète finite rotation completion.
Depends on:
- internal first-mode radius formula;
- prime-ary spectral layer factors;
- #1158 internal state identification.

## 1. Fundamental radius along a prime-power scale tower

For `q>=2`, the first normalized Dirichlet mode radius is

\[
\rho_{1,q}
=q\sqrt{u_{1,q}}
=2qS\left(\frac{\tau}{2q}\right).
\]

Fix a prime `p`.  Define

\[
\boxed{r_0:=2,}
\]

and for `j>=1`,

\[
\boxed{r_j:=\rho_{1,p^j}.}
\tag{RRF-1}

The virtual seed `r_0=2` is chosen so that the same ratio formula includes the first completed p-adic layer.

## 2. Prime spectral layer factor is a radius ratio

The prime-ary completion factor is

\[
c_{p,j}
=\frac{S(\tau/(2p^j))}
{pS(\tau/(2p^{j+1}))}.
\]

For `j>=1`, substitute

\[
S\left(\frac{\tau}{2p^j}\right)
=\frac{r_j}{2p^j}.
\]

Then

\[
c_{p,j}
=\frac{r_j/(2p^j)}
{p\,r_{j+1}/(2p^{j+1})}
=\frac{r_j}{r_{j+1}}.
\]

For `j=0`,

\[
c_{p,0}
=\frac1{pS(\tau/(2p))}
=\frac2{r_1}
=\frac{r_0}{r_1}.
\]

Thus uniformly

\[
\boxed{
c_{p,j}=\frac{r_j}{r_{j+1}},\qquad j\ge0.
}
\tag{RRF-2}

## 3. Exact finite telescoping certificate

For every finite `N>=1`,

\[
\boxed{
\prod_{j=0}^{N-1}c_{p,j}
=\frac{r_0}{r_N}
=\frac2{\rho_{1,p^N}}.
}
\tag{RRF-3}

This is a finite exact identity.  No infinite-product convergence is required.

Since

\[
\rho_{1,p^N}\to\tau,
\]

(RRF-3) completes to

\[
\prod_{j\ge0}c_{p,j}=2/\tau.
\]

Thus every prime-ary completion product is simply the telescoping product of successive first-mode radius refinements.

## 4. Dyadic specialization and #1158 finite state

For `p=2`, the #1158 internal dyadic state has

\[
\Pi_N=2^{N+1}s_N,
\]

with the already proved cross-family identification

\[
s_N=S\left(\frac{\tau}{2^{N+1}}\right).
\]

But

\[
\rho_{1,2^N}
=2^{N+1}S\left(\frac{\tau}{2^{N+1}}\right).
\]

Therefore for every finite `N>=1`,

\[
\boxed{
\Pi_N=\rho_{1,2^N}.
}
\tag{RRF-4}

This is stronger than equality of the limiting completion constants: the two constructions have the same scalar completion state at every dyadic refinement level.

## 5. Viète factors are consecutive spectral-radius ratios

The #1158 Viète half-root factor is

\[
c_N=C\left(\frac{\tau}{2^{N+1}}\right),
\qquad N\ge1.
\]

The dyadic layer formula gives

\[
c_N=c_{2,N-1}.
\]

Using (RRF-2) and (RRF-4),

\[
\boxed{
 c_N
=\frac{\rho_{1,2^{N-1}}}{\rho_{1,2^N}}
=\frac{\Pi_{N-1}}{\Pi_N},
}
\tag{RRF-5}

where the virtual seed convention is `Pi_0:=2` for the telescoping ratio; if the #1158 indexing reserves `Pi_0` differently, use the radius formula directly to avoid notation collision.

Hence the finite Viète product satisfies

\[
\boxed{
\prod_{j=1}^{N}c_j
=\frac2{\rho_{1,2^N}}
=\frac2{\Pi_N}.
}
\tag{RRF-6}

Its limit is `2/tau` because the finite fundamental radius itself converges to `tau`.

## 6. Interpretation

The bridge between #1158 and #1159 can now be stated at three strengths:

```text
completion level:
    Pi_rot = tau

factor level:
    Viete c_j = product of Wallis/Euler modes with fixed v_2 index

finite-state level:
    Pi_N = first Dirichlet mode radius rho_(1,2^N)
    c_N = rho_(1,2^(N-1)) / rho_(1,2^N)
```

So the two branches do not merely converge to the same constant; their finite scalar completion trajectories coincide under the dyadic scale identification.

## 7. General prime meaning

For every prime `p`, the sequence

\[
r_N=\rho_{1,p^N}
\]

is a prime-power finite spectral completion trajectory with

\[
r_N\to\tau.
\]

The completed product factor at level `N` is the relative contraction

\[
r_N/r_{N+1}.
\]

Thus Viète's nested radical is the quadratic/dyadic realization of a general principle:

`PRIME_LAYER_FACTOR = SUCCESSIVE_FUNDAMENTAL_RADIUS_RATIO`.

Freeze:

`P_ARY_COMPLETION_TRAJECTORY = FIRST_MODE_RADIUS_AT_LENGTH p^N`.

`LAYER_FACTOR = CONSECUTIVE_RADIUS_RATIO`.

`#1158 PI_N = #1159 RHO_(1,2^N) AT EVERY FINITE DYADIC LEVEL`.

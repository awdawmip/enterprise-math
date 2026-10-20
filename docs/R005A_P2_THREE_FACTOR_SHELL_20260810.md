# R005-A — p=2 Three-Factor Residual Shell Normal Form

Status: `PROVED CONDITIONAL NORMAL FORM + EXACT CERTIFICATE CROSS-CHECK / NOT CANONICAL`  
Date: `2026-08-10`

## 1. Setup

Work in a square basin `A=k^2<n<=U=k^2+2k`, with candidate prime horizon `F=k`. Assume the fourth-root core `q<=C4=floor(U^(1/4))` is fully forced.

By T-A21 and the generic residual lower bound, any residual composite has `Omega(n)=3`. Write its prime factors with multiplicity as `n=abc`, `a<=b<=c`.

## 2. T-A23 — exact three-factor shell

Every residual satisfies

`C4 < a <= C3=floor(U^(1/3))`.

Lower bound: a is a candidate divisor of n. Because n is residual, a is non-forced. The entire fourth-root core is forced, so `a>C4`.

Upper bound: `a^3<=abc=n<=U`, hence `a<=U^(1/3)` and therefore `a<=C3`.

Thus the smallest unresolved prime coordinate lies in the exact root annulus

`U^(1/4) < a <= U^(1/3)`.

## 3. The two smallest factors are candidate coordinates

Because `a>=2`, `b^2<=bc=n/a<=U/2<U`, hence `b<sqrt(U)`. Therefore both a and b lie below the candidate horizon and are candidate divisor witnesses. Since n is residual, both are non-forced.

The third factor c either lies above F, outside the candidate language, or if `c<=F` it too must be non-forced.

So a residual is a three-prime product whose first two multiplicative coordinates are unresolved witness coordinates.

## 4. Prime cubes are impossible

A residual support must contain at least two distinct non-forced candidate prime divisors. Therefore `n=q^3` can never be residual: its candidate support is the singleton `{q}`, so n would itself be an exclusive collision forcing q.

The only three-factor multiplicity types are therefore repeated-prime `q^2 r / q r^2` with two distinct primes, or squarefree `q r s` with three distinct primes.

## 5. Exact certificate cross-check

The separate 49-basin / 50-residual verifier was replayed through this normal form. Every certificate satisfies `Omega=3`, the exact root annulus, candidate/non-forced status of the first two factors, and at least two distinct support primes.

The finite family splits into:

- 45 repeated-prime residuals;
- 5 squarefree residuals.

This check does not claim the 50 examples are exhaustive through a numerical cutoff.

## 6. Multiplicative shell geometry

The square-basin residual problem is localized to `k^2<abc<(k+1)^2` with `U^(1/4)<a<=U^(1/3)` and `a<=b<=c`.

In logarithmic coordinates `alpha=log(a)/log(U)`, `beta=log(b)/log(U)`, `gamma=log(c)/log(U)`, the shell lies near `alpha+beta+gamma=1` with exact smallest-coordinate restriction `1/4<alpha<=1/3`.

This gives a precise arithmetic meaning to a thin collapse-field stratum: residual ambiguity is confined between the fourth-root and cube-root precision surfaces. The logarithmic picture is an interpretation of exact multiplicative inequalities, not a new Euclidean-geometry theorem.

## 7. Algorithmic consequence

A p=2 residual search should not enumerate all composites. A structurally aligned search is:

1. identify non-forced prime witnesses in `C4<q<=C3`;
2. pair them with larger non-forced candidate witnesses;
3. solve the thin product constraint `k^2<abc<=k^2+2k`;
4. test whether the third factor is prime and either above F or also non-forced.

This is the natural p=2 analogue of the prime-gap reciprocal search used for p=3.

## 8. Relation to the finite external-gap arity theorem

Under the external double-checked gap premise, the fourth-root core is forced for `440,232<=k<=894,427,190`. Throughout that interval, any square-basin residual must lie on this exact three-factor root annulus.

Thus the open p=2 problem inside the certified interval is no longer how many factors an unresolved composite can have. It is which non-forced prime pairs can actually close a three-factor product inside the width-2k square shell.

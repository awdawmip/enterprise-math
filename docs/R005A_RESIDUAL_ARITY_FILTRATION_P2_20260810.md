# R005-A — Residual Arity Filtration and Exact Square-Basin Certificate Family

Status: `PROVED GENERIC FILTRATION + 49 EXACT NO-LEAST BASIN CERTIFICATES / NOT EXHAUSTIVENESS CLAIM / NOT CANONICAL`  
Date: `2026-08-10`

## 1. T-A21 — residual arity filtration

Let the divisor-witness domain be `A<n<=U`, with candidate prime witnesses `q<=floor(sqrt(U))`.

For integer `m>=3`, suppose every candidate prime

`q<=floor(U^(1/m))`

is forced. Then every residual composite n satisfies

`Omega(n)<=m-1`,

where Omega counts prime factors with multiplicity.

Proof: if `Omega(n)>=m`, the smallest prime divisor s obeys `s^m<=n<=U`, hence `s<=U^(1/m)`. For `m>=2`, s lies below the square-root candidate horizon. Since n is residual, every candidate prime divisor of n is non-forced, contradicting the forced m-root core.

Thus nested root cores control the maximum multiplicative complexity of the unresolved residual fiber.

## 2. T-A20 is the m=3 terminal case

Generic R005 structure already gives `Omega(n)>=3` for every residual: residual support contains two distinct non-forced candidate divisors; their product is at most A; crossing above A requires at least one further prime factor.

Therefore:

- force the fourth-root core => every residual has exactly `Omega=3`;
- force the cube-root core => residual would need both `Omega>=3` and `Omega<=2`, impossible.

So the cube-root least-basis theorem is the terminal member of a more general residual arity filtration.

## 3. Observation precision ladder

The divisor-witness language has nested cores

`U^(1/2) ⊃ U^(1/3) ⊃ U^(1/4) ⊃ ...`

with different meanings:

- square-root horizon: complete candidate-factor screening language;
- cube-root forced core: eliminates the entire residual fiber;
- fourth-root forced core: any residual is exactly three-factor;
- fifth-root forced core: residual complexity at most four factors;
- general m-th-root forced core: residual `Omega<=m-1`.

Smaller mandatory observation cores need not decide primality, but they bound the complexity of what remains unresolved.

## 4. Square basins lie on the residual side

For p=2, `U=k^2+2k`. The cube-root core is scale `k^(2/3)`; forcing it would eliminate every residual. Actual no-least square basins therefore require a non-forced witness inside that core.

The fourth-root core is scale `k^(1/2)`. If it is forced, residuals may still exist, but T-A21 says they must have exactly three prime factors. This creates an exact structural slot for forms `q^2 r` and `q r s`.

## 5. Exact certificate family

A discovery search surfaced additional square-basin failures beyond the original bounded atlas. Rather than treating discovery as proof, a separate pure-Python verifier checks each certificate from first principles.

Combined with the earlier examples, it verifies:

- 49 distinct square basins;
- 50 residual composites;
- largest listed basin `k=35901`.

For every listed residual it independently checks:

1. exact prime factorization;
2. membership in `k^2<n<(k+1)^2`;
3. every candidate prime factor is genuinely non-forced, by exhaustively checking all T-A12 exclusive-collision forms `q^e` and `q^e*r` with prime `r>k`;
4. every candidate prime up to `floor(U^(1/4))` is forced;
5. `Omega(n)=3`;
6. at least one non-forced support witness lies in the cube-root core, as required by T-A20.

These are exact no-least certificates, not just factorization curiosities. The set is **not claimed exhaustive through any cutoff**.

## 6. Sharpness

In every listed basin the fourth-root core is fully forced, yet an `Omega=3` residual remains. Therefore

`U^(1/4) core forced` does not imply `least basis exists`.

It implies only that any residual has `Omega=3`.

Thus the m=4 arity statement is genuinely weaker than the m=3 least-basis statement and is sharp on an explicit finite family.

## 7. Collapse-field interpretation

For square basins the certified unresolved states lie on a three-factor multiplicative shell `k^2<abc<(k+1)^2`. In logarithmic coordinates this is a thin slab near `log a + log b + log c = 2 log k`.

The two observed finite patterns are repeated-coordinate faces `q^2 r` and squarefree interior points `q r s`. The cube-root and fourth-root cores define nested coordinate-resolution boundaries inside this multiplicative shell.

This is an interpretation of the proved arithmetic filtration, not a Euclidean-geometry theorem.

## 8. Next

- determine whether a square-basin residual with `Omega>=4` exists;
- T-A21 says such an example requires a non-forced witness inside the fourth-root core;
- search fourth-root-core failures directly instead of all composites;
- classify the `Omega=3` thin-shell equations together with non-forcedness prime-gap conditions;
- formalize T-A21 before encoding the finite counterexample family in Lean.

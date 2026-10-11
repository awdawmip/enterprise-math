# Finite global Hesse/Hasse check

Status: **DIRECTED / SHARED CONTEXT / NONBLIND / NONOFFICIAL DR**. This finite continuation used the exposed frozen draft, the parent's quadratic-transform/ODE hint and its subsequently saved derivation. No professional query, remote read/write, identity/session/CLAIM, new branch or native acceptance occurred. The author files were not modified.

## Actual result

The directly extracted ternary Hasse polynomial equals the corrected Fricke pullback, coefficient by coefficient, at both requested primes. Its H-coordinate polynomial is monic of degrees 18 and 36 and squarefree. The old per-k `27^-k` expression is a different polynomial and fails at every one of the six marked lifts above X=216 for each prime.

All concrete pairs below mean `a+b sqrt(2)` in F_p[sqrt(2)], with 2 a nonsquare for both primes.

| p | degree | gcd with Hesse j=1728 factor | H above X=216 | correct Hasse value | old extra-27^-k value |
|---:|---:|---:|---|---|---|
| 19 | 18 | 6 | 5+3 sqrt(2) | 0 | 10+15 sqrt(2) |
| 37 | 36 | 0 | 4+8 sqrt(2) | 0 | 25+17 sqrt(2) |

At p=19, S(X)=X³+6X²+5X+12=(X−7)(X²−6X+1). At p=37 the ascending S coefficients are [11,34,27,7,30,6,1]. The old and corrected H polynomials have gcd degrees 0 and 12 respectively, so the bad p37 formula may accidentally share some global roots while still failing all six requested X=216 lifts. Degree/monicity alone would not detect the normalization error.

The script independently constructs the coefficient of `(xyz)^(p−1)` in `(x³+y³+z³−3hxyz)^(p−1)` via exact integer multinomials. It does not import or execute the author script. It also checks the finite-field Gauss equations, coefficient recurrence, endpoints, squarefreeness and the two elliptic correspondence square identities. Actual invocation:

`PYTHONDONTWRITEBYTECODE=1 python check_global_hasse.py`

Actual output: `PASS`, primes [19,37], j1728 gcd degrees [6,0], old-factor failures [6,6]. `RESULTS.json` retains the exact coefficients, factorization, counterexamples and source pins. No larger regression was performed.

## Finite-characteristic identity for every p=6m+1≥7

Use the explicitly inherited hypergeometric definition

`K(z)=Σ_{k=0}^m binom(m,k)binom(2m,k) z^k`, `S(X)=X^m K(108/X)`.

Here the identification of this explicit S with the task's named `S_p^(3A)` is an inherited input. The calculation below establishes the polynomial identity for that explicit S; it does not independently re-prove Sakai's named-polynomial theorem.

In F_p, −m=1/6 and −2m=1/3. The terminating coefficient recurrence gives

`z(1−z)K''+(1−3z/2)K'−K/18=0`.

For `F(x)=K(4x(1−x))`, the chain rule gives

`x(1−x)F''+(1−2x)F'−2F/9 = 4[z(1−z)K''+(1−3z/2)K'−K/18]`.

The three coefficients of K'', K' and K were independently symbolically subtracted in the script and each difference was exactly zero. This identity divides by neither x nor 1−2x. Since deg F≤2m<p and F(0)=1, its coefficients satisfy

`(n+1)² f_(n+1)=(n+1/3)(n+2/3) f_n`.

For 0≤n<2m every denominator is nonzero, giving uniquely

`f_n=(3n)!/[27^n(n!)³]`, 0≤n≤2m.

All factorial arguments are ≤6m=p−1. No characteristic-zero infinite series is reduced through a denominator divisible by p. Direct multinomial extraction independently gives the same polynomial:

`A_p(h)=Σ_{a=0}^{2m} ((p−1)!/[a!³(p−1−3a)!]) (−3h)^(p−1−3a)`

`=Σ_{a=0}^{2m} (3a)!/[27^a(a!)³] h^(6m−3a)`.

The factorial-ratio sign (−1)^(3a) cancels the sign from (−3)^(-3a), and (−3)^(p−1)=1. Substituting x=1/h³ and multiplying by h^(6m) now yields, as a polynomial identity including h=0,

`A_p(h)=27^(−m)(h³−1)^m S(27h⁶/(h³−1))`.

With h=(H+3)/3, A=(H+3)^6 and B=(H+3)^3−27, this becomes

`P_H(H)=27^(−2m) B^m S(A/B)=Σ s_k A^(m−k)B^k`,

because 27^(2m)=3^(p−1)=1. Its leading coefficient is 1. An extra individual 27^(−k) would instead change the argument of S and is not a permissible normalization.

## Population and elliptic boundaries

The standard elliptic Hasse/Frobenius criterion is the mathematical input connecting A_p to supersingularity, not a consequence of matching degrees. For a smooth plane cubic F_h=0, the exact sequence from multiplication by F_h identifies H¹(O_E) with H²(O_P²(−3)). Its Čech generator is 1/(xyz); Frobenius has image represented by F_h^(p−1)/(x^p y^p z^p). Among monomials of the required total degree, only x^(p−1)y^(p−1)z^(p−1) survives with all three exponents negative in that Čech quotient. Hence the Frobenius scalar is exactly A_p(h). Its vanishing is the classical smooth genus-one supersingularity criterion.

For the Hesse family in characteristic p>3, smoothness requires h³≠1. The identity gives A_p=1 at h³=1; the finite cusps are excluded. Its nonzero leading term excludes a zero at the infinity cusp when homogenized in degree p−1. Thus, using this standard criterion and the already fixed marked Hesse model, the corrected pullback describes the actual Hesse supersingular root set. This is a Hasse polynomial assertion; it does not yet identify a polynomial or differential chosen by a particular p-adic period formula.

The frozen draft's simplicity argument is sound: K(0)=1; finite Chu–Vandermonde gives K(1)=binom(3m,m)≠0 because 3m<p. At a double root r≠0,1 the Gauss ODE recursively forces every Taylor coefficient to zero: the leading recurrence factor r(1−r)(n+2)(n+1) is invertible through degree m<p. This contradicts K(0)=1. The inherited exact discriminant `3^12 X^5(X−108)^3` places the finite branch values at 0 and108, and neither is a root of S. Therefore the degree-six pullback has p−1 distinct finite roots. The discriminant identity itself was already checked in the exposed local review; this helper did not start another all-prime regression.

Elliptic j=1728 has the exact Hesse numerator identity

`h³(h³+8)³−64(h³−1)³=(h⁶−20h³−8)²`.

Let Q(h)=h⁶−20h³−8. Its six distinct roots are j1728 parameters, not a new missing factor to append automatically. At p19, gcd(A_p,Q)=Q, with multiplicity one in A_p; at p37 the gcd is 1. This matches p≡3/1 mod4 respectively. The Fricke identity `R(1728,X)=(X²−576X−1728)²` is also checked exactly. Its p19 quadratic factor in S includes the elliptic contribution, but its entire H pullback should not be mislabeled as only the j1728 population: the Fricke correspondence also contains the other 3-isogenous j sheet.

## Fixed-source scope

Draft pin: 14059 bytes, SHA256 `19b59309b7acc37fb2fa2681ae63273886edf81a960932a697e1eec6267e0772`. Author script: 6026 bytes, SHA256 `300dbfcc57746e989c86ef8a804335b79708f8224bc71ad33df7349e53a1e209`.

The fixed Betina–Lecouturier TeX is 63224 bytes, SHA256 `81835e700f2cec78a89cd9e4b81b155f7b086035521f2efe2cdba19d75a0242b`. Its lines 622 and625 state the N=3 appendix assumption p≡1 mod3 and genus p−2/count p−1. Lines 635 and642 distinguish the simple base-coordinate pole from its double pole on the higher curve. These passages were read as source conditions, not as a source proof of the Hasse/pullback identity or the proposed G_p relation.

The parent's `GLOBAL_ODE_IDENTITY_DERIVATION.md` was fully cross-read after the concrete calculation and agrees with the finite-characteristic derivation above. It is shared directed input, not a blind independent source.

No issue remains in the corrected polynomial for this bounded check. Specific period-polynomial identification, differential/normal-parameter normalization, higher-curve cusp conventions, divided p-adic digits, G_p identification and UR remain outside the verified conclusion. No Source mathematical disposition or parent-completion claim is made.

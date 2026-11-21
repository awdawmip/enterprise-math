# EC49FVB — Three-prime valuation sieve for rational-width lattice phases

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKS / PARENT_DEPENDENT / NOT_REVIEWED.
Frozen BRC16943: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Predecessor EC49FVA PR #2868 @ f6c13f67c8b36ec7a3cbb15ca207b320ae058162. Bernoulli hit observer only; no native signed BRC/X6 transfer or formal Result/Review.

## Statement and model

Use frozen exact rationals
\[
\beta=3/637,\quad \gamma=\beta(E-1)=141024/1653649,\quad
u=4822040484/8132285009.
\]
For \(x\in(0,1)\), define
\[
T_0=(1-x)(1-\beta x),\quad T_E=(1-x)(1+\gamma x),\quad
a=1-T_0=x(1+\beta-\beta x),\quad b=1-uT_E,
\]
\[
R=T_0/(uT_E),\qquad S=bT_0/(auT_E),\qquad t(x)=\log R/\log S.
\]
The frozen model's strict order \(0<a<b<1\) implies \(1<R<S\) and \(0<t(x)<1\).

Let \(M=8132285009=29\cdot673\cdot416677\). Let the set of eight residue classes modulo M be
\[
\mathcal H=\{1,3496921755,3738594415,5459887102,
5701559762,5927647003,6169319663,7890612350\}.
\]

**Theorem.** For EVERY reduced rational width \(x=m/d\in(0,1)\), the phase \(t(x)\) is irrational whenever (i) \(\gcd(d,M)>1\), or (ii) \(\gcd(d,M)=1\) and \(m d^{-1}\bmod M\notin\mathcal H\).

The coarse certificate thus covers \(M-8=8,132,285,001\) of \(M=8,132,285,009\) residue classes for M-unit denominators, and ALL rational widths whose reduced denominators share a prime with M. The eight remaining congruence classes are unresolved by this coarse sieve; no rational phase is asserted in them.

**Primewise formulation.** For \(p\in\{29,673,416677\}\), irrationality holds if \(p\mid d\), or if \(p\nmid d\) and \(x\bmod p\notin\{1,\rho_p\}\), where
\[
(\rho_{29},\rho_{673},\rho_{416677})=(23,295,168371).
\]
The respective certified p-integral residue counts are 27/29, 671/673 and 416675/416677.

## Complete proof

If \(t(x)=h/k\) in lowest terms, then \(0<h<k\), \(R^k=S^h\), so every prime valuation satisfies
\[
k\,v_p(R)=h\,v_p(S). \tag{1}
\]
We contradict (1) at some prime p dividing M. The integer M is squarefree with prime factors exactly 29, 673 and 416677. For each p, \(v_p(u)=-1\), and \(\beta,\gamma,1-\beta,1+\gamma\) have p-unit numerator and denominator. The exact reductions are:

| p | beta mod p | gamma mod p | zeroes of a | zeroes of T0 | zeroes of TE |
|---:|---:|---:|---|---|---|
|29|26|5|0,20|1,19|1,23|
|673|56|73|0,662|1,661|1,295|
|416677|253146|361339|0,277998|1,277997|1,168371|

Every row follows directly from the displayed factorized polynomials and modular inverses. The factors other than \(1-x\) at \(x=1\) remain p-units.

**Denominator case.** If \(p\mid d\), write \(v_p(x)=-j\) with \(j\ge1\). Every quadratic has p-unit leading coefficient, yielding
\[
v_p(a)=v_p(T_0)=v_p(T_E)=-2j,\qquad v_p(b)=-2j-1.
\]
Consequently \((v_p(R),v_p(S))=(1,0)\), contradicting (1). This proves the whole denominator-divisible clause and removes the old denominator-coprimality limitation in this case.

**p-integral case.** If \(p\nmid d\), reduce \(x\) modulo p:
- Away from all three polynomial zero sets, \(a,T_0,T_E\) are units, \(v_p(b)=-1\), and \((v_p(R),v_p(S))=(1,0)\).
- At \(x\bmod p=0\) or the OTHER root of a, \(a\) vanishes to order \(j=v_p(a)\ge1\) while both T factors are units. Then \((v_p(R),v_p(S))=(1,-j)\).
- At the nonshared root of \(T_0\), \(j=v_p(T_0)\ge1\), while a and TE are units. Then \((v_p(R),v_p(S))=(j+1,j)\).

Each pair violates (1) because \(0<h<k\). The only residues not covered by this classification are 1 and the nonshared TE root \(\rho_p\). By CRT, simultaneously selecting one of these two residues at each of the three primes gives exactly 8 residues modulo M, and direct CRT reconstruction gives the explicit set \(\mathcal H\). For a reduced fraction with \(\gcd(d,M)=1\), the residue is \(m d^{-1}\) modulo M. The theorem follows.

## Further higher-lift refinement of the eight exceptional classes

These are additional SUFFICIENT conditions within the formerly excluded primewise residues.

For \(x\bmod p=1\), \(v_p(R)=1\). If \(v_p(1-x)\ge2\), then \(v_p(b)=0\) and \((v_p(R),v_p(S))=(1,1)\). The same pair arises if \(v_p(1-x)=1\) and \(v_p(b)=0\). As \(0<h<k\), a nonzero equal valuation pair contradicts (1).

For \(x\bmod p=\rho_p\), write \(j=v_p(1+\gamma x)\ge1\). If \(j\ge2\), then \(v_p(b)=0\) and \((v_p(R),v_p(S))=(1-j,1-j)\), again impossible in (1). If \(j=1\) and \(v_p(b)>0\), then \((v_p(R),v_p(S))=(0,v_p(b))\), also impossible.

Exact 29-adic examples: \(x=1/842\) gives \(v_{29}(1-x)=2\) and valuation pair \((1,1)\); \(x=603/842\) gives \(v_{29}(1+\gamma x)=2\) and pair \((-1,-1)\). The old 29-only exceptions \(x=1/30\) and \(x=23/30\) both have 673-adic pair \((1,0)\).

## Evidence and remaining questions

Companion script EC49FVB_THREE_PRIME_SIEVE_VERIFY.py, executed using Python's exact Fraction and integer modular arithmetic, returned ALL PASS. It verifies M's prime factors, all three polynomial root sets, arithmetic assumptions, residue counts, CRT residues, denominator-divisible cases and finite exact witnesses, with all covered residues checked at p=29 and p=673. Its finite checks audit arithmetic; the case proof establishes the infinite theorem.

This theorem is independent of the earlier unreviewed composite-minimax endpoint reduction: it proves irrationality of the rational readout phase t. Any downstream full-game second-order prefactor or least-favorable-prior claim remains conditional on the actual EC49FUQ/FUR hypotheses and the EC49FUZ/FVA author proof. Rational valuations are the exact carrier, logarithm is a derived readout; this is neither the full state nor the native physical X6 time.

Next: use prime-power lifts and other primes to reduce the eight unresolved CRT classes; determine whether every rational width has irrational t, or construct a rational-phase example. Then revisit uniform phase error bounds for varying widths.
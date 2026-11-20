# EC49FVB addendum — a two-adic certificate and four-prime CRT refinement

Date: 2026-11-21 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_EXHAUSTION_OF_DECLARED_FINITE_TEST_RANGE / PARENT_DEPENDENT / NOT_REVIEWED.
Companion to EC49FVB_THREE_PRIME_RATIONAL_PHASE_SIEVE_THEOREM.md in PR #2870. Same BRC16943 freeze, Bernoulli formulas and previous author-proof boundaries.

## Theorem

With \(\beta=3/637\), \(\gamma=141024/1653649\), \(u=4822040484/8132285009\), use the earlier rational functions \(a,T_0,T_E,b,R,S\) and \(t(x)=\log R/\log S\in(0,1)\).

For every reduced rational \(x=m/d\in(0,1)\):

1. If \(d\) is even, then \(t(x)\) is irrational.
2. If \(d\) is odd, \(m\) is odd, and \(m d^{-1}\bmod 8\in\{1,5,7\}\), then \(t(x)\) is irrational.

Combining these with the existing 29/673/416677-adic theorem, let \(M=8132285009\), \(L=8M=65058280072\), and \(\mathcal H\subset\mathbb Z/M\mathbb Z\) be the eight residues of the earlier note. The only rational widths NOT certified by the resulting coarse four-prime sieve have \(\gcd(d,L)=1\) and a residue \(m d^{-1}\pmod L\) that simultaneously satisfies
\[
x\bmod M\in\mathcal H,\qquad x\bmod8\in\{0,2,3,4,6\}.
\]
There are exactly \(8\cdot5=\boxed{40}\) such residue classes modulo \(L\). Hence the four-prime certificate covers \(L-40=\boxed{65,058,280,032}\) out of \(L=65,058,280,072\) unit-denominator classes, as well as every reduced rational width with a denominator sharing any prime factor with L.

The 40 classes remain *unresolved by this particular sieve*; no assertion that they contain a rational phase. The ratio is a modular count, not a real-density theorem.

## Complete two-adic proof

The exact prime valuations of coefficients are
\[
v_2(\beta)=0,\qquad v_2(\gamma)=5,\qquad v_2(u)=2.
\]
Rationality \(t=h/k\) with \(0<h<k\) would require \(k v_2(R)=h v_2(S)\).

**Even denominator.** Since m/d is reduced and d even, \(v_2(x)=-j<0\), \(j\ge1\). The terms of highest negative 2-adic order in the polynomials give
\[
v_2(a)=v_2(T_0)=-2j.
\]
Write \(w=v_2(uT_E)\). Since \(v_2(1-x)=-j\), we have
\[
v_2(1+\gamma x)=
\begin{cases}
0,&1\le j<5,\\
\kappa\ge1,&j=5,\\
5-j,&j>5,
\end{cases}
\]
and therefore
\[
w=\begin{cases}
2-j,&j<5,\\
-3+\kappa,&j=5,\\
7-2j,&j>5.
\end{cases}
\]
In all cases \(w>-2j\), and hence
\[
v_2(R)=-2j-w<0.
\]

If \(w<0\), then \(v_2(b)=w\), giving \(v_2(S)=0\). If \(w=0\), then \(uT_E\) is an odd 2-adic unit, so \(v_2(b)\ge1\) and \(v_2(S)=v_2(b)>0\). If \(w>0\), then \(v_2(b)=0\), so
\[
v_2(S)=-w<0,\qquad v_2(R)<v_2(S).
\]
All three valuation patterns contradict \(k v_2(R)=h v_2(S)\) for \(0<h<k\). Thus every even-denominator rational width has an exact irrationality witness.

**Both numerator and denominator odd.** Now \(x\) is a 2-adic unit. Since \(v_2(\gamma)=5\), \(v_2(1+\gamma x)=0\); since \(1+\beta-\beta x\) is odd, \(v_2(a)=0\); and since \(v_2(1-x)\ge1\), \(v_2(uT_E)\ge3\), so \(v_2(b)=0\). Thus
\[
v_2(R)=v_2(S)=v_2(1-\beta x)-2.
\]
Here \(\beta\equiv7\bmod8\). For \(x\bmod8=1,3,5,7\), the valuations \(v_2(1-\beta x)\) are respectively \(1,2,1,\ge3\). Hence the common valuation is nonzero unless \(x\equiv3\bmod8\). A common nonzero valuation contradicts \(0<h<k\), proving the second clause.

An odd denominator with even numerator is not certified by this 2-adic test alone; the combined CRT statement accurately leaves its even residues for the other primes to resolve.

## Verification and scope

The companion standard-library program EC49FVB_TWO_ADIC_REFINEMENT_VERIFY.py actually returned ALL PASS. Exact Fraction arithmetic exhaustively verifies every reduced fraction \(0<m<d\le180\): 3,313 even-denominator and 3,283 odd-numerator/odd-denominator fractions, plus exact coefficient valuations and the CRT class count. That finite check crosschecks the derivation; the preceding case proof establishes the theorem for every rational width.

Scientific novelty here is a new concrete sieve criterion for the frozen BRC16943 hit observer, not a claim to have discovered the general prime-valuation method or to have solved native X6 physical dynamics. The 2-adic residue is an exact information carrier preceding the log phase. The earlier EC49FUQ/FUR endpoint-reduction and downstream composite risk/prefactor statements remain author-proved and not independently reviewed.

**Next problem:** Investigate the 40 surviving CRT classes with additional valuation primes and higher lifts; distinguish existence of a rational phase from non-detection by this finite set of prime certificates.
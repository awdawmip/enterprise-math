# Legendre Pressure Test — Supplement 13

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact CRT/Möbius evaluation of the mirror-incidence first moment and a finite sufficient prime-existence certificate  
Depends on: P017 L042–L045  
Discipline: **this note does not prove Legendre's conjecture.** Inclusion-exclusion and the Chinese remainder theorem are classical. The result below turns the already-proved mirror necessary condition into an exact finite certificate for individual roots `k`.

## 1. From a necessary condition to a computable certificate

Let

\[
M=k(k+1),
\]

and let \(A_k\) be the square-free product of all primes \(a\le k\) dividing \(M\).

L045 defines

\[
S_k=\{1\le r<k:\gcd(r,A_k)=1\}
\]

and the total transverse incidence

\[
J_k
=
\sum_{r\in S_k}
\left(
|\operatorname{Supp}_{\mathrm{tr}}(M-r)|
+
|\operatorname{Supp}_{\mathrm{tr}}(M+r)|
\right).
\]

If the square basin contained no prime, L045 would force

\[
J_k\ge2|S_k|.
\]

Therefore the strict opposite inequality

\[
J_k<2|S_k|
\]

is already a sufficient certificate that the basin contains a prime.

The remaining issue is whether \(J_k\) and \(|S_k|\) can be evaluated directly from finite residue data, without testing the states inside the square basin for primality. They can.

---

## 2. Residue-class counter

For integers \(K\ge0\), \(m\ge1\), and a canonical positive residue

\[
1\le\rho<m,
\]

define

\[
\mathcal C(K;m,\rho)
=
\#\{1\le r\le K:r\equiv\rho\pmod m\}.
\]

Explicitly,

\[
\boxed{
\mathcal C(K;m,\rho)
=
\begin{cases}
0,&\rho>K,\\
1+\left\lfloor\dfrac{K-\rho}{m}\right\rfloor,&\rho\le K.
\end{cases}
}
\]

This is only arithmetic-progression counting.

---

## 3. L049 — Exact CRT/Möbius formula for surviving radii and transverse-prime incidence

Status: `PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`.

Put

\[
K=k-1.
\]

### Surviving radii

By Möbius inclusion-exclusion on the square-free anchor product,

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

### One transverse prime

Fix a transverse prime

\[
p\le k,
\qquad p\nmid M.
\]

Let \(N_p(k)\) be the L045 count of surviving radii for which \(p\) divides one of the two mirror states.

For each square-free \(a\mid A_k\), we must count radii satisfying

\[
a\mid r
\]

and either

\[
r\equiv M\pmod p
\]

or

\[
r\equiv-M\pmod p.
\]

Because \(p\nmid A_k\), one has \(\gcd(a,p)=1\). Write \(a^{-1}\) for the inverse of \(a\) modulo \(p\), and define

\[
 t^+_{a,p}
 =
(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}
 =
(-Ma^{-1})\bmod p.
\]

Since \(p\nmid M\), both residues lie in \(\{1,\ldots,p-1\}\). The unique positive CRT representatives modulo \(ap\) are then

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

Therefore

\[
\boxed{
N_p(k)
=
\sum_{a\mid A_k}
\mu(a)
\left[
\mathcal C(K;ap,\rho^+_{a,p})
+
\mathcal C(K;ap,\rho^-_{a,p})
\right].
}
\]

Finally, L045 gives

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### Proof

The formula for \(|S_k|\) is the ordinary identity

\[
\mathbf1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a)
\]

summed over \(1\le r\le K\).

For \(N_p(k)\), apply the same identity while imposing one of the two mirror congruences. Since \(a\) and \(p\) are coprime, writing \(r=at\) reduces the congruence to

\[
t\equiv\pm Ma^{-1}\pmod p,
\]

which has the displayed unique representative \(\rho^\pm_{a,p}\) modulo \(ap\). L043 guarantees that the plus and minus channels never describe the same radius for a transverse prime, so the two counts add directly. ∎

No state in the square basin is factored in this formula.

---

## 4. L050 — Exact mirror-incidence prime certificate

Status: `PROVED`.

Compute \(|S_k|\) and all \(N_p(k)\) from L049, and set

\[
J_k=\sum_{p\le k,\ p\nmid M}N_p(k).
\]

If

\[
\boxed{J_k<2|S_k|,}
\]

then

\[
\boxed{
\exists\text{ prime }q
\quad\text{with}\quad
k^2<q<(k+1)^2.
}
\]

### Proof

If no such prime existed, every mirror state would be composite; the two unpaired basin states are already composite. L045 would then imply

\[
J_k\ge2|S_k|,
\]

contradicting the strict inequality. ∎

Thus L050 is a finite sufficient certificate for Legendre at a chosen \(k\). It uses only:

- primes at most \(k\);
- the factorization of the explicit anchor \(k(k+1)\) by those primes;
- modular inverses and floor division.

It does not require primality testing of any number in \((k^2,(k+1)^2)\).

---

## 5. Boundary: the certificate is sufficient, not necessary

The strict inequality is not equivalent to prime existence.

For

\[
k=31,
\]

the exact formula gives

\[
|S_{31}|=15,
\qquad
J_{31}=30=2|S_{31}|.
\]

So L050 does not fire. Nevertheless

\[
967
\]

is prime and satisfies

\[
31^2<967<32^2.
\]

Therefore one must not silently upgrade L050 from a sufficient certificate to a characterization.

---

## 6. Computational pressure test

Status: `COMPUTATIONAL`, not a theorem.

The reference implementation compares the L049 residue formulas with direct mirror-support counting on bounded domains.

In a scan of

\[
3\le k\le1000,
\]

L050 fires for 273 values of \(k\). In other words, the first mirror-incidence moment has genuine proving power on a substantial finite subset, but it fails to certify most roots in that range.

This is the correct research signal:

> L045 is not merely decorative, but first-order incidence alone is too weak for a general proof.

The next leverage must therefore reduce the surviving incidence capacity using information that L049 deliberately forgets: joint prime collisions on the same side, exact-support closure, least-factor depth, or higher-order constraints between different radii.

---

## 7. Executable validation

`src/enterprise_math/p017_mirror_certificate.py` and `tests/test_p017_mirror_certificate.py` check that:

- the Möbius formula for \(|S_k|\) agrees with direct gcd enumeration;
- each \(N_p(k)\) formula agrees with direct surviving-radius counting;
- the sum of the prime-indexed formulas equals the L045 state-indexed \(J_k\);
- whenever L050 fires on bounded domains, direct inspection confirms at least one basin prime;
- \(k=31\) is the explicit boundary where the certificate fails while prime existence still holds;
- the reported `3<=k<=1000` coverage count is 273.

Finite computation audits the implementation and the stated coverage statistic; the formulas and certificate are proved above.

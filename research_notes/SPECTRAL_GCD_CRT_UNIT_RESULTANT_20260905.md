# Spectral gcd/CRT and the unit-resultant theorem

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive spectral factorization `Q_M=prod_(d|M,d>1) Psi_d`;
- native prime-power resultant law for distinct primitive factors.

## 1. Full spectral divisor lattice

Let

\[
Q_M(u)=(-1)^{M-1}D_{M-1}(u)
\]

be the monic finite Dirichlet spectral polynomial.  The primitive denominator factorization is

\[
\boxed{
Q_M(u)=\prod_{\substack{d\mid M\\d>1}}\Psi_d(u),
}
\tag{CRT-1}
\]

with pairwise distinct primitive factors.

Hence for `m,n>=1`, with

\[
g=\gcd(m,n),
\]

the monic polynomial gcd is

\[
\boxed{
\gcd_{\mathbf Z[u]}(Q_m,Q_n)=Q_g.
}
\tag{CRT-2}
\]

Here `Q_1=1`.

---

## 2. Remove the exact common scale block

Define the residual spectral polynomials

\[
A_{m,n}(u):=\frac{Q_m(u)}{Q_g(u)},
\qquad
B_{m,n}(u):=\frac{Q_n(u)}{Q_g(u)}.
\]

By (CRT-1),

\[
A_{m,n}
=
\prod_{\substack{d\mid m\\d\nmid g}}\Psi_d,
\qquad
B_{m,n}
=
\prod_{\substack{e\mid n\\e\nmid g}}\Psi_e.
\tag{CRT-3}
\]

Take one residual primitive index `d` from the first product and one `e` from the second.

Suppose `e/d=p^a` is a positive prime power.  Then `d|e`.  Since `e|n` and `d|m`, one has

\[
d\mid m,
\qquad
d\mid n,
\]

so `d|g`, contradicting `d \nmid g`.

The reverse possibility `d/e=p^a` similarly forces `e|g`, contradicting `e \nmid g`.

Therefore no cross pair of residual primitive factors has prime-power quotient in either direction.

---

## 3. Unit resultant after gcd removal

The native primitive resultant theorem says for distinct `d,e>1`,

\[
|\operatorname{Res}(\Psi_d,\Psi_e)|
=
\begin{cases}
p^{\varphi(\min(d,e))},&\max(d,e)/\min(d,e)=p^a,\\
1,&\text{otherwise}.
\end{cases}
\]

Section 2 excludes the first case for every cross residual pair.  Hence

\[
|\operatorname{Res}(\Psi_d,\Psi_e)|=1
\]

for all such `d,e`.

By multiplicativity of the resultant in both arguments,

\[
\boxed{
\left|
\operatorname{Res}\left(
\frac{Q_m}{Q_g},
\frac{Q_n}{Q_g}
\right)
\right|=1.
}
\tag{CRT-4}
\]

This is the spectral unit-resultant theorem.

Classification: `EXACT_FINITE_INTEGER_SPECTRAL_ARITHMETIC`.

---

## 4. Integral Bézout / spectral CRT

For monic integer polynomials, a resultant equal to `±1` implies an integral Bézout identity via the adjugate of the Sylvester matrix.  Therefore there exist

\[
P_{m,n}(u),R_{m,n}(u)\in\mathbf Z[u]
\]

such that

\[
\boxed{
P_{m,n}(u)\frac{Q_m(u)}{Q_g(u)}
+
R_{m,n}(u)\frac{Q_n(u)}{Q_g(u)}
=\pm1.
}
\tag{CRT-5}
\]

Thus, after removing the exact common scale block, the two residual finite spectral systems are not merely coprime over `Q[u]`; they are integrally comaximal.

Consequently

\[
\mathbf Z[u]/(A_{m,n}B_{m,n})
\cong
\mathbf Z[u]/(A_{m,n})
\times
\mathbf Z[u]/(B_{m,n}).
\tag{CRT-6}
\]

This is an exact polynomial CRT decomposition of the residual spectral algebra.

---

## 5. Coprime scale criterion

If `gcd(m,n)=1`, then `g=1` and `Q_g=1`.  Hence

\[
\boxed{
\gcd(m,n)=1
\Longrightarrow
|\operatorname{Res}(Q_m,Q_n)|=1.
}
\tag{CRT-7}
\]

Conversely, if `gcd(m,n)>1`, then `Q_g` is nonconstant and divides both `Q_m` and `Q_n`; therefore

\[
\operatorname{Res}(Q_m,Q_n)=0.
\]

Thus for `m,n>1`,

\[
\boxed{
\gcd(m,n)=1
\iff
|\operatorname{Res}(Q_m,Q_n)|=1.
}
\tag{CRT-8}
\]

while

\[
\boxed{
\gcd(m,n)>1
\iff
\operatorname{Res}(Q_m,Q_n)=0.
}
\tag{CRT-9}
\]

So ordinary integer coprimality is read exactly by the finite spectral resultant.

---

## 6. Exact common-factor extraction

Equation (CRT-2) gives more than a Boolean collision test.  The complete common root block of scales `m,n` is exactly the spectrum at their gcd scale:

\[
\boxed{
\operatorname{CommonSpectrum}(m,n)
=
\operatorname{Spectrum}(\gcd(m,n)).
}
\tag{CRT-10}
\]

No other algebraic collision remains after this block is removed, by (CRT-4).

For several scales `M_1,...,M_r`, the same divisor-factor argument gives

\[
\boxed{
\gcd(Q_{M_1},\ldots,Q_{M_r})
=Q_{\gcd(M_1,\ldots,M_r)}.
}
\tag{CRT-11}
\]

Thus the spectral gcd operation exactly mirrors the arithmetic gcd operation.

---

## 7. BRC root-block implication

The current BRC rational-function root-block compiler stores pairwise resultants as regularity guards.  For a module family whose declared scale blocks are exactly the finite spectral polynomials `Q_M`, the theorem supplies an exact simplification:

1. compute `g=gcd(m,n)` in the scale index;
2. extract the common block `Q_g` once;
3. compile residual blocks `Q_m/Q_g` and `Q_n/Q_g` separately;
4. no additional nontrivial cross-resultant guard is required between the residual spectral blocks, because their resultant is a unit `±1`.

This is stronger than checking a nonzero resultant at sampled parameter points.

Hard boundary: the simplification applies to the declared spectral scale family.  It does not say that arbitrary BRC root blocks with the same degrees or the same number of roots have unit resultant.

---

## 8. Structural consequence

The finite spectral family now reproduces the full arithmetic gcd/CRT pattern:

```text
integer scales m,n
  -> finite spectral polynomials Q_m,Q_n
  -> common factor exactly Q_gcd(m,n)
  -> remove common block
  -> every remaining primitive cross-resultant is a unit
  -> integral Bézout identity
  -> polynomial CRT decomposition
```

Freeze at free-research strength:

`SPECTRAL_POLYNOMIAL_GCD = ARITHMETIC_SCALE_GCD`.

`GCD_REMOVAL -> UNIT_RESIDUAL_RESULTANT`.

`COPRIME_INTEGER_SCALES <-> UNIT_FULL_SPECTRAL_RESULTANT`.

`BRC_SPECTRAL_ROOTBLOCK_GUARD_CAN_FACTOR_THROUGH_SCALE_GCD`.

# Legendre Pressure Test — Supplement 14

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact finite envelopes for all high-band composites and for the L049 three-prime hit union, followed by classical Mertens asymptotic corollaries  
Depends on: P017 L021, L030–L040, L049, T007 integer roots  
Prior art used only in the asymptotic step: [SRC-ROSSER-SCHOENFELD-1962-PRIME-ESTIMATES]  
Discipline: **this note does not prove Legendre's conjecture.** Reciprocal-prime Mertens estimates and prime-counting estimates are classical. The project-specific content is the square-derived high-band threshold, finite resource intervals, and finite hit-count envelopes obtained before those analytic estimates are invoked.

## 1. Two different high-band populations

Let

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\qquad |I_k|=2k.
\]

There are two useful high-band counts.

First, let `N_H(k)` be the number of **all composite states** in `I_k` whose least prime factor `p` satisfies

\[
p^2\ge2k.
\]

This includes both semiprime and three-prime high-band states.

Second, let `T_H(k)` be the number of high-band **three-prime** states. L049 already gives a stronger resource-sensitive inequality for this subset.

L050 gives an analytically transparent finite envelope for both populations and then passes those finite envelopes through classical prime estimates.

---

## 2. Finite envelope for all high-band composites

For every prime `p<=k`, L021 identifies the raw cofactor-window length with the old basin hit count:

\[
|W_p(k)|=H_p(k).
\]

The exact least-factor shell is only a subset of those raw multiples. Since least-factor shells are disjoint,

\[
N_H(k)
\le
A_H(k),
\]

where

\[
\boxed{
A_H(k)
=
\sum_{\substack{p\ \mathrm{prime}\\
\sqrt{2k}\le p\le k}}
H_p(k).
}
\]

This is already a finite exact integer inequality. It contains the semiprime contribution automatically; no primality estimate for the cofactor is needed.

---

## 3. Finite envelope for the L049 three-prime resource union

L049 defines, for each cofactor resource prime `r`, a realized hit-state union `X_r(k)` and capacity

\[
c_r(k)=|X_r(k)|.
\]

Let

\[
C_H(k)=\sum_r c_r(k).
\]

L049 proves

\[
2T_H(k)-E_H(k)\le C_H(k),
\]

where `E_H(k)` is the exact number of prime-square cofactor states.

If a resource prime `r` occurs, some eligible least prime `p` satisfies

\[
p^2\ge2k,
\qquad
p\le r,
\qquad
p^2r\le U,
\qquad
U=(k+1)^2-1=k(k+2).
\]

Hence

\[
\boxed{
\sqrt{2k}
\le r\le
\left\lfloor\frac{k+2}{2}\right\rfloor.
}
\]

Every state in `X_r(k)` is divisible by `r`, so

\[
c_r(k)\le H_r(k).
\]

Define

\[
\boxed{
B_H(k)
=
\sum_{\substack{r\ \mathrm{prime}\\
\sqrt{2k}\le r\le\lfloor(k+2)/2\rfloor}}
H_r(k).
}
\]

Then

\[
C_H(k)\le B_H(k).
\]

Each least-prime shell contributes at most one prime-square cofactor, and every such least prime satisfies `p^3<=U`. Therefore, without using any prime-counting theorem,

\[
E_H(k)\le R_3(U).
\]

Thus

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{B_H(k)+R_3(U)}{2}
\right\rfloor.
}
\]

Everything in Sections 2–3 is finite integer arithmetic.

---

## 4. L050 — High-band log(2) density ceilings

Status: `PROVED`; the limiting clauses are `CLASSICAL ANALYTIC COROLLARIES`.

The finite inequalities above imply

\[
\boxed{
\limsup_{k\to\infty}
\frac{N_H(k)}{2k}
\le
\log2.
}
\]

For the three-prime subset, L049 plus the narrower resource interval gives the stronger statement

\[
\boxed{
\limsup_{k\to\infty}
\frac{T_H(k)}{2k}
\le
\frac{\log2}{2}.
}
\]

Equivalently,

\[
\limsup_{k\to\infty}\frac{T_H(k)}k\le\log2.
\]

### Proof for all high-band composites

For every positive modulus `d`, the `2k`-state basin satisfies

\[
H_d(k)\le\frac{2k}{d}+1.
\]

Hence

\[
\frac{A_H(k)}{2k}
\le
\sum_{\substack{p\ \mathrm{prime}\\
\sqrt{2k}\le p\le k}}
\frac1p
+
\frac{\pi(k)}{2k}.
\]

The reciprocal-prime Mertens theorem gives

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+o(1),
\]

and standard prime-counting estimates give `pi(x)=o(x)`. Therefore the prime-counting remainder tends to zero, while

\[
\sum_{\sqrt{2k}\le p\le k}\frac1p
=
\log\log k-
\log\log\sqrt{2k}+o(1)
\longrightarrow
\log2.
\]

Since `N_H(k)<=A_H(k)`, the first boxed limit follows. ∎

### Proof for the three-prime subset

Similarly,

\[
\frac{B_H(k)}{2k}
\le
\sum_{\substack{r\ \mathrm{prime}\\
\sqrt{2k}\le r\le(k+2)/2}}
\frac1r
+
\frac{\pi((k+2)/2)}{2k}.
\]

The reciprocal-prime interval contributes

\[
\log\log\frac{k+2}{2}
-
\log\log\sqrt{2k}
+o(1)
\longrightarrow
\log2,
\]

and the prime-counting term tends to zero. Also

\[
\frac{R_3(U)}{2k}\longrightarrow0
\]

because `R_3(U)=O(k^(2/3))`.

Dividing the finite three-prime bound by `2k` gives

\[
\limsup\frac{T_H(k)}{2k}
\le
\frac{\log2}{2}.
\]

The Mertens and prime-counting steps in both arguments are established external mathematics. The project contribution is the reduction to the specific square-derived prime intervals before those results are used. ∎

---

## 5. Finite regression values

The integer implementation checks the finite inequalities only.

At `k=110`,

\[
A_H(110)=106,
\qquad
N_H(110)=19.
\]

For the three-prime resource envelope,

\[
B_H(110)=72,
\qquad
R_3(U)=23,
\]

so the coarse L050 three-prime envelope is `47`, while L049's exact hit union gives `4`.

At `k=500`,

\[
A_H(500)=534,
\qquad
N_H(500)=77,
\]

and

\[
B_H(500)=418,
\qquad
R_3(U)=63,
\]

so the coarse three-prime envelope is `240`, while L049 gives `17`.

The looseness is deliberate: L049 is the exact finite tool; L050 is the layer that exposes a uniform analytic constant.

---

## 6. What L050 actually changes

Before L050, the high-band semiprime contribution was still listed as a separate uncontrolled piece. The first L050 inequality changes that diagnosis: **all** high-band composites, including semiprimes, now have a nontrivial asymptotic density ceiling.

It follows that asymptotically at least a fraction

\[
1-\log2
\]

of the square-basin states are **not** high-band composites. They may still be lower-band composites, so this is not a prime-density theorem and gives no Legendre proof.

The remaining obstruction is now more concentrated:

1. lower least-factor shells satisfying `p^2<2k`;
2. a way to couple the high-band deficit to the mirror-incidence demand of L045;
3. a root-scale descent or other deterministic bound strong enough to prevent the lower band from filling the remaining fraction.

The next serious step should target the lower band or a genuine high/low-band coupling. Further refinements of the same Mertens interval should not be promoted unless they improve that obstruction.

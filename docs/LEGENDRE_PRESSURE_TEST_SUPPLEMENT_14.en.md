# Legendre Pressure Test — Supplement 14

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact finite envelope above the L049 hit-state union and its classical Mertens asymptotic corollary  
Depends on: P017 L039, L049, T007 integer roots  
Prior art used only in the asymptotic step: [SRC-ROSSER-SCHOENFELD-1962-PRIME-ESTIMATES]  
Discipline: **this note does not prove Legendre's conjecture.** The reciprocal-prime Mertens theorem and prime-counting estimates are classical. The project-specific content is the finite resource interval and finite hit-count envelope produced before those analytic estimates are invoked.

## 1. From exact hit unions to a coarser analytic envelope

L049 defines, for each cofactor resource prime `r`, the realized high-band hit-state union `X_r(k)` and capacity

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

where `T_H(k)` is the total number of high-band three-prime states and `E_H(k)` is the exact number of prime-square cofactor states.

The exact union is strong but not analytically transparent. The aim here is to place it below a simpler finite quantity whose asymptotic size can be read from classical prime estimates.

---

## 2. Universal resource interval

Let

\[
U=(k+1)^2-1=k(k+2).
\]

If a resource prime `r` occurs in the L049 high-band construction, there is an eligible least prime `p` with

\[
p^2\ge2k,
\qquad
p\le r,
\qquad
p^2r\le U.
\]

Therefore

\[
\boxed{r\ge\sqrt{2k}}
\]

and

\[
\boxed{
r\le\frac{U}{2k}=rac{k+2}{2}.
}
\]

Thus every high-band cofactor resource belongs to the finite prime interval

\[
\boxed{
\sqrt{2k}
\le r\le
\left\lfloor\frac{k+2}{2}\right\rfloor.
}
\]

This interval is forced entirely by the square-basin upper endpoint and the high-band threshold.

---

## 3. L050 — Finite hit-count envelope and the log(2) ceiling

Status: `PROVED`, with the asymptotic clause a `CLASSICAL ANALYTIC COROLLARY`.

Define

\[
B_H(k)
=
\sum_{\substack{r\ \mathrm{prime}\\
\sqrt{2k}\le r\le\lfloor(k+2)/2\rfloor}}
H_r(k).
\]

Then

\[
\boxed{C_H(k)\le B_H(k).}
\]

Moreover, with

\[
R_3(U)=\max\{m\in\mathbb N_0:m^3\le U\},
\]

we have the completely finite integer bound

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{B_H(k)+R_3(U)}{2}
\right\rfloor.
}
\]

Finally, classical reciprocal-prime and prime-counting estimates imply

\[
\boxed{
\limsup_{k\to\infty}\frac{T_H(k)}{k}
\le
\log 2.
}
\]

Equivalently, relative to the `2k` states in the open square basin,

\[
\boxed{
\limsup_{k\to\infty}\frac{T_H(k)}{2k}
\le
\frac{\log2}{2}.
}
\]

### Proof of the finite envelope

Every state in `X_r(k)` is divisible by `r`, so

\[
c_r(k)\le H_r(k).
\]

Section 2 shows that no resource prime outside the displayed interval can occur. Summing gives

\[
C_H(k)\le B_H(k).
\]

For the square correction, each least-prime shell contributes at most one prime-square cofactor. Every such shell has least prime `p` satisfying

\[
p^3\le U.
\]

Hence, without even using a prime-counting theorem,

\[
E_H(k)\le R_3(U).
\]

Combining this with L049,

\[
2T_H(k)-E_H(k)\le C_H(k)\le B_H(k),
\]

and therefore

\[
T_H(k)
\le
\left\lfloor\frac{B_H(k)+R_3(U)}2\right\rfloor.
\]

Everything up to this point is finite integer arithmetic. ∎

### Classical analytic corollary

The basin has length `2k`, so for every positive modulus `r`,

\[
H_r(k)
\le
\frac{2k}{r}+1.
\]

Therefore

\[
\frac{B_H(k)}{2k}
\le
\sum_{\substack{r\ \mathrm{prime}\\
\sqrt{2k}\le r\le(k+2)/2}}
\frac1r
+
\frac{\pi((k+2)/2)}{2k}.
\]

The reciprocal-prime Mertens theorem gives

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+o(1),
\]

while standard prime-counting estimates give

\[
\pi(x)=o(x).
\]

Hence the prime-counting remainder above tends to zero, while the reciprocal-prime interval contributes

\[
\log\log\frac{k+2}{2}
-
\log\log\sqrt{2k}
+o(1).
\]

Since

\[
\frac{\log((k+2)/2)}{\log\sqrt{2k}}
\longrightarrow2,
\]

this difference tends to

\[
\log2.
\]

Also

\[
\frac{R_3(U)}{2k}\longrightarrow0,
\]

because `R_3(U)=O(k^(2/3))`. Dividing the finite L050 bound by `k` yields

\[
\limsup_{k\to\infty}\frac{T_H(k)}k\le\log2.
\]

The Mertens and prime-counting steps are established external mathematics; only the square-derived endpoints and reduction to this prime interval are project-specific. ∎

---

## 4. Finite regression values

The integer reference implementation computes `B_H(k)` directly from the exact hit counts.

At

\[
k=110,
\]

it gives

\[
B_H(110)=72,
\qquad
R_3(U)=23,
\]

so the coarse finite L050 envelope is

\[
T_H(110)\le47.
\]

L049 itself gives the much sharper exact-union bound `4`. This is expected: L050 deliberately sacrifices state-union information to gain analytic transparency.

At

\[
k=500,
\]

we obtain

\[
B_H(500)=418,
\qquad
R_3(U)=63,
\]

and hence

\[
T_H(500)\le240,
\]

while the exact L049 union gives `17`.

Thus L050 is not a replacement for L049. Its role is to provide a uniform asymptotic ceiling from a quantity that is intentionally easier to estimate.

---

## 5. Pressure-test interpretation

The constant `log(2)` is not evidence for a new law of prime distribution. It is simply the classical reciprocal-prime mass of the project-derived resource window

\[
[\sqrt{2k},\,(k+2)/2].
\]

What is new under test is the chain

\[
\text{square basin}
\to
\text{high-band factor threshold}
\to
\text{finite resource interval}
\to
\text{L049 exact hit unions}
\to
\text{L050 analytic envelope}.
\]

The asymptotic result is useful because it proves that high-band **three-prime** composites alone occupy at most a fixed asymptotic fraction of the basin. But it remains far from Legendre: semiprimes and lower least-factor shells are not controlled by this constant.

The next serious target should therefore be one of:

1. a comparable nontrivial envelope for the semiprime contribution;
2. a decomposition of the lower band `p^2<2k` that transports it to a smaller root scale;
3. a genuine inequality coupling L049/L050 to the mirror-incidence demand of L045.

No further refinement of the same reciprocal-prime window should be promoted unless it improves one of these missing components.

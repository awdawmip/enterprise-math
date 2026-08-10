# P022 — Forced Franel Midpoint Lifting Is a Parameter-Transversality Problem

Status: `ACTIVE RESEARCH NOTE / EXACT FIRST-ORDER REDUCTION / GLOBAL NONVANISHING OPEN`  
Owner: `program/p022-geometry-v2`  
Depends on: Jarvis--Verrill mirror congruence; Franel recurrence; forced half-index zero  
Cross-route relevance: P018 defect/response; P023 minimal repair; p-adic precision lifting

## 1. The remaining `p^2` obstruction

For an odd prime

\[
p\equiv5,7\pmod8,
\]

put

\[
m=\frac{p-1}{2}.
\]

The mirror theorem already forces

\[
p\mid F_m.
\]

The stronger one-unit statement needed by the current half-defect program is

\[
p^2\nmid F_m.
\]

This note converts that divisibility question into an exact first-order transversality criterion.

---

## 2. Parameter derivative of the Franel hypergeometric function

Use the analytic/hypergeometric interpolation

\[
\mathcal F(x)
={}_3F_2(-x,-x,-x;1,1;-1).
\]

At every nonnegative integer `n`,

\[
\mathcal F(n)=F_n.
\]

Terms with `k>n` contain a cubic zero at `x=n`, so the first derivative is still the finite sum

\[
\boxed{
\dot F_n
:=\mathcal F'(n)
=3\sum_{k=0}^{n}\binom nk^3
\bigl(H_n-H_{n-k}\bigr).
}
\]

The Franel recurrence extends as the contiguous relation

\[
(n+1)^2F_{n+1}
=(7n^2+7n+2)F_n+8n^2F_{n-1}.
\]

Differentiating the parameter form gives

\[
\boxed{
L_n(\dot F)=-\Phi_n(F),
}
\]

where

\[
L_n(Y)
=(n+1)^2Y_{n+1}-(7n^2+7n+2)Y_n-8n^2Y_{n-1}
\]

and

\[
\Phi_n(F)
=2(n+1)F_{n+1}
-7(2n+1)F_n
-16nF_{n-1}.
\]

---

## 3. First-order refinement of the reflected recurrence

Define, for `0<=n<=p-1`,

\[
G_n=(-8)^nF_{p-1-n}.
\]

Jarvis--Verrill says

\[
G_n\equiv F_n\pmod p.
\]

Write

\[
G_n=F_n+pE_n\pmod{p^2}.
\]

Set

\[
r=p-1-n.
\]

Reflecting the exact Franel recurrence gives

\[
r^2G_{n+1}
=(7r^2+7r+2)G_n+8(r+1)^2G_{n-1}.
\]

Expanding

\[
r=-(n+1)+p
\]

to first order in `p`, subtracting the ordinary Franel recurrence, and dividing by `p` yields

\[
\boxed{
L_n(E)=\Phi_n(F)\pmod p.
}
\]

Thus

\[
L_n(E+\dot F)=0\pmod p.
\]

So `E+dot F` is a homogeneous Franel solution modulo `p`.

---

## 4. The homogeneous correction is a multiple of `F`

Let

\[
a=E_0=\frac{F_{p-1}-F_0}{p}\pmod p.
\]

No explicit formula for `a` is needed.

At the other initial point, use the exact Franel recurrence at `p-1`:

\[
p^2F_p
=(7(p-1)^2+7(p-1)+2)F_{p-1}
+8(p-1)^2F_{p-2}.
\]

Since

\[
G_1=-8F_{p-2}=F_1+pE_1=2+pE_1,
\]

reduction modulo `p^2` gives

\[
\boxed{E_1=2a-3\pmod p.}
\]

On the other hand,

\[
\dot F_0=0,
\qquad
\dot F_1=3.
\]

Therefore

\[
(E_0+\dot F_0,E_1+\dot F_1)
=(a,2a)
=a(F_0,F_1).
\]

Uniqueness of the second-order recurrence modulo `p` now gives

\[
\boxed{
E_n+\dot F_n=aF_n\pmod p
}
\]

for all indices before the recurrence denominator reaches `p`.

---

## 5. P022-LI25 — midpoint lift quotient equals half the parameter derivative

At the forced midpoint `m`, write

\[
F_m=pq_m\pmod{p^2}.
\]

Because

\[
(-8)^m\equiv-1\pmod p,
\]

we have

\[
E_m
=\frac{G_m-F_m}{p}
\equiv-2q_m\pmod p.
\]

But `F_m=0 mod p`, so the homogeneous relation in Section 4 gives

\[
E_m\equiv-\dot F_m\pmod p.
\]

Hence

\[
\boxed{
\frac{F_m}{p}
\equiv
\frac{\dot F_m}{2}
\pmod p.
}
\]

This is the exact desired first-order reduction.

Consequently,

\[
\boxed{
p^2\mid F_m
\iff
\dot F_m\equiv0\pmod p.}
\]

So the `p^2` exceptional problem is a **transversality problem**: is the forced midpoint zero simple in the parameter direction?

---

## 6. P022-LI26 — harmonic and central-binomial forms

From the derivative formula and symmetry under `k -> n-k`,

\[
\dot F_n
=3F_nH_n
-3\sum_{k=0}^{n}\binom nk^3H_k.
\]

At the forced midpoint, `F_m=0 mod p`, so LI25 becomes

\[
\boxed{
\frac{F_m}{p}
\equiv
-\frac32
\sum_{k=0}^{m}\binom mk^3H_k
\pmod p.
}
\]

Using

\[
\binom{m}{k}
\equiv
(-1)^k\frac{\binom{2k}{k}}{4^k}
\pmod p,
\]

we obtain the truncated harmonic-hypergeometric form

\[
\boxed{
\frac{F_m}{p}
\equiv
-\frac32
\sum_{k=0}^{m}
\frac{(-1)^k\binom{2k}{k}^3}{64^k}H_k
\pmod p.
}
\]

Thus a hypothetical Franel midpoint `p^2` exception is exactly a prime for which this harmonic truncated sum vanishes.

This is a substantially narrower target for the existing supercongruence literature than the original raw integer divisibility problem.

---

## 7. What has and has not been solved

LI25--LI26 prove exact equivalences.

They do **not** prove the global nonvanishing

\[
\dot F_{(p-1)/2}\not\equiv0\pmod p
\]

for every `p=5,7 mod 8`.

Current exact computations have found no exception in the tested forced classes, but finite nonvanishing is only pressure-test evidence.

The half-defect conjecture still requires two independent ingredients:

1. this midpoint transversality / simple-lift statement;
2. support avoidance for the canonical A-elimination.

The present theorem solves the *form* of the first obstruction, not its universal nonvanishing.

---

## 8. Prior-art boundary

Prior-art inputs:

- Franel recurrence;
- Jarvis--Verrill mirror congruence;
- standard hypergeometric interpolation and harmonic derivative of binomial coefficients.

P022-specific contribution is the first-order reflected-recurrence calculation and the resulting exact equivalence between midpoint `p^2` lifting and the parameter/harmonic transversality observable.

Historical novelty remains `NOVELTY_UNVERIFIED`; a matching formula may exist in the harmonic-supercongruence literature and should be checked before any novelty claim.

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_midpoint_transversality.py`;
- `tests/test_p022_barlow_franel_midpoint_transversality.py`.

The implementation computes the derivative both by the differentiated recurrence and by the finite harmonic formula, then cross-checks both against the independent mod-`p^2` recurrence oracle already present in the half-defect obstruction module.

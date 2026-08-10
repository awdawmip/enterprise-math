# P025 Supplement 80 — Cyclotomic Precision Horizon and Global Periodic Tail

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 78–79  
Hard block: `NONE`

## 1. Why Stage 79 is not yet a global tail theorem

Stage 79 proves that for one activated odd-prime equal-exponent cyclotomic signature,

\[
\frac{\#\text{allowed ratio classes}}{M}
\ll
\frac1T
\left(\frac{\ell-1}{2\ell+1}\right)^k.
\]

That is a fixed-signature density statement. A global counting theorem requires summing over all possible repeated moduli and all repeated-support patterns.

This supplement performs that summation in the regime where the repeated modulus is no larger than the finite prime-base observation window. It also isolates the exact boundary where the periodic-density model stops improving.

## 2. P025-T159 — the cyclotomic residual uniquely determines the repeated modulus

Let

\[
F=F_{\ell,\pm}
\]

be the nonlinear cyclotomic factor, and write its repeated prime factorization as

\[
F=\left(\prod_{i=1}^k r_i^{e_i}\right)S,
\qquad e_i\ge2,
\]

where `S` is squarefree and coprime to all `r_i`.

Define the cyclotomic multiplicity residual

\[
\boxed{d:=m(F)=\prod_{i=1}^k r_i^{e_i-1}.}
\]

The full repeated modulus is

\[
M=\prod_{i=1}^k r_i^{e_i}.
\]

Therefore

\[
\boxed{
M=d\operatorname{rad}(d).
}
\]

Conversely the exponent of every prime in `M` is exactly one larger than its exponent in `d`. Hence the map

\[
d\longleftrightarrow M=d\operatorname{rad}(d)
\]

is one-to-one.

The CRT class count also becomes a function of `d` alone:

\[
\boxed{
C_\ell(d):=(\ell-1)^{\omega(d)}.
}
\]

Thus a repeated cyclotomic signature may be indexed by the single residual integer `d` rather than by an independent pair `(M,k)`.

## 3. The signature-density weight

For a residual `d`, define

\[
\boxed{
w_\ell(d)
:=
\frac{(\ell-1)^{\omega(d)}}{d\operatorname{rad}(d)}.
}
\]

Only integers whose prime factors satisfy

\[
r\equiv1\pmod{2\ell}
\]

can occur, by Stage 79. Ignoring that support restriction only enlarges the sums below, but retaining it gives the natural theorem-native state.

The weight `w_ell(d)` is exactly

\[
\frac{\text{number of allowed CRT ratio classes}}
{\text{full repeated modulus}}.
\]

## 4. P025-T160 — weighted residual tail is arbitrarily close to `1/Y`

Fix

\[
0<\theta<1.
\]

For residuals supported on primes `1 mod 2ell`, consider

\[
K_{\ell,\theta}
:=
\sum_d
\frac{(\ell-1)^{\omega(d)}d^\theta}
{d\operatorname{rad}(d)}.
\]

This has Euler product

\[
K_{\ell,\theta}
=
\prod_{r\equiv1\,(2\ell)}
\left(
1+(\ell-1)
\sum_{f\ge1}
\frac{r^{f\theta}}{r^{f+1}}
\right).
\]

The local tail is

\[
\sum_{f\ge1}r^{-1-f(1-\theta)}
=
\frac{r^{-(2-\theta)}}{1-r^{-(1-\theta)}}.
\]

Since

\[
2-\theta>1,
\]

the Euler product converges absolutely. Therefore

\[
\boxed{K_{\ell,\theta}<\infty.}
\]

If `d>=Y`, then

\[
1\le(d/Y)^\theta.
\]

Hence

\[
\boxed{
\sum_{d\ge Y}w_\ell(d)
\le
K_{\ell,\theta}Y^{-\theta}.
}
\]

Thus the aggregate reciprocal signature density has a tail

\[
\boxed{O_{\ell,\theta}(Y^{-\theta})}
\]

for every fixed `theta<1`.

This is genuinely stronger than merely having a good bound for each fixed signature: all repeated-support patterns can be summed simultaneously in this weighted periodic regime.

## 5. Endpoint discipline

The above Mellin/Euler-product proof does **not** extend by simply setting `theta=1`.

At `theta=1`, for even one fixed allowed prime `r`, the local contribution becomes

\[
(\ell-1)\sum_{f\ge1}\frac1r,
\]

which diverges because arbitrary exponent towers `r^f` remain possible.

This does **not** prove that an exact `1/Y` tail is false. It proves only that the present moment argument has a real endpoint obstruction.

Therefore the correct status is:

\[
\boxed{
Y^{-1+\varepsilon}\text{-type control is proved by this method;}
\quad Y^{-1}\text{ remains unproved here.}
}
\]

## 6. P025-T161 — finite observation window and the periodic regime

Fix a prime-base height

\[
1\le p,q\le P.
\]

For one repeated residual `d`, let

\[
M=d\operatorname{rad}(d),
\qquad
C=(\ell-1)^{\omega(d)}.
\]

Stage 78's finite incidence bound gives at most

\[
C P
\left(
\left\lfloor\frac{P-1}{M}\right\rfloor+1
\right)
\]

ordered integer pairs compatible with those ratio classes.

If

\[
\boxed{M\le P,}
\]

then

\[
\left\lfloor\frac{P-1}{M}\right\rfloor+1
\le
\frac{2P}{M}.
\]

So the signature contributes at most

\[
\boxed{
2P^2\frac{C}{M}
=2P^2w_\ell(d).
}
\]

This is the **periodic precision regime**: the observation window contains at least one full modulus period, so congruence precision converts directly into density reduction.

## 7. P025-T162 — global periodic activated tail

Suppose the projective threshold is

\[
T\ge1.
\]

Stage 79 proves that every activated state satisfies

\[
d=m(F)\ge2T
\]

(with strictness on the difference branch).

Partition all activated pairs in the periodic regime by their exact residual `d`. Since `d` uniquely determines the repeated modulus, the exact classes form a disjoint semantic partition even though their divisibility envelopes may overlap.

Summing the Stage-161 bound and applying P025-T160 gives

\[
N^{\rm per}_{\ell,T}(P)
\le
2P^2
\sum_{d\ge2T}w_\ell(d)
\]

and hence, for every fixed `0<theta<1`,

\[
\boxed{
N^{\rm per}_{\ell,T}(P)
\ll_{\ell,\theta}
P^2T^{-\theta}.
}
\]

Primality, ordering `p>q`, and the exact cyclotomic equation can only reduce this elementary integer-pair envelope.

Thus **the entire periodic part of the odd-prime equal-exponent activated state has an aggregate pressure tail arbitrarily close to `1/T`**.

## 8. P025-T163 — supermodular precision forces a square-root residual floor

The periodic argument stops when

\[
\boxed{M>P.}
\]

This is not a proof failure caused by bad constants. It is a genuine change in finite-window semantics: a residue class modulo `M` now contains at most one candidate `p` for a fixed `q` in the height-`P` window, so further increasing `M` no longer creates another factor `P/M`.

But P025-T159 gives

\[
M=d\operatorname{rad}(d).
\]

Since

\[
\operatorname{rad}(d)\le d,
\]

one has

\[
M\le d^2.
\]

Therefore

\[
\boxed{
M>P
\Longrightarrow
d>\sqrt P.
}
\]

So every state beyond the congruence observation horizon automatically lies in the much stronger residual tail

\[
\boxed{m(F)>\sqrt P.}
\]

Combining this with activation gives

\[
\boxed{
d>\max\{2T,\sqrt P\}}
\]

up to the sum/difference strictness convention.

## 9. The exact regime split

Stage 80 therefore divides the global problem into two mathematically different regions:

\[
\boxed{
M\le P:
\quad
N^{\rm per}_{\ell,T}(P)
\ll_{\ell,\theta}P^2T^{-\theta}
\quad(\theta<1),
}
\]

and

\[
\boxed{
M>P:
\quad
m(F)>\sqrt P.
}
\]

The second region should **not** be attacked by pretending the periodic density formula remains valid. It requires a value-side theorem for cyclotomic factors with very large multiplicity residual.

This is the new hard boundary.

## 10. Precision-horizon interpretation

The arithmetic mechanism is an exact instance of finite precision horizon saturation.

Below the horizon:

\[
M\le P,
\]

the observation window resolves many periods, and each extra congruence bit lowers candidate density.

Above the horizon:

\[
M>P,
\]

a residue class is already finer than the observation window. Increasing the modulus further no longer pays according to the same `P/M` cost model. The correct state transition is not "keep increasing congruence precision" but

\[
\boxed{
\text{congruence precision}
\to
\text{large-residual value state}.
}
\]

This is exactly the type of theorem-native coordinate switch that P018/P023/E002 were designed to expose.

## 11. Prior-art / novelty discipline

Euler products, absolute-convergence arguments and elementary residue-class incidence are classical mathematics. P025 claims none of them individually.

The project-side candidate is the exact residual-to-modulus bijection, its combination with the Stage-79 projective activation threshold, and the resulting periodic/supermodular precision-horizon split. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_cyclotomic_precision_horizon.py`;
- `tests/test_abc_cyclotomic_precision_horizon.py`.

The executable layer checks

\[
M=d\operatorname{rad}(d),
\]

the exact finite incidence envelope, the fixed-signature pressure bound, and the implication

\[
M>P\Rightarrow d^2>P
\]

on cube and fifth-power fixtures.

## 13. Next frontier

No hard block exists. Continue with:

1. attack the supermodular region `m(F)>sqrt(P)` using the algebraic structure of the cyclotomic value rather than more congruence refinement;
2. test whether the quadratic cube factors admit a stronger value-side count through Eisenstein norms / binary quadratic representations;
3. compare even exponent four, where the hard-state carrier can remain in centered linear factors and the odd-prime cyclotomic theorem fails;
4. relay the horizon-saturation mechanism to A2/E002 as a candidate cross-route law, without promoting the cyclotomic arithmetic itself into Foundation.

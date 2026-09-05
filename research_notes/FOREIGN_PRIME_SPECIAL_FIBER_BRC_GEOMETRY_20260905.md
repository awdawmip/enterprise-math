# Foreign-prime special fiber and the geometric meaning of BRC equalization

Status: `FREE_RESEARCH / EXACT MOD-p FINITE-GEOMETRIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- Frobenius collapse of primitive p-adic levels;
- primitive discriminant formula;
- exact spectral-pullback Weighted-BRC coordinates.

## 1. Foreign prime hypothesis

Let `d>1` and let `p` be an odd prime with

\[
p\nmid d.
\]

Equivalently `p\nmid2d`.  This is the clean foreign-prime case: the p-direction is genuinely new to the primitive denominator and is not the orientation prime two.

For `a>=1`, consider the deepest new primitive branch

\[
\Psi_{dp^a}.
\]

## 2. Exact mod-p Frobenius thickening

The primitive pullback/Frobenius theorem gives

\[
\boxed{
\Psi_{dp^a}(u)
\equiv
\Psi_d(u)^{e_a}\pmod p,
}
\tag{SFB-1}

where

\[
\boxed{e_a=p^{a-1}(p-1).}
\tag{SFB-2}

The degree equality is

\[
\deg\Psi_{dp^a}
=e_a\deg\Psi_d
=e_a\varphi(d).
\]

## 3. The base support is reduced

The primitive discriminant formula has prime support contained in `2d`.  Since `p\nmid2d`,

\[
p\nmid\operatorname{Disc}\Psi_d.
\]

Therefore the reduction

\[
\overline{\Psi_d}\in\mathbb F_p[u]
\]

is squarefree.

Hence the special fiber of the deepest branch order is exactly

\[
\boxed{
\mathscr O_{dp^a}\otimes\mathbb F_p
\cong
\mathbb F_p[u]/(\overline{\Psi_d}^{\,e_a}).
}
\tag{SFB-3}

Its reduced support is

\[
\boxed{
(\mathscr O_{dp^a}\otimes\mathbb F_p)_{\rm red}
\cong
\mathbb F_p[u]/(\overline{\Psi_d}).
}
\tag{SFB-4}

Thus a characteristic-zero new p-adic spectral level becomes a nilpotent Frobenius thickening of the ancestral reduced primitive spectrum.

## 4. Exact nilpotent filtration

Let

\[
I=(\overline{\Psi_d})/(\overline{\Psi_d}^{\,e_a})
\]

be the nilradical of the special fiber.  Then

\[
I^{e_a}=0,
\qquad
I^{e_a-1}\ne0.
\]

For `0<=j<e_a`, multiplication by `Psi_d^j` identifies the graded pieces with the reduced base algebra:

\[
\boxed{
I^j/I^{j+1}
\cong
\mathbb F_p[u]/(\overline{\Psi_d}).
}
\tag{SFB-5}

Each layer has dimension `phi(d)` over `F_p`, and there are exactly `e_a` layers.  Therefore total dimension is

\[
\boxed{e_a\varphi(d)=\varphi(dp^a).}
\tag{SFB-6}

So p-adic depth becomes nilpotent thickness in the special fiber.

## 5. Weighted-BRC of the same pullback

The full primitive branch family created by a `p^a` pullback from p-free `d` is

\[
\Psi_d,\Psi_{dp},\ldots,\Psi_{dp^a}.
\]

With branch weight equal to primitive mode multiplicity `phi`, the exact BRC data are

\[
\boxed{C=a+1,}
\tag{SFB-7}

\[
\boxed{W=p^a\varphi(d),}
\tag{SFB-8}

and the dominant deepest branch has

\[
\boxed{M=\varphi(dp^a)=e_a\varphi(d).}
\tag{SFB-9}

Therefore

\[
\boxed{
E=\frac WM
=\frac{p^a}{e_a}
=\frac p{p-1}.
}
\tag{SFB-10}

## 6. Geometric meaning of equalization

Combining (SFB-2) and (SFB-10):

\[
\boxed{
E
=
\frac{\text{total phase-pullback degree }p^a}
{\text{deepest new-branch Frobenius thickness }e_a}.
}
\tag{SFB-11}

The common factor `phi(d)` cancels because every nilpotent layer is one copy of the ancestral reduced spectral support.

As `a` increases:

- branch count `C=a+1` records the number of characteristic-zero p-adic levels;
- deepest nilpotent thickness grows as `p^(a-1)(p-1)`;
- total phase degree grows as `p^a`;
- their ratio remains exactly `p/(p-1)`.

Thus BRC equalization is depth-blind because both total degree and dominant Frobenius thickness acquire the same factor `p` at every additional p-adic level.

## 7. Relation to support collapse

Over characteristic zero, the factors

\[
\Psi_d,\Psi_{dp},\ldots,\Psi_{dp^a}
\]

are distinct primitive spectral branches.

Modulo `p`, all of them have the same reduced support `bar Psi_d`; only their nilpotent thickness differs.

Hence the same finite structure presents two typed summaries:

```text
characteristic zero branch support:
    a+1 distinct p-adic levels

mod-p reduced support:
    one ancestral support

mod-p thickness:
    remembers depth multiplicity

BRC equalization:
    ratio total phase degree / deepest thickness
```

This is an exact example where reduction recoalesces support while preserving depth in a different carrier.

## 8. Boundary p=2

The prime two is special for odd `d`: before the p-adic tower is considered, the two reflection orientation factors already collapse modulo two.  Therefore the squarefree-base argument above does not apply directly to the full odd `Psi_d` at `p=2`.

The orientation-resolved mod-two theorem supplies the correct typed replacement: the reduced core is one orientation factor and the full dyadic tower thickens that support.

So `p=2` is not an exception to the mechanism, but it requires preserving orientation before reduction.

Freeze:

`FOREIGN_PRIME_P_ADIC_DEPTH -> NILPOTENT FROBENIUS THICKNESS`.

`BRC_E = TOTAL_PULLBACK_DEGREE / DEEPEST_SPECIAL_FIBER_THICKNESS`.

`DEPTH_GROWTH CANCELS IN E`.

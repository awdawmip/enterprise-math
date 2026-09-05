# Exact Weighted-BRC coordinates of primitive spectral pullback branches

Status: `FREE_RESEARCH / EXACT FINITE-BRANCH ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Classification: `PHASE-B REUSE/APPLICATION OF GLOBAL WEIGHTED-BRC TYPING`
Depends on:
- primitive spectral pullback family;
- global Weighted-BRC finite positive-weight summary `(C,W,M)`;
- `deg Psi_e=phi(e)`.

## 1. Canonical pullback branch family

For source primitive denominator `d` and phase multiplier `n`, the exact polynomial pullback is

\[
\operatorname{Monic}(\Psi_d\circ R_n)
=\prod_{e\in\mathcal F_n(d)}\Psi_e,
\]

where

\[
\boxed{
\mathcal F_n(d)
=\{dg:g\mid n,\ (d,n/g)=1\}.
}
\tag{BRC-1}

These distinct primitive factors are the branch representatives.

Assign the positive integer branch weight

\[
\boxed{w_e:=\deg\Psi_e=\varphi(e).}
\tag{BRC-2}

This weight is primitive spectral mode multiplicity.  It is not endpoint prime mass and is not signed/orientation amplitude.

## 2. New-prime part of the phase multiplier

Write

\[
n=\prod_p p^{a_p}
\]

and define the factor supported on primes absent from `d`:

\[
\boxed{
n_{\perp d}
:=\prod_{\substack{p^{a_p}\parallel n\\p\nmid d}}p^{a_p}.
}
\tag{BRC-3}

For a prime already dividing `d`, the fiber condition forces the full exponent `a_p` into `g`: there is no branch choice.

For a prime absent from `d`, the exponent of `p` in `g` may be any

\[
0,1,\ldots,a_p.
\]

Therefore the supported branch count is

\[
\boxed{
C=|\mathcal F_n(d)|
=\prod_{\substack{p^{a_p}\parallel n\\p\nmid d}}(a_p+1)
=\tau(n_{\perp d}).
}
\tag{BRC-4}

## 3. Total positive mode mass

The primitive degree eigenlaw gives

\[
\sum_{e\in\mathcal F_n(d)}\varphi(e)
=n\varphi(d).
\]

Hence the Weighted-BRC total positive mass is

\[
\boxed{W=n\varphi(d).}
\tag{BRC-5}

## 4. Dominant branch mass

The branch `e=dn` is always in the pullback family.  Its weight is

\[
\varphi(dn).
\]

Prime-locally this is maximal:

- if `p|d`, there is only the forced exponent and the local multiplier is `p^a`;
- if `p\nmid d`, among `j=0,...,a`, the local weights are
  `1, phi(p),...,phi(p^a)`, whose maximum is `phi(p^a)`; for the exceptional `p=2,a=1`, the two local maxima tie but have the same value.

Therefore

\[
\boxed{M=\varphi(dn).}
\tag{BRC-6}

The dominant branch is `dn`; ties are possible only through a newly introduced single factor `2`.

## 5. Exact equalization ratio

Thus

\[
E:=\frac WM
=\frac{n\varphi(d)}{\varphi(dn)}.
\]

Using Euler-product factorization of `phi`, all primes already present in `d` cancel, leaving only new prime support:

\[
\boxed{
E
=\prod_{\substack{p\mid n\\p\nmid d}}
\frac{p}{p-1}.
}
\tag{BRC-7}

Therefore the derived logarithmic coordinate is

\[
\boxed{
\Delta=\log E
=\sum_{\substack{p\mid n\\p\nmid d}}
\log\frac{p}{p-1}.
}
\tag{BRC-8}

No numerical logarithm is needed for the native branch algebra; (BRC-7) is the exact rational statement.

## 6. Deterministic versus genuinely branching pullback

The pullback has one branch iff every prime of `n` already occurs in `d`:

\[
\boxed{
C=1
\iff
n_{\perp d}=1
\iff
\operatorname{rad}(n)\mid d.
}
\tag{BRC-9}

The equalization ratio has exactly the same zero-branching criterion:

\[
\boxed{
E=1
\iff
\Delta=0
\iff
\operatorname{rad}(n)\mid d.
}
\tag{BRC-10}

Thus repeated deepening along already-present prime directions is deterministic in Weighted-BRC typing.

A branch split occurs precisely when phase multiplication introduces at least one prime direction not already present in the source primitive denominator.

## 7. Exponent depth and prime-support novelty separate

For a newly introduced prime power `p^a`, the local branch count is

\[
a+1,
\]

so `C` records the depth exponent.

But its local equalization contribution is always

\[
\frac{p}{p-1},
\]

independent of `a`.

Hence

\[
\boxed{
\text{BRC branch count sees new-prime depth},
}
\]

while

\[
\boxed{
\text{BRC equalization ratio sees only new-prime support}.
}
\tag{BRC-11}

This is another exact typing separation:

`PRIME_SUPPORT_NOVELTY != P_ADIC_DEPTH_PROVENANCE`.

## 8. Local branch-weight distribution

For a prime `p\nmid d` with `p^a||n`, the local branch exponent `j=0,...,a` has unnormalized multiplicity weight

\[
w_0=1,
\qquad
w_j=\varphi(p^j)=p^{j-1}(p-1)\quad(j\ge1).
\]

The local total is

\[
\sum_{j=0}^a w_j=p^a.
\]

Thus the normalized mode-multiplicity distribution is

\[
\boxed{
\Pr(j=0)=p^{-a},
\qquad
\Pr(j)=\frac{(p-1)p^{j-1}}{p^a}\quad(1\le j\le a).
}
\tag{BRC-12}

For different new primes these local branch choices factor multiplicatively.

The deepest new-prime level has normalized weight

\[
1-\frac1p,
\]

and the product of these deepest-level weights over all new primes is exactly `M/W=1/E`.

## 9. Relation to endpoint prime mass

The degree weight `w_e=phi(e)` is deliberately distinct from primitive endpoint mass

\[
P_e=|\Psi_e(0)|.
\]

Under pullback:

- total degree weight scales by `n`;
- endpoint prime mass is multiplicatively conserved;
- mixed newly created branches may carry large degree weight while having endpoint mass `1`.

Therefore the algebra supplies a concrete finite example where supported multiplicity and positive endpoint mass must remain separate carriers.

## 10. Reuse resolution

This construction does not define a new BRC family.  It instantiates the already global finite positive-weight `(C,W,M)` carrier on a naturally arising factorization branch family.

Reuse state:

`GLOBAL_WEIGHTED_BRC_CWM -> REUSE_APPLIED`.

The new content is the exact spectral-pullback specialization (BRC-4)--(BRC-12).

Freeze:

`SPECTRAL_PULLBACK_BRANCH_WEIGHT = PRIMITIVE_MODE_MULTIPLICITY`.

`C = TAU(NEW_PRIME_PART)`.

`W = n*PHI(d)`.

`M = PHI(dn)`.

`E = PRODUCT_(NEW_PRIMES) p/(p-1)`.

`OLD_PRIME_DEPTH = DETERMINISTIC_BRC_CHANNEL`.

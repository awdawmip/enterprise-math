# Rényi information spectrum of the divisor-phase Weighted-BRC distribution

Status: `FREE_RESEARCH / EXACT FINITE-INFORMATION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Classification: `PHASE-B INFORMATION READOUT OF EXACT POSITIVE BRANCH WEIGHTS`
Depends on:
- divisor-phase branch weights `w_d=phi(d)`;
- global Weighted-BRC `(C,W,M)` typing.

## 1. Canonical probability distribution on divisor-phase branches

For length `n`, the reduced-denominator branch `d|n` has weight

\[
w_d=\varphi(d).
\]

Since

\[
\sum_{d\mid n}\varphi(d)=n,
\]

define the normalized branch probability

\[
\boxed{
\pi_n(d):=\frac{\varphi(d)}n,
\qquad d\mid n.
}
\tag{RBI-1}

This is exactly the distribution of the reduced denominator of a uniformly chosen finite phase index modulo `n`.

## 2. Prime-coordinate factorization

Write

\[
n=\prod_p p^{a_p}.
\]

A divisor is `d=prod p^(j_p)`.  The probability factorizes independently across prime coordinates:

\[
\boxed{
\pi_n(d)
=\prod_{p^{a}\parallel n}\pi_{p^a}(j_p).
}
\tag{RBI-2}

The local distribution is

\[
\boxed{
\pi_{p^a}(0)=p^{-a},
}
\]

\[
\boxed{
\pi_{p^a}(j)=\frac{(p-1)p^{j-1}}{p^a},
\qquad1\le j\le a.
}
\tag{RBI-3}

## 3. Exact Rényi entropy

For `alpha>0`, `alpha!=1`, define

\[
H_\alpha(n)
:=\frac1{1-\alpha}
\log\sum_{d\mid n}\pi_n(d)^\alpha.
\]

By prime-coordinate independence,

\[
\boxed{
H_\alpha(n)
=\sum_{p^a\parallel n}H_\alpha(p^a).
}
\tag{RBI-4}

For one prime power,

\[
\sum_{j=0}^{a}\pi_{p^a}(j)^\alpha
=
p^{-a\alpha}
\left[
1+(p-1)^\alpha
\sum_{j=0}^{a-1}p^{\alpha j}
\right].
\]

Hence

\[
\boxed{
H_\alpha(p^a)
=
\frac1{1-\alpha}
\log\left[
p^{-a\alpha}
\left(
1+(p-1)^\alpha
\frac{p^{a\alpha}-1}{p^\alpha-1}
\right)
\right].
}
\tag{RBI-5}

The formula extends continuously to the standard endpoints `alpha=0,1,infinity`.

## 4. Hartley entropy is the BRC support coordinate

The support contains one branch per divisor, so

\[
|\operatorname{supp}\pi_n|=\tau(n)=C.
\]

Therefore

\[
\boxed{
H_0(n)=\log\tau(n)=\log C.
}
\tag{RBI-6}

Thus the BRC supported-path count records the order-zero Rényi/Hartley entropy after the derived logarithmic readout.

## 5. Min-entropy is exactly the BRC equalization coordinate

The largest branch mass is

\[
M=\varphi(n),
\]

while total mass is

\[
W=n.
\]

Hence the maximal branch probability is

\[
\pi_{\max}=M/W=\varphi(n)/n.
\]

The min-entropy is

\[
H_\infty(n)
=-\log\pi_{\max}
=\log(W/M).
\]

Therefore

\[
\boxed{
H_\infty(n)=\Delta
=\log\frac n{\varphi(n)}.
}
\tag{RBI-7}

Equivalently

\[
\boxed{E=e^{H_\infty}.}
\tag{RBI-8}

So the Weighted-BRC equalization coordinate is exactly the min-entropy of this canonical finite rotation-branch distribution.

## 6. Exact Shannon entropy

Taking the `alpha->1` limit of (RBI-5), or summing directly, gives

\[
\boxed{
H_1(p^a)
=(1-p^{-a})
\left[
\frac{p}{p-1}\log p-\log(p-1)
\right].
}
\tag{RBI-9}

Thus

\[
\boxed{
H_1(n)
=\sum_{p^a\parallel n}
(1-p^{-a})
\left[
\frac{p}{p-1}\log p-\log(p-1)
\right].
}
\tag{RBI-10}

For fixed prime `p`, as depth `a->infinity`, the local Shannon entropy converges to the finite limit

\[
\frac{p}{p-1}\log p-\log(p-1),
\]

even though the support count `a+1` diverges.

This gives another exact distinction between branch-support growth and effective probability spread.

## 7. Entropy ordering

For every finite probability distribution,

\[
H_\infty\le H_1\le H_0.
\]

Thus here

\[
\boxed{
\Delta
\le H_1(n)
\le\log C.
}
\tag{RBI-11}

The two quantities already retained by `(C,W,M)` are exactly the two extremal Rényi slices surrounding the Shannon entropy.

## 8. What C,W,M preserve and what they do not

For an arbitrary positive Weighted-BRC family, the triple `(C,W,M)` determines

\[
H_0=\log C
\]

and

\[
H_\infty=\log(W/M)=\Delta,
\]

but generally does **not** determine the intermediate Rényi entropies or Shannon entropy, because different positive weight distributions can have the same support count, total mass and maximum mass.

The #1159 divisor-phase family is special because the exact arithmetic weights `phi(d)` are known, so the entire Rényi spectrum can be reconstructed.

Therefore

\[
\boxed{
(C,W,M)
=\text{EXTREMAL INFORMATION SUMMARY, NOT FULL WEIGHT DISTRIBUTION}.
}
\tag{RBI-12}

## 9. Primorial specialization

For the primorial

\[
P_y=\prod_{p\le y}p,
\]

every local exponent is `a=1`.  Then

\[
H_0(P_y)=\pi(y)\log2,
\]

\[
H_\infty(P_y)
=\sum_{p\le y}\log\frac p{p-1},
\]

and

\[
H_1(P_y)
=\sum_{p\le y}
\frac1p\log p
+\left(1-\frac1p\right)
\log\frac p{p-1}.
\]

The three growth laws are visibly different finite prime observables.

## 10. Interpretation

The canonical divisor-phase BRC now has a full information hierarchy:

```text
H_0 = log C
    support/Hartley entropy

H_1
    full Shannon spread of primitive denominator weights

H_infinity = Delta = log(W/M)
    dominant-branch/min-entropy
```

Thus BRC's path-count and equalization coordinates have exact information-theoretic meanings while remaining derived readouts of the finite positive branch weights.

Freeze:

`LOG_C = HARTLEY_ENTROPY`.

`DELTA = MIN_ENTROPY`.

`CWM = EXTREMAL_RENYI_SUMMARY`.

`FULL_SPECTRAL_MULTIPLICITY_WEIGHTS -> COMPLETE_RENYI_FAMILY`.

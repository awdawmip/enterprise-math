# Divisor-phase Weighted-BRC and the finite Mertens equalization coordinate

Status: `FREE_RESEARCH / EXACT FINITE-BRANCH ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Classification: `PHASE-B APPLICATION OF GLOBAL WEIGHTED-BRC CWM`
Depends on:
- primitive denominator decomposition of finite phase/mode labels;
- Euler totient multiplicities.

## 1. Full finite phase population by reduced denominator

Fix a length `n>=1`.  The finite phase labels are

\[
k=0,1,\ldots,n-1.
\]

For a nonzero phase fraction `k/n`, reduce it to lowest terms.  Its reduced denominator is a divisor `d|n`.  Include the zero/base phase as the virtual `d=1` branch.

For each divisor `d|n`, the number of phase labels with reduced denominator exactly `d` is

\[
\boxed{w_d=\varphi(d).}
\tag{DPB-1}

Indeed the reduced numerator runs through the unit classes modulo `d`.

Thus the entire finite phase population decomposes exactly as

\[
\boxed{n=\sum_{d\mid n}\varphi(d).}
\tag{DPB-2}

This is the mode-label version of the primitive spectral divisor decomposition.

## 2. Weighted-BRC C,W,M

Use the divisor branches `d|n` with positive weight `w_d=phi(d)`.

The supported branch count is

\[
\boxed{C=\tau(n),}
\tag{DPB-3}

where `tau(n)` is the divisor-count function.

The total positive mass is

\[
\boxed{W=n.}
\tag{DPB-4}

Euler totient is nondecreasing under divisibility, so the dominant branch mass is

\[
\boxed{M=\varphi(n).}
\tag{DPB-5}

There may be ties, e.g. through a newly introduced factor two, but the maximal value is `phi(n)`.

Therefore

\[
\boxed{
E=\frac WM=\frac n{\varphi(n)}
=\prod_{p\mid n}\frac p{p-1}.
}
\tag{DPB-6}

The derived log coordinate is

\[
\boxed{
\Delta=\log E
=\sum_{p\mid n}\log\frac p{p-1}.
}
\tag{DPB-7}

The exact rational quantity (DPB-6) is the native finite summary; log is a later coordinate readout.

## 3. Probability interpretation

Choose a phase index uniformly from `0,...,n-1`.  Its reduced-denominator distribution is

\[
\boxed{
\Pr(D=d)=\frac{\varphi(d)}n,
\qquad d\mid n.
}
\tag{DPB-8}

The dominant primitive denominator-`n` branch therefore has probability

\[
\boxed{
\Pr(D=n)=\frac{\varphi(n)}n=\frac1E.
}
\tag{DPB-9}

Equivalently for a uniformly chosen integer residue,

\[
\Pr((k,n)=1)=\frac{\varphi(n)}n.
\]

Hence

\[
\boxed{
\Delta
=-\log\Pr((k,n)=1).
}
\tag{DPB-10}

So the BRC equalization coordinate is the information cost of the dominant primitive phase branch under the uniform finite phase population.

## 4. Prime-power example

For

\[
n=p^a,
\]

the branches are

\[
1,p,p^2,\ldots,p^a
\]

with weights

\[
1,p-1,p(p-1),\ldots,p^{a-1}(p-1).
\]

Thus

\[
C=a+1,
\qquad
W=p^a,
\qquad
M=p^{a-1}(p-1),
\]

and

\[
\boxed{E=\frac p{p-1},}
\tag{DPB-11}

independent of depth `a`.

Again branch count remembers p-adic depth while equalization sees only prime support.

## 5. Primorial branch family and finite Mertens product

Let

\[
P_y:=\prod_{p\le y}p.
\]

Then every divisor corresponds to a subset of the primes up to `y`, so

\[
\boxed{C(P_y)=2^{\pi(y)}.}
\tag{DPB-12}

The equalization ratio is

\[
\boxed{
E(P_y)
=\frac{P_y}{\varphi(P_y)}
=\prod_{p\le y}(1-p^{-1})^{-1}.
}
\tag{DPB-13}

This is the finite Mertens/Euler product at exponent one.

Thus prime accumulation has at least two distinct exact finite summaries:

```text
branch support count:
    C = 2^(pi(y))

primitive-branch dilution:
    E = product_(p<=y) p/(p-1)
```

They should not be identified.

## 6. Branch probability factorization

For `n=prod p^(a_p)`, the reduced-denominator exponent at one prime is independent under the product decomposition of the uniform phase labels:

\[
\Pr(v_p(D)=0)=p^{-a_p},
\]

\[
\Pr(v_p(D)=j)=\frac{(p-1)p^{j-1}}{p^{a_p}},
\qquad1\le j\le a_p.
\tag{DPB-14}

The joint divisor probability is the product of these local distributions and equals `phi(d)/n`.

The probability of maximal exponent at every prime is

\[
\prod_{p\mid n}(1-p^{-1})=\varphi(n)/n.
\]

Hence `1/E` is literally the probability that every prime-coordinate of the phase denominator reaches its deepest allowed level.

## 7. Mean depth of one prime coordinate

For `p^a||n`, let `J_p=v_p(D)`.  From (DPB-14),

\[
\boxed{
\mathbb E[J_p]
=a-\frac{1-p^{-a}}{p-1}.
}
\tag{DPB-15}

Thus the uniform phase population is strongly biased toward deep denominator levels, especially for large `p`, even though the BRC equalization contribution `p/(p-1)` is independent of `a`.

This provides a quantitative distinction between branch-depth provenance and support equalization.

## 8. Relation to the primitive pullback BRC theorem

The earlier pullback formula for general source denominator `d` gave

\[
C=\tau(n_{\perp d}),
\qquad
W=n\varphi(d),
\qquad
M=\varphi(dn),
\]

and

\[
E=\prod_{p\mid n,p\nmid d}\frac p{p-1}.
\]

The present divisor-phase decomposition is the virtual-base case `d=1`, where every prime of `n` is new and the branch family is all divisors of `n`.

The virtual base is a branch-label bookkeeping device; there is no nontrivial primitive polynomial `Psi_1`.

## 9. Scope

No novelty is claimed for `sum_(d|n) phi(d)=n`, the probability `phi(n)/n`, or the classical Mertens product.  The theorem-candidate content is their exact realization as Weighted-BRC summaries of the finite rotation phase-denominator branch population.

Freeze:

`DIVISOR_PHASE_BRANCH_WEIGHT = PHI(d)`.

`FULL_PHASE_BRC = (TAU(n), n, PHI(n))`.

`BRC_EQUALIZATION = n/PHI(n) = INVERSE_PRIMITIVE_PHASE_PROBABILITY`.

`PRIMORIAL_EQUALIZATION = FINITE_MERTENS_PRODUCT`.

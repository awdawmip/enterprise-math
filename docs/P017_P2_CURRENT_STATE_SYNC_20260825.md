# P017 — P2 Current-State Synchronization

Status: `OWNER CHECKPOINT / PROVED_WIP + SOURCE-FORMULA CORRECTION + EXTERNAL-COMPUTATION CONDITIONAL FINITE SPLICE / NOT CANONICAL / NO ALL-K P2 CLAIM`

Originally captured: `2026-08-25T21:34:00+08:00`

Last source-audit correction: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Authoritative correction note:

`docs/P017_P2_W1_SOURCE_FORMULA_AUDIT_20260826.md`

Exact rational verifier:

`experiments/p017_p2_w1_source_formula_audit_20260826.py`

## Frozen mathematical state

1. The exact root-normalized detector

   \[
   \omega_K(n)=1-\sum_{p<K+1,\,p\mid n}\nu_p(n)\left(1-\frac{\log p}{\log(K+1)}\right)
   \]

   satisfies

   \[
   \omega_K(n)>0\iff\Omega(n)\le2
   \]

   for every state in the consecutive-square basin.

2. For the P017 binary carry

   \[
   O_m(K)=H_m(K)-H_{2m}(K),
   \]

   the exact bridge

   \[
   O_m(K)-\frac Km=r_K(m)-r_K(2m)
   \]

   reduces the prime-lift carry remainder to the standard Chen short-interval floor remainder.

3. Above the root, odd `O_m` is a Boolean incidence in pairwise-disjoint reciprocal complement windows. Distinct-prime prime-lift collisions factor through one shared small-prime core and one Boolean packet hit. Exact-Mobius top-third and `t=1` collision sectors collapse further; arbitrary Rosser/well-factorable coefficients remain an analytic interface.

4. The additive `O(sqrt(K))` super-root halo has coefficient-uniform bounded L1/L2 discrepancy by the quadratic-excess layer law. A fixed multiplicative super-root strip still requires analytic input.

5. The finite side remains conditionally spliced, under the declared conservative public exhaustive-gap premise, through

   \[
   K\le116{,}009{,}280{,}740{,}973{,}308,
   \]

   corresponding to

   \[
   X=K^2\approx1.3458153218\times10^{34}.
   \]

## 2026-08-26 source-formula correction

A direct audit of the unsimplified Iwaniec–Laborde p. 53 `W_1` lower bound found two normalization/transcription errors in the 2026-08-25 `a=4` effectivity packages:

1. after normalizing `F((1-t)/t)=2e^gamma*t/(1-t)`, the source `dt/t` cancels the `t`; the earlier `J_3` formulas retained an extra `1/t`;
2. the source fourth negative integral has a literal leading factor `2`, omitted in the earlier packages.

Consequences:

### Four-sevenths remains valid but with a smaller reserve

For

\[
\theta=\frac{4999}{10000},\qquad D=X^{4/7},\qquad a=4,\quad b=\frac52,\quad c=\frac72,
\]

the corrected source-normalized coefficient satisfies the exact rational certificate

\[
\boxed{C_1^{(4/7)}>\frac{533}{5000}=0.1066.}
\]

The Lemma-6 coefficient remains

\[
C_2^{(4/7)}=\frac{128}{174790063},
\]

so the corrected certified net reserve is

\[
\boxed{
C_1^{(4/7)}-C_2^{(4/7)}
>
\frac{93162463579}{873950315000}
\approx0.1065992677.
}
\]

The former `>0.145713553` reserve is superseded.

### The existing five-ninth `a=4` specialization is not positive

For

\[
D=X^{5/9},\qquad a=4,\quad b=\frac{13}{5},\quad c=\frac{18}{5},
\]

the corrected verifier proves

\[
\boxed{C_1^{(5/9)}<-\frac{3}{2500}.}
\]

Therefore `docs/P017_P2_EFFECTIVE_FIVE_NINTH_PACKAGE_20260825.md` must not be used as a positive main-term certificate. This invalidates that parameter specialization, not the level exponent `5/9` under every possible choice of weights.

Any older owner artifact that independently integrated the same p. 53 unsimplified formula must be treated as needing source-normalization re-audit before its numerical positivity margin is consumed downstream. In particular, the former `a=4` closed-form positivity number is not authoritative after this correction.

## Effectivity pressure test

The four-sevenths package still admits the trivial `(1/2,1/2)` terminal pair estimate without invoking the refined `(1/14,11/14)` exponent pair. However, explicit B-spline/Poisson bookkeeping at the current finite splice shows that mechanical constant tracking of the generic 1981 proof is numerically far too expensive: even idealized single-block estimates remain order one before the `O((log MN)^2)` bilinear-form multiplicity is charged.

This is a route diagnostic rather than an impossibility theorem. It shifts the priority away from microscopic improvement of generic Fourier constants and toward:

1. re-optimizing the level exponent against the **corrected** `W_1` reserve;
2. exploiting the P017 square-specific super-root complement/collision kernel;
3. using adaptive interval-length anchors to strip chosen small-prime factors with zero floor error;
4. applying generic bilinear machinery only to the irreducible residual sector.

## Current hard frontier

The old comparison `4/7 versus positive 5/9` is retired. The live problem is now:

> choose a corrected positive root-edge parameter package that optimizes finite-scale reserve versus bilinear saving, and combine it with square-specific exact reductions before paying any generic Chen/Iwaniec bilinear constant.

No all-k consecutive-square P2 theorem is claimed here.

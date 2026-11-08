# D25 — Clausen factorization of the original 216 first digit and split-factor experiment

Date: 2026-11-08 (Asia/Hong_Kong). Classification: **AUTHOR_SIDE_EXACT_PROVED / FINITE_611_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Original immutable scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Predecessor: research_notes/portable_direct/20261108_onhour_d25_fourth_digit_wilson_jets_continuation.json.

## Theorem (all primes p=6k+1>3)

In the field F_p define

\[
F_k(x)=\sum_{n=0}^{k}\binom{k}{n}\binom{2k}{n}x^n,\qquad
\theta=x\frac{d}{dx},\quad G_k(x)=(1+12\theta)F_k(x).
\]

For the **unchanged original 216 sum**

\[
W_p=\sum_{n=0}^{p-1}\frac{(6n+1)\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\]

the exact finite-field identity is

\[
\boxed{W_p\equiv F_k(1/2)\,G_k(1/2)\pmod p.}\tag{C1}
\]

In fact, the following polynomial identity holds in F_p[x]:

\[
\sum_{n=0}^{p-1}(6n+1)
\frac{(1/3)_n(1/2)_n(2/3)_n}{(n!)^3}x^n
=F_k(x)(1+12\theta)F_k(x).\tag{C1-poly}
\]

**Proof.** Clausen's exact formal identity is
\[
{}_2F_1(1/6,1/3;1;x)^2
={}_3F_2(1/3,1/2,2/3;1,1;x).
\]
Set p=6k+1. In F_p, 1/6=-k and 1/3=-2k. Up to degree p-1 the Gauss series therefore truncates to F_k(x): its coefficient at n≤k is
(-k)_n(-2k)_n/(n!)² = binom(k,n)binom(2k,n), and the coefficient vanishes for k<n<p. The 3F2 series likewise terminates at n=2k<p (since (1/3)_{2k+1}=0 mod p). Every denominator n! for n<p is invertible, so reduction of Clausen is legitimate coefficientwise through degree p-1. The square F_k² has degree 2k. Apply (1+6θ) to both sides: its weight is 6n+1, while (1+6θ)(F_k²)=F_k(F_k+12θF_k). Finally the exact factorial identity

\[
\frac{(1/3)_n(1/2)_n(2/3)_n}{(n!)^3}(1/2)^n
=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
\]

recovers the original terms, proving C1. QED.

## Discriminating finite experiment; candidate, not theorem

Write a_p=F_k(1/2), b_p=G_k(1/2), and χ_p=(-6/p), for primes p=6k+1. Candidate mechanism:

\[
\chi_p=-1 \ \Longrightarrow\ (a_p=0,\ b_p\ne0),\qquad
\chi_p=+1 \ \Longrightarrow\ (b_p=0,\ a_p\ne0).
\tag{inert/split candidate}
\]

The sign χ_p=-1 corresponds exactly to p≡13 or 19 mod24, both frozen target classes. A real integer-modular program separately computes (i) the original full factorial-ratio recurrence for W_p through n=p-1 and (ii) the terminating binomial recurrence for a_p and b_p. It checked **all 611 primes p≤10000 satisfying p≡1 mod6**. Both C1 and the candidate split held for every checked prime; this finite observation does not prove the candidate for all p.

| p mod24 | Tested | a_p=0 | b_p=0 |
|---:|---:|---:|---:|
| 1 | 143 | 0 | 143 |
| 7 | 156 | 0 | 156 |
| 13 | 157 | 157 | 0 |
| 19 | 155 | 155 | 0 |

Exact witnesses (p,a_p,b_p): (7,2,0), (13,0,6), (19,0,12), (31,21,0), (37,0,29), (373,0,171). At p=373 the F port vanishes but the differential G port remains 171 mod373. This is new discriminating information beyond the scalar W_373=0 mod373.

**Original observation scope / BRC.** Maintain (model, n, signed 6n+1 weight, original coefficient, p-adic valuation grade, a/b factor observer, mod-p projection). Only the first scalar digit is factored by C1. Previous JET4 source/grade information is retained; no promotion to a native X6 or original-class Frobenius operator is made.

## Continuation and Source separation

Next direct mathematical action: prove or falsify the inert factor a_p=0 in classes 13/19 mod24 by an exact Hasse/Deuring or CM trace connection, **first verifying original curve, twist, Hasse normalization and observer maps**; then investigate higher p-adic correction in the existing JET4 and W216 mod p³ frontier.

Native highest outstanding experiment remains issue #1559 (https://github.com/awdawmip/enterprise-math/issues/1559): real original-class p373 H0/B0 divided-power module, [X]U modulo 139129, module rank, Frobenius direction and eta, signed odd Green/Hesse kappa, Delta-R and independent replication. NOT_EXECUTED; executor PENDING_OWNER. Auxiliary first-digit polynomial code does not satisfy that experiment.

Read-only original request on 2026-11-08: onhour11-20261106-1400-exact-research-lane-continuation returned SUCCEEDED with original continuation observed 2026-11-08T09:22:06.261470Z; execution_authorized=false. Gateway v0.6.11 Site diagnostics CONFIGURED_NOT_LIVE_VERIFIED / research_authority_granted=false. No native Researcher session/CLAIM/run/checkpoint is claimed. Historical label chatgpt-research-onhour-enterprise-math-20260923 is provenance, separate from forbidden maintenance chatgpt-hourly-enterprise-math-20260921. Preserve distinct old staging and the original request ID. The native Source owns formal admission; this author-side note is a separate exact mathematical result and finite candidate check.

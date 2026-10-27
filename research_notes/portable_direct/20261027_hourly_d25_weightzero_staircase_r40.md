# D25/LIFT R40 — Uniform S-weight-zero valuation staircase and next normalized p-adic digit

Date: 2026-10-27 (Asia/Hong_Kong). Portable TASK_RESEARCH author result; user-declared logical Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`, distinct from maintenance. This label alone is not current native session/CLAIM authority. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, D25/LIFT/JT2 OPEN. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.**

## New problem after R39

R29/R34 isolated the p≡19 mod24 *low-half* extra S-weight valuation. R38/R39 isolated the p≡13 mod24 *upper W2/S2 shared-band* extra S-weight valuation, its original labels and the Wilson-free regularized W/S unit. The missing all-residue-class law is needed to know at which p-adic precision a weight-zero original S term reappears; p=7 requires a separate valuation check.

For prime \`p=6m+1>=7\`, retain the original rational source, unchanged:

\`\`\`text
s_k=(8k+1)(4k)!/((k!)^4*2304^k), 0<=k<p.
ell = least positive odd representative of p mod 8 in {1,3,5,7},
k_*=(ell*p-1)/8, q=(ell-1)/2, R=(p-1)/2,
e=v_p(ell), ell_0=ell/p^e,
Q_p=((p-1)!+1)/p, H_R=sum(i=1..R)1/i,
D_p=ell_0*(-1)^q*q!*R!/((k_*!)^4*2304^k_*).
\`\`\`

All denominators in D_p and H_R are p-units; D_p itself is a p-unit.

## Theorem A — exact exceptional S-source valuation

The congruence \`8k+1=0 modp\` has **exactly one** solution \`0<=k<p\`, namely \`k_*\`. It obeys

\`\`\`text
4k_* = q*p+R < p²,
v_p(s_(k_*)) = q+1+e,                (A1)
s_(k_*)/p^(q+1+e) in Z_(p)^x.
\`\`\`

Full residue-class classification:

| p mod 24 | ell | q | exact valuation of original s_(k_*) | original source zone |
|---:|---:|---:|---:|---|
| 1 | 1 | 0 | 1 | early 1/8 band |
| 19 | 3 | 1 | 2 | low-half 3/8 band |
| 13 | 5 | 2 | 3 | upper W2/S2 5/8 band |
| 7 | 7 | 3 | 4 for p>7; **5 at p=7** | high-high S3 7/8 band |

The smallest case is essential: at p=7, k_*=6 and \`8k_*+1=49=7²\`, so S has **two**, not one, p-factors in the linear weight.

**Proof.** Since p is odd, \`p²=1 mod8\`, hence \`ell*p=1 mod8\` and k_* is an integer in [0,p−1]. As gcd(8,p)=1, this congruence has precisely one solution. Substitution gives \`4k_*=qp+R\`; q<=3, p>=7, and R=(p−1)/2 imply \`4k_*<p²\`. Legendre yields \`v_p((4k_*)!)=q\`. Both k_*! and 2304 are p-units. The weight is exactly ell*p and has valuation 1+e; e=1 only when p=7. This proves A1 and each table row. QED.

## Theorem B — all-class original-source p-adic first jet

For **all** these primes, the following precision-two formula holds in \`Z_(p)\`:

\`\`\`text
s_(k_*)/p^(q+1+e)
  ≡ D_p * [1+q*p*(H_R-Q_p)]        (mod p²).          (B1)
\`\`\`

In particular, for p≡1 mod24, q=0 and the following is **an exact rational identity**:

\`\`\`text
s_(k_*)/p = R!/((k_*!)^4*2304^k_*).                  (B2)
\`\`\`

The formula unifies R34's p≡19 lower-half source jet (\`q=1\`) and adds the next original-source digit for p≡13's S3 singularity and p≡7's high-high S3 singularity (including the exceptional p=7 normalized valuation).

**Proof by exact factorial blocks.** Put \`F=(p-1)!=-1+pQ_p\` (Wilson). Because \`4k_*=qp+R\`,

\`\`\`text
(4k_*)!/p^q
 = q!*F^q*R! *
   prod(t=0..q-1)prod(i=1..p-1)(1+t*p/i) *
   prod(i=1..R)(1+q*p/i)                            (exact).
\`\`\`

In \`Z_(p)\`, \`H_(p-1)=0 modp\` for odd p; the complete-block double product is therefore \`1 modp²\`. Also

\`\`\`text
F^q = (-1)^q[1-q*p*Q_p]          (mod p²),
prod(i=1..R)(1+q*p/i)=1+q*p*H_R (mod p²).
\`\`\`

Multiply, divide by the **original** unit denominator \`(k_*!)^4*2304^k_*\` and retain \`ell_0=(8k_*+1)/p^(1+e)\`; this gives B1. Its leading D_p is a unit, so A1 is sharp. For q=0 there are no completed p-blocks and B2 follows exactly. QED.

## Reproducible author-side certificate

A Python standard-library checker evaluated original s_(k_*) **independently** using p-free factorial products modulo p² and compared with B1 and all exact valuations for **all 80 primes** \`7<=p<=997, p≡1 mod6\`. Seven full rational \`Fraction\` spot checks at p=7,13,19,31,37,73,181 also passed. Counts: p mod24=1:14; 7:21; 13:22; 19:23. Finite checks corroborate the general factorial proof and are not native original-class CM/H0/B0 evidence.

| p | class | k_* | valuation | normalized s/p^v mod p² | mod p |
|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 6 | **5** | 13 | 6 |
| 13 | 13 | 8 | 3 | 86 | 8 |
| 19 | 19 | 7 | 2 | 314 | 10 |
| 31 | 7 | 27 | 4 | 404 | 1 |
| 73 | 1 | 9 | 1 | 1484 | 24 |
| 181 | 13 | 113 | 3 | 3994 | 12 |
| 373 | 13 | 233 | 3 | 69709 | 331 |
| 733 | 13 | 458 | 3 | 503976 | 405 |

Executed checker: \`20261027_hourly_d25_weightzero_staircase_r40_check.py\` (author-side artifact). **BRC COMPOSE_APPLIED** on \`(original S label, p mod24, unique integer rank, v_p factorial, v_p weight, unit jet, observer modulus)\`; disappearing at mod p^N does not license deletion for later p^(N+1) observations. No P000/ACTIVE worldview change, no native Frobenius inference.

**Next smallest unfinished science:** combine R39's exact paired upper W/S tau transport, R38's unpaired S2 and high-high W3/S3 ports, R36's integral endpoint Green adjoint, and R23's *unchanged-input* low-half p²-divided difference to derive or falsify a genuinely cross-rank WZ compensation. Keep original six z=2 Hasse J/E labels, both finite/infinite boundaries, H0/B0, [X]U modp², Frobenius eta/kappa and p373 native experiment distinct. The original W_p=S_p modp³ target remains OPEN. Native claimant-predecessor repair under #1558 is a separate authorized control matter; this portable result grants no CLAIM/open/Source checkpoint/Result/review.

# D25 / Original 216 grade-two kernel: all-prime character formula

2026-11-08 (Asia/Hong_Kong). **Third consecutive author-side exact mathematics unit**. Extends the preceding two p=1 mod6 results to **every prime p>3** by restoring the original grade-two index upper bound. `PROVED / EXACT_301_PRIME_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`.

Frozen task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Prior proofs at `fc6474d86e5cbb4b1079c5c7e0f0dcb19cd741c8` (original source port) and `4661e0b1812f6e2422d1e4bc19144cbba4b78b06` (quadratic-character prefactor).

## Theorem (every prime p > 3)

Let

\[
w_n=(6n+1)\frac{(2n)!(3n)!}{(n!)^5 216^n}\in\mathbb Z_{(p)},
\quad N=\frac{p+1}{2},\quad L=\left\lfloor\frac{2p-1}{3}\right\rfloor,
\quad M=L-N+1=\left\lfloor\frac{p+4}{6}\right\rfloor.
\]

Define the **original**, valuation-grade-two source digit

\[
T_W(p)=\frac1{p^2}\sum_{n=N}^{L}w_n\pmod p.
\]

All individual terms in this range have coefficient valuation precisely two before the optional weight (6n+1). Then

\[
\boxed{
T_W(p)\equiv
\frac19\left(\frac6p\right)
\sum_{r=0}^{M-1}(6r+4)
\frac{(1)_r(5/6)_r(7/6)_r}{(3/2)_r^3 2^r}
\pmod p.}\tag{A}
\]

The expression is a finite well-defined congruence in (\mathbb F_p); all displayed denominators are units for (0\le r<M).

**Proof.** Every prime (p>3) is (6m+1) or (6m+5). The e=2 range is precisely (N\le n\le L): for such (n), (p<2n<2p) and (p<3n<2p). Set (n=N+r). Independently of the prime residue class, the two factorial remainders are

\[
2n-p=1+2r,\qquad 3n-p=N+1+3r.
\]

Wilson gives ((p+a)!/p\equiv-a!\pmod p) for (0\le a<p). The two signs cancel. Thus the coefficient after dividing by (p^2) is

\[
(6N+6r+1)\frac{(1+2r)!(N+1+3r)!}{((N+r)!)^5 216^{N+r}}\pmod p.
\]

The base at (r=0) is (C_p=(N+1)/(N!^4 216^N)). As (N\equiv1/2\pmod p), its unweighted successive ratios reduce to

\[
\frac{(r+1)(6r+5)(6r+7)}{9(2r+3)^3}
=\frac{(r+1)(r+5/6)(r+7/6)}{2(r+3/2)^3}\pmod p.
\]

Wilson's reflected half-factorial identity gives (((p-1)/2)!^4\equiv1\pmod p), hence (N!^4\equiv1/16\pmod p). Euler's criterion therefore yields (C_p\equiv (6/p)/9\pmod p). Finally (6N+6r+1\equiv6r+4\pmod p), proving (A).

The upper index is (M=m) for (p=6m+1) and (M=m+1) for (p=6m+5), so this proof includes both character classes. QED.

## Why the extension matters

The exact original grade-two tail now has a uniform residue-character formula for **all** primes (p>3). It gives the same numerical observer for the frozen 13/19 classes and the 5 mod6 comparison class, using a single finite hypergeometric recurrence. This is a **source-preserving p²-digit evaluator**, not yet a proof that the full original (W_p\equiv p(-3/p)\pmod{p^3}).

For the frozen classes (p\equiv13,19\pmod{24}), the existing first-digit certificate makes the mother (W_p\equiv p\pmod{p^3}) equivalent to the exact lower-grade defect cancelling this (T_W(p)), with the sign of (T_W) explicitly determined by ((6/p)). The published 2304 grade-two aggregate vanishes for all primes; an original W/V transformation must transmit the generally nonzero W source-port to the lower-grade defect.

## Exact certificate and next action

Standalone checker: `research_notes/portable_direct/d25_w216_grade2_allprime_character_checker_20261108.py`. Executed with standard Python integers at **all 301 primes (5\le p\le2000)**. The original integer-binomial terms modulo (p^3) match the independently generated field recurrence in every instance. Witnesses `(p,M,T_W,S_p,chi_p(6))`: (5,1,1,4,+1); (11,2,1,2,-1); (13,2,10,1,-1); (19,3,9,5,+1); (373,62,266,217,-1).

**Next exact science:** construct and falsify/verify an original source-preserving W/V lower-grade correspondence with this **all-prime** finite kernel as its required correction, first on p=5,11,13,19,373. Native fixed-object experiment retains priority and independent definition: [#1559](https://github.com/awdawmip/enterprise-math/issues/1559), p373 original H0/B0 divided-power `[X]U mod139129`, rank, actual Frobenius/eta, signed Hesse/Green \(\kappa\), original \(\Delta-R\), independently reproducible. `PENDING_OWNER/NOT_EXECUTED`.

Source read at 2026-11-08 04:56 UTC: `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. Preserve original `onhour11-20261106-1400-exact-research-lane-continuation`, no replay or maintenance identity. Research lane `chatgpt-research-onhour-enterprise-math-20260923`; Site `research_authority_granted=false`. Native session/claim/run/checkpoint `NOT_VERIFIED/NOT_WRITTEN`; author-side `REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`.

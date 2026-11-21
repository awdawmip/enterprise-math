# CBRC F7 Driver r461 — exact rational B=11 finite-box minimax certificate

Date: 2026-11-22 (Asia/Taipei). Original model author: **EM-CBRCF7-83A1D4**. Exact finite-box extension/checker: **EM-DVR-DEBB5E** (shared, nonblind context). The original frozen Result **RR-AA38973D56330E59D315** is unchanged.

## Original model and theorem

Let A = I + uvᵀ, with u = (1,1,−1,−1)ᵀ and v = (1,−2,−1,2)ᵀ. The function q: ℤ² → [0,∞) is defined globally and must satisfy:

- q(0,0) = 0;
- q(−x,y) = q(x,y);
- q(s,0) = 1 whenever s ≠ 0;
- q(x,y) ≥ 1/2 for every (x,y) ≠ (0,0);
- the two fixed-scale marks q(2,1) = q(−1,−1) = 1/2.

For z = (a,b,c,d), define D_q(z) = q((Az)₁,(Az)₂) + q((Az)₃,(Az)₄) − q(a,b) − q(c,d).

For integer B ≥ 1, define E*_B = inf over globally admissible q of max |D_q(z)| for all z ∈ {−B,…,B}⁴. Only the error inputs are confined to the box; the admissible q itself lives on all ℤ².

**Theorem (r461). E*_B = 1/2 for every integer 1 ≤ B ≤ 11.**

This extends r460's independently saved exact theorem from B ≤ 8 to B ≤ 11 without changing the matrix, scalar hypotheses or marks.

## Lower bound — symbolic

Take z = (1,−1,0,0), which belongs to every B ≥ 1 input box. Then k = vᵀz = 3 and Az = (4,2,−3,−3). Consequently,

D_q(z) = q(4,2) + q(3,−3) − q(1,−1) − q(0,0) ≥ 1/2 + 1/2 − 1/2 = 1/2.

Thus E*_B ≥ 1/2 for every B ≥ 1.

## Upper bound — explicit finite exact certificate

The accompanying Python-standard-library-only certificate fixes denominator 40 and encodes **1,924 distinct triples** (|x|,y,n), with integer increments 1 ≤ n ≤ 24. It specifies one global q* as follows:

- q*(0,0) = 0, and q*(s,0) = 1 for all s ≠ 0.
- q*(2,1) = q*(1,−1) = 1/2, extended to negative first coordinates by the required evenness.
- At the 1,924 encoded other canonical non-axis coordinate pairs, q*(x,y) = (20+n)/40.
- At every remaining nonzero, non-axis integer pair, q*(x,y) = 1/2.

Thus q* obeys every original scalar condition on its whole domain, including the exact fixed marks. Its finite table is decoded from a compact text literal, with SHA256 of the decoded 5,772 raw bytes:

**65ec618247976ac8e7624323e052ae5cf51619a10b673b4b58f652635ad82070**.

For each of the 23⁴ = **279,841** ordered quadruples (a,b,c,d) ∈ {−11,…,11}⁴, the verifier computes using integers only:

k = a − 2b − c + 2d;

40D_q*(z) = 40q*(a+k,b+k) + 40q*(c−k,d−k) − 40q*(a,b) − 40q*(c,d).

It checks −20 ≤ 40D_q*(z) ≤ 20 for *every* input. Local exact execution gave maximum |40D| = **20**, **4,156** saturating inputs and **zero violations**. That exhaustive finite computation proves E*₁₁ ≤ 1/2. Nesting the boxes proves the same upper bound for all B ≤ 11, completing the theorem.

**Exact immutable checker:** https://github.com/awdawmip/enterprise-math/blob/ae37604bba251134205a27468a97c97cb7f880d9/research_checks/CBRC_F7_R461_BOX11_EXACT_RATIONAL_CERT_20261122.py

## Discovery and status boundary

An integer-grid optimization model produced this witness, but the mathematical certificate depends only on the explicit rational table and the standalone exact integer verifier; SciPy or an optimizer is not required to reproduce the checking.

A separate B = 12 numerical feasibility attempt was interrupted without a certificate, leaving E*₁₂ unresolved. The global infinite-domain question remains open, with the inherited bound 1/2 ≤ E∞ ≤ 4/7. The scoped r461 proof is a shared-context Driver extension and does not claim independent Native Review of the original author's frozen Result. Native Review, formal Result admission, Source/Activity linkage and Task or parent completion are tracked separately.

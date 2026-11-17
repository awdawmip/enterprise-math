# PREFIX-875 — 2-adic lift of signed-half-order BRC collisions; global 19-bit sieve

Date: 2026-11-17. Continuation: PREFIX-873 and PREFIX-874.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged.
Status: AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE / TWO_AUTHOR_SIDE_IMPLEMENTATIONS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Problem and exact observer

A named binary state u in [0,2^p) encodes p independently named source bits. A legal ordered transition is unchanged or toggles exactly one named bit: (u,u) or (u,u xor 2^i), 0<=i<p. Two fixed odd moduli (q1,q2) observe (u mod q1, v mod q2). The full transition observer is lossless exactly when these ordered residues distinguish every legal ordered transition. This is an auxiliary BRC named-source observation model with signed update directions, full source names and provenance, not an assumed native X6 dynamics.

## Theorem 875.A — 2-adic signed-half-order gap collision

Fix p>=3, N=2^p. Let g>=1 be ANY integer with 2-adic factorization g=2^nu*h, h odd and nu>=0. Let qH>qL>=3 be odd positive integers with

  qH-qL=2g.

Suppose integers m>=1 and sigma in {-1,+1} satisfy h divides (2^m+sigma). Define

  k=(2^m+sigma)/h,    j=nu+1,    i=m+j.

Assume i<p and k*qH+2^(j+1)<N.

Then both the ordered port pair (qH,qL) and its reversal (qL,qH) are NOT lossless complete-transition observers.

### Constructive proof, preserving source provenance

Because j<i, addition of 2^j toggles bit j of any integer, while both r=0 and r=2^j have bit i=0. Choose r from {0,2^j} so bit j of x=r+k*qH is 1 if sigma=+1 and 0 if sigma=-1. Set

  T0=(r, r+2^i)       [flip named source i from 0 to 1],
  T1=(x, x xor 2^j)  [flip named source j in direction -sigma].

These transitions are distinct (their old states differ by k*qH>0), and they are legal: the assumed bound gives 0<=x<N and 0<=x xor 2^j<N. As i<=p-1 and j<=i-1, r+2^i<2^p.

Their first observations coincide since x-r=k*qH. Their second endpoint difference is

  (x xor 2^j)-(r+2^i)
    = k*qH-sigma*2^j-2^i
    = k*qH-2^j*(2^m+sigma)
    = k*qH-k*2^(nu+1)*h
    = k*(qH-2g)
    = k*qL.

Thus the second observations coincide as well. The two legal ordered transitions differ in predecessor and named flipped source. Swapping old and new and reversing the port order gives a collision for (qL,qH). QED.

The earlier PREFIX-873 theorem is the nu=0 case. The novelty is the exact lift through arbitrary 2-adic valuation, by shifting both named flip indices instead of restricting the half-gap g to be odd.

## Theorem 875.B — Exact p=32, 19-bit all-half-gap family classification

Set N=2^32 and Q=2^19-1=524287. Every admissible unordered pair of distinct odd port moduli qH>qL>=3 corresponds to exactly one integer half-gap

  1<=g=(qH-qL)/2<=262142.

For each g, write g=2^nu*h. Choose the least positive signed half-order m of 2 modulo odd h and corresponding sigma; for h=1 use (m,sigma)=(1,-1). Let k=(2^m+sigma)/h, j=nu+1. If m+j>=32, the theorem gives no certificate. Otherwise let

  M(g)=largest odd integer <=min(Q, floor((N-2^(j+1)-1)/k)),
  L(g)=2g+3,
  C(g)=max(0, floor((M(g)-L(g))/2)+1).

These are exact finite integer formulas. C(g) counts all odd qH in the maximal safe interval [L(g),M(g)] and their corresponding qL=qH-2g. Disjoint g imply disjoint excluded pairs.

The complete exact arithmetic calculation over g=1..262142 gives:

  2,030 nonempty half-gap families,
  1,630 families with M(g)=Q (the full possible odd qH interval),
  400 partial intervals,
  374,090,098 distinct unordered port pairs,
  748,180,196 ordered orientations with explicit one-bit collision.

Among these, the 360 odd half-gap families contribute 61,017,906 unordered pairs, agreeing exactly with PREFIX-874. The new 1,670 even half-gap families contribute an additional 313,072,192 unordered pairs. All families are disjoint by gap.

This is complete coverage of the stated *signed-order certificate criterion* for all half-gap values. It is not a complete no-go over the entire 19-bit two-port search space: other modulus pairs need new arguments and B_fix,odd(32) remains in {19,20}. No native X6 event admission is inferred from the auxiliary result.

## Verification, artifacts, and finite proof scope

The Python 3 exact checker "PREFIX875_R6_TWO_ADIC_ALL_GAPS_CHECK.py" independently constructs the 2,030 rows two ways:

1. Direct scan of every integer g in [1,262142], extracting its odd part, least signed half-order, safe cap, count and explicit maximum-qH witness.
2. Enumerate odd divisors of 2^m-1 and 2^m+1 for 1<=m<=30 using exact integer square roots and multiply each candidate divisor by every possible 2^nu under the gap cap. Choose its least m to reconstruct the same full rows.

The two computations agree row-for-row. For each row the program checks the two one-bit flips, endpoint bounds, modular collision, and integer difference, without floating-point operations. A separate JS exact-integer implementation independently computed the count and all 2,030 maximum-qH witness instances. The paired JSON stores every parameter interval and explicit representative collision and contains the status ALL_EXACT_ASSERTIONS_PASSED.

Theorem 875.A is mathematical/algebraic for all stated p; Theorem 875.B is a complete finite exact count over the **stated criterion**, not mathematical acceptance by a separate reviewer.

### Prior valid sources

- [PREFIX-873 universal odd-half-gap collision theorem](https://github.com/awdawmip/enterprise-math/blob/b99af78b7ffb090228f4b6e27341f691b7376b6a/research_notes/portable_direct/2026-11-17_r6_prefix873_signed_halforder_gap_collision.md).
- [PREFIX-874 complete odd-half-gap sieve](https://github.com/awdawmip/enterprise-math/blob/eb143259bac3ce72c3f8a4f49a8221ef2986fe94/research_notes/portable_direct/2026-11-17_r6_prefix874_global_odd_gap_19bit_sieve.md).

## Continued research question

To close p=32, derive another source-typed collision family not limited to the qH-qL gap and count its exact union with the 748,180,196 already excluded ordered pairs, or exhibit a valid 19-bit fixed odd observer. Compare with PREFIX-871 gcd necessary conditions and PREFIX-872 conditional first-port fiber capacities. Preserve p=62 coprime 34-bit frontier as a separate objective. P000 and ACTIVE Heartbeat World 6+1 axioms, native 3D slice, BRC joint-relation provenance and scientific freeze are unmodified. No shared X6 Task CLAIM, Result or review authority is claimed here.

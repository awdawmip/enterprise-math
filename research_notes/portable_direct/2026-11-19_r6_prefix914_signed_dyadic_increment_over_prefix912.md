# PREFIX-914 — Exact overlap of all-sign unequal-multiplier collisions with PREFIX-912

Date: 2026-11-19, Asia/Shanghai. Lane: 进取数论研究6.
Frozen science pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: \`AUTHOR_PROVED / TWO_IMPLEMENTATION_EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED\`.

## What is new

PREFIX-913 [theorem and first census](https://github.com/awdawmip/enterprise-math/blob/f3b77d7fae29a505b23b96116711ef0fa9742ed7/research_notes/portable_direct/2026-11-19_r6_prefix913_signed_dyadic_two_flip_all_signs.md) established a signed-dyadic bit-flip collision construction for any positive endpoint multipliers k,ell. For k=3,ell=1, i=2..22, j=1..i-1, both signs, it gave a symmetric exact raw sufficient family of 6,072,620 ordered strict-19-bit odd modulus pairs. That count did not yet establish an increment over the existing PREFIX-912 certificate union.

**This addendum completes the exact overlap**. Retain Q={262145,262147,...,524287}, M=131072, and complete named trajectories Z_x=(x,x), F_x^t=(x,x XOR 2^t), 0<=x<2^32, 0<=t<32. Let C912 denote the explicit symmetric sufficient-collision union documented by PREFIX-912 (7,795,529,828 ordered pairs), and A denote PREFIX-913's *oriented* 3:1 all-sign family. Then the exact integer calculation yields

\[
\begin{aligned}
|A|&=3,036,491,\\
|A\cap A^T|&=362,\\
|A\cap C_{912}^{\rm base}|&=2,963,137,\\
|A\cap (C_{912}\setminus C_{912}^{\rm base})|&=95,\\
|A\setminus C_{912}|&=73,259,\\
|(A\setminus C_{912})\cap(A\setminus C_{912})^T|&=0.
\end{aligned}
\]

The earlier sufficient union C912 is symmetric by construction, so the exact set-theoretic increment is

\[
\Delta_{914}=|(A\cup A^T)\setminus C_{912}|
=2(73,259)-0=\boxed{146,518}.
\]

Therefore

\[
\boxed{|C_{914}|=7,795,529,828+146,518=7,795,676,346}
\]

certified distinct ordered pairs in the 17,179,869,184-pair full domain. The complement of this **explicit sufficient certificate union** has

\[
17,179,869,184-7,795,676,346=\boxed{9,384,192,838}
\]

pairs. These remaining pairs are not certified noncollisions.

## Why the previous union is reconstructed exactly

The exact canonical implementation of PREFIX-912, \`research_notes/portable_direct/PREFIX912_R6_MIXED_12X12_CENSUS.cpp\`, defines a baseline predicate from its inherited sufficient families: overall capacity, 552 special rows, zero-step gcd criterion, two maximum-fiber conditions, 192 panel rows, 1,391 gap-class values, 169 d907 differences, and 37 d908 differences. The checker reconstructs all these exact sets, with the regression cardinalities
\`(base,mid,hi,special,panels,d907,d908)=(258,276,857,552,192,169,37)\`.
The baseline is symmetric in a,b.

PREFIX-908 through PREFIX-912 added precisely the opposite-parity 72-channel square 1<=k,ell<=12 of sufficient equations \`ka-ell*b=2^i+s\` (1<=i<=22, s=±1), together with their transpose. The earlier (2,1) source restricted i<=19; for this family on Q, 2a-b is strictly below 2^20-1, so the wider i<=22 introduces no extra (2,1) pairs. The earlier union's de-duplication and overlap handling affects numerical attribution, not membership: every earlier multiplier pair is in the stated 72-channel union, and conversely these channels are exactly those enumerated in PREFIX-912. Thus membership in C912 is exactly the baseline predicate or existence of any one of the 72 opposite-parity signed-low-bit equations on (a,b) or (b,a).

A is generated without enumerating all Q²: for every signed-dyadic D=eps*2^i-eta*2^j, b=3a-D; the mapping D=3a-b is unique for each oriented (a,b). The checker scans every valid a progression, tests C912 membership, and intersects with the transpose family via D'=3b-a. The second implementation instead scans b first, independently builds the inherited arithmetic families using a reversed loop order, and tests all 72 low-bit channels on surviving pairs. Both independently reproduce the full eight integer counts above.

## A concrete *new* collision witness

The ordered pair (a,b)=(321651,440665) is **outside C912's implemented predicate** and lies in A with k=3,ell=1, i=20,j=19, eps=eta=+1:

\[
3(321651)-440665=524288=2^{20}-2^{19}.
\]

Choose x=83,623 and y=1,048,576. Two named legal XOR tracks are

\[
F_{83623}^{20}=(83623,1132199),\qquad
F_{1048576}^{19}=(1048576,1572864).
\]

The start difference 964,953 equals 3a, and the endpoint difference 440,665 equals b. Both ports have identical residues on these distinct trajectories; all four states lie in 0..2^32-1. The product ab=141,740,337,915 also exceeds the old global-capacity threshold 33*2^32=141,733,920,768. This witness is independently checked against every inherited membership predicate and every old opposite-parity multiplier channel.

## Reproducibility and boundaries

The attached C++17 tool independently reconstructs PREFIX-912's sufficient union and calculates all 3,036,491 PREFIX-913 witnesses by exact integer arithmetic, reporting the eight counts and one uncovered example. Run \`g++ -std=c++17 -O3 -Wall -Wextra -pedantic PREFIX914_R6_SIGNED_DYADIC_912_OVERLAP.cpp -o p914 && ./p914\`.

The accompanying independently written Python 3 script enumerates the candidate population **second-port first**, re-derives inherited base/mid/hi difference sets in a different loop order, checks all old channels, and asserts the same complete category counts. Both local executions returned exit code 0 and exactly the same 146,518 additional ordered pairs. The JSON certificate records counts, exact domain and representative witness.

This is a collision *sufficiency* result about the auxiliary named-XOR two-port observation and is not an assertion of a native X6/BRC event equivalence, a universal classification of noncollision, mathematical independent review, admission, or closure of the mother question \`B_fix,odd(32) in {19,20}\`.

**Next scientific frontier:** quantify the complete same-parity unequal multiplier families beyond (3,1), establish a finite bound or generator for signed-dyadic D classes under p-bit headroom, and compare with exact two-flip carry constraints on the remaining complement. Maintain provenance, the immutable scientific input and symmetric de-duplication. Shared X6 native owner request \`r6-20261119-0400-x6-owner-read-prefix913\` is unresolved as a live authority source; this auxiliary artifact does not grant or assert a shared CLAIM.

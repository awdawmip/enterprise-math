# R131 — Exact pulse certificates and output-sensitive algorithm switching

Date: 2026-11-14 (Asia/Shanghai). Author-side S23 auxiliary mathematics; independent review pending.

Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: R130, immutable research commit 7040bd2b6f134ea105f75370f0e35f1294818b64, research_notes/brc_s23_av_r130_sparse_event_log_20261113/PROOF.md and BENCHMARK.md.

## Observer and output distinction

Consider S_i(theta) = 1[ {x+(A+i*d) theta} < {E theta} ], 0<=i<m,
where m>=1, {z}=z-floor(z), and strict comparison is retained.

Fix the special but unbounded coefficient family

  x=0, d=0, A=B, E=1, B integer >=2, theta in (0,1).

All m coordinates are the same bit S_B(theta)=1[{B theta}<{theta}].
The two output contracts considered are (i) existence of an m-bit signature with an exact rational witness, and (ii) the explicit ordered trace of signatures and cut positions over the full parameter interval.

## R131.1. Exact half-open pulse theorem

For every real theta in (0,1) and integer B>=2,

  S_B(theta)=1 if and only if theta lies in
  Union_{k=1}^{B-1} [k/B, k/(B-1)).

The B-1 intervals are pairwise disjoint; the last right endpoint is 1 and outside the parameter domain. The exact set of cuts where the indicator changes is

  C_B = {k/B : 1<=k<B} U {k/(B-1) : 1<=k<B-1},

and |C_B|=2B-3. Every listed cut is an actual transition; left endpoints have value 1, interior right endpoints value 0. There are 4B-5 singleton/open-cell representatives when every cut and open cell is represented separately.

Proof. Let k=floor(B theta). Since theta is in (0,1), 0<=k<=B-1 and
k/B <= theta < (k+1)/B. Also {theta}=theta and {B theta}=B theta-k.
The strict comparison is equivalent to (B-1)theta<k, or theta<k/(B-1).
For k=0 it is impossible. For k>=1, the resulting interval is
[k/B,k/(B-1)) and is contained in its floor fiber because
k/(B-1) <= (k+1)/B iff k<=B-1. For k<=B-2, strict inequality against
(k+1)/B gives a nonempty zero gap before the next pulse; the last pulse
ends at 1. At k/B the fractional part of B theta is zero and the other
is positive, so the value is 1. At each interior k/(B-1), the two
fractional parts are equal, so the strict comparator yields 0.
There are no collisions between left and right cut families:
k/B=j/(B-1) implies B divides k, impossible for 1<=k<B.
Thus the counts and transition assertions follow. QED.

## R131.2. Constant attainable-word image and logarithmic witnesses

For every m>=1 and B>=2, the achievable joint signatures are exactly
{0^m,1^m}; no mixed word can occur. Exact witnesses are

  theta_0 = 1/(2B),
  theta_1 = (1/B + 1/(B-1))/2 = (2B-1)/(2B(B-1)).

Each is in (0,1). The first lies before the first pulse; the second lies
strictly inside the first pulse. Because d=0, every coordinate is equal.
A deterministic membership-and-witness algorithm scans an m-bit input
once, rejects mixed bits, and otherwise returns the appropriate rational
above. It uses O(m) input inspections and a constant number of integer
arithmetic operations on O(log B)-bit operands. Standard exact
arithmetic therefore gives bit cost polynomial in m+log B. QED.

## R131.3. Exponential explicit-output separation

Any algorithm explicitly materializing all distinct ordered cuts of
this family emits at least 2B-3 records; explicitly materializing each
open cell and singleton signature emits 4B-5 position records.
For input bit-length L=ceil(log_2(B+1)), along B=2^n these
counts are exponential in L. The R131.2 membership-plus-witness
contract, however, is polynomial in m+L.

This lower bound is on *explicit trace output* only: it is not a lower
bound for a compressed representation, an oracle, or every possible
algorithm for the existential query. Indeed the pulse formula itself
compresses the complete ordered trace to O(log B) bits plus fixed
description overhead. QED.

## R131.4. Aligned-clock scaling and repeated periods

Let integers r>=2, e>=1, K>=1 and m>=1. Set x=d=0, A=r*e, E=e and
theta in (0,K/e). Then the common bit is {r*e*theta}<{e*theta}.
Writing phi=e*theta, the complete 1-set is

  Union_{n=0}^{K-1} Union_{k=1}^{r-1}
    [(n+k/r)/e, (n+k/(r-1))/e) intersect (0,K/e).

There are exactly K*(2r-2)-1 distinct actual cut locations in the
open parameter interval. They consist of K*(r-1) pulse starts,
K*(r-2) non-seam pulse ends, and K-1 inter-period seams n/e.
At a seam both fractional parts are zero (singleton bit 0); the left
limit is 1 and the right limit is 0. The image of attainable joint
words is again {0^m,1^m}; witnesses in the first period are
1/(2*r*e) and (1/(r*e)+1/(e*(r-1)))/2.

Proof. The two fractional parts depend only on phi modulo one, and are
{r phi}, {phi}. Apply R131.1 to each interval n<phi<n+1, then observe
that at every interior integer phi=n the limiting 1-to-0 change is
also a genuine cut. Counting the pulse starts, non-seam ends, and seams
gives K(2r-2)-1. QED.

The scale parameter e may be large while the normalized ratio r is
small. This special family realizes the gcd period quotient studied
in R129; no universal extension to arbitrary phase coefficients is
asserted here.

## Algorithmic consequence

R130's exact sparse event log is well suited when the ordered trace or
indexed access to it is the desired output. For the family here the
number of real transitions grows linearly in B even though exactly two
joint signatures occur. A query interface should match the algorithm
to its requested output:

* Existence of a given signature and exact witness: R131.2, in
  polynomial input-bit complexity.
* Full explicit trace: list the pulses, paying the necessary output
  cost, or retain the symbolic R131.1/R131.4 representation until
  expansion is requested.
* General x,A,d,E: compare R130 trace construction with R127 two-integer
  and R126 three-integer feasibility after accounting for preprocessing,
  input bit lengths, precision, output and witness recovery.

For d=0 the equality of all coordinate readouts is proved and can be
used to avoid repeating m identical tests; this statement is about the
specific auxiliary observer only. No native X6 Cell/Link/Port
admissibility, provenance quotient, or foundational theorem is inferred.

## Exact validation and evidence status

Companion check_r131.py (Python Fraction only) independently evaluates
the original strict fractional-part indicator. For B=2..160 it covers
all 50,721 exact singleton/open-cell rational representatives of the
complete cut partitions and checks all pulse values and witnesses;
additionally 5,000 seeded random rational checks with B<1,000,000.
It constructs exact witnesses for a 151-decimal-digit B.
The scaled family is tested on 144 (r,e,K) cases and 12,912 exact
parameter points. Result: R131_PULSE_SWITCH_PASS.

The accompanying benchmark builds an *independent explicit trace*
versus an exact two-witness certificate at B=64,256,1024,4096, each
with 3 repetitions. These are distinct requested outputs; timing is
a diagnostic rather than a same-output speedup claim. See
verification_r131.json and BENCHMARK.md.

Proof status: complete for the four stated special-family theorems,
author-side, not independently reviewed. Finite tests support the
implementation and boundary semantics only.

## Next precise question

For d!=0 and nonaligned A,E, find a computable criterion showing
when a given signature can be decided with a short integer
feasibility certificate rather than expanding the full ordered trace.
Build a working exact two-/three-integer feasibility solver and
benchmark complete bit cost, memory, witness recovery and output type
against R130, preserving the frozen scientific inputs.

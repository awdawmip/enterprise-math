# PREFIX-652-R6 — 精确三槽位分布形状实算及非零误差见证

Date: 2026-11-10 (Asia/Shanghai). Role: independent TASK_RESEARCH.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_INTERVAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Mother target: global variance maximum for the frozen signed two-informative-direction BRC 189-layer first-stop statistical observer.

## Problem, inputs and computation

PREFIX-651 proved an O(q^-3), one-sided three-slot extrapolation with q,2q,4q. We now give a *worked, rigorously enclosed center-point instance* at p=1/6,z=19/128 and q=12,24,48, using exact certified cumulant enclosures already published by PREFIX-645 (immutable source f11c0345bf89321aba48d90671c244bdec25d416:research_notes/portable_direct/PREFIX645_R6_RESULTS.json).

For the Poissonized first-stop maximum Y, let a=E[Y], b=Var(Y), c=κ₃(Y), d=κ₄(Y). The upstream six-decimal exact rational certificates yield strict intervals:
  54327837/500000 < a < 4346227/40000,
  42102733/125000 < b < 67364373/200000,
  -1209500201/1000000 < c < -6047501/5000,
  25187126503/500000 < d < 50374253007/1000000.
The bound endpoints are passed as closed outer interval inputs for the interval program; the original bounds remain strict.

Write t=1/q, B=b-at and set
  γ₁(q) = (c-3bt+at²)/B^(3/2),
  γ₂(q) = (d-6ct+7bt²-at³)/B².
Define R_i=γ_i(12)/3-2γ_i(24)+8γ_i(48)/3 and γ_i,∞=γ_i(q→∞).

The companion certificate uses exact Fraction endpoint arithmetic throughout; square roots are enclosed by integer isqrt at scale 10^18. There are no floating-point comparisons in assertions and no direct evaluation of the original 189-layer transition system in this round. The program computes all twelve finite/infinite shape and extrapolation intervals from the upstream rational cumulants (and a JSON of full intervals on local execution); the committed compact JSON retains the certified comparison bounds and check count.

## Result 652.1: exact 48-slot shape ranges

At the center parameter pair,
  -201083135/10^9 < γ₁(48) < -201083133/10^9,
   451414521/10^9 < γ₂(48) <  451414524/10^9.

These are strict rational enclosures derived from the pinned PREFIX-645 moment inequalities, not estimates based solely on floating point.

## Result 652.2: signed and *nonzero* three-slot extrapolation errors

At the same parameter pair,
  -1/300000 < R₁−γ₁,∞ < -1/400000 < 0,
   0 < 1/160000 < R₂−γ₂,∞ < 1/120000.

Thus both opposite error directions of PREFIX-651 are realized with strictly nonzero signed errors at a concrete model point. These bounds also lie inside the PREFIX-651 universal magnitude bounds:
  |R₁−γ₁,∞| < 1/276480,
  |R₂−γ₂,∞| < 11/829440.

Approximate displays (not verification steps) from the certified intervals:
  γ₁(48) ≈ −0.2010831344, γ₂(48) ≈ 0.4514145224;
  R₁−γ₁,∞ ≈ −0.0000028824, R₂−γ₂,∞ ≈ +0.000007082.

## Proof and numerical meaning

For intervals [l,h], sums use [l₁+l₂,h₁+h₂], negation [-h,-l], products the extrema of four endpoint products, and division by an interval of fixed nonzero sign uses its exact reciprocal endpoints. Every b−at is positive, and the square-root enclosing operation uses isqrt(floor(x·10^36)) for x rational, giving L=floor(sqrt(x)·10^18)/10^18 and U=(floor(sqrt(x)·10^18)+1)/10^18 with L≤sqrt(x)<U. Outward enclosure propagates to γ_i at q=12,24,48 and infinity, then the extrapolation linear combination and difference. The sixteen named strict rational assertions in the companion program establish all stated coarse rational signs, sizes and q=48 ranges. All comparisons are exact Fractions.

This result is conditional on the already published exact six-decimal cumulant bounds of PREFIX-645; they were not recomputed or independently reviewed in this round. Original 96-port native BRC physics was not executed. The (p,z) coordinates are observer variables, not a claim of a native two-dimensional plane; P000 remains unchanged. The 48-slot value is an exact mathematical model observable, not a claim of an executed 48-slot physical experiment.

## Provenance and next

PREFIX-645 source: f11c0345bf89321aba48d90671c244bdec25d416.
PREFIX-651 theorem: fffa4e08af63ebf4caff3117a6ffcfa88a3d0b8f.
Exact test: PREFIX652_R6_THREE_SLOT_INTERVAL_WITNESS.py.
Compact result: PREFIX652_R6_RESULTS.json.
Validation: 16 exact rational assertions passed (local Python 3 standard library).

Next: use the signed error witness to optimize a four-slot cancellation and compare with the q=12,24,48 estimator; independently strengthen the moment envelopes with Bernstein/score localization on a broader parameter rectangle. The mother variance-maximum problem remains open.

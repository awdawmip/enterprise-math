# Exact residual counting with robust sample routing

This note concerns complete ascending order of a `uint64_t` multiset. The
retained observer includes the value and multiplicity of every input occurrence.
It does not include the original position or attached records. The experiment
extends the preceding exact count-and-spill representation; it introduces no
new spatial carrier or BRC address convention.

## 1. The invariant that makes sampling safe

Let A be the current input multiset and let I be the union of the disjoint
numerical intervals chosen for counting. A completed membership scan constructs

\[
\mu_A=\sum_{x\in I}c_x\delta_x+\sum_{y\in E}\delta_y.
\]

Here `c_x` is the exact count of x and E retains every input occurrence outside
I. A sample selects I; it does not certify membership of an unexamined value.
Each actual value is independently checked and contributes to exactly one side
of the identity. Inclusive range checks and 128-bit span arithmetic cover both
endpoints of the uint64 domain without wrapping a full span to zero.

For an accepted node, the counters emit their values in increasing numerical
order. Recursively sorting E and merging the two sorted multisets therefore
produces exactly the ascending order of A. This proves the accepted case by
induction. Small-array comparison sorting and the inherited exact radix
fallback prove the terminal cases. Before a failed cell or spill test, A itself
is unchanged, so abandoning an incomplete histogram and sorting A is safe. For
an aborted scan, the same identity applies to the scanned prefix rather than
the complete array.

Removing a value from the training sample is never removing it from A. Every
such value is still counted if covered or retained in E if uncovered.

## 2. Four routing policies

All policies preserve the preceding sample cap 1,024 (S=min(m,1024) at a modeled
node), small-array cutoff 256,
depth cap 16, counter budget

\[
C(m)=\min(4\cdot2^{20},\max(4096,\lfloor m/2\rfloor)),
\]

and actual spill acceptance `|E| <= floor(m/2)`.

### Dense gate

If the sample's exact numerical span is at most C(m), inspect the true minimum
and maximum of the complete input. If their span also fits, use one dense
counter interval with those true bounds. Otherwise retain the original learned
layout and continue. The rejected probe adds a complete min/max scan; the
successful route avoids recursive holes inside a compact range.

### Global-tail trim retry

Only when the original learned counter demand exceeds C(m), take
`t=floor(S/64)`, select sample order statistics at zero-based ranks `t` and
`S-t-1`, and rebuild from all sample observations inclusively between these two
values. Boundary ties are all retained. This is at most one retry, not an
adaptive sequence of progressively more favorable quantiles.

The layout must still fit the counter budget, and its actual spill count must
still contract. Sample quantiles affect speed, not exactness.

### Combined dense gate and trim

Try the dense gate first, then the trim retry on an oversized original layout.
If the exact dense check rejects, the original useful sparse-bin model remains
available. This is the combination of the preceding two changes.

### Compact sampled interval and exact spills

If the sample span itself fits the counter budget, choose one contiguous
interval containing it, with bounded padding, without a complete-input min/max
probe. Values outside this interval remain exact spills. If the original
sample is not compact and its ordinary layout is too large, perform the same
single trim retry; use a compact interval when the retained bounds fit, and
otherwise use the accepted ragged-bin layout.

The padding is a fixed arithmetic rule, not a parameter fit to held-out times.
For inclusive span W, original sample count S and remaining budget C-W, set
`d=max(8,floor(4W/(S+1)))`. Initially allot left padding up to half the surplus,
d, and the distance to zero; then allot right padding up to the remaining
surplus, d, and the distance to UINT64_MAX. Allocate unused surplus to the left
and then right, subject to the same d and domain caps. All intermediate widths
use 128-bit arithmetic. The resulting interval contains the selected sample
bounds and has width at most C.

One bucket with origin at its low endpoint and shift `bit_width(width-1)` is a
valid representation. Every covered offset has coarse index zero; the exact
local interval test rejects any uncovered offset that also maps to zero. No
shift by 64 is required. The same count, emission and merge implementation can
therefore be reused.

The diagnostic `compact_accepted` records bounded interval selection. It does
not certify a successful scan: a later `compact_spill_radix` path can reject the
actual spill count and take no recursive edge.

## 3. Work certificate and its scope

Let m_i be the actual input size at recursion depth i. Every accepted edge has

\[
m_{i+1}\le\lfloor m_i/2\rfloor,
\qquad \sum_i m_i<2m_0
\]

for a nonempty finite chain (the non-strict bound also covers the empty input).
The input-population sum is not a total instruction count: sample learning,
counter initialization, membership checks, emission and merging each incur
their own work and must be charged separately.

A modeled node has m >= 257. Its original sample size is at most m, its coarse
bucket count at most 1,025 < 4m, and its allocated counter length at most
C(m) < 16m. Each policy has at most one extra sample bounds scan, one optional
full-input extrema probe, and one fixed-size rank-trim retry. `std::nth_element`
is not being asserted to have a standard worst-case linear guarantee. The
sample size is bounded by the fixed constant 1,024 in this implementation, so
its selection cost is bounded independently of large m; the implementation's
comparison cost is not inferred from diagnostic visit counters.

Only the actual retained spills recurse. If e_i actual occurrences are
uncovered after a completed accepted scan, a nonempty spill vector creates one
edge with child size e_i. A rejected prefix records floor(m_i/2)+1 spills and
child size zero. Thus spill counts are occurrence counts, not edge counts, and
their sum over levels can include the same surviving occurrence again.

Count emission totals telescope:
if the final terminal uses a baseline sort on t values, total counter-emitted
values are n-t; a final count leaf gives exactly n. Merge writes can be much
larger than the number of spills, because a low outlier can move a long suffix
of the covered output. The diagnostics record those writes explicitly.

After the permitted repair, a selected layout that is still over budget, a
failed contraction, or the depth cap invokes inherited offset radix on the
unchanged current input, using at most seven 10-bit passes for
uint64. Its extrema scan, allocations and output are included in the measured
call. Small terminals have at most 256 values. Thus, assuming successful
allocation, the implemented algorithm has an O(n) operation and O(n) auxiliary
storage bound in the fixed-64-bit word-cost model. Ancestor buffers and child
buffers obey the same geometric population bound; small actual spills do not
erase the parent's `reserve(floor(m/2)+1)` allocation cost.

This bound is already available to fixed-width radix sorting. For general
w-bit integers the established radix bound is
`O(ceil(w/d) * (n + 2^d))`; arbitrary-precision input requires an explicit bit
cost model. A complete materialized output also requires at least n element
writes in the worst case. These distinctions determine the meaning of a
claimed complexity improvement.

Primary background source: Pat Morin, *Open Data Structures*,
[Counting Sort and Radix Sort](https://opendatastructures.org/ods-cpp/11_2_Counting_Sort_Radix_So.html).
The exact count/spill certificate above is the argument for this implementation.

## 4. A constructive family rescued by the single trim

Consider twenty clusters

\[
I_j=[a+j2^g,a+j2^g+7],\quad j=0,\ldots,19,
\]

with a aligned to 2^g, g >= 8, and all intervals inside uint64. In this positive
family, A consists only of values in these twenty intervals and tails strictly
outside [a,a+19*2^g+7]; internal-gap contamination is excluded by hypothesis.
Suppose S=1,024 sample observations touch every cluster. Let c_- and c_+ be the counts of sampled
tails strictly below and above the cluster union. Require c_- <= 16 and
c_+ <= 16, and enough endpoint-cluster observations to survive the trim:
the first cluster has more than `16-c_-` observations and the last more than
`16-c_+` observations.

Then the selected bounds remain inside the first and last clusters. All sampled
far tails are excluded from layout learning, each interior cluster retains an
observation, and both endpoint clusters remain represented. The inherited
power-of-two grid rule chooses shift g-5. The preceding local-width lemma gives
at most 40 padded counters per cluster, hence total counter demand <= 800.
This fits every modeled node's minimum budget of 4,096. If the actual number of
tail occurrences is T <= floor(m/2), every cluster occurrence is covered, so
the completed scan has |E| <= T <= floor(m/2). Every spill is a tail occurrence;
padding can also cover some nearby tails, so equality |E|=T is not required.

For the concrete witness n=100,000, a=2^48, g=20 and 1 through 16 sampled MAX
tails, the untrimmed sample collapses the ordinary clusters into a huge coarse
cell whose local demand exceeds 19 million counters. The single trim yields
at most 800 counters. This is a deterministic sufficient condition; it does not
assume random sampling or assert that every contamination pattern is rescued.

## 5. Two exact boundaries of this policy

### Seventeen tied high observations

In the same twenty-cluster construction, with 17 identical sampled UINT64_MAX
values, zero-based rank S-17 is already
UINT64_MAX. The high selected bound remains at that extreme and inclusive tie
retention keeps all 17. The original-scale damage can remain, so the fixed
1/64 trim rejects the oversized layout. The witness tests this exact policy
boundary, not an impossibility for every robust estimator.

### Four central poisoned bins

In the twenty-cluster construction, insert sampled values
`a+j*2^20+16384` for j=8,9,10,11 while retaining ordinary sampled values in the
same bins. Keep enough endpoint-cluster mass that the global selected endpoints
remain in the first and last clusters. The grid shift is still 15. Each of the
four affected bins spans at least 16,378 counters, so their sum alone is at least
65,512, which exceeds the 50,000 budget for n=100,000. These contaminants are centrally
ranked and survive a global-tail trim.

Consequently, four specifically positioned input values can defeat this
layout-repair policy even though they are only 0.004% of the array. The complete
sort remains exact through fallback. Contamination location and local occupied
width matter alongside the contamination fraction.

This is a precise unresolved performance region: an excessively wide local bin
may consume the counter budget even when the other bins remain useful. Local
bin omission or local robust interval selection would be different policies,
requiring their own measured actual-spill certificate and frozen evaluation.

## Status

These are author-side constructive arguments and executed diagnostics for an
ordinary research experiment. Read-only parallel source review is documented
with the experiment. They are not a formal shared-task mathematical acceptance
or a claim of novelty of the general counting, radix, sampling or exception
repair ideas.

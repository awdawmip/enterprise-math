# Majority gaps, density packing, and direct ordered emission

This note studies the phase-three implementation for complete ascending order
of a `uint64_t` multiset. The retained carrier is an exact value histogram on
selected intervals plus every uncovered input occurrence. Its observer is the
complete ordered value sequence, including multiplicities. This is the same
count-and-residual interface used in the
[frozen phase-two theory](https://github.com/awdawmip/enterprise-math/blob/1001e80fd510c8de6a9761dc20068e0e3c8c671d/experiments/brc_residual_sort_adaptive_20261110_b0e94005/THEORY.md).
The new work changes interval selection and output construction.

Typed reuse is an extension of that existing BRC residual-sorting family.
The population consists of finite input occurrences, each carrying one unit of
nonnegative integer count mass. Retained branches have a bucket/value label;
uncovered branches keep their exact values as explicit residual occurrences.
Their alternative composition is multiset addition. The desired observer and
allowed subsequent readout are the nondecreasing numeric values with all
multiplicities. Original occurrence indices may be forgotten for this observer;
associated payloads and stable record order are outside the present interface.
The histogram-plus-residual carrier retains exactly the information required
for this declared readout.

## 1. Implemented selection policy

Let a modeled node contain n occurrences and an original sample of
S=min(n,1024) observations. Its inherited counter budget is

    C(n) = min(2^22, max(4096, floor(n/2))).

The original compact interval is considered first when its span fits, followed
by the original learned grid. An oversized grid is offered to density packing.
If that proposal is rejected, the complete original sample is sorted once and
at most three majority-gap cuts are considered. After each cut, the retained
sample window rebuilds a grid with the existing padding rule; selection again
prefers compact, then the full grid, then density packing. The first viable
model gets one actual membership scan. There is no model retry after that scan.

Density packing orders all positive-width bins by decreasing
`learning observations / padded counter width`. Ratios are compared by integer
cross products. Ties use larger learning mass, then smaller width, then smaller
original bin index. Starting with an empty retained set, it keeps each bin that
fits the remaining budget and skips a bin that does not fit. It commits only
if the retained learning mass is at least ceil(S/2), using the original S.

The implemented density rule does not calculate the fractional certificate or
run the dynamic program in Sections 6-7. Those sections analyze the rule and
give a concrete continuation method.

## 2. Exact output directly from bucket intervals and residuals

Let the retained positive-width intervals be

    J_q = [low_q, low_q + width_q - 1],

listed in increasing coarse-bin order. The inherited grid and padding routine
keep each interval inside its own coarse cell. The intervals are therefore
disjoint and ordered. The compact model has one interval with its grid origin
equal to its lower endpoint. Setting omitted widths to zero preserves these
properties.

### Interval exclusion lemma

Every input occurrence whose value lies in a retained J_q passes the exact
`count_sampled` membership test and increments exactly one counter. Hence no
actual residual value lies in any retained interval.

For a grid interval, x in J_q implies x>=grid.origin, its shifted quotient is
q, and x-low_q<width_q. The compact case satisfies the same test. Conversely,
every membership hit is in its retained interval. This proves exclusion for
the actual residual multiset, including padded parts of each interval.

### Direct emission lemma

After recursively sorting the residual vector E, process retained bins in
numeric order. Before each bin, find the first remaining residual value not
less than low_q, copy that lower residual block into the output, and then
expand all counters in J_q. Copy the residual tail after the last bin.

The copied residual prefix is below the entire bin. The exclusion lemma says
that the next unconsumed residual, if any, is above the entire bin. The emitted
bin is internally ordered; all later bins are larger. Induction proves that
the complete output is ordered. Every counter occurrence and every residual
occurrence is written exactly once, so this emitter performs exactly n value
writes at this node.

The input vector can serve as the destination because the counters and the
sorted residual vector are independent storage, and the original input values
are no longer needed after the successful membership scan. No additional
output vector is required. A retained interval with all-zero actual counters
is harmless. A zero-width omitted interval is skipped. No exclusive interval
end needs to be formed in `uint64_t`, including at the maximum value.

The implementation uses `lower_bound` on the remaining sorted residual suffix
once per retained bucket, then block copy and counter fill. With B retained
bins, L counter positions and e residual occurrences, its output-stage work is

    O(L + n + B log(e+1)).

The no-residual path uses the inherited direct count emission. This cost
statement describes the actual binary-search implementation, not a hypothetical
linear two-pointer loop.

### Exact saved-write formula

The old output path first writes n-e counted occurrences and then backward
merges them with E. Let W be that merge's number of value writes. When e>0,

    W = e + #{counted occurrences h : h > min(E)}.

Every residual must be copied. Every counted value greater than the smallest
residual must move while that residual remains to be placed. As soon as the
smallest residual has been placed, the old loop stops and leaves all remaining
counted values in place. This proves the equality, also when values repeat.

Thus old count emission plus merge writes

    n + #{counted occurrences h : h > min(E)},

and direct emission saves exactly W-e writes, between 0 and n-e. One residual
below every counted value can force all counted occurrences to be rewritten;
when every residual is above every counted value the saved-write count is zero.
For e=0, both output paths write n values.

These are value-array writes of a single accepted counting node. Recursive
child sorting, histogram increments, temporary vectors and fallback writes
remain separate work. Savings over the whole sort are the sum over its accepted
counting nodes. Legacy `emitted_values` counts semantic covered occurrences;
it should not be added again to a direct-output write counter.

## 3. The majority-gap operator

Write the original sorted sample as x_0<=...<=x_(S-1). At a repair step the
current window is [l,r), with R=r-l retained observations. Put h=ceil(S/2).
For a positive adjacent gap x_(k+1)-x_k, l<=k<r-1, its side masses are

    left = k-l+1,        right = r-k-1.

The gap is admissible precisely when max(left,right)>=h. The operator chooses
the largest positive admissible numerical gap, breaking equal gaps at the
smaller index. It retains the larger side, breaking equal side masses in favor
of the lower-valued side. The current window is then replaced by that side.

Every cut preserves at least h original observations and removes at least one.
No equal-value block can be split because only positive adjacent gaps are
eligible. This replaces the implicit symmetry of two-ended rank trimming with
an explicit population choice. The retained windows are nested; at most three
cuts are attempted by this implementation.

The largest *admissible* gap matters. A larger gap whose two sides are both
below the original-sample threshold is not eligible, even when another smaller
gap would preserve enough observations. Likewise, when the current window has
exactly h observations, no positive split can preserve h and the process stops.

The certificate concerns retained sample mass. The exact scan, rather than this
certificate, establishes the actual population contraction.

## 4. A source-compatible family repaired in at most two cuts

Set a=2^62, D=2^60, and define twenty core clusters

    K_j = {a + j*2^20 + r : r=0,...,7},      j=0,...,19.

The only other permitted values are the optional tail points a-D and a+D.
These all lie in the `uint64_t` domain. Let n>=1024, so S=1024. Assume the
actual deterministic sample contains strictly more than 512 core observations,
includes both endpoints of every K_j, and may contain either or both tail
points. Assume the complete input has at most floor(n/2) tail occurrences.

### Why repair is reached

If a tail is present in the sample, the original coarse shift is 51 or 52.
All core observations occupy one coarse cell because a is aligned and the
core's total span is only 19*2^20+8. Its learned counter width is at least that
span, which exceeds the maximum budget 2^22. The compact span also exceeds
the budget.

Density packing cannot keep that over-budget core bin. The tail bins together
contain fewer than 512 learning observations, so selecting only them fails the
original-sample mass gate. The majority-gap repair is therefore reached.

### Why the cuts preserve every core observation

The gaps separating a sampled tail from the core are larger than every gap
inside the core. A tail point has fewer than half the original observations;
the opposite side contains the strictly majority core and is the larger side.
Consequently the largest admissible gap removes a tail side and retains all
core observations. If another sampled tail remains, the same argument removes
it on the next cut. With both tails, the intermediate layout still contains
the same oversized core bin, so neither grid acceptance nor density packing
interrupts the second cut.

The strict majority hypothesis is material: with exactly 512 observations on
each side, the specified lower-side tie break can retain a low tail instead of
an upper core. The theorem uses strict majority to avoid that tie.

### The restored layout and actual residual population

After the tails are removed from the sample window, the grid shift is 15.
The twenty core clusters lie in distinct coarse bins with raw width 8. Since
each bin has at least two endpoint observations, its padding is

    max(8, floor(32/(s_j+1))) <= 10.

Both a and every j*2^20 are multiples of 2^15, and the restored grid origin is a.
Each cluster therefore begins at its coarse-cell boundary, so left padding is clipped;
the padded width is at most 8+10=18. The entire counting layout consequently
uses at most 20*18=360 slots, below the minimum budget 4096. Every possible
actual core value is covered, and both tail points remain outside the layout.

The actual residual multiset is exactly the actual tail occurrences. It meets
the assumed half-input bound, so the node accepts recursive residual sorting.
This establishes a concrete family in which at most two one-sided cuts remove
only tails and recover a small counting layout.

A high-only variant uses the same argument with any aligned valid translation
and a sufficiently distant upper tail. In particular, a sample with 300
identical upper-tail observations and 724 suitably distributed core observations
retains the upper-tail boundary under every old symmetric cut 16,64,256.
The majority-gap operator can retain all 724 core observations in one cut.
Exact benchmark constructions and their chosen translations are specified in
the harness; the family above supplies the sufficient geometric conditions.

## 5. What density packing fixes, and what it can miss

For a fixed learned grid, let positive padded widths and learning masses be
(w_j,s_j). Density packing selects a feasible subset under sum(w_j)<=C, then
checks its retained learning mass. Its objective differs from minimizing the
number of omitted bins.

For example, take S=1024, C=50000, and bins

| Bin | Padded width | Learning mass |
|---|---:|---:|
| A | 45000 | 900 |
| B | 40000 | 60 |
| C | 20000 | 64 |

Widest-first omission removes A and then B to fit the budget, leaving mass 64.
Density packing retains A first, then skips the others, leaving mass 900 and
passing the threshold 512.

These exact widths can be realized by the inherited layout code. Choose a
65536-aligned base a=2^48; put B,A,C at coarse positions 0,256,512 respectively.
Use raw inclusive spans 37539,44802,18841 and sample masses 60,900,64, split
equally between each interval's two endpoints. `make_grid` gives shift 16.
The left endpoint is the coarse-cell boundary, so the resulting widths are

    B: 37539 + floor(4*37539/61)  = 40000,
    A: 44802 + floor(4*44802/901) = 45000,
    C: 18841 + floor(4*18841/65)  = 20000.

At n=100000 the budget is 50000. The first old symmetric cut 16 keeps all endpoint
ties, so its model has these same masses and widths. A full input with about
90% values across A and 5% across each other raw interval, followed by at most
1024 sample-position overwrites, gives at most 11024 actual spills when A is
retained. The exact benchmark input recipe and output checks determine its
observed count; this loose bound already certifies half contraction.

Density ordering itself is not a complete solver of the retained-mass problem.
For widths (6,5,5), masses (12,9,9) and budget 10, it keeps the first bin, skips
the remaining two, and obtains mass 12. The required half mass is 15. Selecting
the last two bins instead fits the budget and retains mass 18. This is an
abstract fixed-layout counterexample, not a claim about the frequency of such
layouts in the measured input families.

## 6. An exact upper certificate for the fixed-grid choice

This section is analysis and a separately executed finite selector oracle;
the timed kernel does not calculate this certificate.

Discard bins with w_j>C for the purpose of the optimization: no feasible
integral subset can retain them. Sort the remaining bins by density. Fill the
capacity fractionally in that order: take complete bins while they fit, then
take the fitting fraction of the first nonfitting bin. If P is the full-prefix
mass, r the remaining capacity, and (w,s) the first nonfitting bin, define

    U = P + r*s/w.

If all bins fit, U is their total mass. For any integral feasible subset with
mass M*,

    M* <= floor(U).

To prove the bound, relax each retain decision from {0,1} to [0,1]. Moving equal
width from a later positive-density item to an earlier not-yet-full item does
not decrease mass. Repeated exchanges produce the fractional prefix above,
which is therefore optimal for the relaxation. Every integral subset is a
feasible fractional one, and its mass is an integer.

Let G be the actually obtained density-greedy mass. Then

    G <= M* <= floor(U).

Consequences for the fixed grid are:

- G=floor(U) certifies that greedy retained the maximum possible learning mass.
- floor(U)<ceil(S/2) certifies that no subset can meet the sample-mass gate.
- G<ceil(S/2)<=floor(U) leaves the existence of a passing subset unresolved.

All operations can be exact: ratios use integer cross products and the last
fraction uses integer floor division. The certificate concerns the fixed
sampled intervals and learning masses. It does not optimize actual population
coverage, recursive cost or output writes, and it does not assess other grids.

### Executed finite check

The retained script `selection_certificate.py` enumerates all 3-bin layouts with
each width and learning mass in {1,2,3,4,5}, and each capacity in {1,...,10}.
Here S is the sum of the three masses. It checks all eight subsets as the exact
reference and evaluates the integer upper bound and greedy gate.

The actual executed 156,250 cases all satisfied G<=M*<=floor(U). There were 121,805
sample-optimal certificates, 37,660 certified half-mass-infeasible cases, and 1,629
cases where greedy failed the half-mass gate although a passing subset existed.
The first latter case was widths (1,1,2), masses (1,3,5), capacity 2: greedy mass 4,
exact optimum 5, upper floor 5. Certificate categories can overlap and are not a
partition. These are exact counts on the stated finite domain, not workload
prevalence or sorter timing results. The script and original observed stdout
are preserved in `selection_certificate_results.json` without a reassurance
rerun after saving.

## 7. Exact mass-index dynamic programming as a continuation method

For fixed bins, define D_i[m] as the minimum counter width needed to retain
exactly m learning observations using the first i bins. Initialize
D_0[0]=0 and D_0[m>0]=infinity. The recurrence is

    D_i[m] = min(D_(i-1)[m], D_(i-1)[m-s_i] + w_i),

with the second term present only for m>=s_i. Values above C can be saturated
at C+1, and individually infeasible bins can be removed. Induction on i proves
the recurrence: every subset either omits or includes the final bin.

The largest m with D_B[m]<=C is the maximum feasible retained learning mass.
Thus the recurrence resolves the ambiguous certificate case exactly for the
fixed grid. It costs O(B*S) time. A descending mass update uses O(S) cost
storage; reconstructing the selected set can use per-item take bits. Mutable
one-dimensional predecessor chains alone are unsafe because later updates can
overwrite their historical states.

Active bins have positive learning mass, so B<=S<=1024. A dense take-bit matrix
has at most 1024*1025=1049600 bits, or 128.125 KiB before alignment; row-word
padding may use 136 KiB. Saturated costs need only 32 bits because C<=2^22.
These bounds concern a possible implementation, not measured phase-three work.
The current timed selector deliberately remains the simpler greedy rule; the
certificate and recurrence identify the next exact selection unit if its
additional cost is justified by the experiment.

## 8. Population validity, misleading gaps and total cost

The inherited exact histogram-plus-residual invariant proves output
correctness. Every recursive child still requires actual e<=floor(n/2), giving
sum of recursive node sizes<2n. A scan that encounters its floor(n/2)+1-th spill
aborts on that prefix and radix-sorts the untouched complete original input.
Neither density mass nor a majority-gap cut replaces this population check.

Largest-gap selection can lose ordinary structure when an internal core gap
is larger than the separation of a tail. At the operator level, consider
100 observations at 0, 400 at 10 and 524 at 1000, with the latter two locations
declared the intended core. The largest gap keeps only the 524 upper-core
observations and drops 400 other core observations along with the 100 low-tail
ones. This illustrates the gap rule itself; the small numerical example would
fit the original compact budget and therefore need not reach repair in the
full algorithm. Likewise, sample majority can differ from population majority,
as the preserved hidden-majority witness from phase two demonstrates.

A viable original grid can also have poor actual coverage. Because repair
starts only after a counter-budget rejection, the new selector does not change
that route before its exact scan. First-model selection, actual half rejection
and output construction are separate mechanisms whose measured costs should
remain separate in the report.

At a node, acquisition, grid building, density sorts, the one sample sort,
up to three sample-gap scans, rebuilding, counter initialization, membership,
child sorting and output all incur work. Density ordering costs O(B log B);
sorting the bounded sample costs O(S log S); direct emission adds the actual
O(L+n+B log(e+1)) stage described above. Fixed sample/bin/depth parameters and
the inherited budget and 64-bit radix fallback retain the previous linear word-
operation and auxiliary-storage class. The exact n-write output theorem gives
a concrete operation saving within that class.

This note records source-based proofs, constructive input conditions and one
finite exact selector enumeration. Implementation tests and measured timings
are recorded separately by the harness. The review is author-side work in a
shared research context.

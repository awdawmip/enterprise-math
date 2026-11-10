# Complete half-mass repair on a fixed learned grid

Phase four extends the phase-three density/gap selector with a bounded exact
repair of the whole-bin selection problem. It reuses the same exact membership
scan, actual half-residual recursion rule and direct interval output. The
population is a finite `uint64_t` multiset with unit nonnegative count mass per
occurrence; the observed output is its nondecreasing numeric values with all
multiplicities. Original position and associated record stability are outside
that value-only interface. This is an extension of the existing BRC residual
sorting family.

The direct-output exclusion and exact-write lemmas are inherited from the
phase-three `selection_kernels.hpp` and `THEORY.md`. The earlier exact
histogram/residual invariant and actual contraction rule are also documented
in the [frozen phase-two theory](https://github.com/awdawmip/enterprise-math/blob/1001e80fd510c8de6a9761dc20068e0e3c8c671d/experiments/brc_residual_sort_adaptive_20261110_b0e94005/THEORY.md).
This note isolates the new selection theorem and a realizable distinguishing
input. Implementation tests and timings belong to the separate harness records.

## 1. The exact finite decision problem

At one modeled node, let the original sample contain S observations and let
the current learned grid have positive-width bins j=1,...,B. Each bin has
padded counter width w_j>0 and learning mass s_j>=1. Its current retained
sample window may be smaller than the original sample, so

    sum_j s_j = R <= S.

Let C be the counter budget and h=ceil(S/2). The fixed-grid question is whether
there is a subset K satisfying both

    sum_(j in K) w_j <= C,
    sum_(j in K) s_j >= h.

Only complete existing bins may be retained. Their intervals and learning
masses are fixed during this decision. The denominator remains the original
sample S, including after gap repair has reduced the current window.

Any bin with w_j>C is individually infeasible and may be removed from this
optimization. No integral feasible subset contains it. The remaining bins
retain their original numeric locations for eventual exact membership checks.

## 2. The implemented decision cascade

The new repair is entered only when the inherited density-greedy proposal has
failed the sample half-mass threshold. It proceeds as follows:

1. Check the feasible singleton with greatest learning mass. If it reaches h,
   retain that singleton.
2. Otherwise compute the exact integer floor of the density-ordered fractional
   upper bound. If the floor is below h, reject this fixed-grid selection.
3. Otherwise solve the finite mass-index dynamic program. Select the largest
   attainable mass whose minimum required width is at most C. Accept exactly
   when that mass reaches h.

The inherited successful density proposal still returns immediately. Whole
grids and compact intervals that already meet the budget retain their original
fast paths. After a fixed-grid rejection, the existing bounded majority-gap
rebuild sequence remains available. The first selected representation receives
one actual membership scan, and the actual half-residual test remains decisive
for recursion.

This cascade is complete for the existence question in Section 1. A greedy or
singleton success supplies a feasible witness; a fractional rejection proves
that no such witness exists; the remaining dynamic-programming branch decides
the question exactly. The maximum-retained-mass property belongs to the DP
branch. An early greedy or singleton success can have smaller mass than another
feasible subset while still correctly answering the half-mass question.

## 3. Exact fractional rejection certificate

Sort individually feasible bins by decreasing s_j/w_j using integer cross
products. The inherited tie rules make this order deterministic; they do not
change the fractional bound. Fill capacity fractionally in that order. Suppose
the completely fitting prefix has width W and mass P, and the next bin has
width w and mass s. Its remaining-capacity upper bound is

    U = P + (C-W)*s/w.

If every bin fits, U is the total remaining learning mass. The implementation
only needs floor(U), obtained by integer floor division.

**Upper-bound lemma.** Every integral feasible subset has mass at most floor(U).

Relax the retain variables from {0,1} to [0,1]. If a later-density bin has
positive retained weight while an earlier-density bin is not full, transfer
equal width from the later bin to the earlier bin. This preserves width and
does not decrease mass. Repeating this exchange produces the full prefix plus
at most one fraction described above. It is therefore an optimum of the
fractional relaxation. Integral feasible subsets are included in that relaxed
set; their integer masses are bounded by floor(U).

Consequently floor(U)<h proves that no subset of this fixed grid can satisfy
the required half-mass gate. A bound at least h leaves both feasibility and
infeasibility possible and triggers the exact DP when no earlier witness was
found.

Removing individually infeasible bins before relaxation strengthens this
certificate legitimately: those bins already have retain variable zero in
every integral feasible solution. The resulting certificate remains about the
fixed whole-bin problem, rather than a different grid or actual input coverage.

## 4. Dynamic program and reconstruction

For feasible bins 1,...,B, define D_i[m] as the minimum counter width required
to retain exactly m learning observations using only bins 1,...,i. Let infinity
be represented by C+1, since widths larger than C are irrelevant to feasibility.
Initialize

    D_0[0] = 0,
    D_0[m>0] = C+1.

The recurrence is

    D_i[m] = min(D_(i-1)[m],
                 min(C+1, D_(i-1)[m-s_i] + w_i)),

where the second term is used only for m>=s_i and a reachable predecessor.

**Exactness.** Every subset of the first i bins either omits bin i, giving the
first term, or includes it together with a subset of the preceding bins of
mass m-s_i, giving the second. Conversely, either finite term constructs such
a subset. Induction therefore gives the exact minimum width at every mass.
The maximum m with D_B[m]<=C is precisely the maximum feasible learning mass.

### Descending update

The cost row can be updated in place by decreasing m. Since s_i>0, the source
entry m-s_i is smaller than m and has not yet been updated for item i. It still
holds the preceding-row value. Hence each bin is used at most once.

For reconstruction, allocate a fresh zeroed take-bit row for every processed
item. Set take[i,m] only when taking item i strictly improves the current
minimum width. Equal-width alternatives keep the existing skip choice. Starting
from the chosen final mass, traverse the item rows backward: a set bit selects
that item and subtracts s_i; an unset bit keeps the mass unchanged.

This reconstruction is valid even though the old cost rows are not retained.
A set bit records the identity D_i[m]=D_(i-1)[m-s_i]+w_i; an unset bit records
D_i[m]=D_(i-1)[m]. Following those identities reaches D_0[0]. A mutable
one-dimensional predecessor chain would not provide the same historical-state
guarantee, which is why the per-item decision bits are retained.

### Arithmetic and size bounds

S<=1024 and every positive bin has at least one learning observation, so B<=S.
The time bound is O(B*S). Cost storage is O(S); selected-set reconstruction uses
O(B*S) bits in addition to the existing bin metadata.

The counter budget is at most 2^22. With individually feasible w_i<=C and the
sentinel C+1, an unsaturated candidate sum is at most 2C+1<2^24, so 32-bit cost
entries suffice. The fractional product (C-W)*s can reach 2^32 and therefore
uses a wider intermediate. Existing exact density comparisons use 128-bit
cross products. No floating-point rounding enters the decision.

The dense theoretical take-bit matrix has at most 1024*1025=1049600 bits,
128.125 KiB before alignment; a layout with 17 64-bit words per row uses 136 KiB.
These are storage bounds, not peak resident-memory measurements. Ancestor
histograms, samples and residual vectors remain charged separately.

## 5. Why a singleton shortcut alone is insufficient

Consider three bins with

    widths = (6,5,5),
    masses = (12,9,9),
    C = 10, S = 30, h = 15.

Density greedy first keeps the width 6, mass 12 bin; neither remaining bin fits
the remaining capacity 4. The best feasible singleton also has mass 12. Both
fail the threshold 15. The last two bins together cost 10 and retain mass 18.
The fractional upper bound is floor(12+4*9/5)=19, so it correctly sends this
case to the DP, which finds mass 18.

The phase-three exact finite enumeration already supplies a broader set of
related failures. Across 156,250 three-bin configurations with each width and
mass in 1,...,5 and capacity in 1,...,10, greedy failed the half-mass gate while
a feasible subset existed in 1,629 cases. That retained evidence is motivation
for this exact repair; it is not rerun or relabeled as a phase-four sorter
performance result.

## 6. A realizable padded-grid witness

The following construction uses the inherited grid and padding functions,
rather than an arbitrary abstract width table. Take n=100000, C=50000,
S=1024 and a=2^48. Define three raw intervals starting at

    A: a,
    B: a + 256*65536,
    C: a + 512*65536.

Their raw inclusive spans are 29711,24680,24680. At the deterministic 1024 sample
positions, place the following endpoint observations:

| Bin | Low-end observations | High-end observations | Total mass |
|---|---:|---:|---:|
| A | 205 | 205 | 410 |
| B | 153 | 154 | 307 |
| C | 153 | 154 | 307 |

The complete sample span has bit width 26, giving coarse shift 16. Every raw
lower endpoint is aligned to its coarse cell, so left padding is clipped.
The right padding gives the exact widths

    A: 29711 + floor(4*29711/411) = 29711+289 = 30000,
    B: 24680 + floor(4*24680/308) = 24680+320 = 25000,
    C: 24680 + floor(4*24680/308) = 24680+320 = 25000.

All padded intervals stay inside their 65536-wide coarse cells. The total
counter demand is 80000, exceeding the 50000 budget. A has the greatest density:
410/30000 > 307/25000. Greedy keeps A, then skips both other bins, retaining 410
observations. The best singleton also retains 410. The fractional upper floor is

    floor(410 + 20000*307/25000) = 655.

The DP chooses B and C, which cost exactly 50000 and retain 614 observations.
Neither A+B nor A+C fits, and all three bins do not fit, so 614 is the exact
maximum feasible learning mass for this grid.

### Actual population certificate

Before prescribing the sample positions, fill the input with 40000 values from
A's raw interval, 30000 from B's and 30000 from C's, cycling uniformly through
each interval's consecutive values. Then overwrite the 1024 actual sample
positions with the endpoint observations in the table.

With B and C retained, every original B/C value is covered. Every original A
value is a residual. The sample-position overwrites can increase the original
40000 residual count by at most 1024. Thus actual residual occurrences are at
most 41024, strictly below 50000. The exact actual membership scan therefore
accepts the DP-selected layout. This population bound does not substitute
sample mass for actual coverage.

### Why the preceding gap selector rejects this same construction

This argument concerns the phase-three rule before the exact repair is added.
The adjacent inter-bin gaps are

    A to B: 2^24 - 29710,
    B to C: 2^24 - 24679.

The second is larger. Its lower side contains A+B, mass 717, so the first gap
cut retains A+B and removes C. The rebuilt coarse shift is 15; A and B retain
their original padded widths 30000 and 25000, still exceeding the 50000 budget.
Density greedy still keeps only A's 410 observations and fails the threshold 512.

Within the 717-observation window, the large A/B gap splits 410 from 307, so it
is inadmissible under the original threshold 512. The internal A endpoint gap
has size 29710 and splits 205 from 512; the internal B gap has size 24679 and
splits 563 from 154. The largest admissible gap is therefore the internal A gap.
It retains A's 205 high-end observations and all 307 B observations, exactly 512.

The newly retained numeric span is

    (2^24 + 24679) - 29710 = 16772185 < 2^24,

so the rebuilt coarse shift is 14. The sample now teaches only three endpoint
intervals: one around A's high endpoint, and one around each endpoint of B.
Their widths are 17,9,17, a total of 43, so the model is selected before a third
gap cut.

In the population before sample overwrites, these intervals intersect at most
9 actual values in A and 18 actual values in B. Cycling 40000 values through
29711 positions and 30000 through 24680 positions gives at most two occurrences
per value. Hence at most 54 original occurrences are covered. The 1024 sample
overwrites can increase coverage by at most 1024, so final coverage is at most
1078, far below half the input. The phase-three actual scan must therefore
encounter its 50001st residual and reject, while the new fixed-grid DP selection
has the accepted population bound above.

The endpoint-prescribed sample is a deliberate mechanism witness. Its purpose
is to distinguish sample-feasibility repair from a later grid rebuild, while
keeping a separately proved actual population bound. Performance on fresh
random seed banks remains a different experimental question.

## 7. Exactness, scope and work accounting

Changing which complete bins are retained preserves disjoint ordered intervals.
Every actual occurrence either increments its exact counter or remains an
explicit residual. The established histogram-plus-residual multiset invariant
and the direct interval emitter therefore apply unchanged.

The fixed-grid selector now resolves every whole-bin half-mass feasibility
question, including cases missed by density greedy and a singleton shortcut.
Actual residual population can still disagree with the sample, so recursive
descent continues to require e<=floor(n/2). Rejected scans preserve and sort
the complete original input.

The selected-grid theorem does not search over all possible numerical grids,
gap sequences or interval splittings. Each actual grid passed to the new repair
has an exact existence decision under its stated budget and sample threshold.
That is the finite optimization problem discharged here.

The upper-bound computation is linear once a density order is available. Its
cost, singleton inspection, any order allocation and the conditional O(B*S)
DP must all be included in end-to-end timing. Only ambiguous cases pay for DP;
new diagnostics should distinguish greedy reuse, singleton acceptance,
fractional infeasibility and DP acceptance/rejection. Width feasibility,
sample feasibility, actual scan acceptance and observed runtime are separate
quantities.

Fixed S, B and recursion-depth limits preserve the earlier word-cost class.
The experiment determines whether the conditional exact selection cost is
repaid by reduced failed probes, residual work or fallback sorting. The theorem
establishes the selection capability and the constructive accepted input; it
does not assign an unmeasured runtime gain to that capability.

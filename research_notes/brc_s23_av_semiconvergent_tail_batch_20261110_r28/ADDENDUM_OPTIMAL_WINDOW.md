# R28 addendum: optimal terminal length H=164 and maximal right-neighbor batch K=9

For the frozen S23/AV auxiliary irrational-circle problem, the H=164 terminal-source certificate is minimal among suffixes [j-H,j) of the chosen j=25339 at regime k=0, and the k=0,...,9 batch is maximal among consecutive brackets with fixed lower fraction a/q=3749/14298 and upper neighbors (c+ka)/(j+kq).

## Exact H lower bound

At both endpoints of the strict frozen theta enclosure, compute the 128 original circular cuts t=0,...,127 and their increasing phase rank. For H=163, the set of terminal sources [25339-163,25339) hits precisely 127 historical arcs, missing the arc of circular rank 127, whose left historical cut is source 61. For H=164, adding t=25175 hits exactly that missing arc. The 164 terminal sources have per-arc occupancy multiplicities: 92 arcs occur once and 36 arcs occur twice. Because these windows grow monotonically with H, every H<164 also misses this arc. The order of original phase cuts and each tail-source arc membership are constant across the strict theta enclosure, as certified using exact rational endpoint floors and strict signs (see VERIFY_R28.py and VERIFY_R28_OPTIMAL.py). Therefore H_min=164.

## Exact K upper bound

Put u=q theta-a and v0=c-j theta, both positive. The k-th semiconvergent upper-neighbor error is v_k=v0-ku. The endpoint comparisons show for every theta in the enclosure,

v_9=(6644+9*3749)-(25339+9*14298)theta=40385-154021theta>0,
v_10=v0-10u<0.

The positivity condition for the specified same lower a/q and upper semiconvergent neighbor therefore holds exactly for k=0,...,9. The prior certificate checks no terminal-source historical-cut crossing through k=9, so the 10-regime batch realizes the largest allowable consecutive k-range in this chosen Farey family. This maximality is relative to the fixed lower fraction/upper semiconvergent family; the next convergent bracket may still support a different batch construction.

## Verification and evidence

VERIFY_R28_OPTIMAL.py executes both rational endpoints with Python Fraction. It explicitly checks source and phase-rank identity of the missing H=163 historical arc, H=164 multiplicities, strict v_9 and v_10 signs and strictly positive phase clearance under k=9. Its actual stdout is preserved in RUN_OPTIMAL.txt, ending in PASS_R28_OPTIMAL_H164_AND_MAXIMAL_K9.

These optimality statements identify a certified smallest source window and largest admissible batch for one concrete model family, strengthening the non-enumerative method before investigating larger continued-fraction denominators.

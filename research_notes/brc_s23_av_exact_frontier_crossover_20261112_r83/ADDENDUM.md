# R83 addendum — all-out family defeating a single global convex phase envelope

The first R83 ALL_EXCLUDED witness family was valid but its raw phases were contained in one contiguous interval above the target arc, so an implementation with an additional whole-source convex-envelope prefilter could conceivably reject the entire set before building or scanning the class frontier. This addendum constructs a stricter workload in which that single-interval shortcut is ineffective. It does NOT rule out smarter nonconvex/global modular certificates.

## Construction

For each integer g>=2 set q=g+2, theta0=1/q, I=[theta0,theta0+1/(1000 q^2)], j=x=0, a=1,b=2.

Create g distinct classes with exactly one source each:
- time t=q, branch 0, residue r=0;
- for r=3,...,q-1, time t=q+r, branch r.

At theta=theta0+delta, 0<=delta<=1/(1000q^2), the zero-class source has phase q*delta in [0,1/(1000q)], strictly below target lower boundary theta>=1/q. Each r>=3 source has phase r/q+(q+r)delta, strictly above the target upper boundary 2theta and below 1. R71's exact sufficient class-exclusion certificate succeeds separately for every class. Hence the globally latest qualifying source is NONE for ALL real theta in I.

At theta0, the raw phases of the first and last source are 0 and (q-1)/q. Any single closed real phase envelope containing both and in this common lift necessarily contains [1/q,2/q], the target. Equivalently, the raw unwrapped source values t*theta0 range from 1 to 2-1/q and their convex interval overlaps the target lifted to [1+1/q,1+2/q]. Thus a single global convex-hull exclusion certificate fails at theta0, whereas the exact g class certificates succeed. This is only about that specified convex-hull certificate, not impossibility of other global certificates.

EARLY_WINNER is obtained by inserting an independent identity t*=3q+1 of residue 1. It exceeds every previous time; its phase theta0+(3q+1)delta remains in [theta,2theta) on I, so STABLE(t*) is certified and one maximum-class lookup suffices.

## Executed exact replication, new family

The full checker `check_r83_refined.py` is a one-line-family modification of the original exact benchmark and preserves the identical R71 test, AVL invariants, source oracle and per-case four rational probe checks. Six cases g=32,128,512 x EARLY_WINNER/ALL_EXCLUDED passed.

| g | scenario | heap median ns | persistent AVL median ns |
|---:|---|---:|---:|
|32|EARLY_WINNER|29228|29739|
|32|ALL_EXCLUDED|527746|614525|
|128|EARLY_WINNER|36068|30920|
|128|ALL_EXCLUDED|2135627|2481485|
|512|EARLY_WINNER|68781|32893|
|512|ALL_EXCLUDED|8567108|10570885|

The query-structure performance direction remained the same, but remains one CPython benchmark, not an end-to-end R82 or general bit-cost result. Original R83 evidence and event are preserved unchanged. The refined exact source can be independently reconstructed from the stated rational construction and R71 certificate.

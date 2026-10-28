# Nondecisive mathematical review: prime-fiber capacity threshold

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: for the explicitly defined C(H), the nonmonotonic bit example and
the exact full-capacity set [45,62] union [66,infinity) are proved by the
given finite covers and cited Nagura theorem. No unresolved mathematical
defect was found. This is not a Driver disposition or canonical admission.

Reviewed file: `nt/prime_capacity_threshold.md`.
SHA256: `3b88d1e7566cec28291e1ce1d9b4994a5ff77e1ed543448cb5d350d6479ea89c`.
I read the inherited exact capacity definition in the complete prefix27
source and the primary Nagura PDF tool readback saved as
`nt/nagura_primary_readback.json`. Its introduction explicitly states the
x>25,6x/5 theorem used here. The older quotient remains unreviewed source
provenance; this review is of the new attained-capacity argument.

## Independent checks

For consecutive reachable factors t<u, F_H(q)=t is equivalent to
qt<=H<qu. Integer H therefore gives the displayed closed interval
[qt,qu-1]; no off-by-one error occurs. At H=27 versus 28, the t=3 interval
loses q=7 at its open lower edge, producing 5 versus 4 attained states.

State 9 requires H>=45 because 5 is the least allowed prime. For 45..62
each table row covers the whole range. For 63..65 the missing t=6 interval
lies strictly inside (7,11), whereas the six displayed other witnesses
work simultaneously. The tables for 66..225 have overlapping or adjacent
integer intervals in every row; all witness primes are admissible.

For H>=226, x=H/u is at least H/9>25. The smallest successive ratio u/t
is 4/3, strictly greater than 6/5. Nagura supplies a prime strictly between
H/u and 6H/(5u), itself strictly below H/t. This proves every intermediate
state in the infinite tail. The tail is a theorem-dependent paper proof,
not an extrapolation of a finite scan. Since 65 fails, 66 is the smallest
permanent threshold. The q>H zero state is justified by unbounded primes.

## Actual supplemental verification

I implemented a separate sieve and interval-event accumulation in
`review/independent_checks.py`, distinct from the author's trial division
and per-prime max computation. It checked every threshold 1..1000, using
all relevant primes and prime 1009 for state zero. Exactly [45,62] and
[66,1000] have seven states, with C(27)=5 and C(28)=4. Output is saved in
`independent_checks_result.json`. This is a new small integer verification;
no old prefix/divisor enumeration was repeated. It neither proves Nagura's
theorem nor the infinite tail on its own and is not a formal kernel proof.

## Scope and harvest

The sharp threshold belongs only to S={2,3}, a=(0,0), L=2 and prime
residual q>=5. The statement about minimal residual bits uses the source's
exact finite-horizon quotient, with its unreviewed status retained.
General S,a,L and composite residual fibers remain open.

Reuse resolution: REUSE_APPLIED/COMPOSE_APPLIED for the inherited quotient,
finite capacity, interval witnesses and classical prime-interval theorem.
The resulting threshold is a scoped arithmetic instance; no new global
tool family or literature novelty is asserted. The model is external
classical arithmetic, with no implicit native X6 lift.

Shared control and source context is disclosed; reviewer did not construct
the new argument and is not a clean-blind reviewer. No formal Result,
Working Truth, parent closure or old theorem promotion is granted.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH

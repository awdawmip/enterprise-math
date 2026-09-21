# POWER feedback IV: fixed-terminal moment matching and exact first-collision inversion

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`
Researcher-ID: `EM-DIRECT-16243626C61A`
Session: `local-power-review-16243626C61A` (same local continuation key, not a platform ID)
Progress-Event-ID: `power-terminal-moments-20260921-16243626C61A`
Status: `SCOPED_DERIVATIONS_AND_EXECUTABLE_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`

## Selected question and continuity

Continue the preceding fixed-suffix response problem, not the completed lift-sieve, Smith-verifier or inverse-orbit implementation. Can the terminal response be constructed without supplying an unknown order, finding all discrete logs, or generating the entire subgroup first?

The new answer is a finite interval algorithm: a dyadic suffix has a triangular exponent kernel, whose specified coefficients can be evaluated using multiplicity-aware baby-step/giant-step tables. A second result exactly inverts the first nontrivial identity collision mass, replacing the earlier overly conservative nearest-integer window requirement. This does not improve the known generic square-root order-finding complexity.

Frozen inputs: POWER `6d784d3990afae602a03745173c3f2a16a076b0c`; previous EM implementation `c6348b29fc23d611edd2a22dcb8020da24dc86e4`. Current control/activity read: EM `12428fd480bc3493f8d6a84112878a1084c705f8`; global `89a0efa7536de75a1d9731245bc97cf4d84e236e`. The existing activity and preceding immutable checkpoints were verified, and its actual local session key was retained.

## 1. Collapse the fixed dyadic program, not arbitrary future operations

At a cut j of an m-bit program set b=a^(2^j) and L=2^(m-j). In the group ring:

    product(k=0..t-1) (1+[b^(2^k)]) = sum(x=0..L-1) [b^x],  L=2^t.

This follows from the unique binary representation of each exponent x in that interval. Multiplying by the inverse-exponent version gives:

    product(k=0..t-1) (2[e]+[b^(2^k)]+[b^(-2^k)])
      = sum(d=-(L-1)..L-1) (L-|d|)[b^d].

All multiplicities are retained: exactly L-|d| ordered pairs have difference d. Thus the terminal contribution from a starting state u is

    h(u) = sum_d (L-|d|) * 1_(u*b^d=1).

Define the one-sided weighted match S(z)=sum(d=0..L-1)(L-d)*1_(b^d=z). Then

    h(u) = S(u) + S(u^-1) - L*1_(u=1).

The subtraction corrects double-counting d=0; it is not a negative BRC branch weight. Nonunit u cannot become the identity under multiplication by units and has response zero. For an explicitly supplied positive histogram c, the final coefficient is sum_u c(u)h(u). Constructing c and querying all its states remain real costs.

The matching algorithm also works for non-dyadic positive L, interpreted as the autocorrelation of a uniform exponent interval. It does not equate a non-dyadic interval with an integer-length binary program.

## 2. Construct h without an order oracle: count plus first moment

Choose B and write each nonnegative exponent uniquely as d=iB+j, 0<=j<B. In each baby-residue bucket z=b^j store

    C_z = number of matching offsets j,
    J_z = sum of matching offsets j.

For a full giant block i and target z, query the bucket z*b^(-iB). Its entire weighted contribution is

    (L-iB)*C - J.

A separate final partial-block table records the same two moments for j<L mod B. This handles repeated baby residues correctly even when B exceeds the unknown order. A table storing only one matching offset, as a witness-finding discrete-log interface may do, is insufficient for this counting interface.

No subgroup or order is supplied to the implementation. Tables are built directly from B powers, and all giant blocks are scanned. For k distinct signed targets, the work is O(B+k*ceil(L/B)) table/field operations, plus inverses, input handling and integer bit costs. Storage is O(B+k) records, at most 2B baby buckets across full and partial tables. For one terminal identity coefficient B near sqrt(L) gives O(sqrt(L)) scans and storage instead of constructing O(min(order,L)) group-state support.

This is a classical meet-in-the-middle organization with exact weighted counting, not a newly discovered baby-step/giant-step algorithm. Sage's primary documentation describes interval BSGS and its square-root interval-length cost: https://doc.sagemath.org/html/en/reference/groups/sage/groups/generic.html#sage.groups.generic.bsgs . That witness-finding API alone does not promise all multiplicities and first offset moments; this candidate specializes the required output, rather than claiming a missing generic discrete-log capability.

Budgets are explicit: insufficient scan/table-step allowance returns BUDGET_EXHAUSTED with values=None, not zero, no collision, or no factor. Reported scans exclude pow/gcd, bit arithmetic, Python allocation and caller histogram construction; they are not wall-clock or byte caps. A million-bit wrapper limit is an implementation admission limit, not a theorem boundary.

## 3. Exact terminal class count: closed formula with conditional coordinates

For this derivation only, let s=ord(b), write L=q*s+t, 0<=t<s, and suppose u=b^k. Each exponent residue has occupancy q or q+1; the extra t residues form a cyclic interval. Its autocorrelation gives

    h(b^k) = s*q^2 + 2*q*t + max(0,t-k) + max(0,t-s+k),
    0<=k<s.

Put w=min(t,s-t) and d=min(k,s-k). The nonconstant part is max(0,w-d), over a baseline s*q^2+2*q*t+max(0,2*t-s). Consequently the number of distinct terminal response values on <b> is exactly

    min(L mod s, s-(L mod s)) + 1.

Equality of these values is the coarsest state partition retaining this one linear readout for arbitrary initial masses: merging two distinct values is falsified by a point mass, and equal values clearly permit summation. At t=0 there is only one class on <b>. Ambient states outside <b> need a separate zero response if zero is not already present.

This formula is not a cheap membership/discrete-log oracle. The online matcher does NOT take s or k as inputs. Its diagnostic function cyclic_terminal_value explicitly requires those conditional coordinates and does not validate supplied order claims.

The terminal partition need not be a stepwise lumping. For s=5,L=4 the values are (4,3,3,3,3), but merging the four nonidentity states fails under another unrestricted T_b. The UNCHANGED Enterprise ControlMassQuotient.compile rejects that candidate in the tests. Thus the previous all-future inverse-orbit lower bound remains intact.

## 4. New exact inversion condition: first collision is enough

For identity mass K_L and the TRUE order r, counting positive exponent differences gives the finite integer identity

    K_L(r) = L + 2*sum(j>=1) max(L-j*r,0).

There are finitely many positive summands. Therefore:

- K_L=L exactly when r>=L;
- for 1<=r<L, K_L(r) is strictly decreasing in r: every summand is nonincreasing, and the j=1 term is strictly decreasing;
- K_L>L uniquely specifies r<L.

One may invert by integer binary search, evaluating K_L(r) in O(1) arithmetic operations using q=L//r,t=L%r:

    K_L(r)=r*q^2+2*q*t+t.

No n^2 window, floating rounding, factorization of n, or factorization of a totient is needed. Inconsistent supplied masses are rejected; the arithmetic inversion helper does not authenticate an externally supplied K as an actual group computation.

Example: n=15,a=2,L=8 gives K=16 and exact r=4. At L=4, K=4 only gives r>=4; that equality must not be promoted to exact order. This corrects the earlier small-window weakness without changing its valid large-window theorem.

The implemented order search doubles L and recomputes each fixed-program identity mass. At the first K>L, r<L<=2r. Summing the geometrically increasing sqrt(L) costs yields O(sqrt(r)) scans, with O(sqrt(r)) storage when caps do not bind. Additional integer arithmetic/inversion and bit costs remain. This is the known generic BSGS complexity scale, not a new polynomial-time order algorithm.

There is no contradiction with the earlier example showing that (total mass,current K) is not a sufficient forward state. We do NOT propagate arbitrary histograms from those two scalars. Each query is recomputed from its explicit uniform-interval program, whose special structure establishes the inversion theorem.

## 5. Actual reuse and information accounting

T0 positive BRC branch mass: applied the exact alternative/serial counting laws and retained integer multiplicities. Counts and first moments are statistics of explicitly bounded offsets, not signed amplitudes, normalized probabilities, or physical quantities.

T4 finite fiber/collision observer: applied exact pair occupancy and independently checked all supplied terminal observations against an occupancy definition.

T6 observation-safe quotient: applied the declared-terminal fiber law, proved the exact class count, and executed the existing brc_control_mass.py checker unchanged to reject unjustified stepwise promotion. Its Git blob is e8811e5f194fc57b294be7255214361fe99395d5.

The preceding inverse-orbit code was executed unchanged as a regression/comparison surface, Git blob cf34a9d48e36fae5bbb8c9538864cddf8315690e. POWER's original group_ring_order.py was hash-checked and executed unchanged, Git blob 11d4adf3ff6e56c440cfdd7974be6c28f8ff068a.

Classification: DOMAIN_OPERATOR_CANDIDATE / EXTEND_EXISTING_INTERFACE; classical BSGS specialization. No new top-level tool family, Driver acceptance, task CLAIM, Working Truth or Foundation promotion. P000 unchanged; no geometrical/physical interpretation is asserted.

## 6. Executed verification

Python 3.13.5, Linux x86_64, sparse local checkout from the preceding verified bundle.

- 28 new tests passed; combined with 25 inherited tests: 53 PASS.
- 588 default-window POWER comparisons matched exact masses and inferred orders.
- 6,468 explicit-window POWER comparisons matched exact masses. POWER's small-window rounded order fields were deliberately NOT treated as certified.
- 185,825 terminal observations matched independent exponent-occupancy autocorrelation, including nonunit and outside-subgroup states.
- 30,000 terminal class-count/sum identities and 30,000 collision-inversion identities passed.
- Arbitrary positive prefix histograms and all cut positions were tested by contraction against full forward evolution.
- Duplicate baby residues, partial blocks, every width on small intervals, exact budget refusal, invalid types and non-stepwise terminal partitions were tested.
- A larger case n=100160063,a=2 returned order 8345004, first L=8388608, at most 4,690 full+partial baby buckets, and 19,778 cumulative scans. It was separately audited by r=2^2*3*139*5003, a^r=1, and a^(r/p)!=1 for each prime p dividing r. That factorization was posthoc verification, never an algorithm input.

## 7. Matched cost measurements and the classical baseline

Each fixed-window method below computes the same K_L. Timings are medians of five calls; tracemalloc is separate and reports Python allocations, not RSS. Small timings are host-sensitive. The state-based methods retain stronger intermediate representations, so this is not an all-prefix replacement benchmark.

| n,a | L | full states / inverse states / moment buckets | full ms / inverse ms / terminal ms |
|---|---:|---:|---:|
| 1009,11 | 1024 | 1008 / 505 / 32 | 1.455251 / 1.479740 / 0.072395 |
| 10007,5 | 16384 | 10006 / 5004 / 128 | 18.184738 / 21.422044 / 0.119241 |
| 65537,3 | 131072 | 65536 / 32769 / 392 | 195.976872 / 115.018172 / 0.234011 |
| 10403,2 | 8192 | 5100 / 2551 / 93 | 10.642888 / 9.043693 / 0.178923 |

For n=65537, peak traced allocations were 15,176,960 / 10,602,252 / 63,792 bytes respectively. The 392 moment buckets include a partial-block table; the baby width is 363, not 392 different forward states.

Crucially, end-to-end adaptive mass-based order search is SLOWER than an independently implemented classical adaptive BSGS order baseline: 0.222386/0.064515, 0.506601/0.154372, 0.909343/0.378638 and 0.464328/0.121207 ms on these four cases. On n=100160063 the times are 5.314808 vs 2.979540 ms. The classical baseline also receives no order and is checked against the same references.

Interpretation: this closes an avoidable full-state expansion cost in the POWER-derived terminal observer. It does NOT establish a better generic order-finding method than BSGS. Large ratios against full group-ring propagation must not be advertised as an RSA/Shor breakthrough. No RSA-270 run or full EM/POWER repository test suite occurred.

## 8. Reproduction and next frontier

    PYTHONPATH=src pytest -q tests/test_group_ring_terminal_response.py tests/test_group_ring_inverse_quotient.py
    PYTHONPATH=src python research_notes/power_terminal_moments_20260921_16243626C61A/validate.py --power-source reference/POWER_review/group_ring_order.py --out results.json

Current candidate source: src/enterprise_math/group_ring_terminal_response.py. Tests, results.json, order_audit.json and MANIFEST.json preserve the exact checked scope. The standalone bundle retains unchanged reference sources and comparison code.

The fixed-terminal construction gap is now closed at square-root interval cost, not logarithmic cost. The next useful structural unit is a batch/multi-cut strategy that shares baby tables and explicit offset moments across many requested terminal observations, with the caller's prefix-histogram cost included. Any purported advantage should be compared with ordinary BSGS/discrete-log baselines, not solely the earlier full-state implementation. Arbitrary future-kernel support and all-prefix information remain outside the terminal-only interface.

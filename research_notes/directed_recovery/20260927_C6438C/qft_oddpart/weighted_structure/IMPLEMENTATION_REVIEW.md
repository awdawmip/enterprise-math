# Source-specific review of paid and leading-zero aggregation

Status: **SHARED_CONTEXT_AUTHOR_CROSS_CHECK / READ_ONLY / NOT_ADMITTED**.
This is a bounded static mathematical and implementation review. It did
not modify another author's source, run scientific arithmetic, repeat a
checker, or infer a general efficiency result from small examples.

Reviewed source SHA256 values:

| File | SHA256 |
|---|---|
| `aggregation/leading_zero_aggregator.py` | `f6597bcd54c4e9525ef142e3a661a0f30a14bc184169cf8d053005a8149cb7cb` |
| `aggregation/paid_aggregator.py` | `b6aec3c6dc4732e4be2bf19ca0bcc2d52a4e7630356c96abc7be8168b23a51fe` |
| `target_address/typed_target_address.py` | `c36a288369aa14f91f791b1ad07556747206b811a0573c3b6d682dd49ca319ff` |
| `period_discovery/typed_odd_part.py` | `188defd9307e461e8617243f76a8b6109309d6ac6b1834a71511172b58a6618c` |
| Previous `aggregation_theory/period_aggregator.py` | `6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c` |
| Previous `carry_executor.py` | `f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810` |

The mathematical comparison is the adjacent
`WEIGHTED_ODD_PART_STRUCTURE.md`, particularly equations (6)--(8),
and the previous frozen period-aggregation theorem and implementation.
The review found **no substantive mathematical or source-contract
defect** in the listed implementation versions. This conclusion assumes
the existing unchanged trusted program, phase-bank and native arithmetic
admission. It is not a hostile-Python monkeypatch guarantee or independent
formal admission of the new algorithm.

## 1. Counted suffix route

`pair_count` (line 11) obtains H=vM+u through actual typed division and
forms Mv^2+2vu plus the two interval-overlap terms through actual typed
products, comparisons and additions. Since 0<=rho<M, the comparison
M-rho is nonnegative and is the ordinary difference returned by the
adapter. At rho=0 the second overlap is zero; at M=1 the result is H^2.
The two tails are truncated only where the proved interval count is
zero, not by discarding amplitude signs.

`gamma_leading_zero` (line 39) first obtains a fresh actual address
replay from `_verify_address`. A certified nonmember gives a zero
relative Gram matrix because both work arguments cannot be in the
same cyclic support. Otherwise the implementation takes the maximum
leading zero length K. It does not assume a favorable prefix, reject
an early one, or modify its probability. K=0 is valid and has no promised
acceleration; the public API restricts the original depth to be positive.
The mathematical depth-zero identity is therefore outside this API,
while an empty suffix ell=0 is supported.

The calculation of g=2^min(ell,s), M=R/g and A=2^max(ell-s,0) is the
correct general-even-period reduction. For each negative or positive d,
typed arithmetic first obtains d mod R and delta=(r-d) mod R. Dividing
delta by g correctly decides divisibility of the original r-d and, on
success, gives the required quotient modulo M. Reducing A and taking
its actual verified inverse modulo M is valid; M=1 bypasses the inverse.
This covers s>ell and q=1 without silently replacing the modulus by q.

The suffix `CarryExecutor` (line 75) retains the original program and
bank while replacing history by h[K:depth]. Its coefficient routine
does not use a newly shortened modular schedule. Earlier K controls
are zero, and the active feedback index differences are unchanged,
so the actual order of every remaining word is identical. Negative
displacements use the inherited transpose rule. Every coefficient is
still a full admitted carrier matrix.

The weighted sum (lines 103--122) aligns the dyadic matrix denominators,
passes each `(count, signed_entry)` product to the actual positive-path
observer, and requires an integer result. Structural zero entries are
skipped but nonzero residual or negative entries are retained. Its
final `den << (2*K)` is exactly the raw factor 4^K in equation (8).
It avoids the inherited `_combine` helper's extra per-call division
by four. The final reduction is a representation reduction, not a
normalization of a branch. An empty term list correctly returns zero.

## 2. Paid wrapper versus the frozen contraction

`PaidAggregator._verify_address` (line 61) binds the original N, shift
at depth-1, target and actual inherited modular table. It verifies that
table and fully replays the order/address certificate before extracting
R,r or membership status. Certificate dictionary equality alone is not
the trust boundary: the downstream canonical full replay distinguishes
JSON booleans from integers and rejects altered scientific content.
An incomplete odd-budget result cannot be consumed as a period.

The `_contract_verified_period` core (line 90) preserves the frozen
algorithm: chronological high residue transitions e -> 2e+y-x,
low seeds rH+c modulo q, the two reversed carry constraints, and one
inherited division by four per layer. The new explicit reduction of
x modulo q before subtraction makes q=1 operands canonical; it does
not change the mathematical destination. Boundary matrices are
immutable and the next accumulators are fresh, so repeated q=1 seed
references do not alias mutable state.

For s>depth the permitted interval of displacements has width below R,
so at most one of r and r-R can occur. The typed R-r comparison and
the two strict interval tests match the old unique-alias branch. For
s=depth the high loop is empty and the low seeds still select the
correct zero or pure-seed matrices. At no point is a full residual
matrix replaced by its trace, corner or norm.

## 3. Order/address premises and the final comparison

The order source uses n=ceil(log2 N) actual squarings to remove the
two-primary part, a budgeted first return for the odd part, and the
first square return of b^q for the two-primary exponent. Every actual
unit order is below N, so that width bound is valid. A missing return
is PARTIAL, not a discovered smaller order.

The target source then performs the odd-projection search, two-primary
bit lifting, typed CRT assembly and a final actual b^r=z comparison.
For the bit lift, failure of a test to equal 1 or eta proves that the
target is not a power of the cyclic generator. At the final lift bit,
the test has exponent one; selecting that bit makes the complete
two-projection equality exact. Thus it does not leave an untested
noncyclic-component residual after a nominally successful lift.

The odd and two projections, bound to the same CRT r, would already
imply b^r=z by Bezout in the abelian unit group. The final comparison
is retained as a redundant executable check. The older explanation
that the ambient unit group being noncyclic makes this last check
mathematically essential was too strong; the adjacent theorem records
the correction without changing a frozen package. The implementation's
actual MEMBER/NONMEMBER decisions remain correct.

## 4. Resource and execution boundaries

This review does not establish an advantage over the old aggregator.
The leading-zero route enumerates all 2^(ell+1)-1 signed displacements;
for a long suffix it can be slower. It retains the nonzero coefficient
terms before summing, so it can use O(2^ell D^2) matrix storage in
addition to boundary matrices, temporaries and all observer receipts.
Fresh order discovery, target recovery, verification, modular inverse,
integer weights and bit lengths all remain chargeable.

The nested `suffix_evidence` must be included when summing native phase
actions, observers and retained work; the outer executor's own counters
alone do not include another executor's counters. Similarly, separate
typed table instances and replay records must not be merged merely
because they have equal modulus/multiplier labels. The evidence exposes
the relevant nested records; this note has not independently executed
or re-accounted a final result artifact.

The proposed bounded comparisons should include K=0 MEMBER, ell=0,
M=1 with g>1, s>ell, odd q, signed/wrapped displacement, and a nonmember.
Those are coverage recommendations, not claims that this static review
has run them. The parent is responsible for the separate actual checker
and its full raw receipts.

# Whole-period aggregation review

Status: SOURCE-SPECIFIC SYMBOLIC AND STATIC REVIEW / SHARED CONTEXT /
NOT ADMITTED. No scientific computation, numerical reference, remote
write or external query was performed by this reviewer. Existing author
results are attributed below; they were not independently rerun.

## Bound sources

- `aggregation_theory/PERIOD_AGGREGATION.md` SHA-256:
  `be20eb9409b1b250edfe9e0bc83fda9701253a71add4f98e3ccea8325d2302be`.
- `aggregation_theory/period_aggregator.py` SHA-256:
  `6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c`.
- `aggregation_theory/check_period_aggregator.py` SHA-256:
  `19308af165e5c979e679ae024494d5ba6ad52a3554882a409f718cb78e1eba16`.
- Inherited `carry_executor.py` SHA-256:
  `f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`.

The inherited source, exact carrier, chronology and alias reviews are
recorded in `CODE_REVIEW.md`, `TEST_PLAN.md` and `ALIASES_REVIEW.md`.

## Symbolic contraction and boundaries

The residue recurrence stores B-A, so appending high digits x,y sends e
to 2e+y-x modulo q. The chronological operator appends on the left of
each actual vector; consequently the matrix update is
O_j^x M_e (O_j^y)^T. This preserves the noncommuting word order.

For the low block, u+r0=v+2^s c implies
m-n=r0+2^s(B-A-c). Thus the selected high residue is rH+c, with a positive
carry contribution. Both possible high-boundary carries are needed;
the low boundary still has zero incoming carry. Each accepted pair has
a unique carry path, including when q=1 makes the two initial matrices
equal. Fresh accumulators prevent equal-valued seeds from being mutated
through aliases.

The stated edge cases are correct. At s=0 there is no low block and the
selected residue is r. At s=i the high seed is only e0e0^T in residue zero.
At q=1, summing all four high terms yields (I+O)M(I+O)^T; the two carry
values do not double-count a low pair. At s>i, R>=2^(i+1)=2L, so the two
candidates r and r-R cannot both lie in [-(L-1),L-1]. The strict tests
r<L and R-r<L correctly exclude both overflow endpoints. At depth zero
the symbolic statement uses the original basis correlation; the current
public implementation intentionally requires positive depth.

The scalar-slot and bit-length statements have the appropriate scope.
Residue states are summation indices, not dropped physical coordinates.
The q-state cost is polynomial in q, not in log q. Live matrix-slot bounds
exclude term lists, native intermediates and retained receipts. With fixed
dyadic words a common denominator bounds exact arithmetic, but neither
slots nor core-call counts are a total byte/bit-operation bound.

## Exact period, target address and comparator

The proof does not replace exact order by an arbitrary return exponent.
For a unit modulo N, raising b to 2^ceil(log2 N) removes its complete
two-part. A first consecutive return then certifies the exact odd part q;
the first squaring return of b^q certifies the remaining two-part. This
is a valid O(Q+log N+log Q) modular-operation discovery route under a paid
odd-part budget Q, with O(Q) potential receipt storage. It is a symbolic
algorithm in this unit, not what the current executed certifier uses.

The proposed target-address procedure also charges its work. Searching
the q-projection recovers r modulo q, and repeated powers in the order-2^s
projection recover the low binary digits. A genuine target power cannot
fail a bit test. The final b^r=z check is essential for rejecting unrelated
elements in a noncyclic ambient unit group. The straightforward O(s^2)
bit-lifting work, integer CRT and verification are retained in the cost.

For the actual reverse-square schedule, the odd part is also the odd part
of the original base's order. The same information therefore lets a
classical comparator recover that order's two-part and attempt the usual
gcd postprocessing. No factoring advantage is inferred from avoiding J
explicit aliases. Nor is a whole-distribution or arbitrary joint-work
sampler implied by the correlation oracle. In the middle regime the
unresolved q-state cost remains; in the terminal two-part suffix the prior
disjoint-coset fair-bit shortcut is available to the same comparator.

## Restricted rank lower bound

The selected high rows A=0,B=e and low columns u=0,v=l_e are valid under
2^H,2^k>=R. Odd R makes multiplication by 2^k invertible, so the selected
cut submatrix is exactly an R-dimensional identity. The resulting width
lower bound applies to an exact local linear representation of the
collision indicator at that chronological cut. It does not lower-bound
the particular contraction with the admitted words and pure seed, an
approximation, a nonlocal arithmetic method or all classical Shor
simulators. The manuscript states these restrictions explicitly.

## Implementation and existing eight-case check

The implemented certifier makes an actual fresh typed cycle walk until
its first return, at cost O(R), and retains the entire trace. Every query
replays that certificate and checks its actual target value. The code
does not implement the proof's small-odd-part discovery or digit-log route.
It strictly checks public integer depth/R/r/target inputs and inherits the
fixed program/history/phase binding guard.

High residue routing uses typed add/divide/subtract operations. Each high
and low layer invokes the existing signed `_combine` once, contributing
one factor 1/4. There is no duplicate final normalization. The s>i branch
uses the inherited positive/negative displacement executor. Immutable
Correlation objects make the q=1 duplicated seed safe.

The eight-case checker compares all D6 matrix entries with the complete
typed-alias sum, after actual full61 phase/codec admission. It covers odd
and even periods, nonzero targets, modular wraparound, retained residual
entries and the history101 noncommuting feedback sequence. It compares
the same actual words rather than an ideal reference. Its original eight
fixtures all have q=3; they are not evidence for execution of q=1, s=i or
s>i. Separate author boundary checks may extend that coverage and should
be identified by their own source and payload hashes.

The existing author summary reports eight complete matrix equalities,
eight rejected negative controls and 2,568 actual native core calls. The
payload SHA-256 is
`2a7dae92955c8ad4c4ab5b91ee49936d30dd6587bbc4ba18b79e2d453533fef5`.
The resource-accounting script reads existing receipts and separately
counts initial cycle discovery, every successful query replay, failed
replay, partial discovery, program setup, alias discovery and routing.
Equal modulus/multiplier table instances are not deduplicated out of cost.
The reported 58,313 counted typed adder-digit replays have a stated scope;
they do not include all native phase and signed-observer work, which is
reported separately. Sequential cache warmth and full admission costs
prevent interpreting query timings alone as a general simulator speedup.

The period verifier performs semantic evidence replay rather than strict
external JSON schema validation. The actual matrix query additionally
uses strict integer parameters and rechecks the target against freshly
reconstructed cycle states, so ordinary Python numeric equality in the
semantic comparison does not change this query's mathematical inputs.
Malformed external certificate schemas are outside a promise of uniform
ValueError handling or adversarial resource limits.

No substantive algebraic or arithmetic defect was found in the stated
contract and bounded implementation reviewed. This conclusion is not an
independent scientific execution or admission result.

## Separate boundary evidence addendum

The subsequently completed `check_period_boundaries.py` was also read
statically, at SHA-256
`c3a65bad94eb481a5bb9f51d2b81854db76443ef3a1a4456a757f0b0004ec6c6`.
It preserves the same frozen aggregation source and independently performs
fresh typed first-return discovery. Its nine reported complete-matrix
equalities cover:

- N17/a4/depth3, actual R=2: q=1 with a nonempty high block, both addresses,
  and seven or eight individual displacement aliases.
- N17/a3/depth3, actual R=8: s=i with addresses 0, 1 and R-1, including
  wraparound and nonzero residual entries under history101.
- N97/a5/depth2, actual R=24: s>i with the zero, positive, negative and empty
  displacement cases. The negative alias is -1; the middle target has no
  allowed displacement and returns the zero matrix.

These prime-modulus inputs are boundary verification fixtures, not difficult
factoring benchmarks. The checker compares the entire matrix with the
complete independently discovered alias sum, and reports 377 actual native
core calls. The source, payload and original eight-case sources remain
unchanged. The boundary payload SHA-256 is
`e1e94d19eb7f1155e63222710f97359be93389e88eb9bac73e1a9a154a51b35a`;
gzip SHA-256 is
`058b69363d6b5b312200db159881ca3b05313ab09713369000bbde2fb7828e2c`.

This reviewer read/decompressed the existing archives and verified their
byte hashes and receipt counts using only standard-library data handling.
The eight-case archive has gzip SHA-256
`2e5c9e9258ffe7f0102246b136d9204c5a64305c2b2d8fa09812f6dc6d5c2848`
and 2,568 stored receipts; the boundary archive has 377. No native module
was imported or rerun during this metadata verification. No unresolved
substantive finding remains for the reviewed bounded contract.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1

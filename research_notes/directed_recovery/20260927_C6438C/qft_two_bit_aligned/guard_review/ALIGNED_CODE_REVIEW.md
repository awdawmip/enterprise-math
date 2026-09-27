# Aligned two-bit adapter: static shared-context review

Verdict: **no remaining material blocker for the declared bounded run**.
This review read the complete implementation, checker and design, then read
the final incomplete-request patch and verified all final file hashes. It did
not import either Python module, execute scientific arithmetic, run a host
numerical comparator, or repeat a science test. The author's py_compile status
is compilation evidence only. This is shared-context review, not formal
independent admission or an executed-result verdict.

Final reviewed files:

| File | SHA-256 |
| --- | --- |
| aligned_two_bit.py | a6fd6cf5bfe10829c1918c50a952de22e5e2bc6cd538011f37a3bffdff5acdb2 |
| check_aligned_two_bit.py | 6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969 |
| DESIGN.md | 90605ff87a2a9f37576c57bb9f5363407c29778f87fef0c17aa6621713908876 |

The mathematical contract is the frozen two-bit note
`9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26`.
Its fixed progression formulas were checked against the full frozen direct
source `3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521`.

## Formula, boundaries and arithmetic routing

The adapter derives V, M, U, P, H, L and the observed quotient h=R/V on the
typed integer route. It rejects nonzero alignment remainder after paid work.
The compressed interval obeys M=H*P, with high bit k-ell; the original raw
denominator exponent remains 2g. Public exponent differences, loop addresses,
observed-parity sign selection and resource metadata are host wiring, not a
substitute numerical correlation evaluator.

Both displacement orientations r and R-r are retained. At r=0 the latter
starts at R, so zero displacement is not duplicated. Equal half-modulus heads
still have multiplicity one each and are added twice as two distinct
orientations. Heads outside the interval return recorded zero work without
attempting a nonempty floor table.

An even h uses one constant-sign branch. An odd h uses the even/odd index
branches with typed doubled step, canonical head and expected length. Empty
branches remain visible. Each branch calls the frozen private single
`_progression`, never its public two-orientation API. The two required sums
obtain their own canonical lengths. Their count difference must be zero or
one; when one is removed, typed operations establish that the shifted last
displacement equals M. This is exactly the empty A_one(M) term. The shifted
sum keeps the sign of the original unshifted head, with the explicit minus
sign in the stretch identity, including nonzero low remainder. Even if that
remainder is zero, the implementation still pays for the shifted call.

At most eight single progressions and sixteen top-level tables are asserted
per query. These bounds do not omit recursive nodes or digit costs. The
production path does not enumerate all displacements, labels or residues;
the checker's all-residue and all-pair loops are a separately charged test.

## Failure-state issue found and fixed before execution

The preliminary implementation allowed another `two_negative` call to replace
an existing inflight record after paid rejection, while the old arithmetic
remained in the runner. A later certificate could then include unrequested
work and fail fresh replay. The final source rejects any new request while
inflight is present, before input processing or scientific work. Two planned
negative checks retry valid input after the paid unaligned rejection and
require the complete snapshot and CALLS length to remain unchanged.

This is a terminal failed observer, not a resumable partial-request protocol.
A new observer is needed for new work; the failed observer retains its raw
trace and may be inspected. Unreturned local branch/orientation dictionaries
are not promised to survive an exception. Their recorded signed/typed
operations do survive in the runner snapshot. DESIGN now states this limit.

## Strict replay and checker evidence

Admission checks strict integer inputs, pinned implementation/dependencies and
proofs. Fresh verification executes requests in order, captures completed
replay before a semantic mismatch is raised, and captures paid incomplete
work on a failed request. Complete strict comparison excludes only the named
native cache call-delta field. The comparison does not normalize scientific
values or turn booleans into integers. A non-string key is rejected; the
checker saves attempted mutations with explicit key types.

The six declared tuples cover ell=0, adjacent/separated bit positions,
highest bit, h odd/even, t zero/nonzero, r=0, coincident half-modulus heads,
R>L and the shifted M empty tail with nonzero weight. The declared grid has
36 residue answers and 720 ordered pairs. Its comparator extracts both bits
using typed division and accumulates signed Euclidean-residue buckets with
typed arithmetic, once per tuple. Host sign routing compares observed bit
parities; there is no host pow/mod or ideal propagation comparator.

The planned negatives comprise ten ordinary pre-rejections, two paid
unaligned rejections with two nested reuse rejections, and twelve certificate
mutations. The latter consist of four early, seven complete paid replays and
one paid incomplete unaligned replay. The tail/sign mutations target values
that the symbolic fixture structure actually changes; they are not vacuous
identity edits. Coverage assertions separately check both orientations,
canonical counts, empty tails, table limits and negative outputs.

Production, comparator, positive replay, paid input rejection and negative
replay are distinct cost categories. The checker reconciles disjoint native
call intervals with the full CALLS stream and does not add maxima or nested
receipt copies as new work. Success/failure output paths are protected by
pre-existence checks and exclusive writes. Failure capture includes finished
cases, live available runners, comparator buckets/pairs and mutation attempts;
module-import failures and failure-save I/O remain outside that guarantee.

There are no execution counts or performance claims in this review. The
result remains a supplied-modulus scalar observer under V|R, not a general
unaligned implementation, order/address solver, full matrix Gram contraction
or Shor sampler. Actual execution and full-byte evidence review remain the
next separately recorded steps.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1

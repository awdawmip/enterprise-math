# Construction method and completeness obligation

Status: METHOD FIXED; FULL RUN AND INDEPENDENT AUDIT PENDING.
Task and q/K boundaries are exactly those in CHECKPOINT_01.md.

## Existing implementation reused

Production prime generation calls primesieve.numpy.primes(lower, upper - 1)
from the unmodified official primesieve 2.3.0 Windows wheel. The loaded C++
library reports version 7.5. The task adapter uses an exact int64 NumPy carrier
below 2^63, computes adjacent differences, and retains every difference >=916.
The runtime/wheel distribution hashes are fixed in
isolated-primesieve-environment-manifest.json.

This reuses the segmented sieve of Eratosthenes, rather than claiming a new
prime-generation algorithm. The mathematical sieve invariant is: a composite
integer n has a prime divisor <=sqrt(n); crossing off all such prime multiples
eliminates every composite, and starting at each prime's square does not erase
primes. Wheel/pre-sieve implementation optimizations must preserve that invariant.
The finite computational attestation relies on the pinned implementation and
recorded execution, with independent checks described below; it is not a formal
verification of the compiler, processor or binary.

The toolkit facade offers prime/status and finite quotient primitives but does
not supply the required complete high-range labelled consecutive-gap catalogue.
Those domain interfaces are NOT_APPLICABLE as a replacement catalogue provider.
The accepted R005 scanner is reused unchanged. The small plain-sieve function in
validate_adapter.py is an intentionally independent validation oracle, not a new
production toolkit. No Bellman, Morse, recurrent or signed-amplitude mechanism is
needed by this fixed finite enumeration.

## Partition and pair completeness

The full scan is the half-open interval
[1291000000000000,1295000000000000), partitioned into 4000 disjoint half-open
blocks of width 1000000000. This padding supports four independent published
pi(x) count differences at 1e12 boundaries; it does not broaden the requested q.

Each block records its exact integer boundaries, count, first/last primes,
maximum internal consecutive gap and a witness attaining that maximum,
all internal gap rows >=916, and a SHA-256 of the full ordered uint64_le
prime sequence. Empty blocks must retain their empty state, never silently
turn into a fabricated boundary prime.

For the ordered nonempty block sequences P_1,...,P_r, every consecutive pair of
the concatenation occurs either inside exactly one P_i, or is
(last(P_i),first(P_(i+1))). No other pair is consecutive.
Thus the complete pair count is
sum_i (|P_i|-1) + (r-1) = sum_i |P_i|-1.
All >=916 pairs and the largest pair difference follow by taking the union of
internal rows and those boundary pairs, retaining their original start labels.
The reducer must reject a missing block, overlap, order drift or inconsistent
boundary. The observed first/last primes must bracket the complete task band.
For gap starts between the first emitted prime and the last emitted prime minus
one, every possible consecutive-prime pair has its successor inside the observed
complete sequence.

The final task catalogue filters the complete labelled rows to starts in
[1291005053866735,1294364244470160]. Its coverage metadata must state that exact
band; out-of-band padding rows remain in the construction ledger. Its maximum
gap bound may use the audited whole-run maximum as an upper bound on the subset.
Any observed gap above frozen G=916 must remain visible and prevent an unsupported
attestation.

## Independent checks

The adapter was compared to a plain independent sieve through 100000 and to the
accepted deterministic uint64 Miller-Rabin function on every integer in two
high-range windows. A known real 916-gap was cut inside its composite interior;
the two partial blocks plus their boundary pair reconstructed the exact full gap.
These are genuine pilot checks, not full-band coverage.

The author-hosted TOS pi table was fully downloaded and byte hashed. Only its
five relevant original rows are projected into independent-prime-count-targets.json.
Both endpoints of every 1e12 cell are even and exceed 2, so the published
pi(upper)-pi(lower) is also the count on this construction's [lower,upper) convention.
After all blocks finish, each of the four sums must equal its independent count.
Counts alone do not prove positional completeness; they check the complete
sieve execution and indexing in addition to the algorithm's invariant.

Every reported relevant 916-gap and dangerous candidate will receive separate
endpoint/interior verification, including explicit composite factor witnesses
when required. A zero-row catalogue is allowed only after the complete coverage,
pair stitching, maximum-gap and independent-count obligations all succeed.
The accepted scanner must then run without its row-verification skip flag.
Its own attestation Boolean never supplies the missing completeness proof.

## BRC observer boundary

The retained carrier consists of coverage-indexed labeled prime-gap events,
ordered boundary ports (first,last), integer counts and exact maximum witnesses.
For this frozen future observer (gap threshold 916 and the q78553 shadow map),
smaller individual gaps may be discarded after their maximum/count checks and
boundary ports are retained. The full prime-sequence digest is a reproducibility
checksum, not a substitute for the lost prime values. Future queries below the
retained threshold require regeneration; a count or first-occurrence table alone
cannot recover the required start labels.

Alternative union across block populations and serial boundary gluing are
different operations. The cross-boundary pair is retained explicitly before
the threshold projection. No positive-weight or total-only compression is used
to infer gap locations. This applies the current BRC provenance/observer typing
without introducing artificial recurrence or a new general tool family.

## Sources

- Frozen accepted scanner at source 0d0344880a4cbb2b78ae8a5a074758fc3392c70f,
  experiments/r005a_p2_gap_shadow_inversion.py,
  SHA-256 6fe2dc9fe05ac16ef2bbd1919d3d03fc5b36037d010ca95afeafb62f4958d3f5.
- BRC substrate at that source,
  definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json.
- [TOS prime counts](https://sweet.ua.pt/tos/primes.html),
  [data](https://sweet.ua.pt/tos/primes/1d12.txt.gz).
- [TOS prime gaps](https://sweet.ua.pt/tos/gaps.html),
  [aggregate data](https://sweet.ua.pt/tos/gaps/t0.txt.gz).
- [Official primesieve Python distribution](https://pypi.org/project/primesieve/2.3.0/).


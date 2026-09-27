# Structural hybrid for the single-negative-bit scalar query

Status: DESIGN_AND_SOURCE_ONLY. No scientific import, observer execution or
performance experiment is authorized or claimed by this file. The first run
requires this stage's actual startup receipt and parent source review.

The input remains strict integers g>=1, 0<=k<g, R>=1, 0<=r<R and stride=1.
L=2^g, U=2^k and w(x)=(-1)^bit_k(x). The unchanged answer is the signed
ordered-pair sum K over 0<=x,y<L with y-x=r modulo the supplied counting
modulus R. Its external raw normalization is 4^(-g); negative values remain
valid. The observer neither supplies an order nor changes a phase program.

The route is selected by mathematical structure, never by fixture number:

1. If k=g-1 or k=0, call the frozen EndpointSignedGapObserver. Its existing
   highest-bit priority covers g=1,k=0. Do not compute U or test divisibility
   in the routing runner for endpoint inputs.
2. Otherwise compute U by k actual typed doublings, then the actual signed
   Euclidean division U=qR+v. If v=0, obtain the returned zero through the
   actual typed subtraction U-U and retain that receipt.
3. If v>0, call the unchanged frozen DirectSignedGapObserver with all original
   inputs. Its repeated scale construction is retained and charged.

The zero route is justified by pairing each x with x with bit k toggled. This
stays inside [0,L), flips w and changes x by U or -U. When R divides U it
preserves each residue. Every signed residue histogram is zero, hence so is
its cyclic autocorrelation K(R,r). This is an already available cancellation
special case. The typed division certifies the only extra arithmetic premise;
the strict input domain proves that complete pairs of U-blocks fill [0,L).
An arbitrary zero output or a claimed branch flag is not a certificate.

## Source and evidence contract

The new HybridSignedGapObserver owns three separate runners: routing,
endpoint, and direct. No frozen source is edited or monkeypatched. Export
retains the complete routing arithmetic and complete endpoint/direct
certificates, including their unused empty runner records. Each hybrid request
records its routing operation interval and its nested request index and full
returned record. Thus all mathematical work and its ordered provenance remain
available without pretending nested copies are independent executions.

The pinned endpoint source is c75e7e82cc0ef2413048153716f5100f3a9d1d4f50c375b7cb1690c3cfe6e036
from sep27-qft-gap-shortcuts/endpoint_gap/endpoint_signed_gap.py. The pinned
direct source is 3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521
from sep27-qft-gap-direct/direct_gap/direct_signed_gap.py. Both use frozen
signed-gap helper 86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a
and typed floor runner 633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2.
Their original proof/source checks remain in force. This design is itself
pinned by the new implementation.

The new schema is BRC_STRUCTURAL_HYBRID_SIGNED_GAP_V1. Fresh verification first
checks strict JSON, schema, own/dependency/proof pins and all request inputs.
It constructs a fresh hybrid observer and executes the same ordered input
list. The whole certificate must match under strict JSON, including every
route, value, division, operation, nested record and full evidence. Only the
three named native_kernel_calls_delta fields are normalized because a global
primitive-column cache can already be warm. Their original nonnegative
strict-integer values and the actual global CALLS stream remain in execution
evidence. No mathematical field or typed digit cost is omitted. Tuple/list
equivalence is inherited JSON encoding, while bool and integer remain distinct.

The verifier does not separately replay each nested certificate after replaying
the whole hybrid input list: that would repeat paid arithmetic. Its fresh
endpoint/direct objects execute the frozen algorithms and their complete
exported certificates are part of the final strict comparison. Mismatched
certificates retain the complete successful fresh replay; interrupted replay
retains available incomplete data without invoking additional arithmetic.

## Declared bounded checker and cost accounting

The proposed sole run reuses the nine tuples and all 31 residues of the frozen
direct experiment, whose original gzip hash is
3ac0ebc17112afb9f068e39c1ebb91afd8f6e3f6aeb3d6cd46044d0733b26354 and decoded
raw hash is 48780f175bc4bcf673345ee8c0b9e0240cc1c2a0e166037720c5fc06b8483157.
Read and hash the whole payload; use its saved values as historical references.
Do not rerun direct-only, one-window or exhaustive historical computations.
For each tuple retain one production certificate and one fresh positive replay.

Eight invalid input tuples cover bool, g, lower/upper k, R, lower/upper r,
and unsupported stride. Certificate negatives cover schema/source/bool,
branch choice, zero quotient/remainder/U/subtraction/output, nested endpoint
and direct values/provenance, and routing evidence. Every paid negative replay
is saved; strict early rejections are distinguished from paid work.

Production, positive replay and negative replay costs are separate. Within each
hybrid execution, add the routing, endpoint and direct runner digit/typed/host
wiring costs once each. Do not sum repeated nested request copies or cumulative
snapshots. Record moment requests/nodes/cache hits and signed operation counts
per runner. The three runners share the process-global actual full-adder
columns; retain the single global CALLS stream once instead of multiplying its
observation by the number of certificates that embed the same source receipt.
Construction, hashes, serialization and Python overhead are not inferred from
digit counts. A whole-checker wall time is not a matched performance benchmark.

Before execution, reject any existing success, summary or failed-execution
artifact. Keep exclusive writes and a LIVE registry of current observer,
completed cases, replay captures and attempted mutations. Unexpected failure
retains available runner arrays, counters and global calls without invoking
evidence generation that might observe a new primitive. Pre-import and
incomplete-constructor failures cannot promise a fully constructed observer;
that boundary must remain explicit.

Aligned-progression and two-bit lifting are excluded from this version. This
is a bounded structural dispatcher for one scalar family, not arbitrary masks,
full matrix Gram contraction, an order oracle or general Shor dequantization.
Any improvement must be established by the new paid run, not by summing the
best historical branch costs.

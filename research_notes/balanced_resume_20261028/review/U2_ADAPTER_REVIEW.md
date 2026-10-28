# Nondecisive implementation and mathematical-interface review: U2 adapter

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the adapter addresses the two stated finite-prefix I1/I2 interface
defects with explicit incidence forwarding and source/path retention. No
unresolved defect was found in the bounded API and targeted checks below.
All G1-G5 native-event/occupancy obligations remain UNKNOWN.

Reviewed note: `native/U2_INCIDENCE_ADAPTER.md`, SHA256
`47d14702e4d5bcb4dac14ec175ab55d36ee5017bb3c516f28af0ff2708e47796`.
Reviewed implementation: `native/u2_incidence_prefix.py`, SHA256
`7a4ce17c5c5e5ef00c99b95e01b81336c069bfdabe9ecc93cb9b74108ec3c030`.
I read the complete adapter and the relevant complete pinned Packet/kernel
interfaces, plus the original INTERFACE_CERTIFICATE's I1/I2 and G1-G5.

## Source and dataflow checks

`load_kernel` validates the exact original router blob before importing it.
That router validates its own BRC dependency blob and unchanged function/class
ASTs. The adapter therefore calls the pinned packet and positive BRC
primitives rather than replacing them with a stand-alone matrix propagator.

Every material label and every incoming port must have an explicit family.
Triple canonicalization catches reordered duplicates; each triple contains
its actual incoming port and three distinct axes. Material incidence is
passed to `R.packets` at every actual material visit. No missing material or
incoming family is silently replaced by the old default incidence.

The transfer table is built as K[destination][source]. The separately returned
W[source][destination]=K[destination][source] is correctly its transpose;
the nonsymmetric example is material for detecting this error class.

Leaves are not recoalesced before propagation. They retain source identity,
initial incoming port, current signed X6 chart, incoming port, exact weight
and ordered events. The original Packet constructor appends the full triple
to its tag, so each event preserves its complete packet membership. Shared
tags identify siblings and prior layers retain their parent input. Extra
source-by-target-by-incoming summaries are explicitly derived observers,
not replacements for these joint leaves.

At each finite layer the exact total is N*rho^ell: packet alternatives and
three legs sum to the parent before attenuation, and each empty site has
twelve bulk successors of weight rho/12. Resource overflow raises an error
and returns no silently truncated result. The tail bound controls only total
positive response, as stated; it supplies no unbounded-history closure.

The two-edge return correction uses the source row mass. A receiving
material has anchored diagonal 1/3 regardless of its separate supplied
family, so replacing a bulk neighbor coefficient 1/12 adds the stated
3*lambda^2*r_a(q). Thus different receiving kernels do not invalidate the
displayed formula within this conditional grammar.

## Actual independent checks

`review/second_round_checks.py` imports the exact adapter and pinned kernel
and uses three labelled material Cells with material-specific, nondefault
single-triple families. At depth 2 the leaf counts are 36,108,1188. It
checks all 1,332 returned leaves' complete path lengths, edge displacements,
incoming reversals, packet membership and source identities. It also
recomputes all source/target/incoming totals directly from retained leaves
and verifies that an omitted material family raises an error. All checks
passed; the exact adapter SHA is recorded in the result JSON.

This is a different targeted adapter run, not a rerun of the historical
97/3329/25074 scientific checks or the author's own three cases. It is not
an exhaustive proof of arbitrary Python environments or a formal kernel
certificate. The finite-depth induction and direct dataflow establish the
stated semantics; the run supplements them.

## Scope and harvest

T0_BRC is REUSE_EXECUTED and the source-specific adapter is an extension of
an existing family, not a new mathematical theorem or global tool family.
Triple syntax does not establish signed native triad admission, packet
fractions do not establish indivisible action provenance, and source
labelling does not supply reaction/storage, physical time or occupancy laws.
The full signed X6 substrate and separately typed depth are preserved.

Shared control/source context is disclosed. Reviewer did not write the
adapter and is not a clean-blind reviewer. This report is nondecisive
research evidence and grants no formal Driver acceptance, Task closure,
Working Truth or parent completion.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH

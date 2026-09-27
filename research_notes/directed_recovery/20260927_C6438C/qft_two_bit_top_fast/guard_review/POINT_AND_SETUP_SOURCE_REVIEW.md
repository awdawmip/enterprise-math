# Shared-context proof and source-only review

Verdict: no material mathematical or source defect found in the complete
candidate read here. This is a source-only review: the checker and its design
are not yet reviewed, and this note is not authorization or readiness evidence
for a scientific run. No scientific import, host numerical example or native
execution was performed. No saving is measured here.

| Read file | Exact SHA-256 |
|---|---|
| `POINT_AND_SETUP_REUSE.md` | `e4c0f33e1fd6c8d62d3604eb37db41b937ba999e536b61cfeac6e1300c9690e6` |
| `top_bit_fast.py` | `8c73aa1ad2f195b9d8f440112dac7b08cacbc1e544e65850a754dc38f2fa48e8` |

The prior full top-general source, proof and complete bounded result have been
separately reviewed. They remain frozen; this is a successor with a new schema.

## Formula and domain

For d=Vz+t, the reviewed stretch identity is
A(d)=(-1)^z[(V-t)B(z)-tB(z+1)]. In the low piece d<L/2,
z<M/2 and B(z+1)=B(z)-3, including the low piece's last point.
In the high piece d>=L/2, B(z+1)=B(z)+1, including z+1=M
where the extended overlap is zero. Substitution gives exactly
(-1)^z[(V-2t)B(z)-alpha*t] with alpha=-3 or 1. The two
piece formulas agree at their shared junction. This proof is symbolic; no
numerical fixture was evaluated in this review.

The actual singleton code at lines 187–228 uses typed floor divisions for z,t
and z parity, then typed products/subtractions/sign multiplication. It selects
the branch only when the already typed segment count is exactly one. Empty
segments retain a typed zero. Longer segments use the unchanged degree-three
moment expression and final exact division by three. The input gate still
requires k=g-1 and stride one, but no alignment between V and R. Both
orientations, their multiplicity, and raw exponent 2g are retained.

## Cache and chronology

Scale data depend on (g,ell). Because k=g-1, that strict public pair also fixes
M,V and both coefficient sets; R and r do not affect these cached values.
The private lookup points into an append-only setup list. A fresh setup is
attached before typed work and marked complete only after construction.
Coefficient records likewise appear provisionally before their construction.
No coefficient is constructed for an empty or singleton segment. Each longer
segment records its piece reference and whether that piece was already built.

The setup's scale operation range ends before later lazy coefficient work;
the latter has its own range and may occur inside a request/segment range.
These are overlapping semantic references to one chronological runner stream,
not separate chargeable copies. For a first coefficient construction the
segment start precedes its work; `moment_evaluation_signed_operations_start`
marks the subsequent matrix-moment part. On a hit no new coefficient arithmetic
is performed. A result reader must count the shared raw stream once, including
both first constructions and all later segment work.

## Failure and verification

Public input validation and source checks occur before a new inflight request.
An early invalid public input leaves a previously complete observer reusable.
A failure during numerical work leaves the inflight request, provisional
setup/coefficient records and paid raw operations visible through
`incomplete_snapshot`; subsequent calls and export reject that incomplete
observer. There is no numerical rollback or resume claim. As in the prior
source, intermediate local values inside a failed coefficient helper are not
all attached individually, but the actual runner operations and provisional
record are retained. Constructor/import failures before an observer is
available are outside this method-level capture contract.

Serialized verification creates a fresh empty-cache observer and repeats the
full request sequence. Complete comparison binds setup contents and references,
cache hits, requests, source/proof pins and raw operation chronology; only the
declared native primitive cache-call delta is excluded. Paid partial failures
are appended as incomplete snapshots; a completed mismatching replay is saved
before rejection. Deep-copy boundaries detach returned requests and exported
evidence. Live internal containers are trusted synchronous implementation
state, not hardened against arbitrary external mutation; fresh serialized
replay provides the certificate boundary.

## Required checker coverage, still pending at this review

The bounded checker should make first construction versus cache reuse visible,
including both piece caches; unchanged inputs may reuse the prior full saved
comparator. Separate public request sequences should exercise the same
(g,ell) across different R, different ell under the same g, a different g,
and return to an earlier setup. It should cover n=0, n=1, n>=2; low/high
singletons including endpoints and observed odd/even z; both orientations;
and a typed failure after setup attachment that blocks reuse/export while
retaining paid evidence. Early invalid input followed by a valid request is a
different control. Cache/setup/reference and singleton-result tampering must
fail strict fresh replay with any paid work retained.

Any final execution claim must bind the reviewed checker and its actual raw
outputs separately. This fixed selected-highest-bit scalar optimization does
not supply unknown order/address information, non-top mixed moments, matrix
Gram integration, general-history sampling or a completed Shor algorithm.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1 (reviewer's actual
read snapshot; subsequent coordinator journal refreshes are not represented
as new local reads).

# Adjacent selected-bit correlation: exact executable extension

The new observer computes the supplied-modulus signed correlation for two
adjacent selected bits, including bits below the top position. One actual
bounded run passed: 37 values agree with 1,152 new typed ordered-pair updates.
All six production cases cost more than the same-input typed comparator:
126,950 versus 52,700 full-adder digit replays. This is an executable-domain
extension, not a demonstrated speedup or complete Shor dequantization.

Read `EXECUTION_NOTE.md` for the actual results and complete cost boundaries;
`ADJACENT_COST_READBACK.json` and `guard_review/ADJACENT_RECORD_REVIEW.json`
bind the full retained records. The two readbacks consumed saved outputs and
receipts without repeating scientific arithmetic. All reviews are
shared-context author evidence, not formal independent admission. The source,
proof and design retain their original pre-execution markers; this note and
the actual summary identify what later ran.

## What the implementation computes

For g>=2, k=ell+1<g, supplied R>=1 and 0<=r<R, let
`s(x)=(-1)^(bit_ell(x)+bit_k(x))` for 0<=x<2^g. The integer output is
the sum of s(x)s(y) over y-x congruent to r modulo R. Raw correlation
normalization is `4^-g`. Negative outputs are valid. The implementation uses
the frozen direct one-bit progression plus the proved shifted-window
correction, with at most eight degree-three floor tables per query. Both
opposite displacement orientations remain, including duplicate heads at a
half-modulus residue. The zero displacement is included once.

This is a scalar observer. It takes R as supplied information and does not
discover an order, address a modular orbit, propagate a quantum reference,
or contract noncommuting phase matrices. It uses actual typed arithmetic and
retains its complete signed traces. Degree-five arithmetic, general mixed
recurrences, point shortcuts and setup caching are not used in this version.

## The bounded record

The six tuples `(g,ell,k,R)` are (3,0,1,5), (4,0,1,5), (4,1,2,6),
(4,1,2,9), (3,0,1,11), and (4,0,1,1), each over all residues.
They all have k<g-1. The grid includes odd/even moduli, R=1, R greater than
the interval length, negative outputs, empty progressions and half-modulus
double orientations. Comparator source was reused verbatim but all 1,152
pairs are new actual executions, not the predecessor's 720 saved pairs.

| Work category | Streams | Digit replays |
|---|---:|---:|
| Production | 6 | 126,950 |
| New typed pair comparator | 6 | 52,700 |
| Positive fresh replay | 6 | 126,950 |
| Paid negative replay | 10 | 133,552 |
| Total | 28 | 440,152 |

Twelve invalid inputs reject before work. Fourteen certificate controls
include nine complete paid replays, one retained valid prefix followed by
an invalid request, and four zero-work structural refusals. A separate
production-boundary invalid input preserves the detached state and allows
the original grid to finish; its overlapping snapshots are not double billed.
No deliberate mid-arithmetic interruption was executed. One actual core
invocation supplies the shared full-adder columns; it does not make the
440,152 recorded digit replays free. The 45.467767-second whole-run record is
not a matched performance benchmark.

## Restore and continue

`DEPENDENCIES.md` gives exact immutable source locations, hashes and sibling
layouts for the scientific runner, native arithmetic and metadata readers.
`PRIOR_EVIDENCE_REUSE.md` separates new work from inherited algorithms,
historical professional evidence and the already published Top-fast result.
`CONTINUE.md` gives the next concrete reduction target. Local paths are
restoration locators, not restrictions on dialogue capabilities.

This source package contains the complete original gzip through lossless
indexed text chunks, plus the proof, actual source/checker, three static
reviews, both full-record audits, original startup receipt and log. The ZIP
also contains the original gzip and a complete member hash index. Restore
with `readable_evidence/build_readable_evidence.py --restore`; it refuses to
silently replace a different existing original. Metadata restoration and
saved-record inspection do not require rerunning the experiment.

`next_design/ADJACENT_FAST_DESIGN.md` and its formal shared-context review
propose a separately versioned point/setup optimization. Its companion reader
only counted saved lengths: 268 old top-level tables would become 160 under
the proposed routes. This is a counterfactual call count, not an executed
optimization or measured digit saving. All four prospective files are exact
copies; no successor scientific implementation is included. DEPENDENCIES
explains the metadata reader's original sibling layout.

The intended source authority is awdawmip/enterprise-math under
`research_notes/directed_recovery/20260927_C6438C/qft_two_bit_adjacent_shift/`.
The actual publication commit belongs in the separate delivery receipt once
the publisher returns it; it is not predicted in this frozen package. Drive
is an original-byte backup, not the authoritative research state.

The recorded startup observed own ea7426cf4c0a0d6a8d9646cb9f053519c8567fc1.
Packaging uses the parent-confirmed GK snapshot
52978d9a04c50d038d9f7caef6ef502561d99fe0 and preceding scientific source
87a5888dc433a6c41dd315c4117c43a6aafb659a. Later checkpoints do not rewrite
this intake. The parent separately observed EM main bf2e72cef4f935d502b65790abab08ae36491a15
during preparation; this is context, not this package's future commit.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1.

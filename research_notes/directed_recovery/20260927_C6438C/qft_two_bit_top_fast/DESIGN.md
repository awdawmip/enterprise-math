# Singleton and setup-reuse optimization: declared execution

Status: CODE_ONLY / NOT_EXECUTED. Review the exact source and this checker
before the single coordinator-run experiment. No saving is assumed.

The source is top_bit_fast.py,
8c73aa1ad2f195b9d8f440112dac7b08cacbc1e544e65850a754dc38f2fa48e8;
the symbolic point/cache contract is POINT_AND_SETUP_REUSE.md,
e4c0f33e1fd6c8d62d3604eb37db41b937ba999e536b61cfeac6e1300c9690e6.
The copied implementation is a new file/schema; the exact base remains
top_bit_general.py, 33a46d5f3dacf61e83cedd75cb3424f2375485b3b58984429d5c9fc76b8c96d0.
prepare_source.py, prepare_checker.py and checker_body.txt are source-building
provenance only and not runtime dependencies; a later one-line range-label
correction is present in the final observer rather than its initial generator.

## Changes under test

Keep the old strict k=g-1, stride-one, supplied positive R contract. The new
source has no alignment gate. Every orientation is split at L/2 using the
same typed lengths. Empty segments retain real typed zero; singleton segments
use the proved compressed point expression with typed d/V and z/2 divisions.
Only segments with n>=2 call the unchanged degree-three moment calculation.
All arithmetic, including signs, coefficients and setup scales, stays on the
frozen actual typed backend. Branches read observed outputs or public inputs.

An append-only per-observer setup list is keyed by public (g,ell), with index
references in each request. Scales are built once per key. Each piece's ten
coefficients is built lazily only if a non-singleton segment needs it. Complete
coefficient records may be reused by later segments/requests. The provisional
setup and coefficient records are attached before their work; incomplete
inflight work blocks further calls and certificate export. The certificate
contains the full setup list, requests and raw arithmetic. Fresh replay starts
with empty local caches and compares the entire certificate, excluding only
the existing native-column call delta. Lookup dictionaries and JSON storage
are uninstrumented bookkeeping, not arithmetic savings claims.

The segment's full signed-operation interval includes any lazy coefficient
construction; moment_evaluation_signed_operations_start separately marks the
moment part. Setup scale intervals and coefficient intervals are subordinate
references into the same raw stream, not additional paid streams.

## Fixed comparisons and new branch control

Reuse the predecessor's complete original raw payload, 75,217,873 bytes,
SHA256 4f6fae5355d3a809b765af17c6be7b2ac709cf63ec2e6fbd4e5b81a35cf79dc9,
and original gzip 2,684,245 bytes,
ba39feafb35e6d902c1ba1de8c7e64aba581eca7d02e429064c389f6d79e9dc0.
The checker reads all bytes, binds source/guard/helper/native pins, requires
the old PASS and exact saved positive-replay equality, and uses the saved
37 values and 720 pair records. It does not import or execute the old checker
or call a new comparator. Historical costs remain separate columns.

The six main fixtures are exactly
(2,0,1,3), (3,1,2,3), (3,1,2,5), (4,2,3,6), (4,2,3,9), (3,1,2,11).
Every residue is queried once on one fresh observer per fixture. The six
complete certificates each receive one fresh positive replay. Coverage checks
require empty, singleton and moment routes, both point pieces and parities,
nonzero point remainders, actual lazy coefficient reuse, an entirely unused
coefficient cache, negative results and preserved half-modulus multiplicity.
There are six setup misses and 31 hits in these six main production streams.

One separate observer executes four additional accepted queries chosen only
to test setup switching and R-independence: case-index/residue pairs
(1,0), (0,0), (1,1), (2,0), with zero-based case indices above. Their expected
values are read from the same full saved predecessor payload. They must give
setup indices [0,1,0,0] and hit flags [false,false,true,true], then receive one
fresh full replay. Charge these four queries and replay separately as cache
controls. This is deliberate new-version control work on historical inputs;
the predecessor implementation and its comparator are not rerun.

This grid does not separately exercise two setup keys with the same g and
different ell, or a deliberately interrupted valid numerical request. Those
are source-reviewed boundaries, not claims of executed control coverage.

## Rejection controls

Twelve strict invalid inputs reject before typed work: exact types, bit bounds,
non-top k, nonpositive R, noncanonical r and unsupported stride. After the
first main r=0 production query, one additional invalid non-top request must
leave the complete before/after snapshot and CALLS unchanged; the original
r=1 and r=2 then continue. This zero-work contained interval and duplicate
snapshots do not add a paid cost stream.

Eighteen forgery controls are fixed before execution. Thirteen alter evidence
and must retain a complete honest paid replay before rejecting: setup scale,
setup input, setup index, setup-hit flag, setup-complete flag, cached
coefficient, coefficient reference, point parity, point slope, point result,
table output, half-modulus orientation and raw exponent. One changes the
second request to an invalid non-top input; its paid first request, completed
setup and raw work must be retained, with inflight=None. Four source/schema/
bool/non-string-key controls reject early. Typed-key encoding retains the
non-string key. Every attempted forgery is asserted to differ from its source.

The paid valid-prefix rejection is not a terminal arithmetic failure, and the
early-invalid continuation is not recovery of interrupted numerical work.
No eligible input is deliberately made to fail inside the scientific runner.
An unexpected failure keeps all available raw fields and independent CALLS,
with per-field snapshot errors; constructor objects that never return,
pre-main import errors and failed failure-file I/O are outside this guarantee.

## Cost and output boundaries

Five paid categories are production, positive replay, cache control, cache
control replay and negative replay. The expected charged stream counts are
6+6+1+1+14=28. The old 96,452 production and 34,544 comparator digit costs are
historical baselines, never added to new work. Count digits, typed/signed
operations, moment nodes/requests/cache hits, bit wiring and arithmetic
bit-length separately. Disjoint intervals cover the process-global native
calls once. Timing is the whole checker before final serialization and
includes reading historical evidence and controls; it is not a matched speed
benchmark. No elapsed-time improvement is assumed from arithmetic counts.

The checker requires an actual canonical startup guard for this activity,
TASK_RESEARCH, startup boundary, permission true and no sync debt. It pins
current source/design/proof and historical sources before and after work.
It refuses existing success/summary/failure artifacts and uses exclusive writes:
TOP_BIT_FAST_RESULTS.json.gz, TOP_BIT_FAST_SUMMARY.json,
TOP_BIT_FAST_FAILED_EXECUTION.json.gz. The execution log is separately retained.

Success would show correctness on this declared bounded grid and actual costs.
It would not establish general faster Shor simulation, unknown-order recovery,
non-top mixed-floor closure, matrix correlation or complete sampling. The
point route is restricted to n=1; it does not conceal a scan of a long segment.

Global-Knowledge-Sync: main@6e443c7 / GLOBAL_KNOWLEDGE_V1

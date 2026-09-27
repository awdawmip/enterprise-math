# Aligned two-bit observer: actual bounded execution

Status: **PASS**, one declared coordinator execution. The six frozen tuples
produced 36 residue values equal to the actual typed pair comparator. The
comparator made one complete bucket pass per tuple, totaling 720 ordered pairs.
There was no ordinary numerical reference calculation or historical rerun.

This closes the stated V=2^ell dividing R scalar adaptation and its retained
proof/receipt contract on the declared grid. It is not a full Gram integration,
order-finding routine, unaligned mixed-floor algorithm or Shor simulator.
The current implementation remains the executed baseline; proposed structural
zero and affine shortcuts belong to a separate version.

## Actual inputs and production cost

Every residue r=0,...,R-1 was included. The raw normalization is always 4^-g,
not the scale of the compressed problem. The counts below are adder-digit
replays; they are not elapsed-time estimates.

| (g,ell,k,R) | Residues | Typed pairs | Production | Typed comparator |
|---|---:|---:|---:|---:|
| (2,0,1,1) | 1 | 16 | 4,664 | 387 |
| (3,0,1,3) | 3 | 64 | 16,088 | 2,268 |
| (3,1,2,2) | 2 | 64 | 6,800 | 2,186 |
| (3,1,2,4) | 4 | 64 | 7,273 | 2,530 |
| (4,1,3,6) | 6 | 256 | 18,074 | 12,547 |
| (4,2,3,20) | 20 | 256 | 24,864 | 15,613 |
| Total | 36 | 720 | 77,763 | 35,531 |

Production used more digit work than the comparator in **every** tested tuple.
The finite proof gives at most eight private single-bit progressions and sixteen
top-level moment tables per query, but their fixed reconstruction and replay
costs are substantial here. There is no measured speedup claim. Production
actually made 236 private progression calls and 332 top-level table calls,
with 96 retained moment nodes, 380 requests and 284 cache hits. Recursive work
and calls that return an empty progression remain in the receipts.

The grid exercised both compressed-step parities, H>1, ell=0 and ell>0,
negative values, half-modulus multiplicity, r=0, nonzero low remainders,
R>L empty orientations, and the omitted shifted boundary A_one(M)=0. In
particular a nonzero shifted coefficient and a removed M endpoint both occurred.
The latter is certified by typed endpoint equality, not a nonempty out-of-range
moment table. Both orientation heads are recorded before orientation execution;
the readback follows that actual order.

## Complete cost ledger

| Category | Receipts | Adder digits | Typed operations | Signed operations | Host wiring | Host bit-length calls |
|---|---:|---:|---:|---:|---:|---:|
| Production | 6 | 77,763 | 21,703 | 21,071 | 832,038 | 56,838 |
| Typed pair comparator | 6 | 35,531 | 3,538 | 2,556 | 380,513 | 10,512 |
| Positive fresh replay | 6 | 77,763 | 21,703 | 21,071 | 832,038 | 56,838 |
| Paid input rejection | 2 | 43 | 5 | 5 | 475 | 18 |
| Negative fresh replay | 8 | 64,015 | 18,637 | 18,056 | 685,864 | 48,282 |

All categories together used **255,115 adder-digit replays**. The global CALLS
list contains one actual 12-state `recurrent_mass_power`, depth one, constructing
the full-adder primitive. It occurs in the first production interval. Later
operations reuse its actual columns; one native call is therefore not the cost
of the computation. Every saved full-adder cell in all 28 receipts was matched
to the retained native columns by the I/O reader. Its digit and arithmetic
wiring recount agrees with the original counters. Signed-to-typed indices
cover each retained arithmetic operation exactly once.

Host wiring counters cover the existing arithmetic layer's bit operations and
bit-length calls. Python allocation, JSON, indexing, hashing and readback work
are excluded. Maxima are not summed: production's observed maximum recursion
depth was three and observed integer width seven bits. These boundary counters
are not a claim about all internal or future values.

The recorded elapsed interval was **19.39142640004866 seconds before success
serialization**. It includes production, comparison and replays. It excludes
final gzip/JSON writes and is not a matched timing benchmark.

## Replay, rejection and failure records

Six fresh positive replays reproduce each entire certificate, apart from the
explicitly excluded native primitive cache-call delta. Twelve tamper controls
were rejected: seven retain honest complete fresh replays, one retains an
incomplete paid replay, and four reject before arithmetic.

| Tamper | Honest replay adder digits | Retained outcome |
|---|---:|---|
| Drop half-modulus orientation | 6,800 | Complete |
| Compressed length | 6,800 | Complete |
| Shifted zero-tail record | 24,864 | Complete |
| Original branch sign | 6,800 | Complete |
| Compressed step parity | 7,273 | Complete |
| Original raw exponent | 6,800 | Complete |
| Signed output | 4,664 | Complete |
| Input changed to nonalignment | 14 | Incomplete alignment rejection |
| Source, schema, bool input, non-string key | 0 | Four early rejections |

The negative records preserve attempted certificates in a typed-key encoding;
JSON never silently collapses the non-string-key case. Complete captured
negative replays equal the original honest certificate. The incomplete replay
retains its actual V construction and division with nonzero remainder.

There are also twelve input rejections: ten strict-input pre-rejections and
two paid nonaligned inputs. Each paid failure is followed by a valid-input
attempt on the same incomplete observer; both attempts reject with unchanged
inflight record, full trace and counters. This prevents failed-work overwrite
and does not pretend to implement resumable arithmetic requests.

No unexpected-failure artifact was produced. The source refuses existing
success, summary or failed-execution evidence before starting another run.
During an unexpected main-run failure it retains completed records and available
raw runner work. Unreturned local semantic dictionaries, import failures and
failure-save I/O failures are outside the stated recovery promise.

## Immutable local evidence bindings

- Adapter `aligned_two_bit.py`: `a6fd6cf5bfe10829c1918c50a952de22e5e2bc6cd538011f37a3bffdff5acdb2`.
- Checker `check_aligned_two_bit.py`: `6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969`.
- Frozen `DESIGN.md`: `90605ff87a2a9f37576c57bb9f5363407c29778f87fef0c17aa6621713908876`.
- Actual startup guard: `1c9e45ed619a7480402d0719e283b06a52ca78a889bca6bd74c14ca8fbc4297f`.
- Complete raw JSON: 61,934,942 bytes, `61aee1882148519bd9738bacf6f107a39532aa98de6c128854edb98df334aba9`.
- `TWO_BIT_ALIGNED_RESULTS.json.gz`: 2,183,581 bytes, `f6bf350f188d4252c60c897778561e3c4957d65774a25a12334b35261f0b7bd3`.
- `TWO_BIT_ALIGNED_SUMMARY.json`: `e3cb56ab19badfa2104c4a7f698c5bef2794a1e2faef9e58f0cd6eca778f631d`.
- Execution log: `5c9d9840f781387baf85f6a2e3182a719e3a55df586df33789e84072c437c5c4`.
- I/O reader `read_aligned_cost.py`: `2f5e95130164e8edc12286b095d668f431f7ca52455af203d44a0990e4cae784`.
- `ALIGNED_COST_READBACK.json`: `444445fa979ad591b55fc4cf394fb233fb1c417f8e951f88656f6aec9b756040`.

The reader imports only Python standard-library I/O facilities. It reads all
raw bytes, verifies the source/proof/native ancestry and guard, walks every
production and honest replay's outer recording edges, all comparator digit and
pair bucket chains, saved moment-table/cache links and signed-to-typed indices,
then recounts native cells and costs. It consumes saved numeric outputs; it
does not rerun moments or construct a new numerical reference. This is an
author readback under shared context, not formal independent admission.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1

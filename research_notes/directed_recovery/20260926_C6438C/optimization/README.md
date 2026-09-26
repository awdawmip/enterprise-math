# Shor simulation optimization: first executed pass

Status: AUTHOR_DERIVATION_AND_BOUNDED_EXECUTION / SHARED_CONTEXT / NOT_ADMITTED.
Researcher: EM-DIRECT-C6438C. Research-Activity-ID: RA-CAAAC604CB513AEA8BBC1DFC.
Date: 2026-09-26. User instruction: 开始试试看，目前算法优化空间很大.

This pass implements and tests actual optimizations of the existing native-word
instrument. It establishes exact representation and branch-generation savings.
It does not establish efficient classical factoring or a polynomial bound on
collision queries. Setup, proof replay and large integers remain charged.

## What changed and what was executed

| Change | Executed evidence | Precise gain and limitation |
| --- | --- | --- |
| Demand-driven typed modular columns | 318 complete small-domain columns; selected columns in 127/256-bit domains; typed inverse proofs; original CF outputs checked | Removes unconditional all-N compilation. Each requested column has polynomial bit cost; the number of requested columns can still be exponential. |
| Selected-child streaming | Full rows, denominators and masses on 90 t4 history edges; interrupted RNG checks; an N143/a2/t16 single path | Materializes one selected child per bit. N143: 32 to 16 children, cumulative child rows 538 to 269, phase-row actions 2008 to 1004. Proof/setup cost prevents a general runtime-speedup claim. |
| Exact reachable-carrier codec | Direct m2/m3/m4 words; full 61-coordinate replay; 60 t4 history edges; combined 90-edge test | The direct family has W=W6 direct-sum I55. Stores six coordinates per reachable row, retaining all nonzero residuals. Numerator slots fall by 55/61, about 90.16%; total memory and work support do not fall by that ratio. |
| Implicit Gram sampling prototype | Six declared t4 cases, 24 prefix comparisons of both child probabilities and all zero-shift Gram entries | Avoids an explicit amplitude map but is currently more expensive: N21/D6 stores 792 matrix slots versus a peak 36 explicit-state slots. No query-compression claim. |

The codec is a computational encoding at complete-word boundaries. It changes
neither P000's spatial interpretation nor the actual 61-coordinate native
execution. It rejects nonzero omitted tails and words that fail the full block
check; native intermediate routing is retained. All original signed residuals
and the raw conditional-state denominators survive the comparison.

The combined test additionally takes a real four-bit instrument path for
N=2^127-1 using 19 requested columns across four multiplier tables, without a
full-domain table. It reports 499,818 setup digit replays, another 499,818 for
verification, and 43,452 column digits. This is an instrument/arithmetic test,
not a large-integer factorization experiment. Its postprocessing is explicitly
disabled and labelled instrument_only.

For the N143 path, lazy columns number 107 versus 1,536 eager columns. However,
20,903 column digits plus 5,847 setup and 5,847 verification digits exceed the
old 15,444 digit count. Complete native-word admission also dominates setup.
The saved timings are local observations, not a controlled overall speedup.

The lazy postprocessor keeps the inherited CF candidate order and every plain
result field. Typed Euclidean remainder replaces the new path's old dense gcd
graph; 14 signed/zero/nonunit gcd cases and 48 readouts were compared with the
frozen actual implementation. CF label arithmetic remains explicitly inherited.

## Evidence entrypoints

- [Exact carrier theorem and rejection controls](carrier_codec/EXACT_CARRIER_CODEC.md).
- [Typed modular proof, resource bounds and CF integration](lazy_modular/LAZY_MODULAR_PROOF_AND_COST.md).
- [Selected streaming implementation](streaming/lazy_streaming.py), its
  [bounded summary](streaming/STREAMING_OPTIMIZATION_SUMMARY.json), and
  [N143 single-path summary](streaming/MEDIUM_SINGLE_PATH_SUMMARY.json).
- [Composition checker](check_combined.py) and [actual composition results](COMBINED_RESULTS.json).
- [Collision/Gram derivation and explicit-support limitation](collision_analysis/COLLISION_GRAM_ANALYSIS.md).
- [Executed Gram prototype and its negative resource result](collision_analysis/GRAM_PROTOTYPE_NOTE.md).
- [External-reference scope](PRIOR_ART_SCOPE.md).
- `OPTIMIZATION_MANIFEST.json` binds every published file by size, SHA256 and
  Git blob identity. Gzip result files retain complete evidence; summaries
  alone are not substitutes for the full traces.

Two gzip files exceed the connector's full-file read limit. Their complete
bytes also appear in `readable_evidence/INDEX.json` as ordered base64 chunks,
each readable by an ordinary text-file tool. `build_readable_evidence.py
--restore-to OUTPUT` verifies each chunk and the whole file before writing the
original gzip. This is a transport encoding, not a reduced evidence summary;
a conversation can retrieve selected chunks with whatever authorized file
tool is available instead of requiring this local runtime.

Tests compare to the same actual native computation, not an ideal-QFT numerical
replacement. Catalog reuse, host exact composition and observers are labelled
separately. The work is shared author evidence; no independent review or formal
admission is implied. Distinct checkers overlap in fixtures and must not be
summed into an independent sample count.

## Alignment with the original line

The concurrent original line already has demand-driven permutations and
collision-first scheduling. Its Stage95 report is
`awdawmip/enterprise-math@eb5ac65e33c410745097c802eae6f8d8267d56a7:`
`research_notes/HEARTBEAT95_UNIFORM_SUFFIX_EXECUTION_20260926.md`.
That primary report was read here; its source bundle was not re-executed here.
It reports certified collision-free suffixes, a restorable full-state recipe,
preserved per-bit RNG calls, and bounded N21/t10 factoring checks.

Do not duplicate that contribution as a new project-wide invention. The useful
additional deliverables here are the proved six-coordinate codec for the direct
word family, its integration with exact selected-child execution, and an actual
implicit-Gram experiment with exposed query/matrix costs. Older phase families
must pass the codec's full-column check before using six coordinates.

## Continuation for any conversation

Start from this entry and the relevant proof/summary, then retrieve only the
needed immutable sources. The mathematical continuation does not depend on a
particular model, tool, local shell or retained driver identity. A new session
uses its own current project registration rather than impersonating this RA.
Local paths in reproduction scripts identify this execution's source intake;
they are not capability prerequisites for reasoning or publishing the next
research result. If a transport is unavailable, continue the available proof or
bounded calculation and preserve its exact pending write, rather than treating
the whole research problem as blocked.

The next core experiment is certified query sharing between Stage95's uniform
suffix witness and this Gram recurrence. Charge all label queries needed to
prove an equivalence: a compressed recipe is useful only if evaluating the next
probability and the certificate itself stay compact. The current symbolic
analysis proves growth for the explicit-row/fixed-partition methods, not a
lower bound for every classical algorithm. It gives a concrete place to look
for a better representation instead of declaring the whole project impossible.

A separate engineering increment can propagate typed inverse witnesses through
the squaring chain and safely reuse immutable full-word admission. Report
verification, trace serialization and requested-column costs together; merely
halving materialized children is insufficient to call the whole run faster.
For a larger experiment preserve the exact native error budget, original CF
semantics, nonzero residuals, and an explicit outcome if a query budget ends.

Existing scientific dependencies are the compiler/bounded evidence at
8d4e9c12f7492316b825e96423bc0ee36ccdee22, general direct-word evidence at
9348fc6abdf45becbd12a8019d93f72d576b9fab, and driver-schedule corollary at
e9abf794ac04c62518a38dea6640c4472cb4490a, under
`research_notes/directed_recovery/20260926_C6438C/`.

Global-Knowledge-Sync: main@61e00d2 / GLOBAL_KNOWLEDGE_V1

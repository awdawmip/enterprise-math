# Lazy modular columns and one selected native child

Status: AUTHOR_ACTUAL_SHARED_CONTEXT / NOT_ADMITTED.
Researcher `EM-DIRECT-C6438C`; activity `RA-CAAAC604CB513AEA8BBC1DFC`.

`lazy_streaming.py` implements two exact representation changes to the
existing terminal instrument. Modular permutations are certified globally
and evaluated only at requested labels. A round first computes its two exact
branch masses, then materializes only the selected child. All signed residual
coordinates and unnormalized prefix probabilities are preserved. These
changes do not supply an ideal propagator or alter the measurement contract.

## Global permutation certification replaces enumeration

`LazyStreamingProgram` uses the dedicated `LazyModularFactory` from
`../lazy_modular/lazy_modular.py`. Each distinct multiplier is admitted by
`verify_lazy_permutation`; the constructor checks its N, multiplier, full
carrier size and positive verification result. That verifier replays the
typed inverse certificate. Invertibility of multiplication below N and
identity on the padded labels establish the whole permutation without a
full-domain set comparison. This is a different proved interface, not the
removal of the previous permutation check.

The power chain still obtains its next multiplier by evaluating `table[b]`.
At a round, only the occupied source labels are queried. Repeated multipliers
share a lazy table and its column cache. Complete per-column arithmetic
records, inverse proofs, distinct verification work and table metrics are
retained. The runtime never calls `list(table)`, `set(table)` or `tuple(table)`.
Finite support injectivity is checked again as a local sanity condition.

The default sampler postprocessor is `lazy_classical_postprocess` from the
same lazy package. Its typed modular powers and gcd avoid reintroducing an
eager table at the final CF stage. The actual old CF fields and rejection
policy remain unchanged. The small checks separately profile this default
path and observe no eager modular compiler entrypoint.

## Actual two-H4 quotient and the collision formula

At a valid round boundary let the complete row at work label w be `v_w/d`,
with control and shared spectator both zero. Let S be the nonzero support.
The current lazy modular permutation is P. Following the original ascending
control-loop order, compose exactly those complete native phases whose
previous measured bit is one. Write their actual product as `T=A/h`, where
h is the product of their dyadic denominators. The time order is unchanged;
different phase words are not assumed to commute or share a root.

The native bank admission rebuilds each entire H4/sign/swap word through
`CompleteNativeWord`, verifies its complete action against the supplied
phase object, and uses the resulting orthogonal actual-column adapter. This
supplies the orthogonality needed below, including all 61 modes. Requested
phase error certification remains the caller's existing compiler contract.

`native_two_h4_binding()` reads `native_quartet()` itself. It checks all arm,
output-bit and spectator coefficients of the two-H4 composition. Summing the
two intermediate spectator labels gives raw coefficients `(2,2)` for output
0 and `(2,-2)` for output 1 over denominator 4; every output spectator-1
coefficient is zero. Thus the two complete child rows are exactly

`u_z^+ = h v_z + A v_(P^-1 z)`,
`u_z^- = h v_z - A v_(P^-1 z)`,

over denominator `2hd`, with missing source rows zero. This is a quotient of
the actual two native H4 operations, not a spectator reset or a borrowed
ideal Hadamard inserted into execution.

Define the integer observations

`M = sum_w ||v_w||^2`,
`G = sum_(w in S, P(w) in S) v_(P(w))^T A v_w`.

G is signed. Orthogonality of the complete T and the proved bijection P give
the unnormalized child masses

`q0 = (hM+G)/(2h d^2)`,
`q1 = (hM-G)/(2h d^2)`.

They are nonnegative and sum to the parent's `M/d^2`. For a positive parent,
the exact conditional probability is `p0=(hM+G)/(2hM)`. No square root or
renormalization is introduced. All scalar sums are the inherited exact
integer/quadratic observer on actual native-word rows.

Only sources with `P(w) in S` contribute to G. The mass pass evaluates T only
for those rows, caching results by the entire signed row tuple. After the
unchanged exact random choice, `materialize(plan,bit)` evaluates any remaining
needed rows and builds one child on `S union P(S)`. It performs the inherited
exact dyadic common-factor reduction and verifies its mass against q0 or q1.
Equal rows can share T, but labels and collisions cannot be discarded.

The executed negative control demonstrates this distinction with a retained
residual: `u=e0+e5`, denominator 2, N15 and P(w)=2w mod15, T=I. Two copies of u
on labels `{1,2}` give `p0=3/4`; the same row multiset on `{1,4}` gives `p0=1/2`.
Both calculations are checked against the original native two-H4 branch
evaluator. A row histogram alone would be wrong.

## Sampler and optional verified carrier encoding

`sample_selected(program,rng)` uses `branch_plan` followed by exactly one
`materialize` per completed round. Its `branches` method exists for finite
validation/compatibility and deliberately materializes both outcomes; the
single-path sampler does not call it. Deterministic zero/one choices consume
no random draw. Random-source exhaustion returns the original raw parent,
history and events before the unfinished round, exactly as the old sampler.
It does not condition away interruptions.

The default profile admits complete 61-dimensional words and keeps all 61
coordinates. An optional `codec=ExactCarrierCodec(...)` is accepted only
after the original full bank has been admitted and `restrict_bank` has
verified the full forward/inverse block structure. Initial e0 is explicitly
encoded. A restricted word cannot be presented as the original full bank.
The parent's separate combined check covers this optional representation;
the evidence in this directory's small and medium checks uses the full 61.

## Full finite-history checks and a real selected path

`check_streaming_optimization.py` tests frozen-bank N15/t4 and N21/t4 plus
new directly constructed-word N21/t4. Each fixture covers all 30 edges of
its finite history tree, including zero leaves. Old eager-column branches,
unchanged native branches with lazy columns, and the collision/selected-child
quotient agree in every canonical row, denominator and exact child mass.
The two N21 cases retain strictly positive non-principal residual mass.
The combined 90-edge test compares 17202 occupied child-coordinate slots.
Enumeration is a validation activity; the execution algorithm does not
enumerate these trees.

For each fixture, one identical seeded software trajectory is compared with
the old sampler. All returned events and probabilities agree. Two additional
finite random-source budgets, zero and one random calls, give exactly equal
interrupted outcomes and raw parent states. Separate default lazy-CF runs
match all old result fields and use zero eager modular entrypoint calls.

| Selected-path observation | Frozen N15/t4 | Frozen N21/t4 | Direct N21/t4 |
| --- | ---: | ---: | ---: |
| Readout k | 8 | 6 | 6 |
| Children constructed, old to selected | 8 to 4 | 8 to 4 | 8 to 4 |
| Cumulative constructed child rows | 14 to 8 | 27 to 13 | 27 to 13 |
| Phase-vector applications | 0 to 0 | 16 to 8 | 16 to 8 |
| Distinct eager columns to queried lazy columns | 48 to 6 | 96 to 10 | 96 to 10 |

The path metrics use an explicit `INSTRUMENT_ONLY_TEST` postprocessor so that
instrument resource counts exclude factor/CF work. The additional default-CF
equivalence checks are recorded separately. Seeded replays are not proofs of
the conditional uniformity of a physical random source.

## Longer single-path benchmark

`check_medium_single_path.py` runs N143/a2/t16 with the already frozen 61-mode
K33 bank. It executes one sampled path per evaluator, without full history
enumeration, all-control expansion or new phase construction. Both obtain
k22937. Every event and exact probability agrees, and the canonical terminal
state and denominator agree at all 3660 coordinates of 60 retained work rows.

| Observation | Existing eager/two-child path | Lazy/selected-child path |
| --- | ---: | ---: |
| Constructed children | 32 | 16 |
| Cumulative constructed child rows | 538 | 269 |
| Phase-vector applications | 2008 | 1004 |
| Distinct materialized/requested modular columns | 1536 | 107 |
| Column-construction adder-digit replays | 15444 | 20903 |
| Lazy inverse-proof setup adder digits | — | 5847 |
| Distinct lazy proof-verification adder digits | — | 5847 |

This experiment establishes reduced materialization, not universal reduced
arithmetic. The lazy label arithmetic costs more digit work in this medium
fixture, even before setup and verification. The original `FixedRotor` also
uses its certified rank-one quotient, while complete-column admission uses
a generic matrix-vector implementation. A phase-vector count is therefore
not a count of identical machine instructions.

Raw clock observations are retained for bank loading, each setup and each
single-path run. Catalog/word caches may be warm. Full phase admission is
counted separately and can dominate any path-level saving. No end-to-end
speedup, cold-cache benchmark, bit-complexity improvement or uniform factor
success is inferred. Native kernel calls, typed full-adder digit replays,
host bit wiring and logical row operations remain separate units; a cached
native catalog with zero new kernel calls does not mean zero arithmetic work.

## Artifacts and next decision

The complete small evidence is `STREAMING_OPTIMIZATION_RESULTS.json.gz`, with
`STREAMING_OPTIMIZATION_SUMMARY.json`. The longer path is independently saved
as `MEDIUM_SINGLE_PATH_RESULTS.json.gz` and `MEDIUM_SINGLE_PATH_SUMMARY.json`.
Each payload binds its source files and retains actual kernel-call receipts,
typed lazy certificates and exact results. The source algorithm SHA256 is
`635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257`.

The checks run with the current authorized Python runtime, for example:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 -B 'D:/em/TEMP/sep26-shor-general/optimization/streaming/check_streaming_optimization.py'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 -B 'D:/em/TEMP/sep26-shor-general/optimization/streaming/check_medium_single_path.py'
```

Read completed evidence before repeating it. Future optimization can decide
when to reuse a verified native rank-one quotient or precompose ordered
feedback columns; neither is silently assumed here. The number of distinct
work labels can still grow. Common-row caching preserves label collisions
but does not remove that storage bound; the separate implicit-Gram direction
addresses a different representation question. Old frozen sources are
unchanged. P000, the actual typed BRC requirement and the inherited quadratic
readout scope remain unchanged; these are shared author results, not
independent admission or an efficient classical factoring theorem.

Global-Knowledge-Sync: main@61e00d2 / GLOBAL_KNOWLEDGE_V1

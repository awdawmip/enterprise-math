# Certified finite words in the complete streaming instrument

Status: AUTHOR_EXECUTED_BOUNDED_INTEGRATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED.

Researcher `EM-DIRECT-C6438C`; activity `RA-CAAAC604CB513AEA8BBC1DFC`.
The bounded execution outcome is recorded separately in
`COMPILED_STREAMING_SUMMARY.json` and the complete gzip artifact.

## 1. The compiler-result boundary

`compiled_streaming.compile_bank(t,epsilon,**compiler_options)` calls the
bounded `certified_word_compiler.compile_phase_bank` and converts a complete
result into a native-word bank. Its principal return fields are:

- `status`: `CERTIFIED` or `PARTIAL`;
- `bank`, `dim`, `error_certificate`, and `word_bindings` for a complete result;
- `compilation`: the entire source-bound compiler result;
- `cursor`: the compiler continuation cursor.

A `PARTIAL` result has `bank=None` and `error_certificate=None`.
`program_from_compilation(N,a,t,compilation,epsilon=...)` adds `program=None`
for this case. It does not build modular tables or a streaming program from
the completed subset. Resumption stays in the compiler, with the original
target, tolerance, seed words, observer profile, and source bindings.

For every required phase `m=2,...,t`, `bank_from_compilation` requires its
target index, complete dimension, certificate, and error bound. It calls
`verify_phase_record`, which binds the external word, target, dimension,
bound, and certificate hash, then forces full native-column, inverse, Gram,
algebraic-root, and strict positive-path error-observer replay. A nonempty
certificate dictionary or an unverified stated bound is never sufficient.
The exact quarter-turn may report error zero only under its additional exact
certificate rule. The adapter also checks that its complete action equals
the native word `swap(0,1); neg(1)`.

## 2. Exact adapter and denominator contract

`CompleteNativeWord` replays every complete forward and inverse column with
the frozen `stage80.fixed_phase.apply_word`. It checks exact inverse recovery,
full-column orthogonality, and equality of inverse columns with the transpose.
All column denominators are dyadic; their maximum is a common denominator D
for both directions. The adapter stores the actual integer matrices `D W`
and `D W^-1`, including all 61 coordinates.

Its interface is the inherited phase protocol:

`dim`, `den`, `apply_numer(vector,inverse=False)`, `h4_count`,
`sign_count`, `swap_count`, and `inverse_phase_word`.

The historically named `inverse_phase_word` is the temporal forward word for
the negative phase used by inverse QFT, as in the frozen `FixedRotor` class.
The input vector to `apply_numer` contains integer amplitude numerators.
The returned integer vector is `D W v`, or `D W^-1 v` for the inverse call.
It does not independently reduce the output denominator. Therefore the
unchanged `cp_step` can multiply the bypassed branch by D and update the
shared denominator consistently. The later existing common-factor reduction
changes only exact representation, never mass or retained modes.

This matrix cache is an exact quotient of actually executed native columns.
It is not a target matrix, weighted rotation, floating propagator, or
replacement mathematical reference. Cache identity binds the full word and
carrier; compiler certificate verification is performed separately on every
bank admission.

## 3. Whole-schedule error accounting

If a verified phase has full-space operator error at most `delta_m`, the
controlled phase at index m appears exactly `t-m+1` times in the full circuit.
The adapter sums

`E = sum_(m=2)^t (t-m+1) delta_m`.

It requires E to equal the compiler's declared occurrence-weighted bound and
to satisfy `E<=epsilon`. The exact quarter contributes zero. The returned
certificate lists each phase, occurrence count, and contribution; it reports
`operator_norm_bound=E` and `terminal_TV_bound=min(1,E)`.

Controlled direct sums preserve the phase error norm, and all actual and
comparison gates are orthogonal on the whole carrier. Telescoping gives the
full-circuit operator bound E. The previously proved terminal-instrument
transformation is algebraic for any such complete phase maps. It therefore
introduces no additional approximation in the streaming representation.
The same single-terminal distribution and fixed-postprocessing TV bound
applies, including actual retained residual input.

This is a **single complete instrument** budget. It is not automatically a
bound for the joint record of repeated attempts, recursive factors, or random
source failures. A complete transcript needs a separately allocated sum of
conditional kernel budgets. An interrupted readout remains the inherited
explicit incomplete outcome with its original unnormalized state.

## 4. Bounded full-circuit/streaming comparison

`check_compiled_streaming.py` uses the unchanged old target32/vector64 words
as predeclared search seeds, then obtains fresh full-carrier certificates
from the new compiler at the requested accuracy. The target-observer depth
is explicitly 64 in this new compiler profile; it refines an algebraic
certificate and does not alter native weights or the frozen word seeds.

The declared fixtures are `(N,a,t)=(15,2,4)` and `(21,2,6)`, each with
`epsilon=1/1000000`. These small widths test the execution transformation;
they are not presented as default-width all-input factoring demonstrations.

For each complete bank, the full path prepares its small control register
with actual H4 calls and applies the same sparse BRC modular tables used by
`GeneralStreamingProgram`. It then executes frozen `run_qft` using that same
bank. The other path enumerates all complete streaming histories. The check
compares every signed joint amplitude coordinate, every control bin, and the
full inverse recovery, retaining all modes and the spectator. It also applies
the sparse original CF postprocessor and verifies that a declared software
sample has the exact already-computed terminal-bin mass. This is not a
frequency test or an ideal-QFT reference execution.

The script profiles the frozen dense modular entrypoint and requires zero
calls. Complete sparse modular certificates, full source and terminal states,
all streaming terminal leaves, complete compiler records, native adapter
bindings, and native receipts are retained in the gzip artifact.

The bounded compiler is first deliberately interrupted by a one-pair budget;
the test requires `PARTIAL`, no bank, and no program. It then resumes its
cursor to a complete bank. Two additional negative controls change a word
without its certificate, or invent a smaller per-phase error while also
adjusting the advertised bank sum. Both must fail certificate binding, so an
arithmetic budget check alone cannot accidentally admit them.

## 5. Executed bounded outcomes and final source binding

The final run completed all checks using 6724 actual BRC core calls. All 61
modes were retained throughout. The two deliberately forged records were
rejected, the incomplete compiler result created neither bank nor program,
and its saved cursor resumed to a complete verified bank. No call entered
the frozen dense modular-table entrypoint.

| Declared input | Complete leaf slots | Joint amplitude coordinates compared | Inverse recovery coordinates | Outcome |
| --- | ---: | ---: | ---: | --- |
| N=15, a=2, t=4 | 16, including 12 zero leaves | 976 | 976 | All exact equalities passed; CF success 1/2 |
| N=21, a=2, t=6 | 64, no zero leaves | 23180 | 3904 | All exact equalities passed; positive residual mass retained |

These amplitude comparisons cover the declared prepared input in each
fixture. The independent phase-word certificates cover every one of the 61
carrier basis columns; the fixture checks do not claim to enumerate all
input basis states of the entire modular circuit.

Both requested epsilon=1/1000000 and obtained the complete schedule bound
E=1/2000000. N=21's exact rational CF success probability, every complete
leaf, and every retained residual coordinate are in the artifact. The
observer depth was 64 under the new compiler profile; the old seed words
were unchanged.

Final compiler source SHA256:
`e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d`.
Final uncompressed integration payload SHA256:
`6a14cbf3994c9430b1b07067013546acef3d11c77c4ee3139df670bb20815a12`.

The previous successful run is preserved in `prior_4300_digit_cap/`.
The compiler microfix removed Python's decimal integer serialization cap and
added an adapter attribute alias. After that source change, both complete
integration cases were rerun. `POST_CAP_FIX_REPLAY_CHECK.json` confirms that
all scientific case data and actual word columns are exactly unchanged;
only source-bound adapter records differ. It also checks every embedded
phase certificate's hash and binding to the final compiler source (18
record occurrences, 8 distinct certificates). This archival comparison is
an exact observer check with zero additional native calls, separate from
the final actual BRC rerun.

## 6. Scope and reproduction

The exact bounded measurements and artifact hashes are reported in
`COMPILED_STREAMING_SUMMARY.json`; the complete evidence is in
`COMPILED_STREAMING_RESULTS.json.gz`. The executable check is:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' 'D:/em/TEMP/sep26-shor-general/new_word_compiler/check_compiled_streaming.py' --activity RA-CAAAC604CB513AEA8BBC1DFC
```

This integration does not supply a practical complexity bound for exhaustive
word search, prove polynomial classical Shor simulation, or treat a bounded
PARTIAL result as a successful compilation. The existing fixed K33 algorithm
and its distribution-obstruction evidence remain unchanged.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1

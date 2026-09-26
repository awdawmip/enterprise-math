# Requested-accuracy native words in complete factorization

Status: AUTHOR_EXECUTED_BOUNDED_CASES / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. Researcher `EM-DIRECT-C6438C`; activity
`RA-CAAAC604CB513AEA8BBC1DFC`.

The new source-bound phase compiler is connected to the recursive factorization
driver. Completed outputs carry prime certificates and an exact product ledger;
unfinished compilation and exhausted attempts retain explicit unresolved
cofactors with their multiplicities. The CLI also demonstrates persisted phase
compiler continuation across two processes.

## 1. What the implementation does

`compiled_factorization.factor_integer_compiled(N, rng, ...)` calls the
certificate-bearing core through `CompiledPhaseProvider`. Exact even splits,
perfect-power reduction and Wilson prime certificates are inherited from the
existing typed integer prechecks. Other composite nodes use the actual sparse
modular permutation, original CF/gcd postprocessing, and the complete 61-mode
streaming instrument.

For node bit width `n=ceil(log2 N_node)`, the provider requests `t=2n` and
`epsilon(t)=1/(8t)=1/(16n)`. Old K33 words are predeclared candidate seeds;
each admitted word must pass the new requested-accuracy certificate. Seed
availability does not replace fair search or certify a fixed tail at arbitrary
accuracy. The target and seed policy do not depend on an unknown order, factor,
or successful measured history.

Every required phase is admitted through `compiled_streaming.compile_bank`.
Admission binds word, phase index, dimension, source, tolerance and certificate
hash, and replays the complete actual native columns, inverse, Gram entries,
algebraic target observer and strict BRC error margin. The weighted complete
schedule bound is `E=sum_m (t-m+1) delta_m`. All 61 coordinates, including the
59 residual coordinates, remain in the actual word action and subsequent
state. No ideal target matrix, trigonometric propagator, or ideal Shor sample
is executed.

If the compiler returns `PARTIAL`, the provider raises `CompilationPending`.
The core records a `COMPILATION_PARTIAL` unresolved leaf, preserving its
multiplicity. It does not build or sample a program from an incomplete bank.
The result always checks

`product(certified_prime^exponent) * product(unresolved_cofactor^multiplicity) = N`.

`verify_factorization` replays the deterministic factor/prime claims and this
product ledger. Its `stochastic_budget_verified` field is deliberately false:
these deterministic checks do not certify the external random source or
establish the conditional stochastic premise merely by reading a result.

## 2. Probability theorem and its exact scope

`STRONG_SHOR_COMPILATION_THEOREM.md`, `FIXED_ALPHABET_DENSITY.md` and
`EFFECTIVE_COMPILER_CLOSURE.md` give the author proof that for every finite
width and positive rational requested error, finite words from the unchanged
H4/sign/swap alphabet can meet the full-carrier operator bound. Fair enumeration
of words and algebraic observer depths eventually finds a strict certificate.
This proves finite termination of the unbounded mathematical search; a finite
pair budget may return an honest continuation cursor before that point.

Telescoping the complete controlled gates gives terminal TV at most E,
uniformly in the legal modular base. This is a requested-accuracy theorem for
each finite call. It is not a claim that one finite bank works at all widths.
The published fixed K33 bank has a separate asymptotic obstruction to uniform
strong TV approximation; the new variable-word family does not change that
old result.

For a non-prime-power odd composite node the existing ideal success bound is
`1/(8n)`. With `E<=1/(16n)`, actual per-attempt success is at least `1/(16n)`
under fresh conditionally uniform base and readout draws. The implementation
uses its verified `gamma=1/(8n)-E` and computes
`R=ceil(1/gamma)*b`, where `b=s+ceil(log2 n_initial)`. With default sufficient
budgets at fewer than `n_initial` split nodes, the theorem bounds any
retry-limit failure leaf by `2^-s`. A fixed base policy or an insufficient
attempt override does not inherit that statement. Compiler interruption and
external random-source interruption remain explicit separate outcomes.

A single terminal TV bound is not the TV of an entire retry/recursive
transcript. Such a requested full-record bound requires its own sum of
conditional per-kernel error allocations. This implementation records that
distinction rather than silently upgrading the single-run certificate.

## 3. Actual bounded factorization checks

`COMPILED_FACTORIZATION_RESULTS.json.gz` contains four author executions,
their certificates and 16991 actual BRC core-call receipts. The summary is
`COMPILED_FACTORIZATION_SUMMARY.json`.

| Check | Exact outcome |
| --- | --- |
| N=225, compiler pair budget 0 | PARTIAL retains `15^2=225`; no random draw before compilation |
| Repeat N=225 with saved compiler cursors and pair budget 32 | COMPLETE `3^2*5^2=225` |
| N=21, seeded/fixed-base actual sample | COMPLETE `3*7=21` |
| N=21, specified zero-phase draw and one attempt | PARTIAL retains 21 with `RETRY_LIMIT`; original `ZERO_PHASE_RETRY` is preserved |

All four deterministic verifications passed. A negative control that relabelled
the interrupted result as COMPLETE was rejected. These seeded/fixed-base,
bounded demonstrations have `stochastic_budget_verified=false`; their exact
factor and multiplicative claims remain valid.

The full factorization payload SHA256 is
`0569f511651257526bf0b678b40369aaa5a535dc1705c7af02dcba79c199724c`.

The supporting complete-circuit/streaming tests are separate: N15/t4 and
N21/t6 compare 976 and 23180 joint amplitude coordinates exactly, respectively,
with full inverse recovery and all 61 modes. They used 6724 actual BRC core
calls and each certified `E=1/2000000` for requested `epsilon=1/1000000`.
Their final payload SHA256 is
`6a14cbf3994c9430b1b07067013546acef3d11c77c4ee3139df670bb20815a12`.

## 4. Persisted CLI continuation actually exercised

The following two invocations describe the retained two-process demonstration.
Use new output names to keep the frozen evidence intact. Paths below identify
the observed checkout and interpreter; the package can be run from another
authorized checkout with its source bindings and dependencies intact.

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' 'D:/em/TEMP/sep26-shor-general/new_word_compiler/run_compiled_factorization.py' --N 15 --failure-bits 2 --attempts 8 --compiler-pairs 1 --observer-bits 48 --seed 20260926 --out 'D:/em/TEMP/sep26-shor-general/new_word_compiler/replay_partial_n15.json.gz'
```

After that process has exited, a separate process resumes the saved compiler
cursors:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' 'D:/em/TEMP/sep26-shor-general/new_word_compiler/run_compiled_factorization.py' --N 15 --failure-bits 2 --attempts 8 --compiler-pairs 32 --observer-bits 48 --seed 20260926 --resume-cursors-from 'D:/em/TEMP/sep26-shor-general/new_word_compiler/replay_partial_n15.json.gz' --out 'D:/em/TEMP/sep26-shor-general/new_word_compiler/replay_resumed_n15.json.gz'
```

The retained first artifact, `CLI_COMPILE_PARTIAL_N15.json.gz`, is PARTIAL with
cofactor 15 and a verified ledger value 15. Its uncompressed payload SHA256 is
`b8f8e9f95a3b9b706a22821279f0a3335c52b4e43b77907c21820a84d27c9243`.
The retained second artifact, `CLI_RESUMED_N15.json.gz`, is COMPLETE with
certified primes 3 and 5 and verified product 15. Its payload SHA256 is
`0a7aa7c29cdf81d41b542e0f5561bffe123bfc488335bef925f2d8539b0bb322`.

Both use seed 20260926 and are labelled `seeded software demonstration`, with
`random_source_physically_certified=false`. The resumed run declares an
attempt limit of 8 while its certified node budget is 172; therefore
`budgets_meet_uniform_random_bound=false` and `stochastic_budget_verified=false`.
Completion of its exact factor ledger does not depend on claiming otherwise.

`--resume-cursors-from` extracts only
`result.native_word_compiler.phase_cursors` (or that field in a direct wrapper
result). The compiler verifies the cursor's source, request, profile and
completed phase records. The new factorization call starts again with the
provided N and a newly created RNG. This is persisted **compiler continuation**,
not saved RNG-state restoration, a live recursive-work-queue restoration, or
replay of an interrupted stochastic transcript. Earlier prime/product ledgers
remain valid artifacts; the CLI does not import them as trusted active state.
Completed finite calls are the supported saved-checkpoint boundary; an
externally killed unbounded call has no promised crash checkpoint.

## 5. Frozen sources and next result

The final compiler source SHA256 is
`e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d`.
The wrapper, derived core and CLI hashes read for this note are respectively:

- `compiled_factorization.py`: `eb1f12abb9d9b5faf140d2a49a2611bbf6cc18cc4aae8e4b911a43a05e32639d`;
- `compiled_factorization_core.py`: `e10a32bb028a38fc387baec4feb2052bd3f2f4905a18f0ed5a944711d6fe8b43`;
- `run_compiled_factorization.py`: `5298a19b982d0a5395cbeb6de07d70da4ca47e7cb954fc166248218df92e24ea`.

The compiler's decimal I/O microfix removed the arbitrary 4300-digit parser
ceiling and supplied a metadata alias; it changed no native arithmetic or
observer rule. The old-source run remains archived, and the complete streaming
rerun and source rebinding are recorded in `POST_CAP_FIX_REPLAY_CHECK.json`.

`CONSTRUCTIVE_FOUR_SQUARE_FRONTIER.md` supplies the constructive theorem:
four-square completion produces a short candidate word on the same carrier
with an explicit observer horizon. The adjacent unit
`../direct_word_compiler/DIRECT_WORD_EXECUTION_NOTE.md`, included with this
delivery, now records an actual independent-candidate case `m=3, delta=1/4`.
It observes `K=3071=1^2+55^2+3^2+6^2`, produces 190 indexed letters and an
8114-letter canonical expansion, and passes the frozen complete 61-column
phase verifier. Its two-process PARTIAL/restart path is also certified.
Its complete uncompressed payload SHA256 is
`d29cd6b789cc07eafe430117c31b3e5fe918cda041550ea6e0b1894154a5ab82`.

That bounded fixture is complete evidence to consume, not an unfinished
example to repeat. The remaining implementation task is a general direct
constructor accepting arbitrary legal m and positive rational delta, with
derived parameters, resumable bounds, and new actual examples. The current
direct CLI intentionally exercises only the declared m3 case; it does not
yet implement that general parameter interface or replace the frozen fair
compiler in full factorization. The fair compiler remains the actual general
baseline, and its proofs and evidence remain intact.

These are author proofs and bounded author executions, not independent
admission. Work-state growth, Wilson verification and search costs still
prevent any polynomial-time classical factoring claim. No physical Born-rule
or autonomous six-space-axis realization is asserted; the 61 modes remain
computational labels and P000 is unchanged.

Global-Knowledge-Sync: main@8446003 / GLOBAL_KNOWLEDGE_V1

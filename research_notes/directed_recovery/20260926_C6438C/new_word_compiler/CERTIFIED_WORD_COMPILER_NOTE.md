# Resumable fixed-word compiler: bounded execution record

Status: AUTHOR_ACTUAL_BOUNDED_EXECUTION / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. This implementation uses the shared density and effective
compilation proofs; the present author is not an independent reviewer.

Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.
Control Source `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen primitive source `0852cad130c1d877174d235687cf60c19f318c58`.

## Implemented interface

`certified_word_compiler.py` provides:

- `compile_phase(m, tolerance, seeds=(), cursor=None, pair_budget=1,
  observer_start_bits=3, activity=...)` returns `CERTIFIED` or `PARTIAL`.
- `compile_phase_bank(t, epsilon, seed_words=None, cursor=None, pair_budget=1,
  observer_start_bits=3, activity=...)` uses exact m2 and
  `delta=epsilon/(2L)` for m3 through t, where `L=(t-1)(t-2)/2`.
  `seed_words` maps phase indices to finite lists of candidate words.
- `verify_certificate(cert)` actually replays complete native columns,
  inverse recovery, target probes and the signed strict margin.
- `verify_phase_record(record)` additionally binds the external word, phase,
  dimension, claimed bound and certificate hash. The exact m2 outer bound is
  zero only when its full Frobenius upper witness equals zero.
- `CertifiedNativeWord(cert)` is a literal `apply_word` adapter with an exact
  static denominator; it never propagates a target matrix. Integration may
  independently cache its fully rechecked actual columns.

All returned objects are JSON portable. A bank cursor retains complete
certificates and the active phase cursor. Resuming a bank replays its completed
certificates before accepting them. A completed bank contains every phase
index 2 through t; a `PARTIAL` bank must not be injected into a Shor program.
The independent runtime still enforces its own allowed t/input conventions.

The source binding includes the profile, compiler, frozen phase executor,
algebraic observer, closed-zero extension, adapter and verified canonical
kernel. Keep those files fixed throughout one process; after a source edit,
start a fresh process and regenerate affected execution evidence.

The implementation explicitly disables Python's default decimal integer I/O
digit cap. This is needed for arbitrarily long exact certificate integers;
it changes no scientific primitive or arithmetic rule. A standalone smoke
first restored the default 4300-digit cap, imported the compiler, then round
tripped a 5001-digit integer through JSON. It passed with zero BRC calls and
is labeled ordinary I/O only in `LARGE_CERTIFICATE_IO_SUMMARY.json`.

## Fair search and bounded interruption

The concrete dovetail is equivalent to, but not identical to, the illustrative
length/frontier schedule in `EFFECTIVE_COMPILER_CLOSURE.md`:

    stage s = 0,1,2,...
    candidate index i = 0,...,s
    observer bits b = observer_start_bits + s - i

Candidates are the finite seed prefix followed by all words in length then
lexicographic order over the 62 fixed letters. Every finite word has a finite
index, and every index is revisited at unbounded b. Every stage is finite.
Negative determinant words consume their scheduled pair but need no native
column execution. No undecidable equality or unsuccessful candidate can hold
up the next pair. Density and observer convergence therefore give the same
mathematical finite-termination conclusion when the caller continues supplying
budgets. This is not a useful bound on word length or running time.

`pair_budget=0` returns an initial cursor without scientific phase execution.
The budget counts complete candidate/depth pairs, not elapsed time or primitive
instructions. A long individual pair is not a preemptible wall-clock budget.
The cursor records the first unprocessed pair and checks its triangular
position, as well as source, target, tolerance, seeds and observer settings.
Callers can save the returned cursor between conversations or processes.

## Actual observer path

Every accepted native candidate executes all 61 basis columns using frozen
`apply_word`; all 61 are inverted and checked. The complete Gram identity is
an exact observation of those actual columns. Orthogonality also follows from
the unchanged native involutions. No residual coordinate is discarded.

The target is the fixed inherited algebraic phase, not a fitted measured
target. The existing closed-root extension executes first. A traced copy of
its same bisection then invokes frozen `polynomial_probe` at every comparison
and replays the identical nine-state positive graph to retain both actual
endpoint values. The complete tower is checked against the existing extension.
This extra replay provides the previously missing endpoint receipts; it is not
a new root definition, new runtime rotor or higher precision old bank.

From the actual columns, small positive path graphs observe

    A=W00+W11, B=W01-W10, C=sum(j>=2) Wjj.

Choose x=u when A>=0 and x=l otherwise; choose y=l when B>=0 and y=u otherwise.
With Dx=1+x^2, Nx=1-x^2 and Dy=1+y^2, the strict comparison is the sign of

    margin = delta^2 Dx Dy - 2D Dx Dy + 2C Dx Dy
             + 2A Nx Dy + 4B y Dx.

Each addition/product in that expression is a replayable acyclic positive BRC
path graph, with signs retained at distinct endpoints. Acceptance is the
actual final signed endpoint difference `margin>0`. Positive denominators give

    margin = (delta^2 - E_upper) Dx Dy,
    E_upper = 2D-2[C + A c(x) + B s(y)].

Fraction expressions display and independently check that identity; they do
not replace the executed strict decision and never propagate a Shor state.
The complete Frobenius identity includes all off-diagonal and residual error
through the verified full orthogonality. The certificate stores each observer
input, graph edge, endpoint and intermediate result.

## Bounded checks actually executed

Command:

    D:/kimi-query-bridge/.venv/Scripts/python.exe check_certified_word_compiler.py

The run completed with 738 canonical BRC core calls:

- m2 exact quarter turn: full squared Frobenius upper bound 0, requested
  tolerance 2^-40, actual full replay verified.
- m3: the existing pinned 1736-letter seed, all 61 columns and inverse,
  observer depth 18, strict full-carrier tolerance 1/64. The certificate
  stores the exact rational upper bound; no ideal reference was executed.
- Closed-zero observer at m12/depth3: lower endpoint 0 retained correctly.
- Bank zero budget, one-phase partial, then resumed certification; no
  successful partial was injected into a program.
- Six negative controls rejected: external word substitution, unsupported
  smaller error, actual column corruption, strict-margin corruption,
  completed-cursor word substitution and cursor target substitution.
- First ten dovetail positions and finite-word ranks were checked.

This is a bounded implementation check. It is not an execution of the
unbounded fair search, a practical arbitrary-epsilon performance result,
full Shor simulation, or independent admission of the shared proofs.

Artifacts at this execution:

- `CERTIFIED_WORD_COMPILER_CHECKS.json.gz`, decompressed canonical payload
  SHA256 `3092df8ed31d39709868ee1d3193e2492e40b158d857ecf0f4c618b9a12839fe`.
- `CERTIFIED_WORD_COMPILER_SUMMARY.json`.
- Compiler SHA256
  `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d`.
- Check script SHA256
  `ed7504f65e796ad211abf253d2bd00e188906f3c11ea2cb5541c91e63bbc2452`.
- Profile SHA256
  `ab87d2ba39f8289e6aaf64a63f1cfd30979b419aba24c19f0cdbb9a1af921c86`.

The first successful version and its evidence are retained under
`prior_4300_digit_cap/`. The present bounded run was repeated after the I/O
limit fix and harmless `sign_count` adapter alias, so current evidence binds
the current compiler hash rather than silently reusing the earlier receipt.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1

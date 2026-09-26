# Streaming terminal instrument for frozen BRC Shor

Status: AUTHOR_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Researcher EM-DIRECT-0C08F0; activity RA-40F334CAC4876C16B82B0215.
Frozen input HEAD0852cad130c1d877174d235687cf60c19f318c58. Native registration Sourcec412dcb62f4b27189afd8e5748ff5f8dbb3c17dd. Same-context collaborators; not independent review.

## Exact closure delivered

The candidate streams one active control bit through the original frozen Stage80 gates. It gives exactly the same complete terminal joint amplitudes, joint probabilities, control law, and unchanged CF/gcd result law as original Stage80 on the tested inputs. The general equivalence is established by the separate parent proof; finite tests validate implementation, not the general theorem.

This closes a terminal sampling interface without increasing operator moments. It does not prove polynomial classical runtime, spatial hardware, native probability semantics, or equivalence under later coherent access to measured control bits. The inherited Stage80 ideal-TV error is unchanged.

## API and retained state

terminal_instrument.py provides load_frozen_bank(max_m=10), returning bank, intervals, dimension61. It reads Stage80 RESULTS.json integer vectors at original target32/vector64, executes FixedRotor on every61 basis column and actual inverse, and checks the exact saved word_to_basis and inverse_phase_word. No fresh precision, roots, fitting, or replacement phases are used.

StreamingProgram(N,a,t,bank,dim) obtains powers only from input repeated squaring, then reverses them to b_i=a^(2^(t−1−i)). Original actual BRC modular_columns are reused; no order/factor/histogram enters. initial() returns work1, control0, spectator0, internal e0, denominator1.

branches(state,den,history) returns two (state,den) pairs, including empty zero branches. Boundary keys are (0,work,spectator), and history is the tuple of measured low-to-high output bits. Original H4 prepares the active bit and shared spectator; controlled modular multiplication updates work; original CP blocks apply in increasing old-control order using history; original H4 precedes bit projection. The measured bit moves into classical history. All61 residual modes and the original signed-companion semantics remain. The shared spectator returns to0 by evolution in each round; it is never reset.

report_metrics() reports branch/operation counts and maxima for endpoints, allocated mode slots, nonzero coordinates and denominator bits. These are arithmetic resources, not a physical layout.

advance/enumerate_leaves implement a second comparison route: early terminal measurements on the original fully prepared register. That route is not the streaming initializer. Its genuine nonzero intermediate spectator mass is retained.

A small exact rejection Bernoulli sampler is included for interface tests. It assumes externally supplied unbiased independent random bits and almost-sure finite termination, not fixed worst-case random-bit cost. Zero/one probabilities consume no bits; tests explicitly exercise denominator3 rejection. The parent driver provides the final streaming sample/retry wrapper.

## Executed equality evidence

Run Python3.11+ standard library with: python -B -S terminal_instrument.py
For relocation set BRC_STAGE87_SOURCE to the immutable extracted checkout. Default is the existing verified sibling task source.

| N,a,t | all leaf slots | zero leaf slots | joint amplitude coordinate comparisons per route | streaming prefix endpoint peak | original full macro endpoint peak |
|---|---:|---:|---:|---:|---:|
|15,2,4|16|12|976|8|16|
|21,2,6|64|0|23180|12|380|
|15,14,4|16|14|244|4|16|

Both routes compare every joint amplitude including work, spectator and all61 modes by exact integer cross multiplication. Missing entries count as zero. Separately serialized joint squared-coordinate hashes agree. Every control bin and CF/gcd factor/status distribution agrees. Bad base15/a14 retains exact success0; for15/a2 the factor law is no-factor1/2 and (3,5)1/2.

N21/a2/t6 streaming uses at most12 endpoints,732 mode slots,660 nonzero coordinates and1263 denominator bits per current prefix. This is not total memory of the all-leaves validation tree: enumerating64 outcomes remains exponential, and modular-table costs remain. There is no asymptotic speed claim.

For21/a2/t6 the all-leaves validator makes63 prefix calls,126 H4 calls and258 CP invocations. Those are totals over the tree, not a single shot. Complete frozen-bank and modular/gcd construction makes23 actual BRC core calls, separate from repeated certified-column use.

The original early-measurement route has spectator-one mass1/2 after odd H4 count and0 after even count. Injected deletion keeping only spectator0 at the first boundary retains mass1/2 and detects the invalid reset. The streaming order uses two genuine H4 per round and returns spectator0 exactly.

## Reproducibility

Frozen source comes from the existing authenticated Stage87 bundle:
Drive file ID1ox9qTtXGbN0p6Zma29uXtBXM6FcOOXhV;
bundle bytes61398315;
SHA256a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c;
Git HEAD0852cad130c1d877174d235687cf60c19f318c58.
Use the exact extracted LF file bytes; global newline conversion can break native vendor hashes. The original checkout was not edited.

terminal_output/CASE_*.json retains all control probabilities, factor/status law, prefix resources and sample replay. RESULTS.json.gz contains all case documents and native BRC receipts (gzip mtime0). SUMMARY.json gives its uncompressed sha256. MANIFEST.json records local and frozen source hashes.

The initial invocation failed during import because a default parent directory index was wrong; no scientific code executed. It is excluded from test counts and recorded in EXECUTION_LOG.json. The corrected final script, including saved basis-word checks, completed all3 cases.

General semiclassical Fourier transform and one-control Shor are prior work. New task-specific content is their exact adaptation to this frozen BRC61-mode word, retained spectator, complete branch semantics, and reproducible equality evidence. P000 and six native axes plus time are unchanged.


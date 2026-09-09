# RB CM24 identity v1: source-exposed peer code/evidence review

Review date: 2026-09-09. This is a bounded source-exposed peer code review for the owner. It is not a blind mathematical reproduction, a new mathematical run, or a formal Driver disposition.

## Decision

No defect was found in the frozen v1 ODE denominator clearing or its claimed zero-remainder checkpoint. The evidence supports the stated **INCOMPLETE identity checkpoint**, not completion of the exact-map task. No mathematical work needs to be rolled back or replayed because of this review.

The archived source is byte-exact but depends on its canonical repository location for direct invocation. The actual resource wrapper was not included in the original v1 receipt; the author identified the original tool invocation and is preserving its source separately. These are narrow reproducibility/documentation boundaries, not evidence that the recorded run exceeded its budget or that the identity failed.

## Frozen inputs and actual checks

Bound source:
- Checker and archived checker: SHA256 `dea05305c92545ddbf97e521310c0ba1f103213020945750b810e2c8ebc9dd63`, 12,309 bytes.
- source_freeze.json: `85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2`.
- Archived certificate: `c11db2a62c2c1926306117abcac0495ed7a518ae37e1fb6fbd27bfdd75ef6ab8`, 20,568 bytes.
- Original v1 receipt: `d67a19adaf231cca83394206e865d2b5a869034ffef78530e5cc1ab6b8ba7a36`.
- Reused integer polynomial implementation: `32282b30357638b5f0a2b709a0c917b29711b43a4d7f407a113bfb6502ddf269`.

The bounded metadata execution in metadata_review.py checked all seven source pins, receipt-to-source/certificate/stdout/stderr digests, the policy digest, canonical complete JSON serialization, and every serialized polynomial row. N/D0/k/lambda/C4/W contain respectively 20/21/2/4/4/54 terms, totaling 105. Exponent tuples are ordered and unique, coefficients are exact nonzero integers, all unused slots vanish, and generator exponents are in the declared reduced shape. The empty complete remainder is present.

This verifies integrity and representation, not a second computation of the polynomial identity. The original author invocation ran with `--write`, exit 0 and 484,000,000 elapsed nanoseconds. This review did not execute build_certificate, formula, ode_residual, the old square-class checker, or any other mathematics.

## ODE implementation

Write \(\mathcal D=2\delta\), with \(\delta=t\,d/dR\) on \(t^2=R^3-3R\). The reused implementation has
\[
\mathcal D(R)=2t,\qquad \mathcal D(t)=3R^2-3.
\]
It differentiates every R/t monomial and reduces the curve relation. This derivation preserves \(t^2-R^3+3R\). The coefficient generators are constant under it.

For \(X=N/D_0\), the code computes
\[
W=\mathcal D(N)D_0-N\mathcal D(D_0),\qquad
\delta X=\frac{W}{2D_0^2}.
\]
With the frozen \(C=C_4/4\), multiplying
\[
(R+2)t(\delta X)^2
=C(t+k)^2X(X-1)(X-\lambda)
\]
by \(4D_0^4\) gives exactly the implemented residual:
\[
(R+2)tW^2-C_4(t+k)^2N(N-D_0)(N-\lambda D_0)D_0.
\]
The final factor \(D_0\), the factor four, and the difference signs are correct. The original formula's N, D0, k, lambda and C4 agree with the frozen expressions. No substitution \(t=-k\), Q-fiber restriction, sampling, evaluated division, or root evaluation is used in this v1 path.

Normalization applies only the explicit monic relations \(\alpha^4=3,\beta^2=2,i^2=-1,t^2=R^3-3R\), retaining exact integer coefficients. A zero remainder therefore certifies this cleared identity in that presented algebra; it does not establish all nonzero/embedding, descent, divisor or global regularity conditions.

The declared
\(Y=wW/[2(t+k)D_0^2]\) and \(w^2=(R+2)t\) have the correct formal target relation. The code does not independently complete the unsquared differential/exceptional-point proof. Its remaining-gates field correctly keeps that obligation open.

## Reproducibility and resource boundaries

1. **Archived entry is not standalone.** One actual non-mathematical probe ran:
   `python -B -X utf8 <runs/identity_v1/check_exact_map.py.frozen> --root <repo> --help`,
   with a separate TEMP cwd and no child PYTHONPATH. It exited 1 before any mathematics: `ModuleNotFoundError: No module named 'research_artifacts'`.
   ROOT is computed from the archived file's depth before argument parsing, so `--root` cannot repair that initial import. The author clarified that .frozen is an unchanged source archive, not a second runnable package. Preserve it. Document replay by restoring these exact bytes at the original repository path in an isolated checkout, or using a pinned first-publication commit's original path. To compare the old checkpoint after later work, use its archived certificate as `--output`. No source redesign or v1 rerun is required just to document this.

2. **Actual outer wall-time limit and memory enforcement must be distinguished from child polling.** The child checks its deadline at normalize entry, not during each inner multiplication or final serialization. This is cooperative checking, not a standalone preemptive 600-second monitor. The author supplied the actual invocation provenance: tool chunk `dedf6a` used a PowerShell here-string to Python inline orchestration with
   `subprocess.run(argv, cwd=root, capture_output=True, timeout=600)`.
   That statement is author/tool-invocation provenance received during review; this reviewer did not independently replay or retrieve that tool turn. The author is appending an honestly labeled source capture of the runner, without claiming it was originally executed as a file. This closes the documentation gap without changing the historical v1 receipt.
   
   The child sets a Windows Job `JOB_OBJECT_LIMIT_PROCESS_MEMORY` of 4096 MiB and fails if creation, setting or attachment fails. A successful path therefore establishes that limit. No peak-memory measurement is present; do not describe 4096 MiB as measured consumption.

3. **Observed bounds are narrow and honestly named.** The recorded maximum normalized polynomial support is 128 and maximum observed coefficient length is 36 bits, well below the frozen 250,000/65,536 limits. These counters observe normalized outputs, not every transient allocation. The encoded certificate is 20,568 bytes, below 67,108,864. The v1 source hardcodes those latter limits to the same values as its pinned plan; do not claim support for arbitrary changed policy limits from this run. The call counts are the explicit wrapper-boundary counts, not a complete transitive API-call trace. Zero BRC evaluations is accurate for this path and does not manufacture native division/root evidence.

## Uncompleted scope

The certificate expressly leaves field/embedding nonzero facts, all special-fiber valuations and square-class placement/descent, all common-basepoint cancellation and degree, exact j/model relation, unsquared differential/exceptional regularity, and independent counterchecks/full proof-return unfinished. No equality of a full map certificate, new theorem family, task closure, period/homology index, or exhaustive 1980-family classification follows from this checkpoint.

Evidence: sibling review.json (SHA256 `25b4bb29bfc00286bde5d905c611c9a9edba5d04ca29f4542b273fa6ad560fba`), metadata_review.py, and the complete archive-help stdout/stderr. The seven reviewed input files and all seven frozen source pins remained unchanged during the metadata probe. No research-workspace file was written by this reviewer.

Global-Knowledge-Sync: main@3ad395d / GLOBAL_KNOWLEDGE_V1

# Recovery M07

Parent objective: progressively replace floating-point decision semantics with
integer plus typed residuals while preserving local semantics and provenance.

Verified M07 code: candidate branch commit `5c401f57d519caf9bda8e2156b9899e2b3168fed`.
Machine validation: 45 tests, zero failures/errors, one known source-slice package-data skip.

Completed: `multiplicative.py` CLI has independent exact textual `--cell-scale`,
integer precision budgets, exact report V2/hex-data metadata, and failure-before-write
semantics. Legacy `--scale` and V1 output remain unchanged without exact opt-in.

Do not infer exact scale from `--scale`; do not enable exact `--preview`; do not
change the older module's axial lexicographic tie rule; do not call A2 native X6.

Next executable unit: migrate `multiplicative_lab.html`/browser input and cell
quantizer using the existing browser certified-cell implementation plus an exact
legacy lexicographic tie adapter. Preserve unresolved state and asynchronous
computation; keep default switching separate until caller validation passes.

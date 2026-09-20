# Recovery M06

Parent objective: progressively remove floating-point *decision* semantics in prior Enterprise Math research/code, preserving exact source/provenance and local observer semantics.

Verified code frontier: Enterprise Math candidate branch `research/integer-residual-m01-angular-20260919-4a5102`, code commit `26a8cb4c2fda7012268545222b11316354df34dc`.

M06 completed locally: `multiplicative.py::build_field` has an opt-in exact `cell_scale=(integer,integer)` path; legacy path shape is preserved; exact legacy lexicographic tie adapter preserves the base certificate. 35 tests run, zero failures/errors, one explicit package-data skip in the source slice. Finite 4096/65536 matrices and tie audit are in `evidence/migration06`.

Do not repeat M01-M05 or rebuild a residual scalar. Do not infer an exact ratio from legacy `config.scale`. Do not replace the module's lexicographic tie semantics with M03/M04's different tie policy. Do not call A2 native X6.

Next executable unit: expose an exact textual/typed scale through an actual `multiplicative.py` caller/CLI or config V2 while retaining V1 compatibility; then migrate further statistics/readouts one observer at a time. Default switch remains separate.

Outstanding: full-checkout deterministic HTML test, browser UI for this older lab, whole-repository regression, independent review, main code integration, historical experiments, general algebraic/transcendental closure, complex amplitudes/QFT, native X6 path-owner integration.

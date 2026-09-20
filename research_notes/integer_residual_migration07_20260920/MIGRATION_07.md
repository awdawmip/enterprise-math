# Migration 07 — exact textual cell scale on the multiplicative CLI

Status: opt-in machine-output candidate; browser workbench remains legacy float.
Baseline: `9be970404cc12c82b26431415a837820f74289ad`.
Code: `5c401f57d519caf9bda8e2156b9899e2b3168fed`.

M07 moves the M06 exact cell path into a real caller without laundering the old
floating `--scale`. `--scale` remains display-only. `--cell-scale` accepts only
positive exact text: integer, fraction, or ordinary decimal. Decimal spelling is
provenance: `0.50` is retained as `50/100`; `2/2` remains `2/2`. No `float()`,
`Fraction(float)`, denominator guessing, or epsilon reconstruction occurs.

`--cell-bits` and `--cell-max-bits` are independent integer precision budgets.
Exact mode is currently allowed only when `--report` or `--hex-data` is requested.
`--preview` is rejected in exact mode because this older browser workbench has not
yet been migrated. The generated HTML is explicitly reported as legacy display.

Legacy CLI reports remain schema V1 and are unchanged when `--cell-scale` is
absent. Exact reports use `NOLLM_MULTIPLICATIVE_REPORT_V2`, preserve the lexical
scale source, and include a bounded certified-cell summary rather than every
point certificate. Exact hex-data metadata also retains the lexical scale source.

Failure ordering is strict: the exact field and requested hex exportability are
checked before any artifact is written. A report-only low-precision run may
legitimately preserve `UNRESOLVED_BOUNDARY`; a requested hex export refuses such
cells and leaves no HTML/report/data partial output.

Validation: 45 tests = M06 35 + M07 CLI 10, zero failures/errors, with the same one
source-slice skip for unchanged `multiplicative_lab.html` package data. The M06
4096/65536 matrices and 1,080-tie audit were rerun and unchanged. A clean M06
bundle replay with the M07 code patch produced byte-identical test output.

Code patch SHA-256: `130b84602970498d4c847203ffafecd3e4666c111fd58fc0d574edb26dd76311`.

Next: migrate the older `multiplicative_lab.html` browser caller itself. Do not
infer exact state from the legacy float slider, and do not substitute the base
certifier's different tie rule for this module's axial lexicographic tie rule.

# Recovery M18

Parent objective: progressively migrate actual Enterprise Math research/code to
integer plus typed residuals, without guessing exact sources from floating data.
Remote baseline M17: 44c5f034d38726990f83ff3e05d5b0eff520cea7.
Candidate branch: research/integer-residual-m01-angular-20260919-4a5102.

M18: real Phase32 textual machine CLI, strict no-display machine config/report,
original unreduced pitch (inverse certifier scale), precision and readout settings,
JSON/CSV export; no new arithmetic. 209 tests, 207 passed, zero failures/errors,
two known missing-HTML skips; ten finite CLI population comparisons and clean
replay passed. See MIGRATION_18.md and research_notes/integer_residual_migration18_20260921/validation.json.

Next executable unit: Phase32 machine-report reader using saved source/pitch/
precision/readout. Existing multiplicative_report handles a different schema.
Do not silently reinterpret either. Phase32 browser and M15 full-package/native
browser admission remain unpassed; defaults and code main were not switched.
Never overwrite production with the bundle's isolated enterprise_math __init__.

# Recovery M12

Parent: progressive integer-plus-typed-residual migration of real callers.
Baseline: EM candidate `3f6946239e28009bd915075afc201faa508468e8` (M11).
Branch: research/integer-residual-m01-angular-20260919-4a5102.
Activity: RA-1094DE57986E6E3FDCEA65DA, EM-DIRECT-4A5102 / TASK_RESEARCH.

Completed locally: pure machine_config + build_field(include_display=False),
actual --machine-only caller, dedicated machine report schema, precision budget
persistence/replay, float-free JSON/CSV cell export. 148 tests and 13 complete
population comparisons pass. Core cell/BRC/tie algorithms remain unchanged.

Read MIGRATION_12.md and research_notes/integer_residual_migration12_20260920/
validation.json for exact scope. Complete data/logs live under evidence/migration12.
Use migration12.patch only on pinned M11, never overwrite the isolated initializer.

Next: downstream machine-report readers and explicit display adaptation, complete
package/native-browser acceptance, then separately review defaults/main. No
whole-repository completion or independent theorem admission. Do not restart
M01-M11, replace local tie semantics, guess a scale, or bypass managed browser
restrictions. Unknown/unresolved is typed data, not a fake zero.

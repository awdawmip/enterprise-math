# R410 Portable Handoff (2026-10-30)

Current TASK_RESEARCH author-side contribution; GitHub identity awdawmip. Native gateway v0.6.11 gave research_authority_granted=false and executor_binding_configured=false; current control_tasks returned CONTROL_QUOTA. No current formal owner/CLAIM confirmed.

Fixed read pins: global main@cf2a590bdae96d9228f2415d8275b7d7ddfe25b7; Enterprise Math main@9096fd74414565c772faad807e29250637e8266a. Existing R409 frontier e92a78cacb3b2fb8c4a5fed0f3ae7d513b33ca44 in PR #1708.

Exact new result: all integers r>=24 have D_(r,23)>0 for δ_(r,s)=[t^r](1-t)(1+t)^(2s)(1+t²)^(r-s), H=binom(r+s,2s)δ, D=H²-H_previous*H_next. Full coefficients R410_EVIDENCE.json; producer r410_verify.py; independent standard-library integer checker r410_independent_verify.py; mathematical argument R410_PROOF.zh-CN.md.

Run `python r410_verify.py && python r410_independent_verify.py`; expect R410_EXACT_PASS and R410_INDEPENDENT_INTEGER_PASS. Source data and old Catalan kernel retained; symbolic exact identity plus positive coefficients, not numerical extrapolation. Prior R404/R403 need independent review.

State AUTHOR_SIDE_EXACT / GITHUB_SOURCE_DURABLE / DRIVER_UNREVIEWED / NOT_ADMITTED. No native CLAIM, Result, review, world axiom change or actual physics attribution.

Next: s=24 for all integer r>=25; remaining unrestricted positive-kernel territory s>=24, r-s>=129, first point (153,24); investigate uniform proof or exact negative example.
